import streamlit as st
from mybackend import get_dates_and_temperature
import plotly.express as px

st.title("Temperature over time")

dates, temperatures = get_dates_and_temperature("app10/temperature.txt")

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)

