import socket
from main import ConnectionInfo 
recieved_ip = self.ipAddress
recieved_port = self.portNumber

socketmain=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

socketmain.bind((recieved_ip,recieved_port))

while True :
    from main import updateMessages
    data = socketmain.recvfrom(100)
    reply = (updateMessages(self.message))
    decodedreply = reply.encode('ascii')
    socketmain.sendto(decodedreply,data[1])
socketmain.close()
