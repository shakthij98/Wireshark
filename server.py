import socket
from datetime import datetime
def server_program():
    # get the hostname
    #host = '192.168.1.207'
    host="192.168.225.79"
    print host
    port = 6883  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    print 'Bind Complete'
    # configure how many client the server can listen simultaneously
    server_socket.listen(0)
    print 'Listening.....'
    a=1   
    t = []
    
    while a==1:
        conn, address = server_socket.accept()  # accept new connection
        print conn
        print address
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            print data
            if not data:
                a=0
                # if data is not received break
                break


    conn.close()  # close the connection
    print t
    

if __name__ == '__main__':
    server_program()
