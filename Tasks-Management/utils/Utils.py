from model import Task as T
from datetime import datetime
from storage import Storage as S
from colorama import init, Fore, Style
from time import sleep

def welcome_message():
    message = f"""
    {Fore.CYAN}**********************************************
    *                                            *
    *      {Fore.YELLOW}Welcome to Tasks-Management!{Fore.CYAN}          *
    *                                            *
    *   {Fore.GREEN}Organize your tasks efficiently and      *
    *   boost your productivity.{Fore.CYAN}                 *
    *                                            *
    *   {Fore.MAGENTA}Manage deadlines, prioritize tasks,      *
    *   and keep track of your progress easily.{Fore.CYAN}  *
    *                                            *
    **********************************************
    """
    print(message)

def receive_input(value):
    if value == 1:
        name, day, month, year, hour, minute, priority = form_create_task()
        create_task(name, year, month, day, hour, minute, priority)
    else:
        print("This option doesn't exists")


def list_options():
    options = """
    *Choose an option:*

    *1 - Add Task*
    *2 - List Tasks*
    *3 - Remove Task*
    *4 - Search Task*
    *5 - Update Task*
    """
    print(options)

def create_task(name, year, month, day, hour, minute, priority):
    task = T.Task(name,datetime(year,month,day,hour,minute),priority)
    S.task_list.append(task)

def form_create_task():
    name = input("Name:")
    date = input("Date(dd,mm,yyyy hh:mm): ")
    priority = input("Priority(Low - Medium - High): ")
    
    while validate_name(name):
        print("The name must have at least 2 characters (Retry in 2 seconds)")
        sleep(2)
        name = input("Name: ")

    while validate_date(date):
        print("The date must be informed in the format: dd/mm/yyyy hh:mm (Retry in 2 seconds)")
        sleep(2)
        date = input("Date: ")

    formated_priority = format_string(priority)
    while validate_priority(formated_priority):
        print("The priority must be Low, Medium or High (Retry in 2 seconds)")
        sleep(2)
        priority = input("Priority: ")
        fomated_priority = format_string(priority)
    
    day, month, year, hour, minute = extract_date_components(date)
    return name, day, month, year, hour, minute, formated_priority


def validate_date(date_string):
    try:
        # Tenta analisar a string usando o formato especificado
        valid_date = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
        return False  # Retorna o objeto datetime se válido
    except ValueError:
        return True  # Retorna None se a data for inválida

def validate_name(name):
    if len(name)>=2:
        return False
    return True

def validate_priority(priority):
    if priority == "Low" or priority == "Medium" or priority == "High":
        return False
    return True

def format_string(string):
    clean_string = string.replace(" ","")
    formated_string = clean_string.capitalize()
    return formated_string

def extract_date_components(date):
    valid_date = datetime.strptime(date, "%d/%m/%Y %H:%M")
    day = valid_date.day
    month = valid_date.month
    year = valid_date.year
    hour = valid_date.hour
    minute = valid_date.minute
    return day,month,year,hour,minute