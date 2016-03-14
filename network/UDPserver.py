from socket import *
serverPort = 12000

# socket object
serverSocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(('', serverPort))
print "the server is ready to receive"
while True:
    meassage, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)