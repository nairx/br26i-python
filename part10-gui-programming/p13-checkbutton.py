import tkinter as tk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")
python=tk.BooleanVar()
java=tk.BooleanVar()
tk.Checkbutton(root,text="Python",variable=python).pack()
tk.Checkbutton(root,text="Java",variable=java).pack()
def show():
    print("Python:",python.get())
    print("Java",java.get())

tk.Button(root,text="Submit",command=show).pack()

root.mainloop()