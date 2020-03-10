# print("###########################################")
# print("         to-do file read and write")
# print("###########################################")
# print()


# Opens the .txt file where tasks are stored, saves them to memory, and prints them to the console
def read_tasks():
    task_data = []
    with open("task_file.txt", "r") as task_file:
        for line in task_file.readlines():
            task_data.append(line.rstrip())
    return task_data


# Appends entry to the task_file
def add_task(task):
    if task not in read_tasks():
        with open("task_file.txt", "a") as task_file:
            task_file.write("\n" + str(task))
    else:
        print("\nError: task already in to-do list\n")


# removes the task input if it exists in the file. Rewrites the file without the removed task
def remove_task(task):
    remove_data = read_tasks()
    if task in remove_data:
        remove_data.remove(task)
        with open("task_file.txt", "w") as task_file:
            for counter, line in enumerate(remove_data):
                if not counter:
                    task_file.write(line)
                elif counter:
                    task_file.write("\n" + line)
    else:
        print("\nError: Task not in to-do list\n")
