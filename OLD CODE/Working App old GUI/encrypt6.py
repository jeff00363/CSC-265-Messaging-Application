from PyQt5 import QtCore, QtWidgets
import mainChat
import logIn
from cryptography.fernet import Fernet
import sys, socket

format = 'utf-8'

listKey = [b'a3uo8T5xtcfRIVbWuMmkIDjAiRnFff8ZoBVOagf16xg=']
f = Fernet(listKey[0])


def encrypt(msg):
    eCr = f.encrypt(msg)
    return eCr


def decrypt(msg):
    dCr = f.decrypt(msg)
    decoded = dCr.decode(format)
    return decoded


class makeClient(object):
    def __init__(self):
        self.messages = []
        self.mainChat = QtWidgets.QMainWindow()
        self.connUi = QtWidgets.QWidget(self.mainChat)
        self.connChatUi = QtWidgets.QWidget(self.mainChat)
        self.connChatUi.setHidden(True)
        self.chatGfx = mainChat.Ui_Form()
        self.chatGfx.setupUi(self.connChatUi)
        self.chatGfx.pushButton.clicked.connect(self.sendMsg)
        self.FromUIConn = logIn.Ui_Form()
        self.FromUIConn.setupUi(self.connUi)
        self.FromUIConn.pushButton.clicked.connect(self.connectUI)
        self.mainChat.setGeometry(QtCore.QRect(1080, 20, 350, 500))
        self.mainChat.show()
        self.chatUser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connToServ(self, userIP, portNum, userName):
        try:
            self.chatUser.connect((userIP, portNum))
            self.chatUser.send(userName.encode(format))
            print("--Connected to server--")
            return True
        except Exception as cant_connect:
            print('Unable to connect to server %s' % cant_connect)
            self.FromUIConn.hostTextEdit.clear()
            self.FromUIConn.portTextEdit.clear()
            return False

    def sendMsg(self):
        nickname = self.FromUIConn.nameTextEdit.toPlainText()
        msgUser = (str(nickname) + ": " + (str(self.chatGfx.textEdit.toPlainText())))
        encodedMsg = msgUser.encode(format)
        encryptedMsg = encrypt(encodedMsg)
        self.chatGfx.textBrowser.append(msgUser)
        try:
            self.chatUser.send(encryptedMsg)
        except Exception as unable_send:
            print('Unable to send msgDisplay %s' % unable_send)
        self.chatGfx.textEdit.clear()

    def msgDisplay(self, msg):
        self.chatGfx.textBrowser.append(msg)
    def connectUI(self):
        userIP = socket.gethostbyname(socket.gethostname())
        PORT = 9997
        userName = self.FromUIConn.nameTextEdit.toPlainText()

        if len(userName) < 1:
            userName = str(userIP)
        if self.connToServ(userIP, PORT, userName):
            self.connUi.setHidden(True)
            self.connChatUi.setVisible(True)
            self.recv = Thread(self.chatUser)
            self.recv.sig.connect(self.msgDisplay)
            self.recv.start()
            print("--Thread started--")


class Thread(QtCore.QThread):
    sig = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(Thread, self).__init__()
        self.socket = client_socket

    def run(self):
        while True:
            self.recMsg()

    def recMsg(self):
        msg = self.socket.recv(2048)
        deCr = decrypt(msg)
        self.sig.emit(deCr)


app = QtWidgets.QApplication(sys.argv)
chatApp = makeClient()
app.exec()
