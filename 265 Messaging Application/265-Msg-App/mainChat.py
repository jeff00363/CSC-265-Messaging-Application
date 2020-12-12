# MADE WITH PY QT DESIGNER, GFX CLIENT DRAG AND DROP


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, userChat):
        userChat.setObjectName("userInput")
        userChat.resize(648, 504)
        self.userMsgInput = QtWidgets.QPushButton(userChat)
        self.userMsgInput.setGeometry(QtCore.QRect(530, 390, 101, 71))
        self.userMsgInput.setObjectName("userNameInput")
        self.userTxt = QtWidgets.QTextEdit(userChat)
        self.userTxt.setGeometry(QtCore.QRect(10, 390, 501, 71))
        self.userTxt.setObjectName("userTxt")
        self.textWindow = QtWidgets.QTextBrowser(userChat)
        self.textWindow.setGeometry(QtCore.QRect(9, 10, 631, 361))
        self.textWindow.setObjectName("textWindow")
        self.retranslateUi(userChat)
        QtCore.QMetaObject.connectSlotsByName(userChat)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("userInput", "userInput"))
        self.userMsgInput.setText(_translate("userInput", "Send Msg"))
