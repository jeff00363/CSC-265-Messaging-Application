import socket
recv_ip ="192.168.1.109"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4 > 3 :
    msg = input ("Enter your message:")
    nmsg = msg.encode('ascii')
    s.sendto(nmsg,(recv_ip,recv_port))
    print("\n")
    print(s.recvfrom(100))
s.close()