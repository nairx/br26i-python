import tkinter as tk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New")

recent_menu = tk.Menu(file_menu,tearoff=0)
recent_menu.add_command(label="file1.txt")
recent_menu.add_command(label="file2.txt")
recent_menu.add_command(label="file3.txt")

file_menu.add_cascade(label="Recent",menu=recent_menu)
menu_bar.add_cascade(label="File",menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()