import socket
import threading
import data_player

Data_Base={}
def connect_DB(port):
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("connected")
    data = client_socket.recv(1024).decode()
    return data,client_socket, client_address
def build_player(data):
    player = data_player(data.split()[1].split("?"))
    Data_Base[player.get_name()] = (player.get_password(),0,0,0)

def check_player(data):
    player = data_player(data.split()[1].split("?"))
    if Data_Base[player.get_name()][0] == data_player(data.split()[1].split("?"))[1]:
        return True
    return False

def add_data(data):
    name= data.split()[0]
    win = data.split()[1]
    best=data.split()[2]
    player=data_player(name,Data_Base[name])
    password=Data_Base[name][0]
    player.check_best_time(best)
    player.add_games()
    if win==1:
        player.add_wins()
    Data_Base[name] = (password,player.get_games(),player.get_wins(),player.get_best_time())

def handle_DB(PORT):
    data, client_socket, client_address= connect_DB(PORT)
    check_mission = data.split()[0]
    if (check_mission == 1):
        build_player(data.split()[1])
        response = "accepted"
    elif (check_mission == 2):
        if check_player(data.split()[1]):
            response = "right"
        else:
            response = "wrong"
    elif (check_mission == 3):
        add_data(data.split()[1])
        response = "accepted"
    client_socket.send(response)

def main():
    connect_DB(12345)

if __name__ == '__main__':
    main()
