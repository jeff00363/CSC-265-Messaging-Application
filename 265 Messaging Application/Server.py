import socket, threading
from cryptography.fernet import Fernet

inRoom = {}
port = 9999
hostIP = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostIP, port))
server.listen(20)

listKey = [b'a3uo8T5xtcfRIVbWuMmkIDjAiRnFff8ZoBVOagf16xg=']
f = Fernet(listKey[0])

def encrypt(msg):
    eCr = f.encrypt(msg)
    print(eCr)
    return eCr
def decrypt(msg):
    dCr = f.decrypt(msg)
    decoded = dCr.decode()
    print(dCr)
    return decoded


def handshake():
    print("--Server running on \n IP : %s  \n Port : %s" % (hostIP, port))

    while True:
        client_conn, addr = server.accept()
        userName = client_conn.recv(2048).decode()
        inRoom[userName] = client_conn

        thread = threading.Thread(target=msgPipeline, args=[client_conn, userName])
        thread.start()

        print('Connection made from IP : %s, User name : %s\n' % (addr[0], userName))
        print('%s active connection(s) with the server remain\n' % len(inRoom))

def send_msg(msg, otherClients):
    if len(inRoom) is not None:
        for userName in inRoom:
            if userName != otherClients:
                #user_msg = otherClients + ':-' + msg
                user_msg = msg
                inRoom[userName].send(user_msg.encode()))

def msgPipeline(client_conn, userName):
    print('--Waiting for a response\n')
    while True:
        try:
            msg = client_conn.recv(2048).decode()
            msgEncode = msg
            send_msg(msgEncode, userName)
            print(userName + ":- " + msg)
        except Exception as e:
            print(e)
            client_conn.close()
            del (inRoom[userName])
            print(userName, " has left")
            if len(inRoom) < 1:
                print('No active connection with the sever remain\n')
            else:
                print('%s active connection(s) with the server remain\n' % len(inRoom))
            break

if __name__ == "__main__":
    handshake()
