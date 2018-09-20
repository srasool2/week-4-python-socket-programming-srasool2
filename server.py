import socket

def server():
    '''
    function to define the server behaviour.
    '''
    server_socket = socket.socket() # creating the socket object.
    server_socket.bind((socket.gethostname(), 9500)) # bind to the socket object on port 5000 .

    server_socket.listen(1) # list on the socket.
    connection, address = server_socket.accept() # accept the client connection
    print("Connection from: " + str(address)) # print the details of the client.
    while True:
        data = connection.recv(1024) # receive the data from the client
        if not data: # if no data break.
            break
        print("Client Sent: " + str(data)) # show data sent by client.
        if str(data).lower() == "hi":
            resp = "hello"
        else:
            resp = "Goodbye"
        connection.send(resp) # send back the response.
    connection.close()


if __name__ == '__main__':
    server()