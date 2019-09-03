import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP stream
s.bind((socket.gethostname(), 12345))
s.listen(5)

while True:
    clientsocket, address = s.accept() #socket id and IP of client
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg,"utf-8")) #what to send, format

    while True:
        time.sleep(3)
        msg = f"The time is! {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))  # what to send, format


    #clientsocket.close()
    #print(f"Connection from {address} has been closed!")

