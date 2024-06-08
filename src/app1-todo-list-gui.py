import functions
import FreeSimpleGUI as sg

label = sg.Text("Type your to-do: ")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("This is my To-do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
# the instances layout=[[label, input_box]] will be in the same row,
# otherwise if we write [[label], [input_box]], we would have two rows