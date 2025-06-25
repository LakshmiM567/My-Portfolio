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


# CONTACT
google_form_url = "google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLS.../viewform?embedded=true"

st.markdown("""
<div style="margin-top: 30px;">
<iframe src="{form_url}" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">
Loading…
</iframe>
</div>
""".format(form_url=google_form_url), unsafe_allow_html=True)"  # <-- Replace this with your actual form URL

st.markdown("""
<div style="margin-top: 30px;">
<iframe src="{form_url}" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">
Loading…
</iframe>
</div>
""".format(form_url=google_form_url), unsafe_allow_html=True)


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
