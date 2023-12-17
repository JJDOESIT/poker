import pickle
import _thread
import socket


from sys import argv
from server.data import Data
from server.ready import Ready
from server.actions import Actions
from server.deal import Deal
from server.blinds import Blinds
from client.animations import Animations


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("0.0.0.0", int(argv[1]))
s.bind(address)
print(f"Listening on port {argv[1]} ...")
s.listen(4)

data = Data()
ready = Ready(data)
actions = Actions(data)
animations = Animations()
deal = Deal(data, animations)
blinds = Blinds(data)


def thread(client_socket):
    global data, deal, actions, blinds
    personal_id = None

    try:
        for key, value in data.players_connected.items():
            if value == "open":
                personal_id = key
                break
        data.players_connected[personal_id] = "taken"
        client_socket.send(str(personal_id).encode())
    except:
        print("Error")

    while True:
        # Receive singular player data
        try:
            recv_data = client_socket.recv(50000)
            recv_data = pickle.loads(recv_data)
            data.sync_players(recv_data, personal_id)
            ready.handle_ready_up(recv_data, personal_id)
            actions.handle_move(recv_data, personal_id)
            blinds.initilize_betting_players()
            deal.deal_cards(personal_id)

        # If no data is received, disconnect the player
        except:
            print(f"Client {personal_id} disconnected")
            data.players_connected[personal_id] = "open"
            data.check_for_reset()
            dealer = data.dealer
            deal.check_for_redo(personal_id)
            blinds.check_for_redo(personal_id, dealer)
            data.check_for_redo(personal_id)
            break
        # Send the other players data back
        try:
            sent_data = pickle.dumps(data)
            client_socket.sendall(sent_data)
        except:
            pass


# Listen for new connections and start new threads
while True:
    client_socket, client_address = s.accept()
    print(f"Client Connected!")
    _thread.start_new_thread(thread, (client_socket,))
