import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")

text = tk.Text(root,height=10,width=50)
text.pack()

def show():
    data = text.get("1.0",tk.END)
    print(data)

tk.Button(root,text="Submit",command=show).pack()

root.mainloop()