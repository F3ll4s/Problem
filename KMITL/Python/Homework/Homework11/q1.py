class Clock:
    def __init__(self, hour, minute, second):
        self.setTime(hour, minute, second)

    def setTime(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def run(self):
        if self.second >= 60:
            self.minute += self.second // 60
            self.second = self.second % 60

        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute = self.minute % 60

        if self.hour >= 24:
            self.hour = self.hour % 24

        print(f"{self.hour:02}:{self.minute:02}:{self.second:02}")

    def getTime(self):
        return (self.hour, self.minute, self.second)


class AlarmClock(Clock):
    def __init__(self, a_hour, a_minute, a_second, hour=0, minute=0, second=0,):
        super().__init__(hour, minute, second)
        self.setAlarmClock(a_hour, a_minute, a_second)
        self.switch = False
        self.equal = False

    def setAlarmClock(self, h, m, s):
        self.a_hour = h
        self.a_minute = m
        self.a_second = s

    def alarm_on(self):
        self.switch = True

    def alarm_off(self):
        self.switch = False

    def is_equal(self):
        current = self.getTime()
        alarm = (self.a_hour, self.a_minute, self.a_second)
        print(current)
        print(alarm)
        if current == alarm:
            self.equal = True
        else:
            self.equal = False
    def run(self):
        if self.a_second >= 60:
            self.a_minute += self.a_second // 60
            self.a_second = self.a_second % 60

        if self.a_minute >= 60:
            self.a_hour += self.a_minute // 60
            self.a_minute = self.a_minute % 60

        if self.a_hour >= 24:
            self.a_hour = self.a_hour % 24
        self.is_equal()
        print(self.switch)
        print(self.equal)

        if self.switch and self.equal:
            print("Alarm Ringing")
        else:
            print("Alarm NOT Ringing")

x = Clock(20, 120, 120)
y = AlarmClock(20, 120, 120)

x.run()
y.alarm_on()
y.run()