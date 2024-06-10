import FreeSimpleGUI as sg
from functions import convert

feet_text = sg.Text("Enter feet: ")
feet_input = sg.InputText(tooltip="entering feet", key="feet")
inches_text = sg.Text("Enter inches: ")
inches_input = sg.InputText(tooltip="entering inches", key="inches")
convert_butoon = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Converter", layout=[[feet_text, feet_input], 
                                        [inches_text, inches_input],
                                        [convert_butoon, output_label]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            try:
                if values["feet"] == "":
                    feet_int = 0
                    if values["inches"] == "":
                        inches_int = 0
                    else:
                        inches_int = int(values["inches"])
                else:
                    if values["inches"] == "":
                        feet_int = int(values["feet"])
                        inches_int = 0
                    else:
                        feet_int = int(values["feet"])
                        inches_int = int(values["inches"])
                meters = convert(feet_int, inches_int)
                window['output'].update(value=f"{meters} m")
            except ValueError:
                window["output"].update(value="Wrong input. Please try again.")
        case sg.WIN_CLOSED:
            break
    
window.close()