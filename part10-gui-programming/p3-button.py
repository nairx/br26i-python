import tkinter as tk

root = tk.Tk()

root.title("My Application")

root.geometry("400x300")


def greet():
    print("Hello World")

button = tk.Button(root,text="Submit",command=greet)
button.pack()

root.mainloop()