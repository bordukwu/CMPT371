def send_304_response(client_socket, content):
    response_headers = [
        'HTTP/1.1 304 Not Modified',
        'Cache-Control: no-cache',
        'Content-Length: 0',
        # Add other necessary headers as per your requirements
        # For example: ETag, Expires, Date, etc.
        'Connection: close',
        '',  # This empty line indicates the end of the headers
    ]
    
    response = '\r\n'.join(response_headers)
    response2 = 'HTTP/1.0 304 Not Modified\n\n' + 'HTTP/1.0 304 Not Modified\n\n' + content
    
    # client_socket.sendall(response.encode())
    print("line 80", response)
    client_socket.sendall(response2.encode())
    # print("line 81", response2)