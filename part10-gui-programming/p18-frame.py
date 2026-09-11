import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")

top_frame = tk.Frame(root)
top_frame.pack()
tk.Label(top_frame,text="User Details").pack()
tk.Entry(top_frame).pack()

bottom_frame = tk.Frame(root)
bottom_frame.pack()
tk.Button(bottom_frame,text="Save").pack()

root.mainloop()