clients = "David, Angeles, "
"""var clients saves name of clients"""


def create_client(client_name):
    """this function add the name clients with the capital letter"""
    global clients
    if client_name not in clients:
        clients += client_name.capitalize()
        _add_comma()
    else:
        print("The client is already in the clients list")


def list_clients():
    """this function shows the clients list"""
    global clients
    print(clients)


def update_client(client_name, updated_client_name):
    """this function update data about clients"""
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ",", updated_client_name + ",")
    else:
        print("Client is not in the clients list")


def _add_comma():
    global clients
    clients += ", "


def _print_welcome():
    """welcome message to clients"""
    print("Welcome to my store page:")
    print("*" * 70)
    print("What would you like to do today?")
    print("[C]reate")
    print("[U]pdate")
    print("[D]elete")


def _get_client_name():
    return input("What is the client name? ")
if __name__ == '__main__':
    _print_welcome()
    command = input().upper()
    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == "U":
        client_name = _get_client_name()
        updated_client_name = input("What is the updated client name? ")
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == "D":
        pass
    else: 
        print("Invalid command")
        