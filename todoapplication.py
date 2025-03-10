def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    print("Welcome to the Task Manager!")

    while True:
        display_menu()
        
        try:
            choice = int(input("Choose an option (1-4): "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()