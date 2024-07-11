import mysql.connector
import os
import streamlit as st
import plotly.express as px

SQL_USER = os.getenv("sql_user")
SQL_PASSWORD = os.getenv("sql_password")

cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                              host="localhost", database="my_db")

cursor = cnx.cursor(buffered=True)
my_query = '''SELECT * FROM temperatures;'''
cursor.execute(my_query)
rows = cursor.fetchall()

dates = [rows[i][0] for i in range(len(rows))]
temperatures = [rows[i][1] for i in range(len(rows))]

st.title("Temperature over time")
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)

