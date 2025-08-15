tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found!")
        return
    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    if not tasks:
        print("No tasks to delete!")
        return
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task '{removed}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
