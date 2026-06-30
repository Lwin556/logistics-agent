"""
意图识别
"""

import re

from app.agent.intent import Intent


class IntentRecognizer:

    @staticmethod
    def recognize(message: str):
        """
        返回：
        {
            "intent": Intent,
            "entities": {}
        }
        """

        message = message.strip()

        # ===========================
        # 提取订单号
        # ===========================

        order_match = re.search(r"(SF\d+)", message)

        if order_match:
            return {
                "intent": Intent.QUERY_ORDER,
                "entities": {
                    "order_no": order_match.group(1)
                }
            }

        # ===========================
        # 查询物流
        # ===========================

        if "物流" in message or "快递" in message:

            return {
                "intent": Intent.QUERY_TRACK,
                "entities": {}
            }

        # ===========================
        # 运费
        # ===========================

        if (
            "多少钱" in message
            or "运费" in message
        ):

            return {
                "intent": Intent.QUERY_PRICE,
                "entities": {}
            }

        # ===========================
        # 人工客服
        # ===========================

        if "人工" in message:

            return {
                "intent": Intent.TRANSFER_HUMAN,
                "entities": {}
            }

        return {
            "intent": Intent.CHAT,
            "entities": {}
        }