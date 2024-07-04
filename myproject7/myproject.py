import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for the x-axis: ", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for the y-axis: ", ("GDP", "Happiness", "Generosity"))
st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv("myproject7/happy.csv")

first = df[str(x_axis).lower()]
second = df[str(y_axis).lower()]

figure = px.scatter(x=first, y=second, 
                    labels={"x": x_axis, "y": y_axis})

st.plotly_chart(figure)