import sys
reload(sys)
sys.setdefaultencoding('utf8')
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client.connect(('localhost',9090)) 
while True:

  
    msg = 'hello world'  
    client.send(msg.encode('utf-8'))  #send message, python 3 only accpet bute stream
    data = client.recv(1024) 
    print('recv:',data.decode()) 
client.close() 