from Database import db_writer
from Agent_config import AgentFactory


def reg_tool(agent: AgentFactory):
    # Register the tool function with the user proxy agent.
    # 向用户代理注册工具功能。
    agent.user_proxy.register_for_execution(name="db_writer")(db_writer)
    from autogen import register_function

    # Register the calculator function to the two agents.
    # 将计算器函数注册到两个代理。
    register_function(
        db_writer,
        caller=agent.assistant,  # The assistant agent can suggest calls to the calculator.
        executor=agent.user_proxy,  # The user proxy agent can execute the calculator calls.
        name="db_writer",  # By default, the function name is used as the tool name.
        description="write final Question and Answer string to mysql database ",  # A description of the tool.
    )


def start(agent: AgentFactory, raw_data):
    # Start a sequence of two-agent chats.
    # Each element in the list is a dictionary that specifies the arguments
    # for the initiate_chat method.
    # 开始一系列两个代理的聊天。列表中的每个元素都是一个字典，用于指定 initiate_chat 方法的参数。
    chat_results = agent.allocator_agent.initiate_chats(
        [
            {
                "recipient": agent.annotator_question_agent,
                "message": f"{raw_data}这是分配的数据，根据数据给出问题，注意只给出问题,".format(raw_data=raw_data),
                "max_turns": 1,
                "summary_method": "last_msg",
            },
            {
                "recipient": agent.annotator_answer_agent,
                "message": f"这是原始数据{raw_data}，下面是标注的问题，给出答案，注意只在问题后面给出答案，不要修改问题内容和顺序，\
                    不要输出额外信息。",
                "max_turns": 1,
                "summary_method": "last_msg",
            },
            {
                "recipient": agent.reviewer_agent,
                "message": f"这是原始数据{raw_data}，下面观察问答对，给出评价,只给出评价分数，不要修改问答对内容",
                "max_turns": 1,
                "summary_method": "last_msg",
            }
        ]
    )

    json_file_sample = {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "agent_name": "your_agent_name",
    }

    id = 1
    answer = []
    for chat in chat_results:
        history = chat.chat_history
        memoryQuestion = history[0]
        memoryAnswer = history[1]
        agent_name = history[1]['name']
        testString = f"{memoryQuestion} {memoryAnswer} agent:{agent_name}"
        data = {
            "id": id,
            "question": memoryQuestion,
            "answer": memoryAnswer,
            "agent_name": agent_name,
        }
        answer.append(data)

        db_res = agent.user_proxy.initiate_chat(agent.assistant,
                                                message=f"把这些问答对根据下面的格式{json_file_sample}存入数据库中：{testString}")
    return answer
