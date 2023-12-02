import socket
from sys import argv
import subprocess

test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("0.0.0.0", int(argv[1]))
try:
    test_socket.bind(address)
except:
    print("Testbind error")
    exit(1)

test_socket.close()
subprocess.Popen(["start", "py", "server.py", argv[1]], shell=True)
exit(0)
