# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

#创建客户端对象
client = OpenAI(    api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#与AI交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题"},
        {"role": "user", "content": "你是谁"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)
#输出返回结果,类似于解析JSON
print(response.choices[0].message.content)