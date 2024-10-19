from datetime import datetime

def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%d/%m/%Y %H:%M")
        return False
    except ValueError:
        return True

def validate_name(name):
    return len(name) < 2

def validate_priority(priority):
    return priority not in ["Low", "Medium", "High"]

def extract_date_components(date):
    valid_date = datetime.strptime(date, "%d/%m/%Y %H:%M")
    return valid_date.day, valid_date.month, valid_date.year, valid_date.hour, valid_date.minute

def format_string(string):
    clean_string = string.replace(" ", "")
    return clean_string.capitalize()  # Corrige e padroniza o formato
