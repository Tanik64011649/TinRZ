# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modifycal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Modifycal(object):
    def setupUi(self, Modifycal):
        Modifycal.setObjectName("Modifycal")
        Modifycal.resize(560, 650)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        Modifycal.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Modifycal)
        self.centralwidget.setObjectName("centralwidget")
        self.Codeishere = QtWidgets.QLabel(self.centralwidget)
        self.Codeishere.setGeometry(QtCore.QRect(160, 40, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Codeishere.setFont(font)
        self.Codeishere.setAlignment(QtCore.Qt.AlignCenter)
        self.Codeishere.setObjectName("Codeishere")
        self.CodeTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.CodeTextEdit.setGeometry(QtCore.QRect(120, 150, 311, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CodeTextEdit.setFont(font)
        self.CodeTextEdit.setObjectName("CodeTextEdit")
        Modifycal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Modifycal)
        self.statusbar.setObjectName("statusbar")
        Modifycal.setStatusBar(self.statusbar)

        self.retranslateUi(Modifycal)
        QtCore.QMetaObject.connectSlotsByName(Modifycal)

    def retranslateUi(self, Modifycal):
        _translate = QtCore.QCoreApplication.translate
        Modifycal.setWindowTitle(_translate("Modifycal", "MainWindow"))
        self.Codeishere.setText(_translate("Modifycal", "Code is here"))
        self.CodeTextEdit.setPlainText(_translate("Modifycal", "https://docs.google.com/document/d/1gVpQY6iwtiH96Na0cranlqc44Ezfstomk-aMwmbAd7Q/edit?usp=sharing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Modifycal = QtWidgets.QMainWindow()
    ui = Ui_Modifycal()
    ui.setupUi(Modifycal)
    Modifycal.show()
    sys.exit(app.exec_())
