def list_todos(todos):
    """
        List todos
    """

def add_todo(todos):
    """
        Add todos
    """

def edit_todo(todos):
    """
        Edit todos
    """

def delete_todo(todos):
    """
        Edit todos
    """

def menu(todos):
    print("What would you like to do?")
    print("1. List todos")
    print("2. Add a todo")
    print("3. Edit a todo")
    print("4. Delete a todo")
    print("5. Quit")
    choice = input("> ")

def main():
    print("Welcome to your todo list!")
    todos = []
    menu(todos)

main()