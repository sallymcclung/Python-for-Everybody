"""
Exercise 12.1: Change the socket program socket1.py to prompt the user for the
URL so it can read any web page. You can use split('/') to break the URL into
its component parts so you can extract the host name for the socket connect call.
Add error checking using try and except to handle the condition where the user
enters an improperly formatted or non-existent URL.
"""

import socket

while True:
    URL = input('Enter the URL: ')
    parts = URL.split('/')
    first = parts[0]
    if first == 'http:':
        host = parts[2]
        document = ''
        for i in parts[3:]:
            document = document + '/' + i
        break
    elif first.startswith('www.'):
        host = parts[0]
        document = ''
        for i in parts[1:]:
            document = document + '/' + i
        break
    else:
        print('Invalid URL input')
        continue

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET http://'+host+document+' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except:
    print('Invalid URL')
    quit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
