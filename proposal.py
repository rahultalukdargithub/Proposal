# import streamlit as st
# import time

# # ---------------- Page Config ----------------
# st.set_page_config(
#     page_title="For You ❤️",
#     page_icon="❤️",
#     layout="centered"
# )

# # ---------------- Session State ----------------
# if "response" not in st.session_state:
#     st.session_state.response = None

# if "story_done" not in st.session_state:
#     st.session_state.story_done = False

# # ---------------- Custom CSS ----------------
# st.markdown("""
# <style>
# body {
#     background: linear-gradient(to bottom, #fff1f5, #fde2e4);
# }
# .title {
#     text-align: center;
#     font-size: 52px;
#     color: #d6336c;
#     font-weight: 700;
# }
# .subtitle {
#     text-align: center;
#     font-size: 22px;
#     color: #555;
# }
# .text {
#     font-size: 20px;
#     line-height: 1.9;
#     color: #333;
# }
# .center {
#     text-align: center;
# }
# .question {
#     font-size: 34px;
#     color: #c9184a;
#     font-weight: 600;
# }
# .response-box {
#     background-color: white;
#     padding: 30px;
#     border-radius: 16px;
#     box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
#     font-size: 20px;
# }
# .footer {
#     font-size: 16px;
#     color: #777;
#     text-align: center;
# }
# button {
#     height: 3em;
#     font-size: 18px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- Typewriter ----------------
# def type_text(text, delay=0.03):
#     placeholder = st.empty()
#     typed = ""
#     for char in text:
#         typed += char
#         placeholder.markdown(
#             f"<div class='text'>{typed}</div>",
#             unsafe_allow_html=True
#         )
#         time.sleep(delay)

# # ---------------- Header ----------------
# st.markdown("<div class='title'>Hey… ❤️</div>", unsafe_allow_html=True)
# st.markdown("<div class='subtitle'>I hope you read this slowly</div>", unsafe_allow_html=True)
# st.write("")

# # ---------------- Story (Runs ONLY once) ----------------
# if not st.session_state.story_done:
#     type_text(
#         "I don’t know when it happened. "
#         "Maybe it was during one of our random conversations, "
#         "or one of those quiet moments where nothing special was happening — yet everything felt right."
#     )

#     st.write("")
#     type_text(
#         "Somehow, you became my favorite thought. "
#         "The person I want to tell things to first. "
#         "The calm I didn’t know I was looking for."
#     )

#     st.write("")
#     type_text(
#         "With you, things feel lighter. "
#         "Smiles come easier. "
#         "And even ordinary days feel a little more beautiful."
#     )

#     st.write("")
#     st.markdown("<div class='center'>✨ ✨ ✨</div>", unsafe_allow_html=True)
#     st.write("")

#     type_text(
#         "I can truly see myself with you. "
#         "And somewhere deep down, I feel that you might feel the same too."
#     )

#     st.write("")
#     type_text(
#         "I like you. Not casually. Not temporarily. "
#         "But in a way that feels real, warm, and intentional."
#     )

#     st.write("")
#     type_text(
#         "So today, I just wanted to be honest with you."
#     )

#     st.session_state.story_done = True

# else:
#     # Static version (no typing, no delay)
#     st.markdown("""
#     <div class='text'>
#     I don’t know when it happened. Maybe it was during one of our random conversations,
#     or one of those quiet moments where nothing special was happening — yet everything felt right.<br><br>

#     Somehow, you became my favorite thought. The person I want to tell things to first.
#     The calm I didn’t know I was looking for.<br><br>

#     With you, things feel lighter. Smiles come easier.
#     And even ordinary days feel a little more beautiful.<br><br>

#     ✨ ✨ ✨<br><br>

#     I can truly see myself with you.
#     And somewhere deep down, I feel that you might feel the same too.<br><br>

#     I like you. Not casually. Not temporarily.
#     But in a way that feels real, warm, and intentional.<br><br>

#     So today, I just wanted to be honest with you.
#     </div>
#     """, unsafe_allow_html=True)

# # ---------------- Question ----------------
# st.write("")
# st.markdown(
#     "<div class='center question'>Would you like to be mine? ❤️</div>",
#     unsafe_allow_html=True
# )
# st.write("")

# # ---------------- Buttons ----------------
# if st.session_state.response is None:
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Yes, I feel the same 💖"):
#             st.session_state.response = "yes"

#     with col2:
#         if st.button("I need some time 🌸"):
#             st.session_state.response = "maybe"

# # ---------------- Response Box ----------------
# if st.session_state.response == "yes":
#     st.balloons()
#     st.success(
#     "You have no idea how happy this makes me ❤️\n\n"
#     "I promise to be genuine, respectful, and present."
#     "Whatever this becomes, I’m really glad it begins with you.")

# elif st.session_state.response == "maybe":
#     st.info(
#     "That’s completely okay ❤️\n\n"
#     "Take all the time you need."
#     "My feelings are patient and sincere.")

# # ---------------- Footer ----------------
# st.write("")
# st.markdown(
#     "<div class='footer'>Made with sincerity, not shortcuts ✨</div>",
#     unsafe_allow_html=True
# )



import streamlit as st
import time
import base64

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="For You ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- Session State ----------------
if "response" not in st.session_state:
    st.session_state.response = None

if "story_done" not in st.session_state:
    st.session_state.story_done = False

# ---------------- Background Music (optional) ----------------
# Add a soft instrumental mp3 if you want
# st.audio("love_music.mp3", loop=True)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #fff1f5, #fde2e4);
    overflow-x: hidden;
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
    margin-bottom: 30px;
}

.text {
    font-size: 20px;
    line-height: 1.9;
    color: #333;
    animation: fadeIn 1.2s ease;
}

.center {
    text-align: center;
}

.question {
    font-size: 34px;
    color: #c9184a;
    font-weight: 600;
    margin-top: 40px;
}

.response-box {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(12px);
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0px 15px 35px rgba(0,0,0,0.12);
    font-size: 20px;
    animation: fadeUp 1.3s ease;
}

.footer {
    font-size: 16px;
    color: #777;
    text-align: center;
    margin-top: 40px;
}

button {
    height: 3em;
    font-size: 18px !important;
    border-radius: 12px !important;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Floating hearts */
.heart {
    position: fixed;
    bottom: -10px;
    font-size: 20px;
    animation: floatUp 8s linear infinite;
    opacity: 0.6;
}

@keyframes floatUp {
    from { transform: translateY(0); }
    to { transform: translateY(-110vh); }
}
</style>
""", unsafe_allow_html=True)

# ---------------- Floating Hearts ----------------
for i in range(10):
    st.markdown(
        f"<div class='heart' style='left:{i*10}%; animation-delay:{i}s'>❤️</div>",
        unsafe_allow_html=True
    )

# ---------------- Typewriter ----------------
def type_text(text, delay=0.03):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(f"<div class='text'>{typed}</div>", unsafe_allow_html=True)
        time.sleep(delay)

# ---------------- Header ----------------
st.markdown("<div class='title'>Hey… ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>This is something I wanted to say, properly</div>", unsafe_allow_html=True)

# ---------------- Story ----------------
if not st.session_state.story_done:
    type_text(
        "I don’t know exactly when it started. "
        "Maybe during one of our random conversations. "
        "Maybe during a quiet moment that didn’t seem important at the time."
    )

    st.write("")
    type_text(
        "But somehow, you became the person I look for in my day. "
        "The one I want to share things with. "
        "The one who makes things feel lighter without even trying."
    )

    st.write("")
    type_text(
        "With you, smiles come easier. "
        "Even ordinary days feel softer and warmer."
    )

    st.write("")
    st.markdown("<div class='center'>✨ ✨ ✨</div>", unsafe_allow_html=True)

    st.write("")
    type_text(
        "I can truly see myself with you. "
        "And somewhere inside, I feel that you might feel the same too."
    )

    st.write("")
    type_text(
        "I like you. Not casually. Not briefly. "
        "But in a way that feels sincere, calm, and real."
    )

    st.write("")
    type_text(
        "So I just wanted to be honest with you."
    )

    st.session_state.story_done = True

else:
    st.markdown("""
    <div class='text'>
    I don’t know exactly when it started. Maybe during one of our random conversations,
    maybe during a quiet moment that didn’t seem important at the time.<br><br>

    Somehow, you became the person I look for in my day.
    The one I want to share things with.
    The one who makes things feel lighter without even trying.<br><br>

    With you, smiles come easier.
    Even ordinary days feel softer and warmer.<br><br>

    ✨ ✨ ✨<br><br>

    I can truly see myself with you.
    And somewhere inside, I feel that you might feel the same too.<br><br>

    I like you. Not casually. Not briefly.
    But in a way that feels sincere, calm, and real.<br><br>

    So I just wanted to be honest with you.
    </div>
    """, unsafe_allow_html=True)

# ---------------- Question ----------------
st.markdown("<div class='center question'>Would you like to be mine? ❤️</div>", unsafe_allow_html=True)
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
    <div class='response-box center'>
    You have no idea how happy this makes me ❤️<br><br>
    I promise to be honest, respectful, and present.<br><br>
    Whatever this becomes, I am really glad it begins with you.
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.response == "maybe":
    st.markdown("""
    <div class='response-box center'>
    That’s completely okay ❤️<br><br>
    Take all the time you need.<br>
    My feelings are patient and sincere.
    </div>
    """, unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("<div class='footer'>Made with care, courage, and a full heart ✨</div>", unsafe_allow_html=True)
