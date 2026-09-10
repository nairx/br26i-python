import tkinter as tk
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")
menu_bar = tk.Menu(root)
def new_file():
    print("New File")
def exit_app():
    root.destroy()

file_menu = tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit_app)

edit_menu = tk.Menu(menu_bar,tearoff=0)
edit_menu.add_command(label="New",command=new_file)
edit_menu.add_command(label="Open")
edit_menu.add_separator()
edit_menu.add_command(label="Exit",command=exit_app)

menu_bar.add_cascade(label="File",menu=file_menu)
menu_bar.add_cascade(label="Edit",menu=edit_menu)

root.config(menu=menu_bar)
root.mainloop()