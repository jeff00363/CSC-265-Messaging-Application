# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessagingScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui_Form(object):
    def setupUi(self, Ui_Form):
        Ui_Form.setObjectName("Ui_Form")
        Ui_Form.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ui_Form)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 751, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 745, 427))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.SentMessages = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.SentMessages.setGeometry(QtCore.QRect(0, 8, 381, 411))
        self.SentMessages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SentMessages.setObjectName("SentMessages")
        self.RecievedMessages = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.RecievedMessages.setGeometry(QtCore.QRect(380, 10, 361, 411))
        self.RecievedMessages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RecievedMessages.setObjectName("RecievedMessages")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setItalic(True)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.send = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setObjectName("send")
        self.verticalLayout.addWidget(self.send)
        Ui_Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCurrent_Message = QtWidgets.QMenu(self.menubar)
        self.menuCurrent_Message.setObjectName("menuCurrent_Message")
        Ui_Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_Form)
        self.statusbar.setObjectName("statusbar")
        Ui_Form.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCurrent_Message.menuAction())

        self.retranslateUi(Ui_Form)
        QtCore.QMetaObject.connectSlotsByName(Ui_Form)

    def retranslateUi(self, Ui_Form):
        _translate = QtCore.QCoreApplication.translate
        Ui_Form.setWindowTitle(_translate("Ui_Form", "InChat"))
        self.textEdit.setText(_translate("Ui_Form", "ENTER YOUR MESSAGE"))
        self.send.setText(_translate("Ui_Form", "Send Message"))
        self.menuCurrent_Message.setTitle(_translate("Ui_Form", "Current Message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_Form = QtWidgets.QMainWindow()
    ui = Ui_Ui_Form()
    ui.setupUi(Ui_Form)
    Ui_Form.show()
    sys.exit(app.exec_())
