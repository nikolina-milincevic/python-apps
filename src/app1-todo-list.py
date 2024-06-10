import functions

import time

now = time.strftime("%b %d, %Y, %H:%M:%S")
print(now)

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]
            
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
                
    elif user_action.startswith("show"):
        todos = functions.get_todos()
            
        for index, item in enumerate(todos):
            row = f"{index+1}-{item}" 
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
                
            todos = functions.get_todos()  
            new_todo = input("Write your new to do: ")
            todos[number] = new_todo 
            functions.write_todos(todos)
    
        except ValueError:
            print("This is an invalid command. Try again.")
            continue
            
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
                
            todos = functions.get_todos()      
            todo_to_remove = todos[number]
            todos.pop(number)
            functions.write_todos(todos)
                    
            message = f"Todo {todo_to_remove} has been completed :)"
            print(message)
            
        except IndexError:
            print("There is no item with that number. Try again.")
            continue
            
    elif user_action.startswith("exit"):
        break
    
    else:
        print("Command is not valid.")
        
print("bye bye")