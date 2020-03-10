import to_do
import timer

print("###########################################")
print("            to-do list program")
print("###########################################")
print()


def run_event_loop():
    print("What would you like to do?")
    cmd = "EMPTY"
    timer_counter = 0

    while cmd != "x" and cmd:
        cmd = input("\n[L]ist tasks, [A]dd task, [R]emove task, [S]tart timer, E[x]it? ")
        cmd = cmd.lower().strip()
        if cmd == "l":
            for idx, tsk in enumerate(to_do.read_tasks(), start=1):
                print(idx, "- ", tsk)

        # let's users add a task to the to-do list
        elif cmd == "a":
            new_task = input("\nNew task: ")
            to_do.add_task(new_task)
            print("\nUpdated task list:")
            for idx, tsk in enumerate(to_do.read_tasks(), start=1):
                print(idx, "- ", tsk)

        # let's users remove a task from the to-do list
        elif cmd == "r":
            remove_task = int(input("\nEnter number of task you want to remove: "))
            for idx, tsk in enumerate(to_do.read_tasks(), start=1):
                if idx == remove_task:
                    to_do.remove_task(tsk)
            print("\nUpdated task list:")
            for idx, tsk in enumerate(to_do.read_tasks(), start=1):
                print(idx, "- ", tsk)

        # let's the user create a work countdown timer and a rest timer
        # prints the number of timers completed so far
        elif cmd == "s":
            work = int(input("\nHow long [minutes] do you want to work for?: "))
            rest = int(input("How long [minutes] do you want to rest for?: "))
            print("\n")
            timer.pomodoro(work, rest)
            timer_counter += 1
            print("You've completed {} timers so far!".format(timer_counter))

        # catches any input that is not one of the expected ones and outputs error message
        elif cmd != "x" and cmd:
            print("sorry, '{}' is not a valid input".format(cmd))

    print("\nAll done!")


run_event_loop()