import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Hey there!", page_icon="👋", layout="wide", initial_sidebar_state="expanded" )


# CONVERT IMAGE INTO BASE64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64_data}"

image_data = get_base64_image("images/lakshmi.png")


# CUSTOM CSS
st.markdown(f"""
    <style>
    .main {{
        padding: 0;
    }}
    .center-block {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 50vh;
        padding-top: 4vh;
        text-align: center;
        gap: 10px;
    }}

    .profile-pic {{
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}

    .typing {{
        font-size: 30px;
        font-weight: bold;
        color: white;
        white-space: nowrap;
        overflow: hidden;
        animation: typing 3s steps(30, end) forwards;
    }}

    @keyframes typing {{
        from {{ width: 0 }}
        to {{ width: 100% }}
    }}

    .tagline {{
        font-size: 18px;
        font-style: italic;
        color: white;
        margin-bottom: 10px;
    }}

    .stButton > button {{
        background-color: #04AA6D;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        margin-left: 15px;
        padding: 10px 24px;
        font-size: 10px;
        transition: background-color 0.3s ease;
    }}

    .stButton > button:hover {{
        background-color: #04AA6D;
    }}
    </style>
""", unsafe_allow_html=True)


# MAIN CONTENT
with st.container():
    st.markdown(f"""
        <div class="center-block">
            <img src="{image_data}" class="profile-pic" />
            <h1 class="typing">Hey, I am Lakshmi ! 👋</h1>
            <p class="tagline">Software Developer</p>
        </div>
    """, unsafe_allow_html=True)


# BUTTON CENTERED BELOW TAGLINE
    col1, col2, col3 = st.columns([4, 1, 4])
    with col2:
        if st.button("⮕"):
            st.switch_page("pages/1_Overview.py")