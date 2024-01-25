import functions

# Main program loop
while True:
    print("\nTo-Do List Management:")
    print("1. Add Task")
    print("2. Print To-Do List")
    print("3. Delete Task")
    print("4. Modify Task Status")
    print("5. Save and Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        functions.add_to_todo_list()
    elif choice == '2':
        functions.print_todo_list()
    elif choice == '3':
        functions.delete_entry()
    elif choice == '4':
        functions.modify_status()
    elif choice == '5':
        functions.save_todo_list()
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

