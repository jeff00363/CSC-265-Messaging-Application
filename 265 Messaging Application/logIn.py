from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, userEnter):
        userEnter.setObjectName("userEnter")
        userEnter.resize(324, 336)
        self.hostTextEdit = QtWidgets.QPlainTextEdit(userEnter)
        self.hostTextEdit.setGeometry(QtCore.QRect(160, 40, 145, 30))
        self.hostTextEdit.setObjectName("hostTextEdit")
        self.portTextEdit = QtWidgets.QPlainTextEdit(userEnter)
        self.portTextEdit.setGeometry(QtCore.QRect(160, 80, 145, 31))
        self.portTextEdit.setObjectName("portTextEdit")
        self.nameTextEdit = QtWidgets.QPlainTextEdit(userEnter)
        self.nameTextEdit.setGeometry(QtCore.QRect(160, 120, 145, 31))
        self.nameTextEdit.setObjectName("nameTextEdit")
        self.label = QtWidgets.QLabel(userEnter)
        self.label.setGeometry(QtCore.QRect(40, 40, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(userEnter)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(userEnter)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(userEnter)
        self.pushButton.setGeometry(QtCore.QRect(125, 170, 90, 30))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(userEnter)
        QtCore.QMetaObject.connectSlotsByName(userEnter)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("userEnter", "userEnter"))
        self.label.setText(_translate("userEnter", "Hostname"))
        self.label_2.setText(_translate("userEnter", "Port"))
        self.label_3.setText(_translate("userEnter", "Name"))
        self.pushButton.setText(_translate("userEnter", "Connect"))