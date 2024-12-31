import tkinter as tk
from tkinter import simpledialog, messagebox

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


def Delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        selected_task = task_listbox.get(selected_task_index)
        
        task_listbox.delete(selected_task_index)
        tasks.remove(selected_task)
        
        Save_tasks(tasks)
        
        messagebox.showinfo("Task Deleted", f"Task '{selected_task}' deleted successfully!")
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete.")

def Update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


def Add_task():
    new_task = simpledialog.askstring("Add Task", "Enter the new task:")
    if new_task:
        tasks.append(new_task)
        Save_tasks(tasks)  
        Update_task_list()  
        messagebox.showinfo("Task Added", f"Task '{new_task}' added successfully!")
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty. Please enter a valid task.")

def View_tasks():
    if tasks:
        task_list = "\n".join(tasks)
        messagebox.showinfo("Current Tasks", f"Your tasks:\n{task_list}")
    else:
        messagebox.showinfo("No Tasks", "No tasks available.")


def Exit_app():
    root.quit()  


def on_button_click(button, original_color):
    button.config(bg="#90EE90")  
    root.after(200, lambda: button.config(bg=original_color))  


root = tk.Tk()
root.title("To-Do List Manager")


root.configure(bg="#1D2951") 

tasks = Open_tasks()  


task_listbox = tk.Listbox(root, width=50, height=10, bg="#4169E1", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
task_listbox.pack(pady=10)


Update_task_list()


add_button = tk.Button(root, text="Add Task", command=Add_task, bg="#8A2BE2", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=5)
add_button.pack(pady=5)
add_button.bind("<Button-1>", lambda event, b=add_button: on_button_click(b, "#8A2BE2"))

view_button = tk.Button(root, text="View Tasks", command=View_tasks, bg="#00CED1", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=5)
view_button.pack(pady=5)
view_button.bind("<Button-1>", lambda event, b=view_button: on_button_click(b, "#00CED1"))

delete_button = tk.Button(root, text="Delete Task", command=Delete_task, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=5)
delete_button.pack(pady=5)
delete_button.bind("<Button-1>", lambda event, b=delete_button: on_button_click(b, "#FF6347"))

exit_button = tk.Button(root, text="Exit", command=Exit_app, bg="#FFD700", fg="black", font=("Helvetica", 12, "bold"), relief="raised", bd=5)
exit_button.pack(pady=5)
exit_button.bind("<Button-1>", lambda event, b=exit_button: on_button_click(b, "#FFD700"))


root.mainloop()
