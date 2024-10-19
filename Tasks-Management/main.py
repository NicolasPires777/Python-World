from utils.messages import welcome_message, list_options
from utils.input_handler import receive_input

# Exibe a mensagem de boas-vindas e lista as opções
welcome_message()
list_options()

# Recebe a opção do usuário
value = int(input("Choose an option: "))
receive_input(value)
