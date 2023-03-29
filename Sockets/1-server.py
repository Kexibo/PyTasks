"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе. Сигналом окончания связи служит слово "Пока".
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5000))
sock.listen(10)
print('Сервер запущен, для завершения напишите Пока')
message = 0
while message != 'Пока':
    conn, addr = sock.accept() # начинаем принимать соединения 
    print(addr,' :', str(conn.recv(1024))) # выводим информацию о подключении
    if str(conn.recv(1024)) == 'Пока':
        continue
    message = input()
    conn.send(message)
# conn.close()