"""
意图定义
"""

from enum import Enum


class Intent(str, Enum):
    """
    用户意图枚举
    """

    QUERY_ORDER = "query_order"

    QUERY_TRACK = "query_track"

    QUERY_PRICE = "query_price"

    TRANSFER_HUMAN = "transfer_human"

    CHAT = "chat"