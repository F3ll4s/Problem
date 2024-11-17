import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("To-Do List with Checklist")

        bold_font = ctk.CTkFont(family="Arial", size=24, weight="bold")
        label = ctk.CTkLabel(self, text="My To-Do List", font=bold_font)
        label.pack(pady=(20, 10))

        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.pack(pady=(10, 10), fill="both", expand=True)

        add_button = ctk.CTkButton(self, text="Add Task", command=self.open_add_task_window)
        add_button.pack(pady=10)

        delete_button = ctk.CTkButton(self, text="Delete Selected", command=self.delete_task)
        delete_button.pack(pady=10)

        self.tasks = []

    def open_add_task_window(self):
        todo_add = ctk.CTkToplevel(self)
        todo_add.geometry("400x500")
        todo_add.title("Add Task")
        todo_add.lift()  
        todo_add.focus_force()  
        todo_add.attributes('-topmost', True) 
        font = ctk.CTkFont(family="Arial", size=16)
        times = [
            "0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00",
            "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
            "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"
        ]

        todo_add_label = ctk.CTkLabel(todo_add, text="Add Task", font=ctk.CTkFont(family="Arial", size=24, weight="bold"))
        todo_add_label.pack(pady=20)
        task_label = ctk.CTkLabel(todo_add, text="Task:", font=font)
        task_label.pack(anchor="w", padx=20, pady=(20, 0))
        task_entry = ctk.CTkEntry(todo_add, font=font,placeholder_text="Enter a new task")
        task_entry.pack(pady=5, padx=20, fill="x")

        due_date_label = ctk.CTkLabel(todo_add, text="Due Date:", font=font)
        due_date_label.pack(anchor="w", padx=20, pady=(10, 0))
        due_date_entry = ctk.CTkEntry(todo_add, font=font,placeholder_text="Enter the due date")
        due_date_entry.pack(pady=5, padx=20, fill="x")

        time_label = ctk.CTkLabel(todo_add, text="Time:", font=font)
        time_label.pack(anchor="w", padx=20, pady=(10, 0))
        time_entry = ctk.CTkOptionMenu(todo_add, values = times ,font=font)
        time_entry.pack(pady=5, padx=20, fill="x")

        difficulty_label = ctk.CTkLabel(todo_add, text="Difficulty:", font=font)
        difficulty_label.pack(anchor="w", padx=20, pady=(10, 0))
        difficulty_option = ctk.CTkOptionMenu(todo_add, values=["Easy (10-20 minutes)", "Medium (1-3 hours)", "Hard (12+ hours)"], font=font)
        difficulty_option.pack(pady=5, padx=20,fill="x")

        button_add = ctk.CTkButton(todo_add, text="Add Task", font=font, command=lambda: self.add_task(
            task_entry, due_date_entry.get(), time_entry.get(), difficulty_option.get(), todo_add
        ))
        button_add.pack(pady=40)

    def add_task(self, task_entry, due_date, time, difficulty, window):
        task_text = task_entry.get()
        if task_text:
            window.destroy()
            
            task_frame = ctk.CTkFrame(self.task_frame)
            task_frame.pack(fill="x", pady=5, padx=10)

            task_var = ctk.BooleanVar()
            task_checkbox = ctk.CTkCheckBox(task_frame, text=task_text, variable=task_var)
            task_checkbox.pack(side="left")

            view_button = ctk.CTkButton(task_frame, text="View", command=lambda: self.view_task(task_text, due_date, time, difficulty))
            view_button.pack(side="right")

            self.tasks.append({"text": task_text, "due_date": due_date, "time": time, "difficulty": difficulty, "var": task_var, "frame": task_frame})

    def view_task(self, task_text, due_date, time, difficulty):
        
        details_window = ctk.CTkToplevel(self)
        details_window.geometry("300x200")
        details_window.title("Task Details")
        details_window.lift()  
        details_window.focus_force()  
        details_window.attributes('-topmost', True) 
        font = ctk.CTkFont(family="Arial", size=14)

        ctk.CTkLabel(details_window, text=f"Task: {task_text}", font=font).pack(pady=10)
        ctk.CTkLabel(details_window, text=f"Due Date: {due_date}", font=font).pack(pady=10)
        ctk.CTkLabel(details_window, text=f"Time: {time}", font=font).pack(pady=10)
        ctk.CTkLabel(details_window, text=f"Difficulty: {difficulty}", font=font).pack(pady=10)

    def delete_task(self):
        for task in self.tasks:
            if task["var"].get():  
                task["frame"].destroy()  

        new_tasks = []
        for task in self.tasks:
            if task["var"].get():
                task["frame"].destroy()
            else:
                new_tasks.append(task)
                
        self.tasks = new_tasks

app = App()
app.mainloop()
