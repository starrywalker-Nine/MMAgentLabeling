# GLOBAL TEMP VARIABLES FOR THE PROJECT

queueTask = []
task_name = ""

# 问答对 JSON Schema 定义
schema = {
    "type": "object",
    "properties": {
        "question": {"type": "string"},
        "answer": {"type": "string"},
        "agent_name": {"type": "string"},
        "time": {"type": "string"},
        "reviewer_score": {"type": "string"},
    },
    "required": ["question", "answer"],
}

