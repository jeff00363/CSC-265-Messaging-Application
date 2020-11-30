import socket

client_socket = socket.socket()
port = 2001
client_socket.connect(('192.168.1.109',port))


recv_msg = client_socket.recv(1024)
print(recv_msg)

#makes the user
send_msg = input("Enter Username:")
client_socket.send(send_msg.encode())



#send messages to users
while True:
    recv_msg = client_socket.recv(1024)
    print (recv_msg)
    print("Enter as @user:text")
    send_msg = input("Send Message")
    if send_msg == 'Close':
        break;
    else:
        client_socket.send(send_msg.encode())

client_socket.close()