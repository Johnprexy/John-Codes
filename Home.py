from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="House of Joy", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("/home/dell/Desktop/web/style/style.css")        


# -----LOAD ASSETS----- 
lottie_coding = load_lottieurl("https://lottie.host/a9854fdc-628b-4ede-9765-997723aebaeb/YjK93folUl.json")
img_contact_form = Image.open("/home/dell/Desktop/web/Images/calculator.jpeg")
img_about_form = Image.open("/home/dell/Desktop/web/Images/JOHN.png")


#-----Header Section-----
with st.container():
    st.header("Welcome to My Personal Website!")
    st.write("Hi my name is John! :wave:")
    st.write("I am a Software Engineer")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_about_form)
        


#-----PROJECTS-----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("Below are some of my projects that I have worked on.")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader('Created a calculator using Python')
        st.write("##")
        st.write(
            """
            I have meticulously designed and implemented a user-friendly Graphical User Interface (GUI) for a calculator using Python.

Here are the key features and aspects of the calculator GUI:

**Intuitive User Interface:**
I focused on creating an intuitive and user-friendly interface to ensure that users, regardless of their technical background, can easily navigate and perform calculations seamlessly.

**Functionalities:**
The calculator incorporates a comprehensive set of functions, including basic arithmetic operations (addition, subtraction, multiplication, and division) as well as additional functionalities such as percentage calculations and square root.

**Error Handling:**
To enhance user experience, I implemented robust error handling mechanisms. This ensures that the calculator gracefully handles various inputs, preventing unexpected errors and offering a smooth user interaction.

**Responsive Design:**
The GUI is designed to be responsive, adapting to different screen sizes and resolutions. This ensures a consistent and enjoyable user experience across various devices.

**Aesthetic Appeal:**
I paid careful attention to the visual elements, choosing a clean and modern design to enhance the overall aesthetic appeal of the calculator. The layout and color scheme were selected to create a professional and visually pleasing appearance.

**Customization Options:**
Understanding the importance of customization, I integrated options for users to personalize the calculator based on their preferences. This includes the ability to adjust themes and modify certain display settings.

**Code Efficiency:**
The underlying Python code has been optimized for efficiency and readability. This not only facilitates easy maintenance but also allows for future enhancements and modifications.


            """
        )
        st.markdown("[Learn More >](https://github.com/Johnprexy/John-Codes/blob/a6efae0704d73747021db20350d122f04c5db4b6/calculator.py)")
#-----Contact----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
     
    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/akinolajohnayomide@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()