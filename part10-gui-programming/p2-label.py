import tkinter as tk

root = tk.Tk()
root.title("My Application")
root.geometry("400x300")
label = tk.Label(root,text="Welcome to Broadridge",font=("Arian",20))
label.pack()
root.mainloop()