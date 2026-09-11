from tkinter import messagebox

# messagebox.showinfo("Information","Record saved successfully")

# messagebox.showerror("Error","Access Denied")

# messagebox.showwarning("Warning","Please enter your name")

result = messagebox.askyesno("Confirm","Do you want to continue?")
if result:
    print("Deleted")
else:
    print("Cancelled")