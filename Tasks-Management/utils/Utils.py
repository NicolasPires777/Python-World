from ..model import Task as T
from datetime import datetime
from ..storage import Storage as S



def create_task(name, year, month, day, hour, minute, priority):
    task = T.Task(name,datetime(year,month,day,hour,minute),priority)
    S.task_list.append(task)

