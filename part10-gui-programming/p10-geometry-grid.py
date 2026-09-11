import tkinter as tk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")
label = tk.Label(root,text="My Aoplication")
label.grid(row=0,column=0)
label1 = tk.Label(root,text="Heading")
label1.grid(row=50,column=0)
root.mainloop()