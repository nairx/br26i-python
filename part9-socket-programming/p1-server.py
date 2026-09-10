# import socket
# server = socket.socket()
# server.bind(("127.0.0.1",5000))
# server.listen()
# print("Waiting for the client")
# client,address = server.accept()
# print("Client Connected",address)
# client.close()
# server.close()


#server receives the message
# import socket
# server = socket.socket()
# server.bind(("127.0.0.1",5000))
# server.listen()
# print("Waiting for the client")
# client,address = server.accept()
# print("Client Connected",address)
# message = client.recv(1024).decode()
# print(message)
# client.close()
# server.close()


#server receives the message and sends reply
# import socket
# server = socket.socket()
# server.bind(("127.0.0.1",5000))
# server.listen()
# print("Waiting for the client")
# client,address = server.accept()
# print("Client Connected",address)
# message = client.recv(1024).decode()
# print(message)
# client.sendall("Hi, I am Server".encode())
# client.close()
# server.close()


#chatting with client
import socket
server = socket.socket()
server.bind(("127.0.0.1",5000))
server.listen()
print("Waiting for the client")
client,address = server.accept()
print("Client Connected",address)
while True:
    message = client.recv(1024).decode()
    print("Clent:",message)
    if message == "bye":
        break
    response = input("Server: ")
    client.sendall(response.encode())
client.close()
server.close()


import socket
server = socket.socket()
server.bind(("127.0.0.1",5000))   #domain - server.bind(("whatsapp.com",5000)) 
for i in range(2):
    server.listen()
    print("Waiting for the client")
    client,address = server.accept()
    print("Client Connected",address)
    while True:
        message = client.recv(1024).decode()
        print("Clent:",message)
        if message == "bye":
            break
        response = input("Server: ")
        client.sendall(response.encode())
client.close()
server.close()