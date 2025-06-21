import time
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# SET PAGE CONFIG
st.set_page_config(
    page_title="All about me!",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("<h1 style='color:greenyellow;'>Get To Know Me!</h1>", unsafe_allow_html=True)


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


# EMBED LOTTIE ANIMATIONS
def load_lottie_animation(url):
    return f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.6/lottie.min.js"></script>
    </head>
    <body style="background: transparent; margin: 0;">
        <div id="lottie-container" style="width:100%; height:300px;"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
        </script>
    </body>
    </html>
    """


# ANIMATION AND IMAGE URL
lottie_coding_url = "https://lottie.host/65e15d96-f94c-4bd2-8d0b-2208825a0b8d/MPUvNxB3eo.json"
img_lottie_animation = Image.open("images/drones.png")
img_lottie_animation1 = Image.open("images/face_rec.png")
img_lottie_animation2 = Image.open("images/rtclock.jpg")
profile_picture = Image.open("images/lakshmi.png")


# ABOUT ME
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown('<h2 style="color: beige;">About Me</h2>', unsafe_allow_html=True)
        st.markdown(
            """
                <p style="color: beige; font-size: 18px;">
                    I am an aspiring software developer with knowledge in Python. My main areas of focus include:
                </p>
            
            <ul style="color: beige; font-size: 16px;">
                <li><span style="color: greenyellow;">Odoo Development</span>: Building custom modules, especially in the domain of fleet auctions, and understanding core Odoo workflows.</li>
                <li><span style="color: greenyellow;">Web Development</span>: Skilled in HTML5, CSS3, and JavaScript for front-end development. Built basic web apps using MERN stack.</li>
                <li><span style="color: greenyellow;">Backend and Databases</span>: Proficient in Python and PostgreSQL for database-driven applications.</li>
                <li><span style="color: greenyellow;">IoT & Embedded Systems</span>: Designed and implemented Arduino-based projects with real-time systems.</li>
                <li><span style="color: greenyellow;">Problem Solving</span>: Comfortable applying Object-Oriented Programming (OOP) concepts to develop logical and modular code.</li>
            </ul>
            """,
        unsafe_allow_html=True
)


with right_column:


# TRANSPARENT BG FOR LOTTIE ANIMATION
    st.components.v1.html(load_lottie_animation(lottie_coding_url), height=300)

with st.container():
    st.write("---")
    st.markdown('<h2 style="color: beige;">My Experience and Certifications</h2>', unsafe_allow_html=True)
    
    st.markdown('<div style="font-size: 24px; font-weight: 600; color: greenyellow;">Odoo Developer Trainee</h2>', unsafe_allow_html=True)
    st.write("""
    <ul style="color: beige;">
        <li>Gained hands-on experience working on real Odoo modules.</li>
        <li>Developed and implemented a Fleet Auction Module, which allowed users to place bids and select the highest bidder as a customer.</li>
        <li>Worked on module customization, ORM, and understanding Odoo's MVC structure.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div style="font-size: 24px; font-weight: 600; color: greenyellow;">MERN Stack Intern</h2>', unsafe_allow_html=True)
    st.write("""
    <ul style="color: beige;">
        <li>Built a simple Weather App using JavaScript, HTML5, and CSS3.</li>
        <li>Gained practical knowledge in frontend development and basic JavaScript usage.</li>
        <li>Understood the structure of MERN (MongoDB, Express, React, Node.js) projects.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div style="font-size: 24px; font-weight: 600; color: greenyellow;">Full Stack Java Certification</h2>', unsafe_allow_html=True)
    st.write("""
    <ul style="color: beige;">
        <li>Learned core and advanced Java concepts.</li>
        <li>Gained knowledge in JDBC, servlets, JSP, and back-end integration.</li>
        <li>Applied OOP concepts in developing backend logic and simple web applications.</li>
    </ul>
    """, unsafe_allow_html=True)


with st.container():
    st.write("---")
    st.markdown('<h2 style="color: beige;">My Projects</h2>', unsafe_allow_html=True)
    st.write("##")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.markdown('<div style="font-size: 24px; font-weight: 600; color: greenyellow;">🚁 Drone Based Drug Delivery System</div>', unsafe_allow_html=True)
        st.write("""
        <ul style="color: beige; font-size: 16px;">
            <li>💡 Designed a prototype using an <strong>autonomous routing algorithm</strong>.</li>
            <li>🛣️ Simulated delivery paths and <strong>optimized routes</strong> for efficient transportation.</li>
            <li> Calculation of minimum distance and path planning simulation done using Folium and Geopy in Python script.</li>
            <li> QR authentication, verification and simulation implemented using OpenCV and Pybazar.</li>
            <li> Programmed hardware using Raspberry Pi and Raspberry Pi Imager.</li>
            <li>🏥 Focus on <strong>medical supply delivery</strong> in emergency or remote areas.</li>
        </ul>
        """, unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation1)
    with text_column:
        st.markdown('<div style="font-size: 24px; font-weight: 600; color: greenyellow;">🚧 Automatic Boom Barrier using Face Recognition</div>', unsafe_allow_html=True)
        st.write("""
        <ul style="color: beige; font-size: 16px;">
            <li>🚗 Built an <strong>automated access control system</strong> for secure entry into residential buildings.</li>
            <li> Created a boom barrier model and enabled face recognition using a laptop camera.</li>
            <li> Machine learning algorithm was used for training the system of specific features. System recognizes the face of specific person based on previously fed datasets.</li>
            <li> Once the system verifies detection the motor initiates movement of boom barrier.</li>
            <li> Arduino was used for the barrier system.</li>
            <li>📷 Implemented using <strong>Python</strong> libraries.</li>
        </ul>
        """, unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation2)
    with text_column:
        st.markdown('<div style="font-size: 24px; font-weight: 600; color: greenyellow;">⏰ Simulation using Arduino</div>', unsafe_allow_html=True)
        st.write("""
        <ul style="color: beige; font-size: 16px;">
            <li>🧠 Built using <strong>Arduino Uno</strong> and a real-time clock (RTC) module.</li>
            <li>📟 Displayed current time on an LCD and <strong>retained time tracking</strong> even when unplugged.</li>
        </ul>
        """, unsafe_allow_html=True)


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
    col1, col2, col3 = st.columns([1, 10, 1])
    
    with col1:
        if st.button("⬅"):
            st.switch_page("0_Hey there!.py")

    with col3:
        if st.button("⮕"):
            st.switch_page("pages/2_Contact.py")