from PyQt5 import QtCore, QtWidgets
import inappdialog
import chatapp

import sys
import socket
import random


class RecThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(RecThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_msg()

    def receive_msg(self):
        msg = self.client_socket.recv(2048)
        msg = msg.decode()

        print(msg)
        self.signal.emit(msg)


class client(object):
    def __init__(self):
        self.messages = []
        self.mainWindow = QtWidgets.QMainWindow()

        # add widgets to the application window
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)

        self.chatWidget.setHidden(True)
        self.chat_ui = inappdialog.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.send_msg)

        self.connect_ui = chatapp.Ui_Form()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.client_conn_login)

        self.mainWindow.setGeometry(QtCore.QRect(1080, 20, 350, 500))
        self.mainWindow.show()

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def client_conn_login(self):
        host = self.connect_ui.hostTextEdit.toPlainText()
        port = self.connect_ui.portTextEdit.toPlainText()
        nickname = self.connect_ui.nameTextEdit.toPlainText()

        if len(host) == 0:
            host = "localhost"

        if len(port) == 0:
            port = 5000
        else:
            try:
                host = int(host)
                port = int(port)
            except Exception as invalid:
                error = 'Invalid port number \n', str(invalid)
                print(error)
                self.show_error("Port Number Error", error)

        if len(nickname) < 1:
            nickname = socket.gethostname()

        nickname = nickname + '#' + str(random.randint(1, 9999))

    def show_msg(self, msg):
        self.chat_ui.textBrowser.append(msg)

    def connect(self, host, port, nickname):

        try:
            self.tcp_client.connect((host, port))
            self.tcp_client.send(nickname.encode())

            print("Connected to server")

            return True
        except Exception as connect_err:
            error = 'Can\'t to connect to server \n', str(connect_err)
            print(error)
            self.show_error("Connection Error", error)

            return False

    def send_msg(self):
        msg = self.chat_ui.textEdit.toPlainText()
        self.chat_ui.textBrowser.append("You : " + msg)

        print("You : " + msg)

        try:
            self.tcp_client.send(msg.encode())
        except Exception as send_msg_err:
            error = "Unable to send message", str(send_msg_err)
            print(error)
            self.show_error("server Error", error)
        self.chat_ui.textEdit.clear()

    def show_error(self, error_type, msg):
        errorDialog = QtWidgets.QMessageBox()
        errorDialog.setText(msg)
        errorDialog.setWindowTitle(error_type)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        errorDialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = client()
    sys.exit(app.exec())
