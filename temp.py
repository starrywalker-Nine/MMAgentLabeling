import json
from jsonschema import validate, ValidationError
import pymysql
from datetime import datetime
import global_vars

# 创建数据库连接

def db_writer(question: str, answer: str, agent_name: str, reviewer_score:str, table_name: str = "qa_data", schema: dict = global_vars.schema, overwrite_flag : bool = False) -> None:
    # 连接到数据库
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='tcci1234',
                           database='dataPanel',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()

    json_string = f"\"question\": \"{question}\", \"answer\": \"{answer}\", \"agent_name\": \"{agent_name}\", \"time\": \"{datetime.now()}\", \"reviewer_score\": \"{reviewer_score}\""
    json_string = '{' + json_string + '}'
    json_raw_data = json.loads(json_string)

    # 为了简洁，假设数据库表已经存在并且具有适当的列
    insert_query = f"INSERT INTO {table_name} (question,answer,agent_name,time,reviewer_score) VALUES (%s,%s,%s,%s,%s)"
    if overwrite_flag:
        cur.execute(f"TRUNCATE TABLE {table_name}")
        conn.commit()

    # 处理每个 JSON 文件
    data = json_raw_data
    try:
        # 验证 JSON 数据
        validate(instance=data, schema=schema)

        # 将验证通过的 JSON 数据存入数据库
        cur.execute(insert_query, (data["question"], data["answer"], data["agent_name"], data["time"], data["reviewer_score"]))
    except ValidationError as ve:
        print(f"Error: {ve}")
        pass

        # 提交数据库操作并关闭连接
    conn.commit()
    cur.close()
    conn.close()
    return "memory update success!"
question="什么是结构化数据、非结构化数据和半结构化数据？它们各自的特点是什么？"
answer="结构化数据：有固定格式或组织方式的数据，如数据库表格。非结构化数据：没有固定格式或组织方式的数据，如文本、图片。半结构化数据：介于结构化和非结构化之间的数据，如XML、JSON。"
agent_name="CodeLLama2_v1"
reviewer_score="3"
table_name="qa_data"
db_writer(question, answer, agent_name, reviewer_score, table_name)