# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Ahmed\Downloads\final-code-main (3)\final-code-main\final-code\screen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setMinimumSize(QtCore.QSize(1920, 1080))
        Form.setMaximumSize(QtCore.QSize(1920, 1080))
        self.inv = QtWidgets.QPushButton(Form)
        self.inv.setGeometry(QtCore.QRect(980, 410, 291, 251))
        self.inv.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: \n"
"#8abbca;\n"
"color:white;")
        self.inv.setText("")
        self.inv.setIconSize(QtCore.QSize(30, 30))
        self.inv.setObjectName("inv")
        self.exam = QtWidgets.QPushButton(Form)
        self.exam.setGeometry(QtCore.QRect(660, 410, 291, 251))
        self.exam.setStyleSheet("font: 17pt \"MS Shell Dlg 2\";\n"
"background-color: #3caac3;\n"
"color:white;")
        self.exam.setText("")
        self.exam.setIconSize(QtCore.QSize(30, 30))
        self.exam.setObjectName("exam")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 1931, 81))
        self.label_2.setStyleSheet("background-color: #274857")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(790, 20, 51, 51))
        self.label_6.setStyleSheet("background-color: transparent;\n"
"")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("c:\\Users\\Ahmed\\Downloads\\final-code-main (3)\\final-code-main\\final-code\\icons/table.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(740, 290, 471, 61))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
"text-align:center;\n"
"border: none;\n"
"font-size: 20px;\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"color:#8D8D8D;\n"
"font-weight:lighter;")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(850, 20, 301, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 30px \"MS Shell Dlg 2\" center\n"
"")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(760, 470, 81, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\Ahmed\\Downloads\\final-code-main (3)\\final-code-main\\final-code\\icons/exam (2).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(720, 560, 171, 31))
        self.label_4.setStyleSheet("color: white;\n"
"font-size:25px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(1080, 470, 81, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("c:\\Users\\Ahmed\\Downloads\\final-code-main (3)\\final-code-main\\final-code\\icons/exam (1).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(1040, 560, 171, 31))
        self.label_7.setStyleSheet("color: white;\n"
"font-size:25px;\n"
"")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">اختر نوع الجدول الذي تريد انشاءه</span></p></body></html>"))
        self.label.setText(_translate("Form", "Timetable generator"))
        self.label_4.setText(_translate("Form", "جدول الامتحانات"))
        self.label_7.setText(_translate("Form", "جدول الملاحظين"))
