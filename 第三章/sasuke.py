import streamlit as st

# 页面配置
st.set_page_config(
    page_title="宇智波佐助 - 火影忍者",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;700;900&display=swap');

    .main {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
    }

    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
    }

    h1 {
        color: #ff6b35 !important;
        text-shadow: 0 0 20px rgba(255, 107, 53, 0.5), 0 0 40px rgba(255, 0, 0, 0.3);
        font-weight: 900 !important;
        letter-spacing: 8px;
    }

    h2 {
        color: #e94560 !important;
        border-left: 4px solid #ff6b35;
        padding-left: 15px;
        font-weight: 700 !important;
    }

    h3 {
        color: #ff6b35 !important;
        font-weight: 700 !important;
    }

    .subtitle {
        color: #a0a0a0;
        font-size: 1.2em;
        text-align: center;
        margin-top: -20px;
        margin-bottom: 40px;
        letter-spacing: 4px;
    }

    .info-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 107, 53, 0.3);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
    }

    .stat-bar {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        height: 25px;
        margin: 8px 0;
        overflow: hidden;
    }

    .stat-fill {
        height: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, #ff6b35, #e94560);
        display: flex;
        align-items: center;
        padding-left: 10px;
        color: white;
        font-weight: bold;
        font-size: 0.9em;
    }

    .quote-box {
        background: rgba(233, 69, 96, 0.1);
        border-left: 4px solid #e94560;
        padding: 20px;
        margin: 20px 0;
        font-style: italic;
        color: #f0f0f0;
        border-radius: 0 10px 10px 0;
    }

    .timeline-item {
        border-left: 3px solid #ff6b35;
        padding-left: 20px;
        margin: 15px 0;
        position: relative;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 5px;
        width: 12px;
        height: 12px;
        background: #ff6b35;
        border-radius: 50%;
        box-shadow: 0 0 10px #ff6b35;
    }

    .ability-tag {
        display: inline-block;
        background: rgba(255, 107, 53, 0.2);
        border: 1px solid #ff6b35;
        color: #ff6b35;
        padding: 5px 15px;
        border-radius: 20px;
        margin: 5px;
        font-size: 0.9em;
    }

    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ff6b35, transparent);
        margin: 40px 0;
    }

    .sharingan { color: #e94560; font-weight: bold; }
    .mangekyo { color: #9b59b6; font-weight: bold; }
    .rinnegan { color: #8e44ad; font-weight: bold; }

    .footer {
        text-align: center;
        color: #555;
        padding: 30px;
        margin-top: 50px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# 标题区域
st.markdown("""
<div style="text-align: center; padding: 40px 0;">
    <h1 style="font-size: 3.5em;">宇智波佐助</h1>
    <p class="subtitle">UCHIHA SASUKE · うちはサスケ</p>
    <p style="color: #666; font-size: 1em; letter-spacing: 2px;">「我早已闭上了双眼，我的目标只在黑暗中」</p>
</div>
""", unsafe_allow_html=True)

# 基本信息
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="info-card" style="text-align: center;">
        <h3>⚡ 基本资料</h3>
        <table style="width: 100%; color: #ccc; text-align: left;">
            <tr><td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);"><b>出身</b></td>
                <td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);">火之国·木叶隐村·宇智波一族</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);"><b>生日</b></td>
                <td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);">7月23日（狮子座）</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);"><b>身高/体重</b></td>
                <td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);">168cm / 52.2kg（第二部）</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);"><b>血型</b></td>
                <td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);">AB型</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);"><b>忍者登记号码</b></td>
                <td style="padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);">012606</td></tr>
            <tr><td style="padding: 8px;"><b>所属</b></td>
                <td style="padding: 8px;">木叶隐村 → 蛇（鹰）小队 → 木叶</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 能力参数
st.markdown("<h2>📊 能力参数</h2>", unsafe_allow_html=True)

stats_col1, stats_col2 = st.columns(2)

with stats_col1:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("### 忍者八项参数")

    stats = [
        ("忍术", 5), ("体术", 5), ("幻术", 5), ("贤", 4),
        ("力", 4), ("速", 5), ("精", 4), ("印", 5)
    ]

    for name, value in stats:
        stars = "⭐" * value
        width = value * 20
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; color: #aaa; margin-bottom: 5px;">
            <span>{name}</span><span>{stars} ({value}/5)</span>
        </div>
        <div class="stat-bar"><div class="stat-fill" style="width: {width}%;">{name} · {value}</div></div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with stats_col2:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 核心能力")

    abilities = ["雷遁", "火遁", "写轮眼", "万花筒写轮眼", "轮回眼", "须佐能乎",
                 "麒麟", "千鸟", "炎遁·加具土命", "天照", "地爆天星", "因陀罗之矢"]
    ability_html = "".join([f'<span class="ability-tag">{a}</span>' for a in abilities])
    st.markdown(ability_html, unsafe_allow_html=True)

    st.markdown("### 👁️ 瞳术进化")
    st.markdown("""
    <div style="margin-top: 10px; color: #ccc;">
        <p><span class="sharingan">● 单勾玉写轮眼</span> → 目睹灭族之夜开启</p>
        <p><span class="sharingan">● 双勾玉写轮眼</span> → 波之国战斗时开启</p>
        <p><span class="sharingan">● 三勾玉写轮眼</span> → 终结谷与鸣人一战</p>
        <p><span class="mangekyo">● 万花筒写轮眼</span> → 得知鼬的真相后开启</p>
        <p><span class="mangekyo">● 永恒万花筒</span> → 移植鼬的眼睛</p>
        <p><span class="rinnegan">● 轮回眼</span> → 获得六道仙人力量</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 人生历程
st.markdown("<h2>🗡️ 人生历程</h2>", unsafe_allow_html=True)

timeline_col1, timeline_col2 = st.columns(2)

with timeline_col1:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("### 童年与复仇之路")

    events_left = [
        ("灭族之夜", "宇智波鼬屠戮全族，仅留佐助一人。佐助立下誓言：杀死那个男人，复兴宇智波一族。"),
        ("忍者学校毕业", "以第一名的成绩毕业，被分配到第七班，与漩涡鸣人、春野樱成为队友，指导上忍为旗木卡卡西。"),
        ("中忍考试", "大蛇丸在死亡森林施加天之咒印。佐助逐渐感受到与鸣人的差距，内心开始动摇。"),
        ("叛逃木叶", "终结谷与鸣人一战后，为追求力量叛逃至大蛇丸处，成为\"蛇\"小队成员。")
    ]

    for title, desc in events_left:
        st.markdown(f"""
        <div class="timeline-item">
            <h4 style="color: #ff6b35; margin: 0;">{title}</h4>
            <p style="color: #aaa; margin: 5px 0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with timeline_col2:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("### 真相与救赎")

    events_right = [
        ("得知真相", "杀死鼬后，从带土口中得知灭族真相——鼬的一切都是为了保护木叶和弟弟。世界观崩塌。"),
        ("\"鹰\"小队", "组建\"鹰\"小队（水月、香燐、重吾），目标转向摧毁木叶，为鼬复仇。"),
        ("第四次忍界大战", "与秽土转生的鼬重逢，被鼬点醒。与鸣人联手对抗宇智波斑和大筒木辉夜。"),
        ("最终决战", "终结谷与鸣人最后一战，双方各断一臂。最终认可鸣人，回归木叶。")
    ]

    for title, desc in events_right:
        st.markdown(f"""
        <div class="timeline-item">
            <h4 style="color: #e94560; margin: 0;">{title}</h4>
            <p style="color: #aaa; margin: 5px 0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 经典语录
st.markdown("<h2>💬 经典语录</h2>", unsafe_allow_html=True)

quotes_col1, quotes_col2, quotes_col3 = st.columns(3)

quotes = [
    ("我早已闭上了双眼，我的目标只在黑暗中。", "叛逃时期"),
    ("我失去过所有东西，所以我不想再看到我最珍惜的伙伴们，死在我的面前。", "波之国篇"),
    ("因为你... 说我是你最好的朋友。", "终结谷之战")
]

for col, (quote, source) in zip([quotes_col1, quotes_col2, quotes_col3], quotes):
    with col:
        st.markdown(f"""
        <div class="quote-box">
            "{quote}"
            <p style="text-align: right; color: #666; margin-top: 10px; font-size: 0.9em;">— {source}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 人际关系
st.markdown("<h2>🔗 羁绊与关系</h2>", unsafe_allow_html=True)

relation_col1, relation_col2, relation_col3 = st.columns(3)

relations = [
    ("🌀 漩涡鸣人", "\"最好的朋友\"也是\"最大的对手\"",
     "从互相看不顺眼到彼此最深的羁绊。鸣人是唯一能理解佐助痛苦的人，也是将他从黑暗中拉回的人。"),
    ("🌸 春野樱", "\"谢谢你\" — 唯一的爱",
     "从小樱的执着等待到最终走到一起。佐助虽不擅表达，但小樱是他选择回归的理由之一。"),
    ("🌙 宇智波鼬", "\"无论你变成什么样，我都会永远爱你\"",
     "从憎恨到理解，从复仇到继承。鼬用生命守护的和平，最终由佐助来延续。")
]

for col, (title, subtitle, desc) in zip([relation_col1, relation_col2, relation_col3], relations):
    with col:
        st.markdown(f"""
        <div class="info-card" style="text-align: center;">
            <h3>{title}</h3>
            <p style="color: #aaa;">{subtitle}</p>
            <p style="color: #666; font-size: 0.9em;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# 页脚
st.markdown("""
<div class="footer">
    <p style="color: #444; font-size: 0.9em;">🔥 宇智波佐助 · Uchiha Sasuke 🔥</p>
    <p style="color: #333; font-size: 0.8em;">"我可是拼了命去做的，不要用'天才'两个字抹杀我的努力"</p>
    <p style="color: #222; font-size: 0.7em; margin-top: 20px;">Made with Streamlit | Naruto Fan Page</p>
</div>
""", unsafe_allow_html=True)