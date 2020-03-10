import time
import winsound

# print("###########################################")
# print("              Pomodoro Timer")
# print("###########################################")
# print()

WORK_SOUND = "level-up-01.wav"

def working(minutes):
    minutes *= 60
    print("Work timer started")

    while minutes > -1:
        mins, secs = divmod(minutes, 60)
        formatted_time = "{:02d}:{:02d}".format(mins, secs)
        print("\r", formatted_time, end=' ')
        time.sleep(1)
        minutes -= 1

    winsound.PlaySound(WORK_SOUND, winsound.SND_ASYNC)

    print("\nYour work timer is up! Time to rest\n")
    time.sleep(1)


def resting(minutes):
    minutes *= 60
    print("Rest timer started")

    while minutes > -1:
        mins, secs = divmod(minutes, 60)
        formatted_time = "{:02d}:{:02d}".format(mins, secs)
        print("\r", formatted_time, end=' ')
        time.sleep(1)
        minutes -= 1

    winsound.PlaySound(WORK_SOUND, winsound.SND_ASYNC)
    print("\nYour rest timer is up! Get back to work\n")
    time.sleep(1)


def pomodoro(work, rest):
    working(work)
    resting(rest)
