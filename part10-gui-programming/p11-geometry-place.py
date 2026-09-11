# import tkinter as tk
# root = tk.Tk()
# root.title("My Application")
# root.geometry("400x300")
# label = tk.Label(root,text="My Aoplication")
# label.place(x=0,y=0)
# label1 = tk.Label(root,text="Heading")
# label1.place(x=0,y=100)
# root.mainloop()


import tkinter as tk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")
label = tk.Label(root,text="My Aoplication")
label.place(relx=0.1,rely=0.1)
label1 = tk.Label(root,text="Heading")
label1.place(relx=0.5,rely=0.5)
root.mainloop()