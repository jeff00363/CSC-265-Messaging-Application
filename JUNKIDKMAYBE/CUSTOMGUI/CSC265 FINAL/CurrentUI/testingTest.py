from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from CurrentUI import chatapp
from CurrentUI import inappdialog
from cryptography.fernet import Fernet
import sys

import sys, socket, random

format = 'utf-8'

listKey = [b'a3uo8T5xtcfRIVbWuMmkIDjAiRnFff8ZoBVOagf16xg=']

def encrypt(msg):
    message = msg.encode()
    f = Fernet(listKey[0])
    encrypt_msg = f.encrypt(message)
    return encrypt_msg

def decrpyt(msg):
    message = msg
    f = Fernet(listKey[0])
    decrpyt_msg = f.decrypt(encrypt(message))
    return decrpyt_msg


class ReceiveThread(QtCore.QThread):
    sig = QtCore.pyqtSignal(str)
    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.socket = client_socket
    def run(self):
        while True:
            self.receive_msg()
    def receive_msg(self):
        message = self.socket.recv(2048)
        m1 = message.decode()
        decrpyt_mg = decrpyt(m1)
        print(decrpyt_mg)
        self.sig.emit(decrpyt_mg)

class Client(object):
    def __init__(self):
        self.messages = []
        self.ChatWindow = QtWidgets.QMainWindow()
        self.connectWidget = QtWidgets.QWidget(self.ChatWindow)
        self.chatWidget = QtWidgets.QWidget(self.ChatWindow)
        self.chatWidget.setHidden(True)
        self.chat_ui = inappdialog.Ui_ChatWindow()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.send_msg)
        self.connect_ui = chatapp.Ui_MainWindow()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.connect_butt)
        self.ChatWindow.setGeometry(QtCore.QRect(1080, 20, 350, 500))
        self.ChatWindow.show()
        self.user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_butt(self):
        host = self.connect_ui.hostTextEdit.toPlainText()
        port = self.connect_ui.portTextEdit.toPlainText()
        nickname = self.connect_ui.nameTextEdit.toPlainText()
        if len(host) == 0:
            host = socket.gethostbyname(socket.gethostname())
        if len(port) == 0:
            port = 9998
        else:
            try:
                port = int(port)
            except Exception as invalid:
                print('Invalid portNum number %s' % invalid)
        if len(nickname) < 1:
            nickname = socket.gethostname()
        nickname = nickname + "#" + str(random.randint(1, 10))
        if self.connect(host, port, nickname):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)
            self.recv_thread = ReceiveThread(self.user)
            self.recv_thread.sig.connect(self.msg_display)
            self.recv_thread.start()
            print("--Thread started--")

    def msg_display(self, msg):
        self.chat_ui.RecievedMessages.append(msg)

    def connect(self, userIP, portNum, userName):
        try:
            self.user.connect((userIP, portNum))
            self.user.send(userName.encode(format))
            print("--Connected to server--")
            return True
        except Exception as cant_connect:
            print('Unable to connect to server %s' % cant_connect)
            self.connect_ui.hostTextEdit.clear()
            self.connect_ui.portTextEdit.clear()
            return False

    def send_msg(self):
        message = self.chat_ui.textEdit.toPlainText()
        msg_en = encrypt(message).decode()
        self.chat_ui.SentMessages.append("You:- " + message)
        print("You:- " + message)
        try:
            self.user.send(msg_en.encode(format))
        except Exception as unable_send:
            print('Unable to send msg_display %s' % unable_send)
        self.chat_ui.textEdit.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    app.exec()

