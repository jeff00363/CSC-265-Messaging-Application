import socket, threading

clientInRoom = {}
port = 9999
hostIP = socket.gethostbyname(socket.gethostname())
format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostIP, port))
server.listen()


def make_server():
    print("--Server running on \n IP : %s  \n Port : %s" % (hostIP, port))

    while True:
        client_conn, addr = server.accept()
        userName = client_conn.recv(2048)
        userName = userName.decode(format)
        clientInRoom[userName] = client_conn

        thread = threading.Thread(target=receive_msg, args=(client_conn, userName))
        thread.start()

        print('Connection made from IP : %s, User name : %s\n' % (addr[0], userName))
        print('%s active connection(s) with the server remain\n' % len(clientInRoom))

        send_msg('just joined!'.encode(format), userName)


def receive_msg(client_conn, userName):
    print('--Waiting for a response\n')
    while True:
        try:
            msg = client_conn.recv(2048)
            send_msg(msg, userName)
            print(userName + ":- " + msg.decode(format))
        except:
            client_conn.close()
            del (clientInRoom[userName])
            print(userName, " has left")
            if len(clientInRoom) < 1:
                print('No active connection with the sever remain\n')
            else:
                print('%s active connection(s) with the server remain\n' % len(clientInRoom))
            break


def send_msg(msg, otherClients):
    if len(clientInRoom) is not None:
        for userName in clientInRoom:
            if userName != otherClients:
                user_msg = otherClients + ':- ' + msg.decode(format)
                clientInRoom[userName].send(user_msg.encode(format))


if __name__ == "__main__":
    make_server()
