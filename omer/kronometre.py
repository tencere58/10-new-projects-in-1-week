import time
from plyer import notification

ttt = input("choose and write one of these 'countdown(0)' or 'stopwatch(1)' : ")


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        hour, mins = divmod(mins, 60)
        tformat = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)

        print(tformat)

        time.sleep(1)
        t -= 1

        if t == 0:
            t = False
            print("Time is up")
            

            notification.notify(title="Time is up!", message="You can stop studying.")
            break

            '''from win10toast import ToastNotifier
            ToastNotifier().show_toast(title="Time is up!", msg="You can stop studying.",
                               duration=20, threaded=True)
'''


def stopwatch(s):

    while s:


        mins, secs = divmod(s, 60)
        hour, mins = divmod(mins, 60)
        sformat = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)

        print(sformat)
        time.sleep(1)
        s += 1

        if s == stop_w:

            print("Time is up")

            notification.notify(title="Time is full!", message="You can rest")
            break


            '''from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title="Time is full!", msg="You can rest",
                                       duration=20, threaded=True)'''

            s = False


if ttt == "0":

    seconds = input("enter an integer for countdown: ")
    seconds = int(seconds)
    countdown(seconds)
                

if ttt == "1":

    stop_w = int(input("enter an integer for stopwatch: "))
    stopwatch(1)
                