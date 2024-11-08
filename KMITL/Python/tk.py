import time
import datetime


def update_time():
        nigga = datetime.datetime.now()
        current_time = nigga.strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        update_time()

        
        
update_time()