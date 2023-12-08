import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create main window
app = tk.Tk()
app.title("To-Do List App")

# Create and place widgets
entry = tk.Entry(app, width=50)
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=50, height=10)
listbox.pack(pady=10)

# Run the main loop
app.mainloop()