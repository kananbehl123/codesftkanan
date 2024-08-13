#Initialize an empty list to store tasks
tasks = []

Display the menu

print("\nTo-Do List Menu:")
print("1. Add a task")
print("2. View tasks")
print("3. Remove a task")
print("4. Mark task as completed")
print("5. Exit")

while True:
    choice = input("\nEnter your choice: ")

    if choice == '1':
        # Add a task
        description = input("Enter the task description: ")
        task = {'description': description, 'completed': False}
        tasks.append(task)
        print(f"Task added: {description}")

    elif choice == '2':
        # View all tasks
        if not tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(tasks):
                status = "Completed" if task['completed'] else "Not completed"
                print(f"{index + 1}. {task['description']} - {status}")

    elif choice == '3':
        # Remove a task
        if not tasks:
            print("No tasks available to remove.")
        else:
            for index, task in enumerate(tasks):
                status = "Completed" if task['completed'] else "Not completed"
                print(f"{index + 1}. {task['description']} - {status}")

            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Task removed: {removed_task['description']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        # Mark a task as completed
        if not tasks:
            print("No tasks available to mark as completed.")
        else:
            for index, task in enumerate(tasks):
                status = "Completed" if task['completed'] else "Not completed"
                print(f"{index + 1}. {task['description']} - {status}")

            try:
                task_index = int(input("Enter the task number to mark as completed: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]['completed'] = True
                    print(f"Task marked as completed: {tasks[task_index]['description']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '5':
        # Exit the program
        print("Exiting the To-Do List application.")
        break

    else:
        # Handle invalid menu choices
        print("Invalid choice. Please enter a number between 1 and 5.")
