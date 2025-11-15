import json
import os

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')

    def list_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")
        print()

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f'Task #{task_number} marked as completed.')
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")

    def save_tasks(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f, indent=4)
            print("Tasks saved.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.tasks = json.load(f)
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []

def main():
    todo_list = TodoList()

    while True:
        print("Choose an option:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task completed")
        print("4. Delete task")
        print("5. Save tasks")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            task = input("Enter new task: ").strip()
            if task:
                todo_list.add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            try:
                num = int(input("Enter task number to mark completed: "))
                todo_list.mark_completed(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                num = int(input("Enter task number to delete: "))
                todo_list.delete_task(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            todo_list.save_tasks()
        elif choice == "6":
            todo_list.save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
