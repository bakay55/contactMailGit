# streamlit run streamlit_app.py
# pip install streamlit

from pathlib import Path
import json
import streamlit as st

from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
import lottie
st.set_page_config(page_title="Happy Ramazan, Ya dost...", page_icon="🎄")

st.header(":mailbox: Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/hhbakay@yahoo.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)


# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "Animation-1.json"


# Use Local CSS File  # Apply custom CSS
def local_css(file_name):
    with open(file_name) as fi:
        st.markdown(f"<style>{fi.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️🎶🎶", font_size=20, falling_speed=5, animation_length="infinite")


# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["H.H.BAKAY"])[0]
# Display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"Happy Ramazan, {PERSON_NAME}! 🎄", anchor=False)
# Page configuration


# Run snowfall animation
run_snow_animation()


# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=500)

# Personalized holiday message
st.markdown(
    f"Dear {PERSON_NAME}, wishing you a wonderful holiday season filled with joy and peace. 🌟"
    )
st.write("Merhaba, Ya Ahi...")


