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

#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
#创建客户端对象

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    #if message["role"] == "user":
        #st.chat_message("user").write(message["content"])
    #else:
        #st.chat_message("assistant").write(message["content"])
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#输入框

prompt = st.chat_input("请输入您的问题")
if prompt:#字符串自动转换布尔值
    st.chat_message("user").write(prompt)
    print("------------->调用AI大模型,提示词",prompt)
    # 添加用户消息到会话状态
    st.session_state.messages.append({"role": "user", "content": prompt})
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
    # 添加AI助手消息到会话状态
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})


