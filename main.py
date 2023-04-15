'''
Countdown Timer
-------------------------------------------------------------
'''

import time


def countdown(userTime):
    while userTime >= 0:
        mins, secs = divmod(userTime, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        userTime -= 1
    print('Lift off!')


if __name__ == '__main__':
    user_time = int(input("Enter a time in seconds: "))
    countdown(user_time)
