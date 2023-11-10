from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -----LOAD ASSETS----- 
lottie_coding = load_lottieurl("https://lottie.host/a9854fdc-628b-4ede-9765-997723aebaeb/YjK93folUl.json")

#-----About Section-----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("I'm John, and I'm here to transform your digital dreams into reality. As a seasoned software developer, I specialize in crafting tailored solutions that not only meet your needs but exceed your expectations. Imagine having a partner who not only writes code but truly understands your vision. I'm that partner. With a passion for delivering exceptional user experiences and a knack for problem-solving, I thrive on making your ideas come to life. What sets me apart is my dedication to making your success my priority. I don't just build software; I create solutions that empower your business, streamline your processes, and connect with your audience on a deeper level. Let's embark on this journey together and turn your concepts into tangible, game-changing software. Feel free to reach out, and we can explore how I can add value to your project or business. Your success is my mission. Let's make it happen.")
        st.write ("##")
        st.write("[Learn More >](https://www.linkedin.com/in/john-akinola-65a3b3194/)")
        image_column, text_column = st.columns((1, 2))
with right_column:
            st.lottie(lottie_coding, height=300, key="coding")