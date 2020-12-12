import socket, threading
from cryptography.fernet import Fernet

# encoding format
format = 'utf-8'

port = 9997
hostIP = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostIP, port))
server.listen(20)


inRoom = {}  # a dict to store username and server.accept() value as key value pair so we can get the addr just by the user name

# initial contact with the server, and server gets the user name which is added to the dict with userName being the key
# thread also starts so more than one client cant join and send and/or recv msgs
def handshakeAndMsgDoorWay():
    print("--Server running on \n IP : %s  \n Port : %s" % (hostIP, port))

    while True:
        client_conn, addr = server.accept()
        userName = client_conn.recv(2048).decode(format)
        inRoom[userName] = client_conn
        thread = threading.Thread(target=msgPipeline, args=[client_conn, userName])
        print('Connection made from IP : %s, User name : %s\n' % (addr[0], userName))
        print('%s active connection(s) with the server remain\n' % len(inRoom))

        thread.start()

# send msg func sends messages to every one except the person it through sending it form userName and get addr from dict
def sendMsg(msg, otherClientUserName):
    for userName in inRoom:
        if userName != otherClientUserName:
            user_msg = msg
            inRoom[userName].send(user_msg.encode(format))

# this is where we can get our messages from the client. Server cant read them because we dont decrypt on serverside.
# It also has a failsafe so if the client bugs out the server does crash. It just disconnects the client
def msgPipeline(client_conn, userName):
    print('--Waiting for a response\n')
    while True:
        try:
            msg = client_conn.recv(2048).decode()
            msgEncode = msg
            sendMsg(msgEncode, userName)
            print(userName + ":- " + msg)
        except Exception:
            client_conn.close()
            del (inRoom[userName])
            print(userName, " has left")
            if len(inRoom) < 1:
                print('No active connection with the sever remain\n')
            else:
                print('%s active connection(s) with the server remain\n' % len(inRoom))
            break


handshakeAndMsgDoorWay()
