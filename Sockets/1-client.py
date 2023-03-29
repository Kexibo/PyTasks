import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5000))
message = 0
while message != 'Пока':
    message = input()
    sock.send(bytes(message, encoding = 'UTF-8'))
    data = sock.recv(1024)
    print(data)
sock.close()
