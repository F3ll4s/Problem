import customtkinter as ctk

todo_add = ctk.CTkToplevel()
todo_add.geometry("500x600")
todo_add.title("To-Do List")

font = ctk.CTkFont(family="Arial", size=16)
label = ctk.CTkLabel(todo_add, text="Add Todolist", font=ctk.CTkFont(family="Arial", size=24, weight="bold"))
label.pack(pady=20)

task_label = ctk.CTkLabel(todo_add, text="Task:",font=font)
task_label.pack(anchor="w", padx=175, pady=(25, 0))
task_entry = ctk.CTkEntry(todo_add, placeholder_text="Enter a new task",font=font,width=150)
task_entry.pack(pady=5)

due_date_label = ctk.CTkLabel(todo_add, text="Due Date:",font=font)
due_date_label.pack(anchor="w", padx=175, pady=(25, 0))
due_date_entry = ctk.CTkEntry(todo_add, placeholder_text="Enter the due date",font=font,width=150)
due_date_entry.pack(pady=5)

time_label = ctk.CTkLabel(todo_add, text="Time:",font=font)                                                                
time_label.pack(anchor="w", padx=175, pady=(25, 0))
time_entry = ctk.CTkEntry(todo_add, placeholder_text="Enter the time",font=font,width=150)
time_entry.pack(pady=5)

option_difficulty_label = ctk.CTkLabel(todo_add, text="Difficulty",font=font)
option_difficulty_label.pack(anchor="w", padx=175, pady=(25, 0))
option_difficulty = ctk.CTkOptionMenu(todo_add, values=["Easy", "Medium", "Hard"],font=font)
option_difficulty.pack(pady=5)

add_button = ctk.CTkButton(todo_add, text="Add Task",font=font)
add_button.pack(pady=(30,0))

todo_add.mainloop()
