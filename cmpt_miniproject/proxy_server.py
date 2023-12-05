import socket
import getpass

# Define socket host and port for the proxy server
PROXY_HOST = "127.0.0.1"
PROXY_PORT = 8080

# Define the destination web server host and port
WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 8000

# Create proxy server socket
proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
proxy_server.bind((PROXY_HOST, PROXY_PORT))
proxy_server.listen(1)
print('Proxy server listening on port %s ...' % PROXY_PORT)

# Function to forward the request to the destination web server
def forward_request(request):
    print("forwarding request to proxy server for processing")
    # Create a socket to communicate with the destination web server
    web_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    web_server_socket.connect((WEB_SERVER_HOST, WEB_SERVER_PORT))

    # Forward the client's request to the destination web server
    web_server_socket.sendall(request.encode())

    # Receive the response from the destination web server
    response = web_server_socket.recv(1024)
    web_server_socket.close()

    return response

while True:
    # Wait for client connections
    client_connection, client_address = proxy_server.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()

    if request:
        # Forward the request to the destination web server
        response = forward_request(request)

        # Send the response back to the client
        client_connection.sendall(response)

    client_connection.close()
