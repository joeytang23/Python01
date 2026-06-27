import streamlit as st

#设置页面配置
st.set_page_config(
    page_title="Streamlit 入门",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Streamlit 入门展示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit ")
#基于python代码快速构建web页面

#段落文字
st.write("布偶猫，宛如从童话中走出的精灵，又似一个蓬松柔软的“布偶”，因其在被抱起时会像玩偶一样放松地耷拉身体而得名。它们拥有丝滑柔顺的中长毛，触感如顶级丝绸，最迷人的当属那湛蓝如星空的眼眸，纯净而深邃。")
st.write("这种猫咪以其极致的温柔和黏人的性格著称。它们天性平和，对疼痛的忍耐力很高，是绝佳的家庭伴侣。布偶猫非常喜欢人的陪伴，常常像小狗一样跟随主人，在门口迎接你回家，并在你腿上安心入睡。它们不爱吵闹，叫声轻柔，对家中其他宠物和孩童展现出惊人的耐心与友善，是名副其实的“猫中天使”。")
st.write("虽然拥有一身华丽的长毛，但布偶猫的毛发不易打结，日常梳理即可。它们体型较大，成年后公猫可达十几斤，但那份优雅和憨态可掬的模样却让人爱不释手。选择布偶猫，就是选择了一份无条件、充满温暖与依恋的陪伴。")
#图片

# st.image("./resources/cat.png")
st.image("resources/cat.png")
#音频

st.audio("resources/布偶猫.MP3")
#视频

st.video("resources/视频.mp4")
#logo

st.divider()

st.logo("resources/logo.png")
#表格

student_data = {
    "姓名":["王林","李幕婉","贝洛","王一丹","张丹"],
    "学号":["2026001","2026002","2026003","2026004","2026005"],
    "语文":[98,90,59,29,80],
    "数学":[88,78,65,70,39],
    "英语":[99,89,87,59,62],
    "总分":[285,257,211,158,181]
}
st.table(student_data)

#输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名时:{name}")

#密码输入框
password = st.text_input("请输入密码",type ="password" )
st.write(f"你输入的密码时:{password}")

#单选按钮
gender = st.radio("请输入您的性别",["male","female","unknown"],index=2)
st.write(f"您的性别时:{gender}")

