import streamlit as st
import plotly.express as px
from backend import get_scores

# Frontend

st.title("Diary Tone")

d, p, n = get_scores()

st.subheader("Positivity")
figure_p = px.line(x=d, y=p, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure_p)

st.subheader("Negativity")
figure_n = px.line(x=d, y=n, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure_n)