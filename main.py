import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TO DO APP")
root.geometry("400x400")
root.resizable(False,False)

task_list = []

def add_task(event):
    task = task_entry.get()
    task_entry.delete(0,tk.END)
    if task:
        listboox.insert(tk.END, task)
        task_list.append(task)

heading = ttk.Label(root, text="ALL TASK", font=("arial", 20, "bold"))
heading.pack()

frame = ttk.Frame(root, width=400, height=60)
frame.pack(pady=20)

task_entry = ttk.Entry(frame, font="arial 18", width=27)
task_entry.pack()

task_entry.bind("<Return>", add_task)

frame1 = ttk.Frame(root, width=300, height=250)
frame1.pack()

listboox = tk.Listbox(frame1,width=40, height=12 ,font="arial 12")
listboox.pack(pady=10)

deleteButton= ttk.Button(root, text="DELETE")
deleteButton.pack()

root.mainloop()