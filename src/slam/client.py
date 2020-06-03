import socket

host = '127.0.0.1'  # The server's hostname or IP address
port = 65432        # The port used by the server

s = socket.socket()         # Create a socket object

s.connect((host, port))
s.send("Hello server!")
f = open('tosend.png','rb')
print('Sending...')
l = f.read(1024)
while (l):
    print('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print("Done Sending")
print s.recv(1024)
s.close()