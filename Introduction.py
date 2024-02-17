from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="VAK Introduction",
    page_icon="👋",
)

st.title("VAK Learning Styles Introduction")

st.markdown(
    """
    Welcome to the VAK Learning Styles Exploration!

    VAK stands for Visual, Auditory, and Kinesthetic, representing three primary learning styles.
    Understanding your preferred learning style can enhance your learning experience and
    help educators tailor their teaching methods to better suit their students.

    **Visual Learners:** Learn best through visual aids like charts, graphs, and images.
    """
)
st.image(Image.open("./pic/stock-photo-asian-teacher-giving-lesson.jpeg"), width=650)
st.markdown("### ")
st.markdown("**Auditory Learners:** Learn best through listening, such as lectures, discussions, and podcasts.")
st.image(Image.open("./pic/360_F_207453673_hpyt6tz0yyUkd7WQz8xq97JVHzBIVmp2.jpg"), width = 650)
st.markdown("### ")
st.markdown("**Kinesthetic Learners:** Learn best through hands-on experiences and physical activities.")
st.image(Image.open("./pic/istockphoto-1075599562-612x612.jpg"), width=650)