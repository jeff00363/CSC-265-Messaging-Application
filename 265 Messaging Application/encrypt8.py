from PyQt5 import QtCore, QtWidgets
import mainChat
import logIn
from cryptography.fernet import Fernet
import sys, socket, random

listKey = [b'a3uo8T5xtcfRIVbWuMmkIDjAiRnFff8ZoBVOagf16xg=']
f = Fernet(listKey[0])

format = 'utf-8'


def encrypt(msg):
    eCr = f.encrypt(msg)
    print(eCr)
    return eCr


def decrypt(msg):
    dCr = f.decrypt(msg)
    decoded = dCr.decode()
    print(dCr)
    return decoded


class Thread(QtCore.QThread):
    sig = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(Thread, self).__init__()
        self.socket = client_socket

    def run(self):
        while True:
            self.recMsg()

    def recMsg(self):
        message = self.socket.recv(2048)
        deCr = decrypt(message)
        print(deCr)
        self.sig.emit(deCr)


class Client(object):
    def __init__(self):
        self.messages = []
        self.mainWindow = QtWidgets.QMainWindow()
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget.setHidden(True)
        self.chat_ui = mainChat.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.sendMsg)
        self.connect_ui = logIn.Ui_Form()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.connectUI)
        self.mainWindow.setGeometry(QtCore.QRect(1080, 20, 350, 500))
        self.mainWindow.show()
        self.user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectUI(self):
        userIP = self.connect_ui.hostTextEdit.toPlainText()
        PORT = self.connect_ui.portTextEdit.toPlainText()
        userName = self.connect_ui.nameTextEdit.toPlainText()
        if len(userIP) == 0:
            userIP = socket.gethostbyname(socket.gethostname())
        if len(PORT) == 0:
            PORT = 9997
        else:
            try:
                PORT = int(PORT)
            except Exception as invalid:
                print('Invalid portNum number %s' % invalid)
        if len(userName) < 1:
            userName = socket.gethostname()
        if self.connect(userIP, PORT, userName):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)
            self.recv = Thread(self.user)
            self.recv.sig.connect(self.msgDisplay)
            self.recv.start()
            print("--Thread started--")

    def msgDisplay(self, msg):
        self.chat_ui.textBrowser.append(msg)

    def connect(self, userIP, portNum, userName):
        try:
            self.user.connect((userIP, portNum))
            self.user.send(userName.encode())
            print("--Connected to server--")
            return True
        except Exception as cant_connect:
            print('Unable to connect to server %s' % cant_connect)
            self.connect_ui.hostTextEdit.clear()
            self.connect_ui.portTextEdit.clear()
            return False

    def sendMsg(self):
        nickname = self.connect_ui.nameTextEdit.toPlainText()
        message = (str(nickname) + ": " + (str(self.chat_ui.textEdit.toPlainText())))
        encodedMsg = message.encode()
        encryptedMsg = encrypt(encodedMsg)
        self.chat_ui.textBrowser.append(message)
        print(message)
        try:
            self.user.send(encryptedMsg)
            # self.user.send(message.encode(format))
        except Exception as unable_send:
            print('Unable to send msgDisplay %s' % unable_send)
        self.chat_ui.textEdit.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    app.exec()