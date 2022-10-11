# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenInv1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setMinimumSize(QSize(1920, 1080))
        Form.setMaximumSize(QSize(1920, 1080))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1500, 20, 301, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 129, 139);\n"
"font: 30px \"MS Shell Dlg 2\" center\n"
"")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1830, 20, 51, 51))
        self.label_8.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_8.setPixmap(QPixmap(u"icons/table.png"))
        self.label_8.setScaledContents(True)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-30, 0, 1951, 81))
        self.label_7.setStyleSheet(u"background-color: rgb(18, 129, 139)")
        self.label_not_enough = QLabel(Form)
        self.label_not_enough.setObjectName(u"label_not_enough")
        self.label_not_enough.setGeometry(QRect(790, 320, 400, 50))
        self.label_not_enough.setLayoutDirection(Qt.LeftToRight)
        self.label_not_enough.setStyleSheet(u"color:red;font-size:18px")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(820, 560, 231, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(880, 250, 301, 51))
        self.textBrowser.setStyleSheet(u"background-color: transparent;\n"
"text-align:center;\n"
"border: none;\n"
"font-size: 10px;\n"
"color:#8D8D8D;\n"
"font-weight:lighter;")
        self.help = QPushButton(Form)
        self.help.setObjectName(u"help")
        self.help.setGeometry(QRect(940, 730, 101, 31))
        self.help.setCursor(QCursor(Qt.PointingHandCursor))
        self.help.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"color:#2D2D2D;")
        self.help.setIconSize(QSize(30, 30))
        self.browse = QPushButton(Form)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(1070, 560, 101, 31))
        self.browse.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"color:#2D2D2D;")
        self.browse.setIconSize(QSize(30, 30))
        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(850, 640, 131, 41))
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(18, 129, 139);font: 10pt \"MS Shell Dlg 2\";color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(23, 167, 181);\n"
"font-size:11pt;\n"
"}")
        self.back.setIconSize(QSize(30, 30))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(890, 340, 201, 211))
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_4.setPixmap(QPixmap(u"icons/open-folder.png"))
        self.label_4.setScaledContents(True)
        self.generate = QPushButton(Form)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(1000, 640, 131, 41))
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(18, 129, 139);font: 10pt \"MS Shell Dlg 2\";color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(23, 167, 181);\n"
"font-size:11pt;\n"
"}")
        self.generate.setIconSize(QSize(30, 30))
        self.label_7.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.label_not_enough.raise_()
        self.lineEdit.raise_()
        self.textBrowser.raise_()
        self.help.raise_()
        self.browse.raise_()
        self.back.raise_()
        self.label_4.raise_()
        self.generate.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u062c\u062f\u0648\u0644 \u0627\u0644\u0645\u0644\u0627\u062d\u0638\u064a\u0646", None))
        self.label_8.setText("")
        self.label_7.setText("")
        self.label_not_enough.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:19pt;\">Excel \u0627\u062e\u062a\u0627\u0631 \u0645\u0644\u0641</span></p></body></html>", None))
        self.help.setText(QCoreApplication.translate("Form", u"\u0645\u0633\u0627\u0639\u062f\u0629", None))
        self.browse.setText(QCoreApplication.translate("Form", u"\u0627\u062e\u062a\u0627\u0631", None))
        self.back.setText(QCoreApplication.translate("Form", u"\u0631\u062c\u0648\u0639", None))
        self.label_4.setText("")
        self.generate.setText(QCoreApplication.translate("Form", u"\u0627\u0643\u0645\u0644", None))
    # retranslateUi

