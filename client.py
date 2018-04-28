import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))
while True:
 req = input()
 s.send(req)
 rsp = s.recv(1024)
 print(rsp)
s.close()
