import os, socket, sys, threading

class echoMessage(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)

        self.sock = sock

    def run(self):
        return_msg = self.sock.recv(1024)
        name = return_msg.decode()

        if sockets.get(name) == None:
            sockets[name] = self.sock

        return_msg = self.sock.recv(1024)
        message = return_msg.decode()
        name = message.split(": ", 1)[0]

        while return_msg:
            for username, socket in sockets.items():
                if username != name:
                    socket.send(message.encode())

            return_msg = self.sock.recv(1024)
            message = return_msg.decode()
            name = message.split(": ", 1)[0]

args = sys.argv

if len(args) != 2:
    print("Incorrect Usage: py server.py <port number>")
    exit(0)

port = args[1]

print("Starting server on port " + port)

sockets = {}

while(True):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('', int(port)))
    serversocket.listen(5)
    sock, addr = serversocket.accept()

    echoThread = echoMessage(sock)
    echoThread.start()

sock.shutdown(0)
sock.close()
os._exit(0)