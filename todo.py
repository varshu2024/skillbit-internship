tasks = []

def show_menu():
    print("\n📝 To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} | Due: {task['due']} | Priority: {task['priority']}")

def add_task():
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (e.g. 2025-06-10): ")
    priority = input("Enter priority (Low/Medium/High): ")
    task = {"task": task_name, "due": due_date, "priority": priority.capitalize()}
    tasks.append(task)
    print("✅ Task added!")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"🗑️ Deleted task: {removed['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("👋 Exiting To-Do List. Stay organized!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
