#FILEPATH = "./todos.txt"
FILEPATH = "./src/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads the text file and returns the list of 
    to-do items. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
        
        
def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet_local = float(parts[0])
    inches_local = float(parts[1])
    return {"feet": feet_local, "inches": inches_local}
    
    
def convert(feet_local, inches_local):
    meters = feet_local * 0.3048 + inches_local * 0.0254
    return meters



if __name__ == "__main__":
    print("Hello")
    print(get_todos())
    