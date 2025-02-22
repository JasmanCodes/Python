class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet!")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def mark_task_completed(self, task_index):
        if task_index < 1 or task_index > len(self.tasks):
            print("Invalid task index!")
        else:
            self.tasks.pop(task_index - 1)
            print("Task marked as completed!")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
