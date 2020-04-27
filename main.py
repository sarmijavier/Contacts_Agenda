import sys
import csv
import os


CLIENT_TABLE = 'clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']


clients =[]

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():

    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
    
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)
        
   

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')
    

def list_clients():
    print('uid|name|company|email|position')
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
                uid=idx,
                name=client['name'],
                company=client['company'],
                email=client['email'],
                position=client['position']
                
                
            ))


def update_client(id_client):
    global clients

    for id, client in enumerate(clients):

    	if id == id_client:

    		client['name'] = input('please, put the new name')
    		client['company'] = input('please, put the new company')
    		client['email'] = input('please, put the new email')    		
    		client['position'] = input('please, put the new position')

    return clients

   		

def delete_client(client_name):
    global clients

    for id,client in enumerate(clients):
        if client['name'] == client_name:
            del clients[id]

    return clients


def search_client(client_name):
    for client in clients:
        if client['name'] == client_name:
            return True
        else:
            return False


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print("""
                (0))  ((O)     W  W      c  c     .-.   \\\    ///       
                 ||    ||  wWw(O)(O)     (OO)   c(O_O)c ((O)  (O)) wWw   
                 || /\ ||  (O)_ ||     ,'.--.) ,'.---.`, | \  / |  (O)_  
                 ||//\\|| .' __)| \   / //_|_\/ /|_|_|\ \||\\//|| .' __) 
                 / /  \ \(  _)  |  `. | \___  | \_____/ ||| \/ ||(  _)   
                ( /    \ )`.__)(.-.__)'.    ) '. `---' .`||    || `.__)  
                 )      (       `-'     `-.'    `-...-' (_/    \_)    
                 """)

    
    print('*' * 100)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client') 


def _client_get_client_datas():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client;


def _get_client_field(field_name):
    field = None
    while field == None:
        field = input('What is the client {}?'.format(field_name))
    
        return field


def _get_client_name():
    client_name = None

    while not client_name:

        client_name = input('What is the client name ?  ')
        if client_name == 'exit':
            client_name = None
            break
    
    if not client_name:
            sys.exit()
    return client_name



 
if __name__=='__main__':
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        
        client = _client_get_client_datas()
        create_client(client)
        
    elif command == 'D':
            
        name =  input('please, put the client\'s name  ')
        delete_client(name)
        
    elif command == 'U':
      	
      	id = input('please, put the id client')
      	id = int(id)
      	update_client(id)
      	
      	

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    elif command == 'L':
        list_clients() 

    else:
        print('Invalid command')
        

    _save_clients_to_storage()
    























