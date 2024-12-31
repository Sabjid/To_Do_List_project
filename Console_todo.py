FILENAME = "Tasks.txt"

def Open_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def Save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def Add_task():
    tasks = Open_tasks()  
    new_task = input("Enter New Task: ").strip()
    if new_task:
        tasks.append(new_task)
        Save_tasks(tasks)  
        print(f"Task '{new_task}' added successfully!")
    else:
        print("Task cannot be empty. Please enter a valid task.")

def View_tasks():
    tasks = Open_tasks()  
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("NO TASK FOUND...")

def Delete_task():
    tasks = Open_tasks()  
    View_tasks()
    if tasks:
        try:
            task_num = int(input("Enter Task Number To Delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                Save_tasks(tasks)  
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n\t___WELCOME TO___ \n\t....TO-DO LIST MANAGER...\t")
        print("1: Add Task")
        print("2: View Tasks")
        print("3: Delete Task")
        print("4: Exit")

        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            Add_task()
        elif choice == "2":
            View_tasks()
        elif choice == "3":
            Delete_task()
        elif choice == "4":
            print("THANK YOU! YOUR TASKS HAVE BEEN SAVED...")
            break
        else:
            print("INVALID CHOICE... PLEASE SELECT AGAIN.")

if __name__ == "__main__":
    main()


