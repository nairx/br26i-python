import tkinter as tk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")

gender = tk.StringVar(value=0)

tk.Radiobutton(root,text="Male",variable=gender,value="Male").pack()

tk.Radiobutton(root,text="Female",variable=gender,value="Female").pack()

def show():
    print(gender.get())

tk.Button(root,text="Submit",command=show).pack()

root.mainloop()