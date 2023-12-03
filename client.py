import socket
import pickle


class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = None

    # Connect to the server
    def connect(self, ip, port):
        try:
            self.client_socket.connect((ip, int(port)))
            self.id = int(self.client_socket.recv(1024).decode())
        except:
            self.id = -1

    # Send objects to the server
    def send_object(self, object):
        data_string = pickle.dumps(object)
        self.client_socket.send(data_string)

    # Receive objects from the server
    def receive_object(self):
        recv_data = self.client_socket.recv(4096)
        recv_data = pickle.loads(recv_data)
        return recv_data

    # Sync all the players
    def sync_players(self, player_list, received_player_list):
        for index in range(4):
            player_list[index] = received_player_list[index]
