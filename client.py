import os, socket, sys, threading

class Output(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)

        self.sock = sock

    def run(self):
        return_msg = self.sock.recv(1024)
        message = return_msg.decode()

        while return_msg:
            sys.stdout.write(return_msg.decode())
            return_msg = self.sock.recv(1024)

args = sys.argv

if len(args) != 2:
    print("Incorrect Usage: py client.py <port number>")
    exit(0)

address, port = 'localhost', args[1]

name = sys.stdin.readline().strip()

print("Connecting to server on port " + port + " with username " + name)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((address, int(port)))

output = Output(sock)
output.start()

sock.send(name.encode())

message = sys.stdin.readline()

while message:
    sock.send((name + ": " + message).encode())
    message = sys.stdin.readline()

sock.shutdown(0)
sock.close()
os._exit(0)