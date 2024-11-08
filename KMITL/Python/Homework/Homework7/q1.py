class Clock:
    def set_time(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def get_time(self):
        return f"{self.hour:02}:{self.minute}:{self.second:02}"
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second -= 60
            self.minute += 1
            if self.minute == 60:
                self.hour += 1
                self.minute -= 60
                if self.hour == 24:
                    self.hour = 0
    def display_time(self):
        if 0 <= self.hour <= 11:
            print(f"{self.hour:02}:{self.minute}:{self.second:02} AM") 
        elif 12 < self.hour <= 23:
            current_hour = self.hour - 12
            print(f"{current_hour:02}:{self.minute}:{self.second:02} PM") 
        elif self.hour == 12:
            print(f"{self.hour:02}:{self.minute}:{self.second:02} PM") 
        else:
            print("Dont know") 
        
clock = Clock()
clock.set_time(14,30,5)
clock.tick()
print(clock.get_time())
clock.display_time()