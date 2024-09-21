import streamlit as st
import streamlit as st

st.set_page_config(
    page_title="Portfolio-AbhinavKR",page_icon="◼️",layout="wide"
)
st.markdown(
    """
<style>
.block-container {
    padding-top: 0rem;  /* Adjust this value as needed */
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<link href="https://fonts.googleapis.com/css2?family=Courier+New&display=swap" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

# header
st.title("hi there! 👋")
st.subheader("I'm AbhinavKR, a passionate learner and developer from India 🇮🇳")
st.write(
    "I am enthusiastic about web development, cyber security, and Linux, and I'm always eager to explore new technologies."
)

# Skills Section
with st.container():
    with st.expander("Skills", expanded=False):
        skills = [
            "C",
            "C++",
            "Python",
            "HTML",
            "CSS",
            "SQL",
            "Git",
            "Linux",
            "Bash Scripting",
            "Photoshop",
            "Figma",
            "Google Colab",
            "Web Integration",
        ]
        st.write(", ".join(skills))

# Interests Section
with st.container():
    with st.expander("Interests", expanded=False):
        interests = [
            "Web Development",
            "Cyber Security Tools",
            "Linux Customization",
            "Basic Data Science",
            "Cyber Security",
            "Open Source Projects",
        ]
        st.write(", ".join(interests))

with st.container():
    with st.expander("About Me", expanded=False):
        st.markdown("""
        ### Hello! I am Abhinav Kumar Rai from India,

        -I thrive on exploring new technologies and enjoy contributing to **open-source projects**. My goal is to create impactful digital solutions that make a difference.

        ### Work Ethic and Team Spirit:

        -I'm very serious about my work and committed to delivering high-quality results. I believe in the power of teamwork and love collaborating with others to achieve common goals.

        ### Hobbies:

        In my free time, I enjoy:
        - Playing games, which help me unwind and sharpen my problem-solving skills.
        - Catching up on sleep, allowing me to recharge for new challenges ahead.

        ### Learnerning:

        -My passion for learning drives me to continuously seek new knowledge and skills. I'm excited to connect with fellow developers and explore opportunities to grow within the tech community.

        -If you share my enthusiasm for creating innovative digital solutions, I would love to collaborate on exciting projects!
        """)
with st.container():
    st.header("Contact Me")
    st.write("Email: [Gmail](mailto:kumarabhinav.akr@gmail.com)")
    st.write("GitHub: [GitHub-Profile](https://github.com/abhinav4961)")


st.write("Thank you for visiting my portfolio!")
