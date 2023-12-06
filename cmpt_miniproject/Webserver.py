"""
Implements a simple HTTP/1.0 Server

"""

# http server inspired by:
# https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842
# password check in console for user input from:
# https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/


import socket
import getpass




#helper functions
def send_304_response(client_socket, content):
    response_headers = [
        'HTTP/1.1 304 Not Modified',
        'Cache-Control: no-cache',
        'Content-Length: 0',
        # other necessary headers
        'Connection: close',
        '',  #the end of the headers
    ]
    
    response = '\r\n'.join(response_headers)
    response2 = 'HTTP/1.0 304 Not Modified\n\n' + 'HTTP/1.0 304 Not Modified\n\n' + content
    
    # client_socket.sendall(response.encode())
    print("line 80", response)
    client_socket.sendall(response2.encode())
    # print("line 81", response2)




# Define socket host and port
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

send_304 = False
content = ""
validPass = ""
validPassFlag = False


while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print("line 63", request)
    if request:
        request_lines = request.split('\r\n')
        request_headers = {}

        # Extracting headers from request
        for line in request_lines[1:]:
            if not line.strip():
                break
            header_name, header_value = line.split(': ')
            request_headers[header_name.lower()] = header_value

        # Check Content-Length header
        content_length = request_headers.get('content-length')
        if content_length:
            print(f"line 78, Content-Length header present: {content_length} bytes")
        else:
            content_length_response = "'HTTP/1.1\n\n 411 Length required'"
            print("line 87 'HTTP/1.1 411 Length required'")
            client_connection.sendall(content_length_response.encode())



    # Parse HTTP headers
    headers = request.split('\n')
    # print("line 30", headers)
    filename = headers[0].split()[1]
    print("line 32", filename)


    if validPassFlag == False:

        validPass = getpass.getpass(prompt='Enter password: ')
        print("line 13", validPass)


        if validPass.lower() != 'password' :

            response = 'HTTP/1.0 403 Forbidden\n\n403 Forbidden - Invalid Password'
            client_connection.sendall(response.encode())
        elif validPass.lower() == 'password':
            validPassFlag = True

    else:
        
        try:
            if filename != '/test.html':
                response400 = 'HTTP/1.0 400 Bad Request\n\n400 Bad Request: Invalid Path'
                print("line 40", response400)
                client_connection.sendall(response400.encode())
                
            
            elif send_304 == True and filename == '/test.html':
                send_304_response(client_connection, content)


            elif send_304 == False and filename == '/test.html':

                fileRead = open('test.html')
                content = fileRead.read()
                # print("line 44", content)
                fileRead.close()
                response = 'HTTP/1.0 200 OK\n\n' + 'HTTP/1.0 200 OK\n\n' + content
                
                # print("line 49", response)
                client_connection.sendall(response.encode())     
                send_304 = True   



        except FileNotFoundError:
            
            response = 'HTTP/1.0 404 NOT FOUND\n\n404 File Not Found'    
            client_connection.sendall(response.encode())


    client_connection.close()

    






