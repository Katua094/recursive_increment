import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Timer Complete!")

# Set the desired countdown time in seconds
countdown_time = 300  # 5 minutes

countdown_timer(countdown_time)
