import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("./app2/images/photo.png", width=500)
    
with col2:
    st.title("Ardit Sulce")
    content = """
    Hi, my name is Ardit! I am a python programmer and a teacher. I love to teach. 
    But most of all, I love to type some interesting multiline content.
    """
    st.info(content)

under_content = """
This is a content of a web page that is not contained in any of the columns, \
but goes under both of the existing columns.
"""
st.write(under_content)
    
