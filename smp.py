# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Project\English words\sample.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 398)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(200, 100, 251, 61))
        self.textLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textLabel.setObjectName("textLabel")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(390, 300, 71, 71))
        self.commandLinkButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/playy/Downloads/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(210, 300, 61, 71))
        self.commandLinkButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/playy/Downloads/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(300, 300, 61, 71))
        self.commandLinkButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/playy/Downloads/repeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon2)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "English Words"))
#         self.textLabel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"

# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">{CardName}</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
