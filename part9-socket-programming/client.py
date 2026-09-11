# import socket
# client = socket.socket()
# client.connect(("127.0.0.1",5000))
# client.close()



#sending message
# import socket
# client = socket.socket()
# client.connect(("127.0.0.1",5000))
# client.sendall("Hello, I am client".encode())
# client.close()


#sending message and receives a message
# import socket
# client = socket.socket()
# client.connect(("127.0.0.1",5000))
# client.sendall("Hello, I am client".encode())
# message = client.recv(1024).decode()
# print(message)
# client.close()


#Chatting with Server
# import socket
# client = socket.socket()
# client.connect(("127.0.0.1",5000))  #client.connect((whatsapp.com",5000)) 
# while True:
#     message = input("Client: ")
#     client.sendall(message.encode())
#     if message == "bye":
#         break
#     response = client.recv(1024).decode()
#     print("Server: ",response)

# client.close()


