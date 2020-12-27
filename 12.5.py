"""
Exercise 12.5: Change the socket program so that it only shows data after the headers
and a blank line have been received. Remember that recv receives characters (newlines
and all), not lines.
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

received = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    received = received + data

nlpos = received.find(b'\r\n\r\n')
noheaders = received[nlpos+4:].decode()
print(noheaders)
mysock.close()
