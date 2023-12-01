"""
Implements a simple HTTP/1.0 Server

"""

# inspired by:
# https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842


import socket


# Define socket host and port
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Parse HTTP headers
    headers = request.split('\n')
    print("line 30", headers)
    filename = headers[0].split()[1]
    print("line 32", filename)
    

    try:
        if filename != '/test.html':
            response400 = 'HTTP/1.0 400 Bad Request\n\n400 Bad Request: Invalid Path'
            print("line 40", response400)
            client_connection.sendall(response400.encode())
            
            

        if filename == '/test.html':

            fileRead = open('test.html')
            content = fileRead.read()
            print("line 44", content)
            fileRead.close()
            response = 'HTTP/1.0 200 OK\n\n' + content
            print("line 49", response)
            client_connection.sendall(response.encode())
    except FileNotFoundError:
        
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'    
        client_connection.sendall(response.encode())


    client_connection.close()

    

# Close socket
server_socket.close()

# import socket

# from handleRequest import handleRequest

# # Define socket host and port
# SERVER_HOST = "127.0.0.1"
# SERVER_PORT = 8000

# # create server socket
# serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# # Bind server socket to loopback newtwork interface

# serv_socket.bind((SERVER_HOST, SERVER_PORT))

# # turn the socket to listening mode - server has a max backlog of 10 connections that are established but not accepted
# serv_socket.listen(10)
# print("Listening on port %s ..." % SERVER_PORT)

# while True:
#     # Accept new Connections in an infinite loop
#     client_socket, client_addr = serv_socket.accept()

#     print("New connection from", client_addr)

#     chunks = []
#     while True:
#         data = client_socket.recv(2048)
#         if not data:
#             #client is done with sending 
#             break 
#         chunks.append(data)

#     # # Get the client request
#     # request = client_socket.recv(1024).decode()
#     # print(request)

#     # # Return an HTTP response
#     # response = handleRequest(request)
#     # client_socket.sendall(response.encode())

#     #Echo the client data back to it
#     client_socket.sendall(b''.join(chunks))

#     # Close connection
#     client_socket.close()

# # Close socket
# serv_socket.close()
