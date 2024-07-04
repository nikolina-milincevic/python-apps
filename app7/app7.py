import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, 
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days_local):
    dates = ["2024-07-04", "2024-07-05", "2024-07-06"]
    temperatures = [7, 10, 11]
    temperatures = [days_local * i for i in temperatures]
    # this is just to showcase how dynamic plotting works
    return dates, temperatures
    
d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperatures (C)"})
st.plotly_chart(figure)
