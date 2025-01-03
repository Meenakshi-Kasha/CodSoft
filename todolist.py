import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            status = "[Done]" if task["completed"] else "[Pending]"
            print(f"{idx}. {task['task']} {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]["task"]
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task '{old_task}' updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task '{self.tasks[task_number - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)
        print(f"Tasks saved to {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
            print(f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty to-do list.")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Save Tasks to File")
        print("7. Load Tasks from File")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to update: "))
            new_task = input("Enter the new task description: ")
            todo.update_task(task_number, new_task)
        elif choice == "4":
            task_number = int(input("Enter task number to mark as completed: "))
            todo.mark_task_completed(task_number)
        elif choice == "5":
            task_number = int(input("Enter task number to delete: "))
            todo.delete_task(task_number)
        elif choice == "6":
            filename = input("Enter filename to save tasks: ")
            todo.save_to_file(filename)
        elif choice == "7":
            filename = input("Enter filename to load tasks: ")
            todo.load_from_file(filename)
        elif choice == "8":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
