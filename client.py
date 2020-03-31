import sys
import socket
import time

def client_program():
    #host = '192.168.1.38'  # as both code is running on same pc
    host = '192.168.225.79'
    port = 6883 # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    message = 'Hello world shakthij98'  # take input
    
    for i in range(5):
        print i
        client_socket.send(message)
        time.sleep(5)  

    # send message
    #data = client_socket.recv(1024).decode()  # receive response        

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
