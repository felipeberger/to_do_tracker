import to_do
import timer
import csv

print("###########################################")
print("            to-do list program")
print("###########################################")
print()


def run_event_loop():
    print("What would you like to do?")
    cmd = "EMPTY"

    while cmd != "x" and cmd:
        cmd = input("\n[L]ist tasks, [A]dd task, [R]emove task, [S]tart timer, E[x]it? ")
        cmd = cmd.lower().strip()
        if cmd == "l":
            print("Labels: Task No, Task, Time Spent")
            for idx, tsk in enumerate(to_do.read_tasks(), start=1):
                print(idx, "-", "{}, {} minutes".format(tsk[0], tsk[1]))

        # let's users add a task to the to-do list
        elif cmd == "a":
            new_task = input("\nNew task: ")
            to_do.add_task(new_task)
            print("\nUpdated task list:")
            for idx, tsk in enumerate(to_do.read_tasks(), start=1):
                print(idx, "-", "{}, {} minutes".format(tsk[0], tsk[1]))

        # let's users remove a task from the to-do list
        elif cmd == "r":
            while True:
                try:
                    remove_task = int(input("\nEnter number of task you want to remove: "))
                    break
                except ValueError:
                    print("Not a valid number, please try again")
            for idx, tsk in enumerate(to_do.read_tasks(), start=1):
                if idx == remove_task:
                    to_do.remove_task(tsk)
            print("\nUpdated task list:")
            for idx, tsk in enumerate(to_do.read_tasks(), start=1):
                print(idx, "-", "{}, {} minutes".format(tsk[0], tsk[1]))

        # let's the user create a work countdown timer and a rest timer
        elif cmd == "s":
            while True:
                try:
                    task_selected = int(input("\nWhat task do you want to work on? [task number]: "))
                    work = int(input("How many minutes do you want to work for?: "))
                    rest = int(input("How many minutes do you want to rest for?: "))
                    print("\n")
                    break
                except ValueError:
                    print("Wrong input, please try again")
            timer.pomodoro(work, rest)
            time_worked = work
            data_update = to_do.read_tasks()
            with open("task_file.txt", "w", newline='') as task_file:
                csv_writer = csv.writer(task_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for idx, tsk in enumerate(data_update, start=1):
                    if idx == task_selected:
                        time_worked += int(tsk[1])
                        tsk[1] = time_worked
                for row in data_update:
                    csv_writer.writerow(row)

        # catches any input that is not one of the expected ones and outputs error message
        elif cmd != "x" and cmd:
            print("sorry, '{}' is not a valid input".format(cmd))

    print("\nAll done!")


run_event_loop()
