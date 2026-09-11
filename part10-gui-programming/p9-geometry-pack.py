import tkinter as tk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")
label = tk.Label(root,text="My Aoplication")
label.pack()
# label.pack(side="right") # left bottom top
# label.pack(side="top",anchor="e") #w-west e-east
label1 = tk.Label(root,text="Heading")
label1.pack(padx=50,pady=50)
root.mainloop()