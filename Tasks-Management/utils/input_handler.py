from time import sleep
import utils.validators as V
import utils.task_manager as TMa

def receive_input(value):
    if value == 1:
        name, day, month, year, hour, minute, priority = form_create_task()
        TMa.create_task(name, year, month, day, hour, minute, priority)
    else:
        print("This option doesn't exist")

def form_create_task():
    name = input("Name:")
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
        fomated_priority = format_string(priority)

    day, month, year, hour, minute = V.extract_date_components(date)
    return name, day, month, year, hour, minute, formated_priority
