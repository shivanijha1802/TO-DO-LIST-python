# todo.py
# Console-based To-Do List Application
# Author: Shivani Jha 
# Date: 2025-06-25
# Description: Add, View and Remove tasks with persistant storage in tasks.txt

import os

FILENAME = "tasks.txt"

# To load tasks from file
def load_tasks():
    if not os.path.exists(FILENAME):
        return []       # It will return a empty list if file doesn't exist
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# To save updated tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# To add new task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"\nYour Task added: {task} \nGo for it!")

# To view tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found. Add new Tasks first!")
    else:
        print("\nYour To-Do List is here:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}.{task}")

# To remove a task by its number
def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        remove = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"\nYour task removed: {remove}")
    else:
        print("\nInvalid task number. No such task found!")

# Main function
def main():
    while True:
        print("\n===== TO-DO-LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter your Task: ")
            add_task(task)
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter your task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Plese enter a valid task number.")
        elif choice == "4":
            print("\nExiting TO-DO LIST... \nBest of luck for your Tasks completion!\n")
            break
        else:
            print("Please enter a valid choice.")

# To run the app
if __name__ == "__main__":
    main()