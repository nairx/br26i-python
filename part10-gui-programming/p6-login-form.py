import multiprocessing as mp
import threading
import tkinter as tk
from tkinter import messagebox
 
VALID_CREDENTIALS = [
    ("admin@example.com", "admin123"),
    ("user@example.com", "user123"),
    ("manager@example.com", "manager123"),
]
 
 
def validate_credentials(email, password, queue):
    email = email.strip().lower()
    password = password.strip()
 
    allowed = any(
        stored_email.lower() == email and stored_password == password
        for stored_email, stored_password in VALID_CREDENTIALS
    )
    queue.put(allowed)
 
 
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("1200x700")
        self.root.configure(bg="#2d2d2d")
 
        self.main_panel = tk.Frame(root, bg="#f1f1f1", highlightbackground="black", highlightthickness=2)
        self.main_panel.pack(fill="both", expand=True, padx=60, pady=60)
 
        self.title_label = tk.Label(
            self.main_panel,
            text="Login Form",
            font=("Arial", 28, "bold"),
            bg="#f1f1f1",
            fg="black",
            anchor="w",
            justify="left",
        )
        self.title_label.pack(anchor="w", padx=55, pady=(40, 30))
 
        self.email_label = tk.Label(
            self.main_panel,
            text="Email:",
            font=("Arial", 24, "bold"),
            bg="#f1f1f1",
            fg="black",
            anchor="w",
        )
        self.email_label.pack(anchor="w", padx=55, pady=(10, 0))
 
        self.email_entry = tk.Entry(
            self.main_panel,
            width=30,
            font=("Arial", 20),
            bd=3,
            relief="solid",
            bg="#f8f8f8",
        )
        self.email_entry.pack(anchor="w", padx=55, pady=(10, 20))
 
        self.password_label = tk.Label(
            self.main_panel,
            text="Password:",
            font=("Arial", 24, "bold"),
            bg="#f1f1f1",
            fg="black",
            anchor="w",
        )
        self.password_label.pack(anchor="w", padx=55, pady=(10, 0))
 
        self.password_entry = tk.Entry(
            self.main_panel,
            width=30,
            font=("Arial", 20),
            bd=3,
            relief="solid",
            show="*",
            bg="#f8f8f8",
        )
        self.password_entry.pack(anchor="w", padx=55, pady=(10, 20))
 
        self.login_button = tk.Button(
            self.main_panel,
            text="Login",
            font=("Arial", 24, "bold"),
            bg="#f1f1f1",
            fg="black",
            relief="flat",
            command=self.start_login,
            bd=0,
            highlightthickness=0,
        )
        self.login_button.pack(anchor="w", padx=55, pady=(10, 30))
 
    def start_login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
 
        if not email or not password:
            messagebox.showwarning("Missing data", "Please enter both email and password.")
            return
 
        self.login_button.config(state="disabled", text="Checking...")
 
        thread = threading.Thread(target=self.run_validation, args=(email, password), daemon=True)
        thread.start()
 
    def run_validation(self, email, password):
        queue = mp.Queue()
        process = mp.Process(target=validate_credentials, args=(email, password, queue))
        process.start()
        process.join()
 
        if queue.empty():
            result = False
        else:
            result = queue.get()
 
        self.root.after(0, lambda: self.handle_result(result))
 
    def handle_result(self, result):
        self.login_button.config(state="normal", text="Login")
 
        if result:
            messagebox.showinfo("Access granted", "Login successful!")
        else:
            messagebox.showerror("Access denied", "Invalid email or password.")
 
 
def main():
    if __name__ == "__main__":
        root = tk.Tk()
        app = LoginApp(root)
        root.mainloop()
 
 
main()
 
 