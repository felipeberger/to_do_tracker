import csv


# Opens the .txt file where tasks are stored, saves them to memory, and prints them to the console
def read_tasks():
    task_data = []
    with open("task_file.txt", "r") as task_file:
        csv_reader = csv.reader(task_file, delimiter=',')
        for row in csv_reader:
            task_data.append(row)
    return task_data


# Appends entry to the task_file
def add_task(task):
    add_task_data = read_tasks()
    if task not in add_task_data:
        add_task_data.append([task, "0"]) # adds a zero after task, which will be used for the time-tracking function
    else:
        print("\nError: task already in to-do list\n")
    with open("task_file.txt", "w", newline='') as task_file:
        csv_writer = csv.writer(task_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in add_task_data:
            csv_writer.writerow(row)


# removes the task input if it exists in the file. Rewrites the file without the removed task
def remove_task(task):
    remove_data = read_tasks()
    if task in remove_data:
        remove_data.remove(task)
        with open("task_file.txt", "w", newline='') as task_file:
            csv_writer = csv.writer(task_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in remove_data:
                csv_writer.writerow(row)
    else:
        print("\nError: Task not in to-do list\n")
