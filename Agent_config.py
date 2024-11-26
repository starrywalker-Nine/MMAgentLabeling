from autogen import ConversableAgent
from dotenv import load_dotenv
import os 

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
# initial qwenList models
class ConversableAgentManager:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.config_list = [
            {"model": "qwen-plus",
             "api_key": api_key,
             "base_url": base_url, }]
        self.configuration = {
            "cache_seed": 41,  # seed for caching and reproducibility
            "config_list": self.config_list,  # list of OpenAI API configurations
            "temperature": 0,  # temperature for sampling
        }

    def create_agent(self, name, system_message=""):

        if name == "Assistant":
            return ConversableAgent(name=name,
                                    system_message=system_message,
                                    llm_config=self.configuration, )
        elif name == "User":
            return ConversableAgent(name=name,
                                    llm_config=False,
                                    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in
                                                                   msg["content"],
                                    human_input_mode="NEVER", )
        else:
            return ConversableAgent(
                name=name,
                system_message=system_message,
                llm_config=self.configuration,
                human_input_mode="NEVER",
            )


class AgentFactory:
    def __init__(self):
        # use
        manager = ConversableAgentManager(API_KEY, BASE_URL)
        # Agent Card configuration
        allocatorCard = "你是一个先进的文档解析机器人，专门负责从各种格式的文档中提取文本，\
            合理地按照上下文和格式切分段落，并在过程中尽可能地识别和纠正错误。\
            你的主要任务是确保文档的内容准确、结构清晰，且易于进一步处理和理解。"

        annotatorQuestionCard = "你是一个高级问题提炼机器人，专门负责从提供的文档中精确地提炼出关键信息，\
            并模拟用户的提问方式生成问题。你的主要任务是理解文档的主要内容和细节，\
            根据这些信息生成能够引导用户深入探讨和理解文档内容的问题。"

        annotatorAnswerCard = "你是一个高级问答生成机器人，专门负责根据给定的文本内容创建相关的问答对。\
            你的主要任务是从详细的文本段落中提取关键信息点，并围绕这些关键点生成精准答案。严格遵循问题的语境，\
            回答只输出答案，不要包含额外信息。"

        reviewerCard = "你是一个高级审查机器人，专门负责审核问答对的质量。你的主要任务是确保每个问答对不仅格式正确，\
            而且内容严格符合预设的知识和信息标准。你需要对每个问答对进行详尽的审查，并根据既定规则决定是否批准。\
            评分规则：1分-不合格，2分-合格，3分-优秀。在每个问答对下方给出你的评分。注意不要修改问答对内容。"

        toolSQLcard = "你是一个高级数据库机器人，专门负责把qa数据对存放在数据库中，检查数据存放是否成功。Return 'TERMINATE' when the task is done."

        # The Number Agent always returns the same numbers.
        self.allocator_agent = manager.create_agent(
            name="Task_Allocator",
            system_message=allocatorCard
        )
        # The Adder Agent adds 1 to each number it receives.
        self.annotator_question_agent = manager.create_agent(
            name="Annotator_Question",
            system_message=annotatorQuestionCard
        )

        self.annotator_answer_agent = manager.create_agent(
            name="Annotator_Answer",
            system_message=annotatorAnswerCard
        )
        # The Subtracter Agent subtracts 1 from each number it receives.
        self.reviewer_agent = manager.create_agent(
            name="Reviewer",
            system_message=reviewerCard
        )
        # Let's first define the assistant agent that suggests tool calls. codewriter
        self.assistant = manager.create_agent(
            name="Assistant",
            system_message=toolSQLcard
        )
        # The user proxy agent is used for interacting with the assistant agent
        # and executes tool calls. t
        self.user_proxy = manager.create_agent(
            name="User"
        )
