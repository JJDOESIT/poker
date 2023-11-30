import socket
import pickle
import _thread
from data import Data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 6276)
s.bind(address)
s.listen(4)
print("Listening...")

data = Data()

def thread(client_socket):
    global data
    personal_id = None

    try:
        client_socket.send(str(data.id).encode())
        personal_id = data.id
        data.players_connected.append(data.id)
        data.id += 1
    except:
        print("Error")
    while True:
        try:
            recv_data = client_socket.recv(4096)
            recv_data = pickle.loads(recv_data)
        except:
            print(f"Client {personal_id} disconnected")
            data.players_connected.remove(personal_id)
            break
        try:
            sent_data = pickle.dumps(data)
            client_socket.send(sent_data)
        except:
            pass

while True:
    client_socket, client_address = s.accept()
    print(f"Client Connected!")
    _thread.start_new_thread(thread, (client_socket,))