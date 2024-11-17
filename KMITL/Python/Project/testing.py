import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("To-Do List with Checklist")

        # Header
        bold_font = ctk.CTkFont(family="Arial", size=24, weight="bold")
        label = ctk.CTkLabel(self, text="My To-Do List", font=bold_font)
        label.pack(pady=(20, 10))

        # Frame for the task list
        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.pack(pady=(10, 10), fill="both", expand=True)

        # Entry and Add button
        self.task_entry = ctk.CTkEntry(self, placeholder_text="Enter a new task")
        self.task_entry.pack(pady=(10, 0), fill="x", padx=20)

        add_button = ctk.CTkButton(self, text="Add Task", command=self.add_task)
        add_button.pack(pady=10)

        # Button for deleting tasks
        delete_button = ctk.CTkButton(self, text="Delete Selected", command=self.delete_task)
        delete_button.pack(pady=10)

        # List to store tasks (each as a tuple of text, checkbox variable, and task frame)
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            # Create a frame for each task with a checkbox and a "View" button
            task_frame = ctk.CTkFrame(self.task_frame)
            task_frame.pack(fill="x", pady=5, padx=10)

            # Checkbox for the task
            task_var = ctk.BooleanVar()
            task_checkbox = ctk.CTkCheckBox(task_frame, text=task_text, variable=task_var)
            task_checkbox.pack(side="left")

            # "View" button for the task
            view_button = ctk.CTkButton(task_frame, text="View", command=lambda t=task_text: self.view_task(t))
            view_button.pack(side="right")

            # Add task to the list
            self.tasks.append((task_text, task_var, task_frame))
            self.task_entry.delete(0, "end")

    def delete_task(self):
        # Remove completed tasks from the list
        for task_text, task_var, task_frame in self.tasks:
            if task_var.get():  # If the checkbox is checked
                task_frame.destroy()  # Remove the task frame from the UI

        # Update the task list to remove deleted tasks
        self.tasks = [task for task in self.tasks if not task[1].get()]

    def view_task(self, task_text):
        # Function to display more information about the task
        # This can be customized to show a pop-up or perform any action
        print(f"Viewing task: {task_text}")
        ctk.CTkMessageBox.show_info("Task Info", f"Task: {task_text}")

app = App()
app.mainloop()
