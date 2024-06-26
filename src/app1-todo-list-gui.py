import functions
import FreeSimpleGUI as sg
import time
import os

# to make thisa stand alone app
# we are going to use platypus
# i need to download it with line
# brew install --cask platypus
# on mac and some other way on windows or linux
# you should first have homebrew installed (I have)

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type your to-do: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# tooltip is what shows when you put mouse over the input box
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("This is my To-do App", 
                   layout=[[clock], 
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=10)
    # timeout=10 means that the loop will be executed every 10 milisec
    if event != sg.WIN_CLOSED:
        window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"])
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", 
                         font=("Helvetica", 20))
            
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", 
                         font=("Helvetice", 20))
            
        case "Exit":
            break
        
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()