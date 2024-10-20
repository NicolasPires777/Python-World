from utils.messages import welcome_message, list_options
from utils.input_handler import receive_input

welcome_message()

while True:
    list_options()
    value = int(input("Choose an option: "))
    response = receive_input(value)
    if not response:
        break
