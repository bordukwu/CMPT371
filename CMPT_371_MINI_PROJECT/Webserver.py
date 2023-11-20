import socket

# create server socket 
serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)

#Bind server socket to loopback newtwork interface

serv_socket.bind(('127.0.0.1',8000))

#turn the socket to listening mode - server has a max backlog of 10 connections that are established but not accepted
serv_socket.listen(10)

while True:
    #Accept new Connections in an infinite loop 
    client_socket,client_addr = serv_socket.accept()

    print('New connection from', client_addr)

    chunks = []
    while True:
        data = client_socket.recv(2048)
        if not data:
            #client is done with sending 
            break 
        chunks.append(data)

    #Echo the client data back to it
    client_socket.sendall(b''.join(chunks))

    client_socket.close()
