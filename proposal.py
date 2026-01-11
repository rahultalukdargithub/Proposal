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
# col1, col2 = st.columns(2)

# with col1:
#     yes = st.button("Yes, I feel the same 💖")

# with col2:
#     no = st.button("I need some time 🌸")

# # ---------------- Response Box ----------------
# if yes:
#     st.balloons()
#     st.success(
#     "You have no idea how happy this makes me ❤️\n\n"
#     "I promise to be genuine, respectful, and present."
#     "Whatever this becomes, I’m really glad it begins with you.")

# elif no:    
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
from pathlib import Path

# ---------------- CONFIG ----------------
PASSWORD = "onlyyou"   # change this
HER_NAME = "You"       # optional personalization

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="For You ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
for key in ["unlocked", "story_done", "response", "show_secret"]:
    if key not in st.session_state:
        st.session_state[key] = False if key != "response" else None

# ---------------- CSS ----------------
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
    animation: fadeIn 1s ease;
}

.center { text-align: center; }

.question {
    font-size: 34px;
    color: #c9184a;
    font-weight: 600;
    margin-top: 40px;
}

.response-box {
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(14px);
    padding: 35px;
    border-radius: 22px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    font-size: 20px;
    animation: fadeUp 1s ease;
}

.letter {
    font-family: 'Georgia', serif;
    font-size: 21px;
    line-height: 2;
}

.footer {
    text-align: center;
    color: #777;
    margin-top: 50px;
}

button {
    height: 3em;
    font-size: 18px !important;
    border-radius: 14px !important;
}

@keyframes fadeIn {
    from {opacity:0}
    to {opacity:1}
}

@keyframes fadeUp {
    from {opacity:0; transform:translateY(20px)}
    to {opacity:1; transform:translateY(0)}
}

.heart {
    position: fixed;
    bottom: -20px;
    font-size: 22px;
    opacity: 0.5;
    animation: floatUp 10s linear infinite;
}

@keyframes floatUp {
    from {transform: translateY(0)}
    to {transform: translateY(-120vh)}
}
</style>
""", unsafe_allow_html=True)

# ---------------- FLOATING HEARTS ----------------
for i in range(12):
    st.markdown(
        f"<div class='heart' style='left:{i*8}%; animation-delay:{i}s'>❤️</div>",
        unsafe_allow_html=True
    )

# ---------------- PASSWORD LOCK ----------------
if not st.session_state.unlocked:
    st.markdown("<div class='title'>For You ❤️</div>", unsafe_allow_html=True)
    pwd = st.text_input("A small lock, just for us", type="password")
    if pwd == PASSWORD:
        st.session_state.unlocked = True
        st.rerun()
    st.stop()

# ---------------- MUSIC (plays once) ----------------
if Path("love_music.mp3").exists():
    st.audio("love_music.mp3", loop=True)

# ---------------- TYPEWRITER ----------------
def type_text(text, delay=0.03):
    placeholder = st.empty()
    typed = ""
    for c in text:
        typed += c
        placeholder.markdown(f"<div class='text'>{typed}</div>", unsafe_allow_html=True)
        time.sleep(delay)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>Hey… ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>I wanted to say this, properly</div>", unsafe_allow_html=True)

# ---------------- STORY ----------------
if not st.session_state.story_done:
    type_text(
        "I don’t know when it started. Maybe during one of our random conversations. "
        "Maybe during a quiet moment that didn’t seem important at the time."
    )
    st.write("")
    type_text(
        "But slowly, you became the person I look for in my day. "
        "The one I want to tell things to first."
    )
    st.write("")
    type_text(
        "With you, things feel lighter. Smiles come easier. "
        "Even ordinary days feel a little warmer."
    )
    st.write("")
    type_text(
        "I can truly see myself with you. "
        "And somewhere deep down, I feel that you might feel the same too."
    )
    st.write("")
    type_text(
        "I like you. Not casually. Not temporarily. "
        "But in a way that feels calm, real, and sincere."
    )
    st.session_state.story_done = True
else:
    st.markdown("""
    <div class='text'>
    I don’t know when it started, but you slowly became the person I look for in my day.
    With you, things feel lighter, calmer, and more real.
    </div>
    """, unsafe_allow_html=True)

# ---------------- QUESTION ----------------
st.markdown("<div class='center question'>Would you like to be mine? ❤️</div>", unsafe_allow_html=True)

# ---------------- BUTTONS ----------------
if st.session_state.response is None:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, I feel the same 💖"):
            st.session_state.response = "yes"
    with col2:
        if st.button("I need some time 🌸"):
            st.session_state.response = "maybe"

# ---------------- RESPONSE ----------------
if st.session_state.response == "yes":
    st.balloons()
    st.markdown("""
    <div class='response-box center'>
    You just made my heart very, very happy ❤️<br><br>
    Thank you for choosing honesty and warmth.<br><br>
    There’s something more I want to show you.
    </div>
    """, unsafe_allow_html=True)

    if st.button("One last thing ✨"):
        st.session_state.show_secret = True

elif st.session_state.response == "maybe":
    st.markdown("""
    <div class='response-box center'>
    That’s completely okay ❤️<br><br>
    Take all the time you need.<br>
    My feelings are patient and sincere.
    </div>
    """, unsafe_allow_html=True)

# ---------------- SECRET PAGE ----------------
if st.session_state.show_secret:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div class='title'>For You, Always ❤️</div>", unsafe_allow_html=True)

    from PIL import Image

    image_extensions = [".jpg", ".jpeg", ".png", ".webp"]
    photos = []
    
    photos_dir = Path("photos")
    
    if photos_dir.exists():
        for p in photos_dir.iterdir():
            if p.suffix.lower() in image_extensions:
                try:
                    Image.open(p)  # validate image
                    photos.append(str(p))
                except:
                    pass  # skip invalid images safely
    
    if photos:
        st.image(photos, caption=["A memory ❤️"] * len(photos))
    else:
        st.markdown(
            "<div class='text center'>Some memories are still loading… 💗</div>",
            unsafe_allow_html=True
        )

    # Letter
    st.markdown("""
    <div class='letter response-box'>
    I don’t know where this journey will take us,
    but I know this much — I’m grateful it starts here.<br><br>

    I choose honesty. I choose kindness.
    And today, I choose you.<br><br>

    Whatever comes next, I hope we walk into it together.
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<div class='footer'>Made with courage, care, and a full heart ✨</div>", unsafe_allow_html=True)

