class Task:
    def __init__(self, name, date, priority):
        self.name = name
        self.date = date
        self.priority = priority

    def show_info(self):
        print(f"Task: {self.name}\nDate:{self.date}\nPriority:{self.priority}")

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_priority(self):
        return self.priority

    def set_name(self, name):
        self.name = name
    
    def set_date(self, date):
        self.date = date

    def set_priority(self, priority):
        self.priority = priority

    def edit_task(self, name, date, priority):
        self.name = name
        self.date = date
        self.priority = priority



