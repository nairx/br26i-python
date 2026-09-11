import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.geometry("400x300")

text = tk.Text(root)
text.pack(fill="both",expand=True)

def exit_app():
    root.destroy()

def open_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename,"r") as file:
            data = file.read()
        text.delete("1.0",tk.END)
        text.insert("1.0",data)

def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        data = text.get("1.0",tk.END)
        with open(filename,"w") as file:
            file.write(data)

def new_file():
    text.delete("1.0",tk.END)


menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Exit",command=exit_app)
menu_bar.add_cascade(label="File",menu=file_menu)
root.config(menu=menu_bar)




root.mainloop()
