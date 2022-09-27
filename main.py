clients = "david, angeles, "

def create_client(client_id):
    global clients
    clients += client_id
    _add_comma()


def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    clients += ", "


def _print_welcome():
    print("Welcome to my CRUD example page")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate")
    print("[D]elete")

if __name__ == '__main__':
    list_clients()
    create_client("evander")
    print(clients)