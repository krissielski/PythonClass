#Lesson15 - Networking


# Physical Address (MAC address) [12-34-56-78-9A-BC]
# TCP/IP  (IP Address)           [192.168.1.1]
# TCP/IP - Port                  [192.168.1.1:80]

# URL                            ["Google.com"]

# URL -> DNS - > IP

# Client/Server
#

import socket

#Client
CLIENTHOST = "192.168.0.43"    
CLIEHTPORT = 4004

#Create Client socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect( (CLIENTHOST,CLIEHTPORT)  )

clientsocket.send( b'Python Rules' )

clientsocket.close()

