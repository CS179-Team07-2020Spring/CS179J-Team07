import sys
reload(sys)
sys.setdefaultencoding('utf8')
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9090)) # bind the port to listen
server.listen(5) #start listening
while True:
    conn,addr = server.accept() 
    print(conn,addr)
    while True:
        data = conn.recv(1024)  # recieve data
        print('recive:',data.decode()) #
        conn.send(data.upper()) # send data
    conn.close()