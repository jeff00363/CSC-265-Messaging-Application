import socket
from main import ConnectionInfo 
recieved_ip = self.ipAddress
recieved_port = self.portNumber

socketmain=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True :
    from main import updateMessages
    messgage = (updateMessages(self.message))
    decodemessage = msg.encode('ascii')
    socketmain.sendto(decodemessage,(recieved_ip,recieved_port))
socketmain.close()