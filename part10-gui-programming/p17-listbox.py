import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")
listbox = tk.Listbox(root)
listbox.insert(tk.END,"Python")
listbox.insert(tk.END,"MERN")
listbox.insert(tk.END,"Java")
listbox.insert(tk.END,".NET")

listbox.pack()

def select():
    selection = listbox.curselection()
    if selection:
        value = listbox.get(selection[0])
        print(value)

tk.Button(text="Select",command=select).pack()

root.mainloop()