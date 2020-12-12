from PyQt5 import QtCore, QtWidgets
import mainChat
import logIn
from cryptography.fernet import Fernet
import sys, socket

format = 'utf-8'

listKey = [b'a3uo8T5xtcfRIVbWuMmkIDjAiRnFff8ZoBVOagf16xg='] # encrypt key
f = Fernet(listKey[0]) # fernet object

userIP = socket.gethostbyname(socket.gethostname())
PORT = 9997

# encrypt and decrypt func
def encrypt(msg):
    eCr = f.encrypt(msg)
    return eCr

def decrypt(msg):
    dCr = f.decrypt(msg)
    decoded = dCr.decode(format)
    return decoded


# making client and connecting to the socket also setting up the GUI fields
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
        self.FromUIConn.userNameInput.clicked.connect(self.fromServ)
        self.mainChat.setGeometry(QtCore.QRect(1000, 550, 650, 500))
        self.mainChat.show()

# msg is sent to the GUI to show on the client side
    def msgDisplay(self, msg):
        self.chatGfx.textWindow.append(msg)

# connection with server through userIP and PORT and sending the userName to server form initial sending and adding
    # name to list of clients connected with the server
    def connToServ(self, userName):
        self.chatUser.connect((userIP, PORT))
        self.chatUser.send(userName.encode(format))
        print("--Connected to server--")

# sending an encrypted message
    def sendMsg(self):
        nickname = self.FromUIConn.nameTextEdit.toPlainText()
        msgUser = (str(nickname) + ":-" + (str(self.chatGfx.userTxt.toPlainText())))
        encodedMsg = msgUser.encode(format)
        encryptedMsg = encrypt(encodedMsg)
        self.msgDisplay(msgUser)
        self.chatUser.send(encryptedMsg)
        self.chatGfx.userTxt.clear()

# recv the msg from serv through the Thread that gets the message from the server and display it on the UI
    def fromServ(self):
        userName = self.FromUIConn.nameTextEdit.toPlainText()
        self.connToServ(userName)
        self.connUi.setHidden(True)
        self.connChatUi.setVisible(True)
        self.recv = Thread(self.chatUser)
        self.recv.sig.connect(self.msgDisplay)
        self.recv.start()
        print("--Thread started--")

# using the function of threading and QTcore. the thread recvs the msg and sends it to the UI and we decrypt it before it sends it anywhere
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


# Chatapp is made and started and userCleint is init and started

chat = QtWidgets.QApplication(sys.argv)
chatApp = makeClient()
chat.exec()