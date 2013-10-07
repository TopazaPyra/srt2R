# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Oct  3 17:15:05 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(517, 221)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/srt2R/srt2R.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.srtFilesFolderLabel = QtGui.QLabel(self.centralwidget)
        self.srtFilesFolderLabel.setGeometry(QtCore.QRect(40, 50, 81, 16))
        self.srtFilesFolderLabel.setObjectName(_fromUtf8("srtFilesFolderLabel"))
        self.folderLabel = QtGui.QLabel(self.centralwidget)
        self.folderLabel.setGeometry(QtCore.QRect(40, 100, 171, 16))
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.convertButton = QtGui.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(360, 150, 101, 31))
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.srtFilesFolderEdit = QtGui.QLineEdit(self.centralwidget)
        self.srtFilesFolderEdit.setGeometry(QtCore.QRect(120, 45, 311, 24))
        self.srtFilesFolderEdit.setObjectName(_fromUtf8("srtFilesFolderEdit"))
        self.folderEdit = QtGui.QLineEdit(self.centralwidget)
        self.folderEdit.setGeometry(QtCore.QRect(220, 95, 211, 24))
        self.folderEdit.setObjectName(_fromUtf8("folderEdit"))
        self.srtFilesFolderButton = QtGui.QToolButton(self.centralwidget)
        self.srtFilesFolderButton.setGeometry(QtCore.QRect(440, 45, 26, 22))
        self.srtFilesFolderButton.setObjectName(_fromUtf8("srtFilesFolderButton"))
        self.folderButton = QtGui.QToolButton(self.centralwidget)
        self.folderButton.setGeometry(QtCore.QRect(440, 95, 26, 22))
        self.folderButton.setObjectName(_fromUtf8("folderButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.action_propos = QtGui.QAction(MainWindow)
        self.action_propos.setObjectName(_fromUtf8("action_propos"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Convertisseur srt vers R", None))
        self.srtFilesFolderLabel.setText(_translate("MainWindow", "Fichiers srt :", None))
        self.folderLabel.setText(_translate("MainWindow", "Répertoire de destination :", None))
        self.convertButton.setText(_translate("MainWindow", "Convertir", None))
        self.srtFilesFolderButton.setText(_translate("MainWindow", "...", None))
        self.folderButton.setText(_translate("MainWindow", "...", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))
        self.action_propos.setText(_translate("MainWindow", "À propos", None))

