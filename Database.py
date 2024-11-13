# defining the tools that can be used by the agents
import json
from jsonschema import validate, ValidationError
import pymysql
from datetime import datetime

# 问答对 JSON Schema 定义
schema = {
    "type": "object",
    "properties": {
        "question": {"type": "string"},
        "answer": {"type": "string"},
        "agent_name": {"type": "string"},
        "time": {"type": "string"},

        # "reviwer_score": {"type": "integer", "minimum": 1, "maximum": 3},
        # "reviewer_comments": {"type": "string"},
        # "agentInfo": {
        #     "type": "object",
        #     "properties": {
        #         "agent_name": {"type": "string"}
        #         }
        #     }
    },
    "required": ["question", "answer"],
}


# 创建数据库连接

def db_writer(question: str, answer: str, agent_name: str, table_name="qa_data", schema=schema, overwrite_flag=False):
    # 连接到数据库
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='tcci1234',
                           database='dataPanel',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()

    json_string = f"\"question\": \"{question}\", \"answer\": \"{answer}\", \"agent_name\": \"{agent_name}\", \"time\": \"{datetime.now()}\""
    json_string = '{' + json_string + '}'
    json_raw_data = json.loads(json_string)

    # 为了简洁，假设数据库表已经存在并且具有适当的列
    insert_query = f"INSERT INTO {table_name} (question,answer,agent_name,time) VALUES (%s,%s,%s,%s)"
    if overwrite_flag:
        cur.execute(f"TRUNCATE TABLE {table_name}")
        conn.commit()

    # 处理每个 JSON 文件
    data = json_raw_data
    try:
        # 验证 JSON 数据
        validate(instance=data, schema=schema)

        # 将验证通过的 JSON 数据存入数据库
        cur.execute(insert_query, (data["question"], data["answer"], data["agent_name"], data["time"]))
    except ValidationError as ve:
        print(f"Error: {ve}")
        pass

        # 提交数据库操作并关闭连接
    conn.commit()
    cur.close()
    conn.close()
    return "memory update success!"
