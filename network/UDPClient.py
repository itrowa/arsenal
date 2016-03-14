from socket import *
serverName = 'hostname'
serverPort = 12000

# create a socket object?
# AF_INET: 表明是IPv4; SOCK_DGRAM: 表明是udp socket.
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message, (serverName, serverPort))

# receive message and print.
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()