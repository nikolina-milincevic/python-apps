import FreeSimpleGUI as sg
from functions import convert

sg.theme("Black")

feet_text = sg.Text("Enter feet: ")
feet_input = sg.InputText(tooltip="entering feet", key="feet")
inches_text = sg.Text("Enter inches: ")
inches_input = sg.InputText(tooltip="entering inches", key="inches")
convert_butoon = sg.Button("Convert")
output_label = sg.Text(key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Converter", layout=[[feet_text, feet_input], 
                                        [inches_text, inches_input],
                                        [convert_butoon, exit_button, output_label]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            try:
                if values["feet"] == "":
                    feet_float = 0.0
                    if values["inches"] == "":
                        inches_float = 0.0
                    else:
                        inches_float = float(values["inches"])
                else:
                    if values["inches"] == "":
                        feet_float = float(values["feet"])
                        inches_float = 0.0
                    else:
                        feet_float = float(values["feet"])
                        inches_float = float(values["inches"])
                meters = convert(feet_float, inches_float)
                window['output'].update(value=f"{meters} m")
            except ValueError:
                window["output"].update(value="Wrong input. Please try again.")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    
window.close()