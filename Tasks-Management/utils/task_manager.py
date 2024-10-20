from datetime import datetime
from time import sleep
from model import Task as T
from storage import Storage as S

def create_task(name, year, month, day, hour, minute, priority):
    task = T.Task(name, datetime(year, month, day, hour, minute), priority)
    S.task_list.append(task)

def list_tasks():
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
    sleep(1)
            