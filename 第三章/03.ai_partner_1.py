import streamlit as st
import os
from openai import OpenAI
#设置页面配置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="👽️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

    }
)

#大标题
st.title("AI智能伴侣")

st.logo("resources/logo.png")

#系统提示词

system_prompt = "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题"

#创建客户端对象

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#输入框

prompt = st.chat_input("请输入您的问题")
if prompt:#字符串自动转换布尔值
    st.chat_message("user").write(prompt)
    print("------------->调用AI大模型,提示词",prompt)
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system","content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    print("<------------------ 大模型返回的结果", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)


