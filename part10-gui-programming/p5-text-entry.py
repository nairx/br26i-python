import tkinter as tk

root = tk.Tk()

root.title("My Application")

root.geometry("400x300")

label = tk.Label(root,text="Enter your name")
label.pack()

entry = tk.Entry(root)
entry.pack()

def show_name():
    name = entry.get()
    label.config(text="Hello "+name)

button = tk.Button(root,text="Submit",command=show_name)
button.pack()

root.mainloop()