from PyQt5 import QtCore, QtWidgets
import mainChat
import logIn
from cryptography.fernet import Fernet
import sys, socket

format = 'utf-8'

listKey = [b'a3uo8T5xtcfRIVbWuMmkIDjAiRnFff8ZoBVOagf16xg=']
f = Fernet(listKey[0])

userIP = socket.gethostbyname(socket.gethostname())
PORT = 9997

def encrypt(msg):
    eCr = f.encrypt(msg)
    return eCr

def decrypt(msg):
    dCr = f.decrypt(msg)
    decoded = dCr.decode(format)
    return decoded


class makeClient(object):
    def __init__(self):
        self.chatUser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msg = []
        self.mainChat = QtWidgets.QMainWindow()
        self.connUi = QtWidgets.QWidget(self.mainChat)
        self.connChatUi = QtWidgets.QWidget(self.mainChat)
        self.connChatUi.setHidden(True)
        self.chatGfx = mainChat.Ui_Form()
        self.chatGfx.setupUi(self.connChatUi)
        self.chatGfx.userMsgInput.clicked.connect(self.sendMsg)
        self.FromUIConn = logIn.Ui_Form()
        self.FromUIConn.setupUi(self.connUi)
        self.FromUIConn.userNameInput.clicked.connect(self.handshake)
        self.mainChat.setGeometry(QtCore.QRect(1000, 550, 650, 500))
        self.mainChat.show()

    def msgDisplay(self, msg):
        self.chatGfx.textWindow.append(msg)

    def connToServ(self, userName):
        self.chatUser.connect((userIP, PORT))
        self.chatUser.send(userName.encode(format))
        print("--Connected to server--")

    def sendMsg(self):
        nickname = self.FromUIConn.nameTextEdit.toPlainText()
        msgUser = (str(nickname) + ":-" + (str(self.chatGfx.userTxt.toPlainText())))
        encodedMsg = msgUser.encode(format)
        encryptedMsg = encrypt(encodedMsg)
        self.msgDisplay(msgUser)
        self.chatUser.send(encryptedMsg)
        self.chatGfx.userTxt.clear()

    def handshake(self):
        userName = self.FromUIConn.nameTextEdit.toPlainText()
        self.connToServ(userName)
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


chat = QtWidgets.QApplication(sys.argv)
chatApp = makeClient()
chat.exec()