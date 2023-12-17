import socket
from sys import argv
import subprocess
import platform

test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("0.0.0.0", int(argv[1]))
try:
    test_socket.bind(address)
except:
    exit(1)

test_socket.close()

if platform.system() == "Linux":
    subprocess.Popen(
        ["start", "python3", "server.py", argv[1]],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
elif platform.system() == "Windows":
    subprocess.Popen(
        ["start", "py", "server.py", argv[1]],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
exit(0)
