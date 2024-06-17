import streamlit as st 
import pandas

st.set_page_config(layout="wide")

st.header("My first company web page")
content = """
Hello and welcome to my first independently written web page. 
Please excuse my silly writing. There is a need for me to write 
a couple of words here that are not just copy-pasted, after all 
I consider myself as a half-creative soul, so these are the first 
words that just came out of my (mouth? pen?) keyboard.\\
In what follows, please met some people who must be delighted
their photos are all over internet. I assume the names are
fake and that they don't match the person on the photo,
but don't let that kill your mood.
"""
st.write(content)

st.subheader("Our team")
col1, empty1, col2, empty2, col3 = st.columns([1.5, 0.3, 1.5, 0.3, 1.5])
df = pandas.read_csv("myproject2/data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("myproject2/images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("myproject2/images/" + row['image'])
        
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("myproject2/images/" + row['image'])