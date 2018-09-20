import socket


def client():
    '''
    function to define the client behaviour.
    '''
    client_socket = socket.socket() # creating the socket object.
    client_socket.connect((socket.gethostname(), 9500)) # connecting to the socket object.
    client_str = "Enter Input : "
    message = raw_input(client_str) # Take the input from the user. 

    while message.lower().strip() != 'bye': 
        client_socket.send(message) # send the message given by client to server.
        data = client_socket.recv(1024) # receive the response from the server.
        print('Received from server: ' + data) # show what is received from the server.
        message = raw_input(client_str) # keep taking the input unless client enter bye.

    client_socket.close() # close the socket connection.


if __name__ == '__main__':
    client()