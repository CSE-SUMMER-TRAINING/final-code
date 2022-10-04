# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpEx.ui'
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
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(640, 220, 791, 51))
        self.textBrowser.setStyleSheet(u"background-color: transparent;\n"
"text-align:center;\n"
"border: none;\n"
"font-size: 10px;\n"
"color:#8D8D8D;\n"
"font-weight:lighter;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1590, 10, 241, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 129, 139);\n"
"font: 20px \"MS Shell Dlg 2\" center\n"
"")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1840, 10, 41, 31))
        self.label_9.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_9.setPixmap(QPixmap(u"../../../Downloads/table.png"))
        self.label_9.setScaledContents(True)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(-330, 0, 2251, 51))
        self.label_8.setStyleSheet(u"background-color: rgb(18, 129, 139)")
        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(850, 820, 161, 41))
        self.back.setStyleSheet(u"background-color: rgb(18, 129, 139);font-size:19px;color:white;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 430, 1691, 271))
        self.label_2.setPixmap(QPixmap(u"icons/examtable.png"))
        self.label_2.setScaledContents(True)
        self.label_8.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.label_9.raise_()
        self.back.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:19pt;\"> \u0628\u0631\u062c\u0627\u0621 \u0627\u062e\u062a\u064a\u0627\u0631 \u0645\u0644\u0641 \u0628\u0647 \u0628\u064a\u0627\u0646\u0627\u062a \u0645\u0634\u0627\u0628\u0647\u0647 \u0644\u0647\u0630\u0627 \u0627\u0644\u0645\u0644\u0641</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0645\u0633\u0627\u0639\u062f\u0629", None))
        self.label_9.setText("")
        self.label_8.setText("")
        self.back.setText(QCoreApplication.translate("Form", u"\u0631\u062c\u0648\u0639", None))
        self.label_2.setText("")
    # retranslateUi

