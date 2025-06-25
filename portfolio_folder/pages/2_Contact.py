import streamlit as st


# SET PAGE CONFIG
st.set_page_config(
    page_title="Contact Me!!",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded" 
)

st.markdown("<h1 style='color:greenyellow;'>Get In Touch With Me!</h1>", unsafe_allow_html=True)


# BACKGROUND COLOR
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://www.transparenttextures.com/patterns/grainy.png');
        background-color: #000000; 
        background-repeat: repeat;  /* Ensures the texture repeats */
        background-attachment: fixed; /* Keeps the background fixed while scrolling */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# USE LOCAL CSS FOR CONTACT FORM
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("portfolio_folder/style/style.css")


# CONTACT
with st.container():
    st.write("---")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/lakshmipmurali567@gmail.com" method="POST" target="_blank">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://lakshmimurali-portfolio.streamlit.app/#thank-you">
        <input type="text" name="name" placeholder="Enter your name" required>
        <input type="email" name="email" placeholder="Enter email ID" required>
        <textarea name="message" placeholder="Type your message here!" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


# BUTTON 
st.markdown(f"""
    <style>
    .main {{
        padding: 0;
    }}
    
    .stButton > button {{
        background-color: #04AA6D;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        margin-top: 100px;
        padding: 10px 24px;
        font-size: 10px;
        transition: background-color 0.3s ease;
    }}

    .stButton > button:hover {{
        background-color: #04AA6D;
    }}
    </style>
""", unsafe_allow_html=True)

with st.container():
    if st.button("⬅"):
        st.switch_page("pages/1_Overview.py")
