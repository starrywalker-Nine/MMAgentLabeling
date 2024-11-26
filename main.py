from Database import db_writer
from Agent_config import AgentFactory
import global_vars

def startLabelingFlow(agent: AgentFactory, raw_data):
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
        "reviewer_score": "1-3",
    }

    id = 1
    answer = []
    # chatResults structure: 
    # chat_results[chat_id, chat_history, summary]
    questionLog = chat_results[0]
    questionList = questionLog.summary
    answerLog = chat_results[1]
    answerList = answerLog.summary
    reviewerLog = chat_results[2]
    reviewerList = reviewerLog.summary

    testString = f"Question:{questionList} Answer:{answerList} reviewer_score:{reviewerList} Agent_name: CodeLLama2_v1"
    data = {
        "id": id,
        "question": questionList,
        "answer": answerList,
        "reviewer_score": reviewerList,
    }
    answer.append(data)

    agent.user_proxy.initiate_chat(agent.assistant,
                                            message=f"把这些问答对根据下面的格式{json_file_sample}存入数据库中：{testString}")
        
    if global_vars.task_name != "":
        sub_task_name = f"{global_vars.task_name}_startLabelingFlow"
        print(f"removing {sub_task_name}")
        global_vars.queueTask.remove(sub_task_name)
    return "success"
