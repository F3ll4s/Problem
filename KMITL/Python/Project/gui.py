import customtkinter as ctk
import pickle
from time import strftime
from datetime import date
from PIL import Image
from countdown import CountdownTimer
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Todo List")
        
        global bold_font, normal_font
        
        bold_font = ctk.CTkFont(family="Arial", size=24, weight="bold")
        normal_font = ctk.CTkFont(family="Arial", size=16)
        label = ctk.CTkLabel(self, text="My Todo List", font=bold_font)
        label.pack(pady=(100,0))  
        
        username = ctk.CTkLabel(self, text="Username", font=normal_font)
        username_key = ctk.CTkEntry(self, font=("Arial", 16))
        
        password = ctk.CTkLabel(self, text="Password", font=normal_font)
        password_key = ctk.CTkEntry(self,show='*', font=normal_font)
        
        username.pack(anchor="w", padx=175, pady=(25, 0))
        username_key.pack(pady=(5, 0))
        
        password.pack(anchor="w", padx=175, pady=(10, 0)) 
        password_key.pack(pady=(5, 0))
        
        button = ctk.CTkButton(self, text="Login",command= self.main_page, font=normal_font) 
        button.pack(pady=(40,0))  
        
        button1 = ctk.CTkButton(self, text="Register",command=self.signup,  font=normal_font)
        button1.pack(pady=(15,0))

    def signup(self):
        app._set_appearance_mode("white")
        signup_window = ctk.CTkToplevel()
        signup_window.geometry("500x500") 
        signup_window.title("Todo List")
        signup_window.lift()  
        signup_window.focus_force()  
        signup_window.attributes('-topmost', True)
        bold_font = ctk.CTkFont(family="Arial", size=24, weight="bold")
        label = ctk.CTkLabel(signup_window, text="Register Page", font=bold_font)
        label.pack(pady=(100,0)) 
        signup_username = ctk.CTkLabel(signup_window, text="Username", font=normal_font)
        signup_username_key = ctk.CTkEntry(signup_window, font=normal_font)
        signup_password = ctk.CTkLabel(signup_window, text="Password", font=normal_font)
        signup_password_key = ctk.CTkEntry(signup_window, font=normal_font)
        signup_password2 = ctk.CTkLabel(signup_window, text="Confirm Password", font=normal_font)
        signup_password2_key = ctk.CTkEntry(signup_window, font=normal_font)
        signup_username.pack(anchor="w",padx=175,pady=(25,0))
        signup_username_key.pack(pady=(5,0))
        
        signup_password.pack(anchor="w",padx=175,pady=(10,0))
        signup_password_key.pack(pady=(5,0))
        signup_password2.pack(anchor="w",padx=175,pady=(10,0))
        signup_password2_key.pack(pady=(5,0))
        button = ctk.CTkButton(signup_window, text="Register",font=normal_font) 
        button.pack(pady=(40,0))

        
    def clock_page(self):
        def update_time():
            string_time = strftime('%H:%M:%S %p')
            digital_clock.configure(text=string_time)
            digital_clock.after(1000, update_time)

        root = ctk.CTkToplevel()
        root.title("Digital Clock")
        root.geometry("400x200")  
        root.lift()  
        root.focus_force()  
        root.attributes('-topmost', True)  
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        
        date_label = ctk.CTkLabel(root, text=d2, font=("Arial", 20, "bold"), text_color="white")
        date_label.pack(pady = (50,0))
        digital_clock = ctk.CTkLabel(root, font=("Arial", 35, "bold"), text_color="white")
        digital_clock.pack(pady=10)
        update_time()
    
        countdown = ctk.CTkButton(root, text="Countdown Timer", command=self.countdown_page)    
        countdown.pack(pady=20)
        
    def countdown_page(self):
        cd = ctk.CTkToplevel()
        cd.title("Countdown Timer")
        cd.geometry("600x450")
        cd.lift()  
        cd.focus_force()  
        cd.attributes('-topmost', True)   
        global cd_time, timer_running
        cd_time = 0
        timer_running = None
        
        entry_frame = ctk.CTkFrame(cd)
        entry_frame.pack(pady=(20, 0))  

        hours_entry = ctk.CTkEntry(entry_frame, placeholder_text="Hours", font=normal_font, width=80)
        hours_entry.pack(side="left", padx=(10, 5))  

        minutes_entry = ctk.CTkEntry(entry_frame, placeholder_text="Minutes", font=normal_font, width=80)
        minutes_entry.pack(side="left", padx=5)

        seconds_entry = ctk.CTkEntry(entry_frame, placeholder_text="Seconds", font=normal_font, width=80)
        seconds_entry.pack(side="left", padx=(5, 10))

        timer_label = ctk.CTkLabel(cd, text="00:00:00", font=("Arial", 35, "bold"), text_color="white")
        timer_label.pack(pady=(70, 50))
        
        
        
        def update_timer():
            global cd_time,timer_running
            if cd_time > 0:
                hours = cd_time // 3600
                minutes = (cd_time % 3600) // 60
                seconds = cd_time % 60
                timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
                cd_time -= 1
                timer_running = cd.after(1000, update_timer)
            else:
                timer_label.configure(text="Time's up!")
                timer_running = None

        def set_timer():
            global cd_time, timer_running
            try:
                stop_timer()
                hours = int(hours_entry.get()) if hours_entry.get() else 0
                minutes = int(minutes_entry.get()) if minutes_entry.get() else 0
                seconds = int(seconds_entry.get()) if seconds_entry.get() else 0
                cd_time = (hours * 3600) + (minutes * 60) + seconds
                if cd_time > 0:
                    update_timer()
                else:
                    timer_label.configure(text="Invalid input")
            except ValueError:
                timer_label.configure(text="Invalid input")

        def stop_timer():
            global timer_running
            if timer_running:
                cd.after_cancel(timer_running)
                timer_running = None

        def continue_timer():
            global cd_time, timer_running
            if cd_time > 0 and timer_running is None:
                update_timer()

        def reset_timer():
            global cd_time
            stop_timer()
            cd_time = 0
            timer_label.configure(text="00:00:00")
        start_button = ctk.CTkButton(cd, text="Start", font=normal_font, command=set_timer, height=30, width=90)
        start_button.pack(pady=(10, 0))

        continue_button = ctk.CTkButton(cd, text="Continue", font=normal_font, command=continue_timer, height=30, width=90)
        continue_button.pack(pady=(10, 0))

        stop_button = ctk.CTkButton(cd, text="Stop", font=normal_font, command=stop_timer, height=30, width=90)
        stop_button.pack(pady=(10, 0))

        reset_button = ctk.CTkButton(cd, text="Reset", font=normal_font, command=reset_timer, height=30, width=90)
        reset_button.pack(pady=(10, 0))
        
    def main_page(self):
        app._set_appearance_mode("white")
        login_window = ctk.CTkToplevel(self)
        login_window.geometry("1200x600")
        login_window.title("Todo List")
        
        calendar = ctk.CTkImage(
            light_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/calendar.png'),
            dark_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/calendar.png'),
            size=(100, 100)
        )
        clock = ctk.CTkImage(
            light_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/clock.png'),
            dark_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/clock.png'),
            size=(100, 100)
        )
        todolist = ctk.CTkImage(
            light_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/todolist.png'),
            dark_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/todolist.png'),
            size=(100, 100)
        )
        setting = ctk.CTkImage(
            light_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/setting.png'),
            dark_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/setting.png'),
            size=(100, 100)
        )

        note = ctk.CTkImage(
            light_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/note.png'),
            dark_image=Image.open('C:/Users/ASUS/Documents/Github/Problem/KMITL/Python/Project/images/note.png'),
            size=(100, 100)
        )


        title_label = ctk.CTkLabel(login_window, text="Welcome Back", font=("Arial", 24, "bold"))
        title_label.pack(pady=(60, 10))  

        frame = ctk.CTkFrame(login_window)
        frame.place(relx=0.5, rely=0.5, anchor="center")  

        clock_button = ctk.CTkButton(frame, image=clock, text="", command=self.clock_page)
        clock_button.grid(row=0, column=0, padx=20, pady=20)

        setting_button = ctk.CTkButton(frame, image=setting, text="", command= self.settings_page)
        setting_button.grid(row=0, column=1, padx=20, pady=20)

        note_button = ctk.CTkButton(frame, image=note, text="", command=lambda: print("Note button clicked"))
        note_button.grid(row=0, column=2, padx=20, pady=20)
        
        todolist_button = ctk.CTkButton(frame, image=todolist, text="", command= self.todolist_page)
        todolist_button.grid(row=1, column=0, padx=20, pady=20)

        calendar_button = ctk.CTkButton(frame, image=calendar, text="", command=lambda: ctk.set_appearance_mode("light"))
        calendar_button.grid(row=1, column=1, padx=20, pady=20)

    def settings_page(self):
        settings_window = ctk.CTkToplevel()
        settings_window.geometry("400x300")
        settings_window.title("Settings")
        settings_window.lift()  
        settings_window.focus_force()  
        settings_window.attributes('-topmost', True)
        topic = ctk.CTkLabel(settings_window, text="Settings", font=bold_font)
        topic.pack(pady=(20, 0))
        theme_label = ctk.CTkLabel(settings_window, text="Select Theme:", font=normal_font)
        theme_label.pack(pady=(20, 5))
        theme_option = ctk.CTkOptionMenu(settings_window, values=["Dark", "Light"])
        theme_option.pack(pady=10)

        def change_color():
            global color
            color = theme_option.get()
            ctk.set_appearance_mode(color)
            
        theme_button = ctk.CTkButton(settings_window, text="Change Theme", command=change_color)
        theme_button.pack(pady=10)
        
        close_button = ctk.CTkButton(settings_window, text="Close", command=settings_window.destroy)
        close_button.pack(pady=20)
        
    def todolist_page(self):
        todo_add = ctk.CTkToplevel()
        todo_add.geometry("500x500")
        todo_add.title("To-Do List with Checklist")
        global tasks, task_frame
        tasks = []
        
        def open_add_task_window():
            todo_add = ctk.CTkToplevel()
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

            button_add = ctk.CTkButton(todo_add, text="Add Task", font=font, command=lambda: add_task(
                task_entry, due_date_entry.get(), time_entry.get(), difficulty_option.get(), todo_add
            ))
            button_add.pack(pady=40)

        def add_task(task_entry, due_date, time, difficulty, window):
            task_text = task_entry.get()
            global tasks, task_frame
            if task_text:
                window.destroy()
                
                task_item_frame = ctk.CTkFrame(task_frame)
                task_item_frame.pack(fill="x", pady=5, padx=10)

                task_var = ctk.BooleanVar()
                task_checkbox = ctk.CTkCheckBox(task_item_frame, text=task_text, variable=task_var)
                task_checkbox.pack(side="left")

                view_button = ctk.CTkButton(task_item_frame, text="View", command=lambda: view_task(task_text, due_date, time, difficulty))
                view_button.pack(side="right")

                tasks.append({"text": task_text, "due_date": due_date, "time": time, "difficulty": difficulty, "var": task_var, "frame": task_frame})

        def view_task(task_text, due_date, time, difficulty):
            global tasks
            details_window = ctk.CTkToplevel()
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

        def delete_task():
            global tasks
            for task in tasks:
                if task["var"].get():  
                    task["frame"].destroy()  

            new_tasks = []
            for task in tasks:
                if task["var"].get():
                    task["frame"].destroy()
                else:
                    new_tasks.append(task)
                    
            tasks = new_tasks

        bold_font = ctk.CTkFont(family="Arial", size=24, weight="bold")
        label = ctk.CTkLabel(todo_add, text="My To-Do List", font=bold_font)
        label.pack(pady=(20, 10))

        task_frame = ctk.CTkFrame(todo_add)
        task_frame.pack(pady=(10, 10), fill="both", expand=True)

        add_button = ctk.CTkButton(todo_add, text="Add Task", command=open_add_task_window)
        add_button.pack(pady=10)

        delete_button = ctk.CTkButton(todo_add, text="Delete Selected", command=delete_task)
        delete_button.pack(pady=10)

    
        
app = App()
app.mainloop()
