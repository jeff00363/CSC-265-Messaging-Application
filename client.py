import socket

client_socket = socket.socket()
port = 12345
client_socket.connect(('serverip',port))


recv_msg = client_socket.recv(1024)
print recv_msg

#makes the user
send_msg = raw_input("Enter Username:")
client_socket.send(send_msg)



#send messages to users
while True:
    recv_msg = client_socket.recv(1024)
    print recv_msg
    print("Enter as @user:text")
    send_msg = raw_input("Send Message")
    if send_msg == 'Close':
        break;
    else:
        client_socket.send(send_msg)

client_socket.close()