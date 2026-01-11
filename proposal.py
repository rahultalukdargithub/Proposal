import streamlit as st
from datetime import datetime

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="For You ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
body {
    background-color: #fff0f5;
}
.main-title {
    text-align: center;
    font-size: 48px;
    color: #e75480;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #555;
}
.section {
    font-size: 20px;
    line-height: 1.8;
    color: #333;
}
.heart {
    text-align: center;
    font-size: 40px;
}
.question {
    text-align: center;
    font-size: 32px;
    color: #e75480;
    font-weight: bold;
}
.footer {
    text-align: center;
    font-size: 18px;
    color: #777;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<div class='main-title'>Hey, My Love ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>I made something special… just for you</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- Story Section ----------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write(
    "From the moment you walked into my life, things changed in the most beautiful way. "
    "You became my calm in chaos, my smile on difficult days, and my favorite person without even trying."
)
st.write(
    "Every conversation, every laugh, every silent moment with you feels like home. "
    "And today, I want to tell you something that my heart has known for a long time."
)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.markdown("<div class='heart'>💗 💗 💗</div>", unsafe_allow_html=True)
st.write("")

# ---------------- Memory Section ----------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write(
    "I don’t promise perfection. But I promise effort. "
    "I promise to stand by you, learn with you, grow with you, and choose you every single day."
)
st.write(
    "Life will have ups and downs, but I want all of them — with you."
)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- Proposal Question ----------------
st.markdown("<div class='question'>Will you marry me? 💍</div>", unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2)

with col1:
    yes = st.button("Yes ❤️")

with col2:
    no = st.button("Let me think 🙈")

# ---------------- Response ----------------
if yes:
    st.balloons()
    st.success(
        "You just made me the happiest person alive ❤️\n\n"
        "I can’t wait to start this forever with you."
    )

elif no:
    st.info(
        "That’s okay ❤️\n\n"
        "Take all the time you need. My heart is right here, waiting for you."
    )

# ---------------- Footer ----------------
st.write("")
st.write("")
today = datetime.now().strftime("%d %B %Y")
st.markdown(
    f"<div class='footer'>Made with all my love • {today}</div>",
    unsafe_allow_html=True
)
