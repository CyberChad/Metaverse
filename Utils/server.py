import socket
import time
import pickle

HEADERSIZE = 10

d = {1: "hey", 2: "there"}

msg = pickle.dumps(d)
msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP stream
s.bind((socket.gethostname(), 12345))
s.listen(5)

while True:
    clientsocket, address = s.accept() #socket id and IP of client
    print(f"Connection from {address} has been established!")

    #msg = "Welcome to the server!"
    msg = pickle.dumps(d)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(msg) #what to send, format

