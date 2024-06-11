import streamlit as st 
import functions

todos = functions.get_todos()

def add_todo():
    my_new_todo = st.session_state["new_todo"]
    todos.append(my_new_todo)
    functions.write_todos(todos)


st.title("My To-do App")
# to run this app write in terminal: streamlit run ./src/web.py
st.subheader("This is my to-do app")
st.write("This is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new to-do...",
              on_change=add_todo, key="new_todo")

print("Hello")

st.session_state