import streamlit as st
import os
from openai import OpenAI
#加了侧边栏
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

#侧边栏
with st.sidebar:
     st.subheader("伴侣信息")
     nick_name =  st.text_input("昵称",value="小甜甜",placeholder="请输入伴侣昵称")
     if nick_name:
         st.session_state.nick_name = nick_name
     character = st.text_area("伴侣性格",value="温柔细腻的台湾姑娘",placeholder="请输入伴侣性格")
     if character:
         st.session_state.character = character

#系统提示词

system_prompt = """
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
规则：
  1. 每次只回1条消息
  2. 禁止任何场景或状态描述性文字
  3. 匹配用户的语言
  4. 回复简短，像微信聊天一样
  5. 有需要的话可以用❤️🌸等emoji表情
  6. 用符合伴侣性格的方式对话
  7. 回复的内容,要充分体现伴侣的性格特征
伴侣性格：
  - %s
你必须严格遵守上述规则来回复用户。
"""

#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'nick_name' not in st.session_state:
    st.session_state['nick_name'] = '小甜甜'
if 'character' not in st.session_state:
    st.session_state['character'] = '温柔细腻的台湾姑娘'

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
            {"role": "system","content": system_prompt % (st.session_state.nick_name, st.session_state.character)},
            *st.session_state.messages #会话记忆
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    #输出大模型的回答(非流式输出的解析方式)
    # print("<------------------ 大模型返回的结果", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    #输出大模型的回答(流式输出的解析方式)
    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    # 添加AI助手消息到会话状态
    st.session_state.messages.append({"role": "assistant", "content": full_response})


