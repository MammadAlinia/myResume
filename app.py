from pathlib import Path
import streamlit as st
from PIL import Image
import webbrowser

#  --- directory setup ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_file = current_dir / "assets" / "profile.jpg"

# --- GENERAL SETTING ---
PAGE_TITLE = "Digital CV | Mohammad Alinia"
PAGE_ICON = "🙃"
NAME = "Mohammad Alinia"
DESCRIPTION = """
Unity programmer with 4 years' experience Love to make games an entertain people around the WORLD
"""
EMAIL = "mohammadalinia82@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/@PuppetMaster264",
    "LinkedIn": "https://www.linkedin.com/in/mohammadalinia-linkdin/",
    "GitHub": "https://github.com/MammadAlinia"
}
PROJECTS = {
    "Wood Block Puzzle - a simple puzzle game for mobile platform": "link",
    "AntiBrick - a simple casual game for mobile platform": "link"
}
PERSONAL_PROJECTS = {
    "Kinect body detection ": "",
    "Custom car controller": "",
    "Visualization of A* Algorithm ": "",
    "Visualization of Vector flow Algorithm": "",
    "Simple implementation of Wave Function Collapse Algorithm": ""
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Hello there")

# --- LOAD CSS, PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_file)

# --- HEADER SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("✉️ ", EMAIL)

# --- SOCIAL LINKS ---


cols = st.columns(len(SOCIAL_MEDIA))
for i, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    if cols[i].button(platform):
        webbrowser.open(link)
# --- EXPERIENCE ---
st.write("#")
st.subheader("Experiences")
st.write(
    """
- 4 Years of experience in Unity and C#
- Strong understanding of C# and OOP 
- familiar with most of famous Design Patterns like MVVP, SOLID,... 
- familiar with team working and platforms like git, github
    """
)
