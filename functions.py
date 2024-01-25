from tabulate import tabulate
import subprocess

# Specify the file path
file_path = 'table'

# Initialize to-do list data with headers
todo_list_data = [
    ["Serial No.", "Task", "Status"],
]

# Function to get user input and add to the to-do list
def add_to_todo_list():
    serial_no = len(todo_list_data)  # Calculate serial number
    task = input("Enter Task: ")
    status = input("Enter Status (e.g., 'In Progress', 'Completed'): ")

    # Add user input to the to-do list with serial number
    todo_list_data.append([serial_no, task, status])

# Function to print the to-do list using a Rust program (bat)
def print_todo_list():
    with open(file_path, 'w') as file:
        # Write the formatted to-do list
        file.write(tabulate(todo_list_data, headers="firstrow", tablefmt="pipe"))
    # Use the 'bat' command to display the table using the default terminal pager
    subprocess.run(['bat', file_path])

# Function to delete an entry from the to-do list
def delete_entry():
    serial_no_to_delete = int(input("Enter Serial No. of the task to delete: "))
    for task in todo_list_data[1:]:
        if task[0] == serial_no_to_delete:
            todo_list_data.remove(task)
            break

# Function to modify the status of a task
def modify_status():
    serial_no_to_modify = int(input("Enter Serial No. of the task to modify: "))
    new_status = input("Enter new status for the task: ")
    for task in todo_list_data[1:]:
        if task[0] == serial_no_to_modify:
            task[2] = new_status
            break

# Function to save the to-do list to a file
def save_todo_list():
    with open(file_path, 'w') as file:
        # Write the formatted to-do list
        file.write(tabulate(todo_list_data, headers="firstrow", tablefmt="pipe"))
