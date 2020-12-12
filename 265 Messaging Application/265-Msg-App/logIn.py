# MADE WITH PY QT DESIGNER, GFX CLIENT DRAG AND DROP

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, userInput):
        userInput.setObjectName("userInput")
        userInput.resize(734, 196)
        self.nameTextEdit = QtWidgets.QPlainTextEdit(userInput)
        self.nameTextEdit.setGeometry(QtCore.QRect(290, 50, 171, 61))
        self.nameTextEdit.setPlainText("")
        self.nameTextEdit.setObjectName("nameTextEdit")
        self.labelUserName = QtWidgets.QLabel(userInput)
        self.labelUserName.setGeometry(QtCore.QRect(30, 50, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labelUserName.setFont(font)
        self.labelUserName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelUserName.setObjectName("labelUserName")
        self.userNameInput = QtWidgets.QPushButton(userInput)
        self.userNameInput.setGeometry(QtCore.QRect(480, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.userNameInput.setFont(font)
        self.userNameInput.setObjectName("userNameInput")
        self.retranslateUi(userInput)
        QtCore.QMetaObject.connectSlotsByName(userInput)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("userInput", "userInput"))
        self.labelUserName.setText(_translate("userInput", "User Name :"))
        self.userNameInput.setText(_translate("userInput", "Start Chat"))
