# defining the tools that can be used by the agents
import json
from jsonschema import validate, ValidationError
import pymysql
from datetime import datetime
import global_vars
from Agent_config import AgentFactory

# 创建数据库连接

def db_writer(question: str, answer: str, agent_name: str, reviewer_score:str, table_name: str = "annotation", schema: dict = global_vars.schema, overwrite_flag : bool = False) -> None:
    # 连接到数据库
    conn = pymysql.connect(host='1.14.10.129',
                           user='root',
                           password='tcci1234',
                           database='data_annotation',
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

def reg_tool(agent: AgentFactory):
    # Register the tool signature with the assistant agent.
    agent.assistant.register_for_llm(name="db_writer", description="Connect to Mysql and store some QA labbeled data")(db_writer)
    # Register the tool function with the user proxy agent.
    # 向用户代理注册工具功能。
    agent.user_proxy.register_for_execution(name="db_writer")(db_writer)
    from autogen import register_function
    # TODO: tools already registered handler
    register_function(
        db_writer,
        caller=agent.assistant,  # The assistant agent can suggest calls to the calculator.
        executor=agent.user_proxy,  # The user proxy agent can execute the calculator calls.
        name="db_writer",  # By default, the function name is used as the tool name.
        description="write final Question and Answer string to mysql database ",  # A description of the tool.
    )
    return "tool registed success!"