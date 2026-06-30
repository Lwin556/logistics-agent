"""
model.py

负责：
1. 初始化 OpenAI Client
2. 提供统一的大模型调用方法
3. 后续方便切换 DeepSeek、Qwen、Azure OpenAI 等模型
"""

import os
from openai import OpenAI


class LLMModel:
    """
    大模型统一封装
    """

    def __init__(self):
        # API Key
        self.api_key = os.getenv("QIANWEN_API_KEY")

        if not self.api_key:
            raise ValueError("请先配置 OPENAI_API_KEY 环境变量")

        # Base URL
        # 如果使用 OpenAI 官方接口，可删除这一行
        self.base_url = os.getenv(
            "OPENAI_BASE_URL",
            "https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

        # 模型名称
        self.model = os.getenv(
            "MODEL_NAME",
            "deepseek-v4-pro"
        )

        # 创建 Client
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def chat(self, message: str) -> str:
        """
        普通聊天
        """

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": "你是一名专业物流客服。"
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.choices[0].message.content

    def chat_with_messages(self, messages: list) -> str:
        """
        多轮聊天
        """

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.3,
            messages=messages
        )

        return response.choices[0].message.content

    def get_model_name(self):
        """
        返回当前模型名称
        """
        return self.model
# 单例对象（整个项目共用）
llm = LLMModel()