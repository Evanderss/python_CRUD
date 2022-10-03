import sys
from unicodedata import name
clients = [
    {
        "name": "David",
        "company": "Facebook",
        "position": "Java Developer",
    },
    {
        "name": "Angeles",
        "company": "Canvas",
        "position": "Designer",
    }
]
"""var clients saves name of clients"""


def create_client(client):
    """this function add the name clients with the capital letter"""
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print("The client is already in the clients list")


def list_clients():
    """this function shows the clients list"""
    for index, client in enumerate(clients):
        uid=index
        name=client['name']
        company=client['company']
        position=client['position']
        print(f"{uid} | {name} | {company} | {position}")
            

def update_client(client_name, updated_client_name):
    """this function update data about clients"""
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print("Client is not in the clients list")


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else: 
        print("Client is not in the clients list")


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    """welcome message to clients"""
    print("Welcome to my store page:")
    print("*" * 100)
    print("What would you like to do today?")
    print("[C]reate")
    print("[U]pdate")
    print("[D]elete")
    print("[S]earch")


def _get_client_field(field_name):
    field = None
    while not field:
        field = input(f"What is the client {field_name}?")
    return field

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input("What is the client name? ")

        if client_name == "exit":
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    _print_welcome()
    command = input().upper()
    if command == "C":
        client = {
            "name": _get_client_field("name"),
            "company": _get_client_field("company"),
            "position": _get_client_field("position"),
        }
        create_client(client)
        list_clients()
    elif command == "U":
        client_name = _get_client_name()
        updated_client_name = input("What is the updated client name? ")
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == "S":
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("The client is in the clients list")
        else:
            print(f"the client: {client_name} is not in clients list")
    else: 
        print("Invalid command")
        