import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

def key_pressed(event):
    print("Key pressed:", event.keysym)

# root.bind("<Key>", key_pressed)

root.bind("<Return>", key_pressed)

root.bind("<Button-1>",lambda event:print("Mouse Clicked"))

root.bind("<Button-3>",lambda event:print("Right Mouse Clicked"))

root.bind("<Double-Button-1>",lambda event:print("Mouse Double Clicked"))



root.mainloop()