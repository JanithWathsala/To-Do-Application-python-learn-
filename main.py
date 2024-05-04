import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TO DO APP")
root.geometry("400x400")
root.resizable(False,False)

heading = ttk.Label(root, text="ALL TASK", font=("arial", 20, "bold"))
heading.pack()

frame = ttk.Frame(root, width=400, height=60)
frame.pack(pady=20)

task_entry = ttk.Entry(frame, font="arial 18", width=27)
task_entry.pack()

frame1 = ttk.Frame(root, width=300, height=250)
frame1.pack()

listboox = tk.Listbox(frame1,width=40, height=12 ,font="arial 12")
listboox.pack(pady=10)

deleteButton = ttk.Button(root, text="DELETE")
deleteButton.pack()

root.mainloop()