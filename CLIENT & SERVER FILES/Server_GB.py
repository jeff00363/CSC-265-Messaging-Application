import socket
import threading


class serv(object):
    def __init__(self, hostname, port):
        self.clients = {}

        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server.bind((hostname, port))
        self.tcp_server.listen(10)

        print("Server running on -- IP : %s and port: %s " % (hostname, port))

        while True:
            connection, address = self.tcp_server.accept()
            nickname = connection.recv(2048)
            nickname = nickname.decode()
            self.clients[nickname] = connection

            threading.Thread(target=self.receive_msg, args=(connection, nickname), daemon=True).start()

            print("Connection from %s -- User : %s has joined" % (address[0], nickname))

    def send_msg(self, msg, user):
        for nickname in self.clients:
            if nickname != user:
                msg = user + " : " + msg.decode()
                self.clients[nickname].send(msg.encode())

    def receive_msg(self, connection, nickname):
        print("Waiting for messages \n")
        while True:
            try:
                msg = connection.recv(2048)

                self.send_msg(msg, nickname)
                print(nickname + " : " + msg.decode())
            except:
                connection.close()

                del (self.clients[nickname])

                break

        print(nickname, " has disconnected")



if __name__ == "__main__":
    hostname, port = "localhost", 9999

    chat_server = serv(hostname, port)
