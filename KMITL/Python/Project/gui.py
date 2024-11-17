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
        signup_username = ctk.CTkLabel(signup_window, text="Username", font=("Arial", 16))
        signup_username_key = ctk.CTkEntry(signup_window, font=("Arial", 16))
        signup_password = ctk.CTkLabel(signup_window, text="Password", font=("Arial", 16))
        signup_password_key = ctk.CTkEntry(signup_window, font=("Arial", 16))
        signup_password2 = ctk.CTkLabel(signup_window, text="Confirm Password", font=("Arial", 16))
        signup_password2_key = ctk.CTkEntry(signup_window, font=("Arial", 16))
        signup_username.pack(anchor="w",padx=175,pady=(25,0))
        signup_username_key.pack(pady=(5,0))
        
        signup_password.pack(anchor="w",padx=175,pady=(10,0))
        signup_password_key.pack(pady=(5,0))
        signup_password2.pack(anchor="w",padx=175,pady=(10,0))
        signup_password2_key.pack(pady=(5,0))
        button = ctk.CTkButton(signup_window, text="Register",font=("Arial", 16)) 
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

        hours_entry = ctk.CTkEntry(entry_frame, placeholder_text="Hours", font=("Arial", 14), width=80)
        hours_entry.pack(side="left", padx=(10, 5))  

        minutes_entry = ctk.CTkEntry(entry_frame, placeholder_text="Minutes", font=("Arial", 14), width=80)
        minutes_entry.pack(side="left", padx=5)

        seconds_entry = ctk.CTkEntry(entry_frame, placeholder_text="Seconds", font=("Arial", 14), width=80)
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
        start_button = ctk.CTkButton(cd, text="Start", font=("Arial", 14), command=set_timer, height=30, width=90)
        start_button.pack(pady=(10, 0))

        continue_button = ctk.CTkButton(cd, text="Continue", font=("Arial", 14), command=continue_timer, height=30, width=90)
        continue_button.pack(pady=(10, 0))

        stop_button = ctk.CTkButton(cd, text="Stop", font=("Arial", 14), command=stop_timer, height=30, width=90)
        stop_button.pack(pady=(10, 0))

        reset_button = ctk.CTkButton(cd, text="Reset", font=("Arial", 14), command=reset_timer, height=30, width=90)
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
        
        todolist_button = ctk.CTkButton(frame, image=todolist, text="", command=lambda: print("Todolist button clicked"))
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
        topic = ctk.CTkLabel(settings_window, text="Settings", font=("Arial", 24, "bold"))
        topic.pack(pady=(20, 0))
        theme_label = ctk.CTkLabel(settings_window, text="Select Theme:", font=("Arial", 16))
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
    
        
app = App()
app.mainloop()
