# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Ahmed\Downloads\final-code-main (3)\final-code-main\final-code\helpEx.ui'
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
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(640, 220, 791, 51))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
"text-align:center;\n"
"border: none;\n"
"font-size: 10px;\n"
"color:#6c838f;\n"
"font-weight:lighter;")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1590, 10, 241, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20px \"MS Shell Dlg 2\" center\n"
"")
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(1840, 10, 41, 31))
        self.label_9.setStyleSheet("background-color: transparent;\n"
"")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("c:\\Users\\Ahmed\\Downloads\\final-code-main (3)\\final-code-main\\final-code\\../../../Downloads/table.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(-330, 0, 2251, 51))
        self.label_8.setStyleSheet("background-color:#274857")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(850, 800, 161, 41))
        self.back.setStyleSheet("background-color: #3caac3;\n"
"font-size:19px;color:white;")
        self.back.setObjectName("back")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 390, 1691, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\Ahmed\\Downloads\\final-code-main (3)\\final-code-main\\final-code\\icons/examtable.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(850, 740, 161, 41))
        self.save.setStyleSheet("background-color: #3caac3;\n"
"font-size:19px;color:white;")
        self.save.setObjectName("save")
        self.label_8.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.label_9.raise_()
        self.back.raise_()
        self.label_2.raise_()
        self.save.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:19pt;\"> برجاء اختيار ملف به بيانات مشابهه لهذا الملف</span></p></body></html>"))
        self.label.setText(_translate("Form", "مساعدة"))
        self.back.setText(_translate("Form", "رجوع"))
        self.save.setText(_translate("Form", "حفظ نسخة"))
