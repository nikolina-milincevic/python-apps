import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("./app2/images/photo.png", width=400)
    
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
    
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("./app2/data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("./app2/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("./app2/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")