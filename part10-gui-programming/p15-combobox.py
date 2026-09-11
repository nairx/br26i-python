import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")

courses = ["Python","Java","MERN"]

combo = ttk.Combobox(root,values=courses)
combo.pack()


def show():
    print(combo.get())

tk.Button(root,text="Submit",command=show).pack()

root.mainloop()