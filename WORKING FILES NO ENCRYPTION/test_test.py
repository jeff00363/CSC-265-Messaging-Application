from PyQt5 import QtCore, QtWidgets
import client_ui
import connect_ui

import sys, socket, random

format = 'utf-8'


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
        message = message.decode(format)
        print(message)
        self.sig.emit(message)
class Client(object):
    def __init__(self):
        self.messages = []
        self.mainWindow = QtWidgets.QMainWindow()
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget.setHidden(True)
        self.chat_ui = client_ui.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.send_msg)
        self.connect_ui = connect_ui.Ui_Form()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.connect_butt)
        self.mainWindow.setGeometry(QtCore.QRect(1080, 20, 350, 500))
        self.mainWindow.show()
        self.user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_butt(self):
        host = self.connect_ui.hostTextEdit.toPlainText()
        port = self.connect_ui.portTextEdit.toPlainText()
        nickname = self.connect_ui.nameTextEdit.toPlainText()
        if len(host) == 0:
            host = socket.gethostbyname(socket.gethostname())
        if len(port) == 0:
            port = 9999
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
        self.chat_ui.textBrowser.append(msg)

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
        self.chat_ui.textBrowser.append("You:- " + message)
        print("You:- " + message)
        try:
            self.user.send(message.encode(format))
        except Exception as unable_send:
            print('Unable to send msg_display %s' % unable_send)
        self.chat_ui.textEdit.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    app.exec()