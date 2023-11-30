import socket
import pickle


class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = self.connect()
    
    # Connect to the server
    def connect(self):
        try:
            self.client_socket.connect(('127.0.0.1', 5555))
            return int(self.client_socket.recv(1024).decode())
        except:
            print("Error connecting!")

    # Send objects to the server
    def send_object(self,object):
        data_string = pickle.dumps(object)
        self.client_socket.send(data_string)

    # Receive objects from the server
    def receive_object(self):
        recv_data = self.client_socket.recv(4096)
        recv_data = pickle.loads(recv_data)
        return recv_data
    
        