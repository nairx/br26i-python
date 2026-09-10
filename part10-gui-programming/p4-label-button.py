import tkinter as tk

root = tk.Tk()

root.title("My Application")

root.geometry("400x300")

def change_text():
    label.config(text="Button Clicked")

label = tk.Label(root,text="Hello",font=("Arial",20))
label.pack()
button = tk.Button(root,text="Submit",command=change_text)
button.pack()
root.mainloop()