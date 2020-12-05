# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 813)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1121, 91))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.text_codigo = QtWidgets.QTextEdit(self.centralwidget)
        self.text_codigo.setGeometry(QtCore.QRect(33, 140, 1061, 271))
        self.text_codigo.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.text_codigo.setObjectName("text_codigo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 100, 721, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.text_lexico = QtWidgets.QTextEdit(self.centralwidget)
        self.text_lexico.setEnabled(True)
        self.text_lexico.setGeometry(QtCore.QRect(20, 450, 531, 261))
        self.text_lexico.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.text_lexico.setReadOnly(True)
        self.text_lexico.setObjectName("text_lexico")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 420, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 420, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.b_lexico = QtWidgets.QPushButton(self.centralwidget)
        self.b_lexico.setGeometry(QtCore.QRect(220, 720, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.b_lexico.setFont(font)
        self.b_lexico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_lexico.setStyleSheet("background-color: rgb(106, 103, 14)")
        self.b_lexico.setObjectName("b_lexico")
        self.b_sintactico = QtWidgets.QPushButton(self.centralwidget)
        self.b_sintactico.setGeometry(QtCore.QRect(800, 720, 91, 31))
        self.b_sintactico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_sintactico.setStyleSheet("background-color: rgb(106, 103, 14)")
        self.b_sintactico.setObjectName("b_sintactico")
        self.text_sintactico = QtWidgets.QTextEdit(self.centralwidget)
        self.text_sintactico.setEnabled(True)
        self.text_sintactico.setGeometry(QtCore.QRect(570, 450, 531, 261))
        self.text_sintactico.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.text_sintactico.setReadOnly(True)
        self.text_sintactico.setObjectName("text_sintactico")
        self.b_limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.b_limpiar.setGeometry(QtCore.QRect(80, 90, 41, 41))
        self.b_limpiar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_limpiar.setStyleSheet("background-color:rgb(255,255,255)")
        self.b_limpiar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_limpiar.setIcon(icon)
        self.b_limpiar.setIconSize(QtCore.QSize(30, 30))
        self.b_limpiar.setObjectName("b_limpiar")
        self.b_cargar = QtWidgets.QPushButton(self.centralwidget)
        self.b_cargar.setGeometry(QtCore.QRect(30, 90, 41, 41))
        self.b_cargar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_cargar.setStyleSheet("background-color:rgb(255,255,255)")
        self.b_cargar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/cargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_cargar.setIcon(icon1)
        self.b_cargar.setIconSize(QtCore.QSize(50, 50))
        self.b_cargar.setObjectName("b_cargar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Compilador"))
        self.label.setText(_translate("MainWindow", "Compilador"))
        self.text_codigo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "CODIGO"))
        self.text_lexico.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "ANALIZADOR LEXICO"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>ANALIZADOR SINTACTICO</p></body></html>"))
        self.b_lexico.setText(_translate("MainWindow", "ANALIZAR"))
        self.b_sintactico.setText(_translate("MainWindow", "ANALIZAR"))
        self.text_sintactico.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

