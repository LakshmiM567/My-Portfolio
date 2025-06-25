import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Contact Me!!",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# TITLE
st.markdown("<h1 style='color:greenyellow;'>Get In Touch With Me!</h1>", unsafe_allow_html=True)

# BACKGROUND
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://www.transparenttextures.com/patterns/grainy.png');
        background-color: #000000;
        background-repeat: repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# CONTACT FORM HTML
contact_form = """
<form action="https://formsubmit.co/lakshmipmurali567@gmail.com" method="POST" target="_blank">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_next" value="https://my-portfolio-gfwfww4chtrt2h5gj64ta.streamlit.app/#thank-you">

    <input type="text" name="name" placeholder="Enter your name" required 
        style="width: 100%; padding: 10px; border-radius: 5px; margin-bottom: 10px; border: 1px solid #ccc;"><br>
    <input type="email" name="email" placeholder="Enter email ID" required 
        style="width: 100%; padding: 10px; border-radius: 5px; margin-bottom: 10px; border: 1px solid #ccc;"><br>
    <textarea name="message" placeholder="Type your message here!" required 
        style="width: 100%; height: 150px; padding: 10px; border-radius: 5px; margin-bottom: 10px; border: 1px solid #ccc;"></textarea><br>

    <button type="submit" 
        style="background-color: #04AA6D; color: white; font-weight: bold; border: none; border-radius: 8px; padding: 10px 24px;">
        Send
    </button>
</form>
"""

# FORM LAYOUT
with st.container():
    st.write("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(contact_form, unsafe_allow_html=True)
    with col2:
        st.empty()

# BACK BUTTON
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #04AA6D;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        margin-top: 50px;
        padding: 10px 24px;
        font-size: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    if st.button("⬅"):
        st.switch_page("pages/1_Overview.py")
