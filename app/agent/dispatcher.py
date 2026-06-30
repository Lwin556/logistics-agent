from sqlalchemy.orm import Session

from app.agent.intent import Intent
from app.services.order_service import OrderService
from app.agent.tools import transfer_to_human


class Dispatcher:

    def dispatch(
        self,
        db: Session,
        intent,
        entities,
    ):
        """
        分发任务
        """
        # 🔍 添加调试信息
        print(f"=== DEBUG: dispatch called ===")
        print(f"intent: {intent}")
        print(f"intent type: {type(intent)}")
        print(f"entities: {entities}")
        print(f"entities type: {type(entities)}")
        print(f"QUERY_ORDER: {'QUERY_ORDER'}")
        print(f"intent == 'QUERY_ORDER': {intent == 'QUERY_ORDER'}")
        print(f"intent == Intent.QUERY_ORDER: {intent == Intent.QUERY_ORDER}")
        print("================================")

        # =========================
        # 查询订单
        # =========================
        # if intent == "QUERY_ORDER":
        if intent == Intent.QUERY_ORDER:
            order_no = entities.get("order_no")

            if not order_no:
                return "请提供订单号，例如 SF123456"

            result = OrderService.get_order_detail(
                db=db,
                order_no=order_no
            )

            if not result:
                return f"未找到订单：{order_no}"

            order = result["order"]
            tracks = result["tracks"]

            track_text = "\n".join([
                f"{t.track_time} | {t.city} | {t.remark}"
                for t in tracks
            ])

            return f"""
📦 订单号：{order.order_no}
🚚 状态：{order.status}
📍 当前城市：{order.city}
⏰ 预计送达：{order.eta}

🧭 物流轨迹：
{track_text}
"""

        # =========================
        # 默认兜底
        # =========================
        return "暂不支持该查询类型"