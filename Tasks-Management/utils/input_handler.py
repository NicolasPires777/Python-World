from time import sleep
import utils.validators as V
import utils.task_manager as TMa

def receive_input(value):
    if value == 1:
        name, day, month, year, hour, minute, priority = form_create_task()
        TMa.create_task(name, year, month, day, hour, minute, priority)
        return True
    elif value == 2:
        TMa.list_tasks_by_priority()
        return True
    elif value == 3:
        form_delete_task()
        return True
    elif value == 4:
        form_search_task()
        return True
    elif value == 5:
        form_update_task()
        return True
    elif value == 6:
        return False
    else:
        print("This option doesn't exist")
        return True

def form_create_task():
    name = input("Name: ")
    date = input("Date(dd/mm/yyyy hh:mm): ")
    priority = input("Priority(Low - Medium - High): ")

    while V.validate_name(name):
        print("The name must have at least 2 characters (Retry in 2 seconds)")
        sleep(2)
        name = input("Name: ")

    while V.validate_date(date):
        print("The date must be informed in the format: dd/mm/yyyy hh:mm (Retry in 2 seconds)")
        sleep(2)
        date = input("Date: ")

    formated_priority = V.format_string(priority)
    while V.validate_priority(formated_priority):
        print("The priority must be Low, Medium or High (Retry in 2 seconds)")
        sleep(2)
        priority = input("Priority: ")
        formated_priority = V.format_string(priority)

    day, month, year, hour, minute = V.extract_date_components(date)
    print("Saving...")
    sleep(1)
    print("Sucessfull! Redirecting...")
    sleep(1)
    print("")
    return name, day, month, year, hour, minute, formated_priority

def form_delete_task():
    print(f"Here is your tasks: ")
    sleep(1)
    TMa.list_tasks()
    sleep(1)
    delete = int(input("Which task do you want to delete?: "))
    TMa.remove_task(delete-1)

def form_update_task():
    print(f"Here is your tasks: ")
    sleep(1)
    TMa.list_tasks()
    sleep(1)
    update = int(input("Which task do you want to update?: "))
    TMa.update_task(update-1)

def form_search_task():
    decision = int(input("Which field do you want to use as a filter?\n1 - Name\n2 - Date\nDecision: "))
    if decision == 1:
        name = input("What's the name of the task?: ")
        tasks = TMa.search_by_name(name)
    elif decision == 2: 
        date = input("What's the date of the task? (yyyy-mm-dd): ")
        tasks = TMa.search_by_date(date)
    else:
        print("Option not found, returning to menu...")
        sleep(1.5)
    print(f"Tasks found:")
    i = 0
    for task in tasks:
        print(f"{i+1} - {task.name}\nDate: {task.date}\nPriority: {task.priority}\n")
        i+=1
    sleep(2)
    