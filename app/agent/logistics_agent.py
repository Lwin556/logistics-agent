from app.agent.dispatcher import Dispatcher
from app.agent.intent import Intent
from app.agent.intent_recognizer import IntentRecognizer
from app.llm.model import llm
from sqlalchemy.orm import Session

class LogisticsAgent:

    # def __init__(self):
    #     self.dispatcher = Dispatcher()

    def __init__(self, db: Session):  # 在初始化时传入 db
        self.db = db
        self.dispatcher = Dispatcher()

    def chat(self, message: str):

        result = IntentRecognizer.recognize(message)

        intent = result["intent"]

        entities = result["entities"]

        # 聊天交给 LLM
        if intent == Intent.CHAT:
            return llm.chat(message)

        # 业务交给 Dispatcher
        return self.dispatcher.dispatch(
            self.db,
            intent,
            entities
        )


# agent = LogisticsAgent()