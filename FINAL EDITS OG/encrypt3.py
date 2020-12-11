import mainChat
import logIn
from PyQt5 import QtCore, QtWidgets
from cryptography.fernet import Fernet

import sys, socket, random


format = 'utf-8'
listKey = [b'a3uo8T5xtcfRIVbWuMmkIDjAiRnFff8ZoBVOagf16xg=']
f = Fernet(listKey[0])


def encrypt(msg):
    message = msg.encode()
    encrypt_msg = f.encrypt(message)  # symmetric encryption (cannot be manipulated or read without the key going over the network)
    return encrypt_msg
def decrypt(msg):
    message = msg
    decrypt_msg = f.decrypt(message)
    return decrypt_msg

class make_client:
    def __init__(self):
        self.user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listOfMsg = []
        self.mainWindow = QtWidgets.QMainWindow()
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget.setHidden(True)
        self.chat_ui = mainChat.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.sendMsg)
        self.logUI = logIn.Ui_Form()
        self.logUI.setupUi(self.connectWidget)
        self.logUI.pushButton.clicked.connect(self.connectFromUI)
        self.mainWindow.setGeometry(QtCore.QRect(1080, 20, 350, 500))
        self.mainWindow.show()

    def connectToServer(self, userIP, portNum, userName):
        try:
            self.user.connect((userIP, portNum))
            self.user.send(userName.encode())
            print("--Connected--")
            return True
        except Exception as cant_connect:
            print(cant_connect)
    def sendMsg(self):
        message = self.chat_ui.textEdit.toPlainText()
        print("You:- " + message)
        msg_en = encrypt(message)
        self.chat_ui.textBrowser.append("You:- " + message)
        try:
            self.user.send(msg_en)
        except Exception as cant_send:
            print(cant_send)
        self.chat_ui.textEdit.clear()

    def connectFromUI(self):
        portNum = self.logUI.portTextEdit.toPlainText()
        userName = self.logUI.nameTextEdit.toPlainText()
        userIP = self.logUI.hostTextEdit.toPlainText()
        userName = userName + str(random.randint(1, 9999))
        if len(userIP) == 0:
            userIP = socket.gethostbyname(socket.gethostname())
        if len(portNum) == 0:
            portNum = 9999
        else:
            portNum = int(portNum)
        if self.connectToServer(userIP, portNum, userName):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)
            self.recv_thread = Thread(self.user)
            self.recv_thread.sig.connect(self.msg_display)
            self.recv_thread.start()
            print("--Thread started--")

    def msg_display(self, msg):
        self.chat_ui.textBrowser.append(msg)


class Thread(QtCore.QThread):
    sig = QtCore.pyqtSignal(str)
    def __init__(self, sock):
        super(Thread, self).__init__()
        self.socket = sock

    def receive_msg(self):
        message = self.socket.recv(2048)
        m1 = message.decode()
        decrpyt_mg = decrypt(m1)
        print(decrpyt_mg)
        self.sig.emit(decrpyt_mg)

    def run(self):
        while True:
            self.receive_msg()



app = QtWidgets.QApplication(sys.argv)
cli = make_client()
app.exec()