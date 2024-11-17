import customtkinter as ctk

class CountdownTimer:
    def __init__(self):
        self.cd = ctk.CTk()
        self.cd.title("Countdown Timer")
        self.cd.geometry("600x450")
        if ctk.get_appearance_mode() == "light":
            self.cd.configure(bg="#black")    
        self.cd_time = 0
        self.timer_running = None

        self.entry_frame = ctk.CTkFrame(self.cd)
        self.entry_frame.pack(pady=(20, 0))  

        self.hours_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Hours", font=("Arial", 14), width=80)
        self.hours_entry.pack(side="left", padx=(10, 5))  

        self.minutes_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Minutes", font=("Arial", 14), width=80)
        self.minutes_entry.pack(side="left", padx=5)

        self.seconds_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Seconds", font=("Arial", 14), width=80)
        self.seconds_entry.pack(side="left", padx=(5, 10))

        self.timer_label = ctk.CTkLabel(self.cd, text="00:00:00", font=("Arial", 35, "bold"), text_color="white")
        self.timer_label.pack(pady=(70, 50))  

        self.start_button = ctk.CTkButton(self.cd, text="Start", font=("Arial", 14), command=self.set_timer, height=30, width=90)
        self.start_button.pack(pady=(10, 0))

        self.continue_button = ctk.CTkButton(self.cd, text="Continue", font=("Arial", 14), command=self.continue_timer, height=30, width=90)
        self.continue_button.pack(pady=(10, 0))

        self.stop_button = ctk.CTkButton(self.cd, text="Stop", font=("Arial", 14), command=self.stop_timer, height=30, width=90)
        self.stop_button.pack(pady=(10, 0))

        self.reset_button = ctk.CTkButton(self.cd, text="Reset", font=("Arial", 14), command=self.reset_timer, height=30, width=90)
        self.reset_button.pack(pady=(10, 0))

        self.cd.mainloop()

    def update_timer(self):
        if self.cd_time > 0:
            hours = self.cd_time // 3600
            minutes = (self.cd_time % 3600) // 60
            seconds = self.cd_time % 60
            self.timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.cd_time -= 1
            self.timer_running = self.cd.after(1000, self.update_timer)
        else:
            self.timer_label.configure(text="Time's up!")
            self.timer_running = None

    def set_timer(self):
        try:
            self.stop_timer()
            hours = int(self.hours_entry.get()) if self.hours_entry.get() else 0
            minutes = int(self.minutes_entry.get()) if self.minutes_entry.get() else 0
            seconds = int(self.seconds_entry.get()) if self.seconds_entry.get() else 0
            self.cd_time = (hours * 3600) + (minutes * 60) + seconds
            if self.cd_time > 0:
                self.update_timer()
            else:
                self.timer_label.configure(text="Invalid input")
        except ValueError:
            self.timer_label.configure(text="Invalid input")

    def stop_timer(self):
        if self.timer_running:
            self.cd.after_cancel(self.timer_running)
            self.timer_running = None

    def continue_timer(self):
        if self.cd_time > 0 and self.timer_running is None:
            self.update_timer()

    def reset_timer(self):
        self.stop_timer()
        self.cd_time = 0
        self.timer_label.configure(text="00:00:00")

