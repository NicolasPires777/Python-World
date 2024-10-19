from colorama import Fore

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
