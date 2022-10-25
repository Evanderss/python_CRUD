import csv
import os


CLIENT_TABLE = "C:/Users/Lennox/Documents/Cursos Back End Developer/python_CRUD/.clients.csv"
CLIENT_SCHEMA = ["name", "company", "position"]
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode="r") as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = "{}.tmp".format(CLIENT_TABLE)
    with open(tmp_table_name, mode="w") as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)
    

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
        print("*"*50)
        print(f"{uid} | {name} | {company} | {position}")
            

def update_client(client_id, updated_client_name):
    """this function update data about clients"""
    global clients
    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client_name
    else:
        print("Client is not in the clients list")


def delete_client(client_id):
    global clients
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break
        else: 
            print("Client is not in the clients list")


def search_client(client_name):
    for client in clients:
        if client["name"] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name):
    field = None
    while not field:
        field = input(f"What is the client {field_name}?")
    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'position': _get_client_field('position'),}
    return client


def _print_welcome():
    """welcome message to clients"""
    print("Welcome to my store page:")
    print("*" * 100)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[R]ead list of clients")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")


if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()
    command = input().upper()
    if command == "C":
        client = _get_client_from_user()
        create_client(client)
    elif command == "R":
        list_clients()
    elif command == "U":
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
    elif command == "D":
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == "S":
        client_name = _get_client_field("name")
        found = search_client(client_name)
        if found:
            print("The client is in the clients list")
        else:
            print(f"the client: {client_name} is not in clients list")
    else: 
        print("Invalid command")
    _save_clients_to_storage()
        