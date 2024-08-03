import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

def update_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        display_task = task["name"]
        if task["completed"]:
            display_task = display_task + " (Completed)"
        listbox.insert(tk.END, display_task)

def add_task():
    task_name = simpledialog.askstring("Add Task", "Enter task name:")
    if task_name:
        tasks.append({"name": task_name, "description": "", "due_date": "", "completed": False})
        update_tasks()

def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task = tasks[task_index]
        new_task_name = simpledialog.askstring("Edit Task", "Edit task name:", initialvalue=task["name"])
        if new_task_name:
            task["name"] = new_task_name
            update_tasks()

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        del tasks[selected_task_index[0]]
        update_tasks()

def complete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()

def show_task_details():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task = tasks[task_index]

        details_window = tk.Toplevel(root)
        details_window.title("Task Details")
        details_window.geometry("300x200")
        details_window.config(bg="#ffffff")
        name_label = tk.Label(details_window, text="Task Name:", bg="#ffffff")
        name_label.pack(pady=5)
        name_value = tk.Label(details_window, text=task["name"], bg="#ffffff")
        name_value.pack(pady=5)

        description_label = tk.Label(details_window, text="Description:", bg="#ffffff")
        description_label.pack(pady=5)
        description_entry = tk.Entry(details_window)
        description_entry.insert(0, task["description"])
        description_entry.pack(pady=5)

        due_date_label = tk.Label(details_window, text="Due Date:", bg="#ffffff")
        due_date_label.pack(pady=5)
        due_date_entry = tk.Entry(details_window)
        due_date_entry.insert(0, task["due_date"])
        due_date_entry.pack(pady=5)

        def save_details():
            task["description"] = description_entry.get()
            task["due_date"] = due_date_entry.get()
            details_window.destroy()

        save_button = tk.Button(details_window, text="Save", command=save_details)
        save_button.pack(pady=10)

root = tk.Tk()
root.title("The To-Do List")
root.geometry("400x400")
root.configure(bg="#FAF3E0")

title = tk.Label(root, text="The To-Do List", font=("Arial", 24), bg="#FAF3E0", fg="#8B4513")
title.pack(pady=10)

frame = tk.Frame(root, bg="#FAF3E0")
frame.pack(pady=10)

task_label = tk.Label(frame, text="Enter the Task:", font=("Arial", 12), bg="#FAF3E0")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_entry = tk.Entry(frame, font=("Arial", 12))
task_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Add Task", command=add_task, font=("Arial", 12), bg="#FAEBD7", fg="#8B4513")
add_button.grid(row=1, column=0, padx=5, pady=5)

edit_button = tk.Button(frame, text="Edit Task", command=edit_task, font=("Arial", 12), bg="#FAEBD7", fg="#8B4513")
edit_button.grid(row=1, column=1, padx=5, pady=5)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task, font=("Arial", 12), bg="#FAEBD7", fg="#8B4513")
remove_button.grid(row=2, column=0, padx=5, pady=5)

complete_button = tk.Button(frame, text="Complete Task", command=complete_task, font=("Arial", 12), bg="#FAEBD7", fg="#8B4513")
complete_button.grid(row=2, column=1, padx=5, pady=5)

details_button = tk.Button(frame, text="Show Details", command=show_task_details, font=("Arial", 12), bg="#FAEBD7", fg="#8B4513")
details_button.grid(row=3, column=0, padx=5, pady=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), bg="#FFF8DC", fg="#8B4513")
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

update_tasks()

root.mainloop()