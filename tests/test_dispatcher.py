from app.agent.dispatcher import Dispatcher
from app.agent.intent import Intent

dispatcher = Dispatcher()

print(
    dispatcher.dispatch(
        Intent.QUERY_ORDER,
        {
            "order_no": "SF123456"
        }
    )
)