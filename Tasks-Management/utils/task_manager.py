from datetime import datetime
from time import sleep
from model import Task as T
from storage import Storage as S
from . import input_handler as I

def create_task(name, year, month, day, hour, minute, priority):
    task = T.Task(name, datetime(year, month, day, hour, minute), priority)
    S.task_list.append(task)

def list_tasks_by_priority():
    low = []
    medium = []
    high = []
    c = 1
    for task in S.task_list:
        if task.priority == "Low":
            low.append(task)
        elif task.priority == "Medium":
            medium.append(task)
        elif task.priority == "High":
            high.append(task)
        else:
            return False
    print("\nHigh priority tasks:")
    for i in high:
        print(f"{c} - {i.name} | Date: {i.date}")
        c+=1
    print("\nMedium priority tasks:")
    for i in medium:
        print(f"{c} - {i.name} | Date: {i.date}")
        c+=1
    print("\nLow priority tasks:")
    for i in low:
        print(f"{c} - {i.name} | Date: {i.date}")
        c+=1
    print("\nReturning to menu...")
    sleep(3)

def list_tasks():
    i = 1
    for task in S.task_list:
        print(f"{i} - {task.name}")
        i+=1

def remove_task(num):
    try:    
        del S.task_list[num]
        print("Task deleted! Returning to menu...")
        sleep(2)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False   

def update_task(num):
    try:    
        task = S.task_list[num]
        print(f"Selected task: {task.name}")
        sleep(1)
        name, day, month, year, hour, minute, priority = I.form_create_task()
        create_task(name, year, month, day, hour, minute, priority)
        del S.task_list[num]
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False          