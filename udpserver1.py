import socket

recv_ip ="192.168.1.109"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((recv_ip,recv_port))

while 4 > 2 :
    data = s.recvfrom(100)
    print("\nmessage from sender",data[0])
    print("sender IP + port --socket ", data[1])
    rply = input("type your rply :")
    n_rply = rply.encode('ascii')
    s.sendto(n_rply,data[1])
s.close()
