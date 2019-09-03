import socket
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP stream
s.connect((socket.gethostname(), 12345))

while True:

    full_msg = b''
    new_msg = True

    while True:
        msg = s.recv(16) #receive data into buffer chunk size 1024 bytes

        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

print(full_msg)