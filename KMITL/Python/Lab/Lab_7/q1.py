class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def print(self):
        print(f"{self.hour:02}:{self.minute}:{self.second:02} Hrs")
        
time1 = Time(9,30,0)
time1.print()
