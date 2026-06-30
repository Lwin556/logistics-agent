"""
物流智能客服工具集

这里先使用模拟数据，
后续会替换为数据库查询。
"""

from typing import Dict


# ===========================
# 模拟订单数据
# ===========================

MOCK_ORDERS = {
    "SF123456": {
        "order_no": "SF123456",
        "status": "运输中",
        "city": "杭州转运中心",
        "eta": "明天下午"
    },
    "YD888888": {
        "order_no": "YD888888",
        "status": "已签收",
        "city": "北京市朝阳区",
        "eta": "已送达"
    }
}


# ===========================
# 查询订单
# ===========================

def query_order(order_no: str) -> Dict:
    """
    查询订单信息
    """

    order = MOCK_ORDERS.get(order_no)

    if order:
        return order

    return {
        "error": "订单不存在"
    }


# ===========================
# 查询物流轨迹
# ===========================

def query_track(order_no: str):
    """
    查询物流轨迹
    """

    tracks = {
        "SF123456": [
            "深圳仓库 已发货",
            "广州转运中心",
            "杭州转运中心",
            "派送中"
        ]
    }

    return tracks.get(
        order_no,
        ["暂无物流信息"]
    )


# ===========================
# 运费计算
# ===========================

def query_price(
    origin: str,
    destination: str,
    weight: float
):
    """
    运费计算
    """

    first_weight = 12
    extra_weight = 6

    if weight <= 1:
        price = first_weight
    else:
        price = first_weight + (weight - 1) * extra_weight

    return {
        "origin": origin,
        "destination": destination,
        "weight": weight,
        "price": round(price, 2)
    }


# ===========================
# 转人工
# ===========================

def transfer_to_human():
    """
    转人工客服
    """

    return {
        "message": "正在为您转接人工客服，请稍候..."
    }