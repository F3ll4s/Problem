import customtkinter as ctk
import pickle
import time

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Todo List")

        self.username_label = ctk.CTkLabel(self, text="Username").grid(row=1, column=10, pady=(10, 0))
        self.username_entry = ctk.CTkEntry(self).grid(row=1, column=11, pady=(10, 0))

        self.password_label = ctk.CTkLabel(self, text="Password").grid(row=2, column=10, pady=(10, 0))
        self.password_entry = ctk.CTkEntry(self, show='*').grid(row=2, column=11, pady=(10, 0))

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login).grid(row=3, column=10, columnspan=2, pady=(10, 0))
        self.register_button = ctk.CTkButton(self, text="Register", command=self.signup).grid(row=4, column=10, columnspan=2, pady=(10, 0))

    def login(self):
        login_window = ctk.CTkToplevel(self)
        login_window.geometry("500x500")
        login_window.title("Smart Task Manager")
        
        task_manager_text = ctk.CTkLabel(login_window,text="Smart Task Manager")

    def signup(self):
        register_window = ctk.CTkToplevel(self)
        register_window.geometry("400x300")
        register_window.title("Sign Up")

        register_username_label = ctk.CTkLabel(register_window, text="Username").grid(row=1, column=1, padx=20, pady=(10, 0), sticky="w")
        register_username_entry = ctk.CTkEntry(register_window).grid(row=1, column=2, padx=20, pady=(10, 0), sticky="ew")

        register_password_label = ctk.CTkLabel(register_window, text="Password").grid(row=2, column=1, padx=20, pady=(10, 0), sticky="w")
        register_password_entry = ctk.CTkEntry(register_window, show='*').grid(row=2, column=2, padx=20, pady=(10, 0), sticky="ew")

        confirm_password_label = ctk.CTkLabel(register_window, text="Confirm Password").grid(row=3, column=1, padx=20, pady=(10, 0), sticky="w")
        confirm_password_entry = ctk.CTkEntry(register_window, show='*').grid(row=3, column=2, padx=20, pady=(10, 0), sticky="ew")

        register_button = ctk.CTkButton(register_window, text="Register", command=lambda: self.register(register_username_entry, register_password_entry, confirm_password_entry)).grid(row=4, column=1, columnspan=2, padx=20, pady=(10, 0), sticky="ew")

    def register(self, username_entry, password_entry, confirm_password_entry):
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if password == confirm_password:
            print(f"User {username} registered successfully!")
        else:
            print("Passwords do not match. Try again.")

app = App()
app.mainloop()
