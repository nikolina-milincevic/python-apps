import functions
import FreeSimpleGUI as sg

label = sg.Text("Type your to-do: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# we add this key so that printing values later gives us a dict
# whose key is todo and not a 0

add_button = sg.Button("Add")

window = sg.Window("This is my To-do App", 
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

# if we set event = window.read() and then print it,
# it would be a touple. this is easier to work with.
# without while loop, each time we hit add button,
# the window closes.
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"]+"\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
    
window.close()