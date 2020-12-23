"""
Exercise 12.2: Change your socket program so that it counts the number of characters
it has received and stops displaying any text after it has shown 3000 characters. The
program should retrieve the entire document and count the total number of characters
and display the count of the numbers at the end of the document.
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

received = received.decode()
print(received[:3000])
print('Total data count:',len(received))
mysock.close()
