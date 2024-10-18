from utils import Utils as U

U.welcome_message()
U.list_options()
value = int(input("Choose an option: "))
U.receive_input(value)