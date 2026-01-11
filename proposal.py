import streamlit as st
import time

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="For You ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- Session State ----------------
if "response" not in st.session_state:
    st.session_state.response = None

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #fff1f5, #fde2e4);
}
.title {
    text-align: center;
    font-size: 52px;
    color: #d6336c;
    font-weight: 700;
}
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #555;
}
.text {
    font-size: 20px;
    line-height: 1.9;
    color: #333;
}
.center {
    text-align: center;
}
.question {
    font-size: 34px;
    color: #c9184a;
    font-weight: 600;
}
.footer {
    font-size: 16px;
    color: #777;
    text-align: center;
}
button {
    height: 3em;
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Helper: Typewriter Effect ----------------
def type_text(text, delay=0.03):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(
            f"<div class='text'>{typed}</div>",
            unsafe_allow_html=True
        )
        time.sleep(delay)

# ---------------- Header ----------------
st.markdown("<div class='title'>Hey… ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>I hope you read this slowly</div>", unsafe_allow_html=True)
st.write("")
time.sleep(1)

# ---------------- Main Message ----------------
type_text(
    "I don’t know when it happened. "
    "Maybe it was during one of our random conversations, "
    "or one of those quiet moments where nothing special was happening — yet everything felt right."
)

st.write("")
type_text(
    "Somehow, you became my favorite thought. "
    "The person I want to tell things to first. "
    "The calm I didn’t know I was looking for."
)

st.write("")
type_text(
    "With you, things feel lighter. "
    "Smiles come easier. "
    "And even ordinary days feel a little more beautiful."
)

st.write("")
st.markdown("<div class='center'>✨ ✨ ✨</div>", unsafe_allow_html=True)
st.write("")

type_text(
    "I can truly see myself with you. "
    "And somewhere deep down, I feel that you might feel the same too."
)

st.write("")
type_text(
    "I’m not here with promises of perfection. "
    "I’m just here with honesty."
)

st.write("")
type_text(
    "I like you. Not casually. Not temporarily. "
    "But in a way that feels real, warm, and intentional."
)

st.write("")
type_text(
    "So today, I wanted to ask you something — "
    "not to rush you, not to pressure you — "
    "just to be honest about how I feel."
)

st.write("")
st.write("")

# ---------------- Proposal Question ----------------
st.markdown(
    "<div class='center question'>Would you like to be mine? ❤️</div>",
    unsafe_allow_html=True
)
st.write("")

# ---------------- Buttons ----------------
if st.session_state.response is None:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes, I feel the same 💖"):
            st.session_state.response = "yes"

    with col2:
        if st.button("I need some time 🌸"):
            st.session_state.response = "maybe"

# ---------------- Response ----------------
if st.session_state.response == "yes":
    st.balloons()
    st.markdown("""
    <div class='text center'>
    You have no idea how much this means to me.<br><br>
    I promise to respect you, care for you, and be genuine with you — always.<br><br>
    Whatever this becomes, I’m really glad it starts with you ❤️
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.response == "maybe":
    st.markdown("""
    <div class='text center'>
    That’s completely okay ❤️<br><br>
    Take all the time you need.<br>
    My feelings are patient and sincere.
    </div>
    """, unsafe_allow_html=True)

# ---------------- Footer ----------------
st.write("")
st.write("")
st.markdown(
    "<div class='footer'>Made with sincerity, not shortcuts ✨</div>",
    unsafe_allow_html=True
)
