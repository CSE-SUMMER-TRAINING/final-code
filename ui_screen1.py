# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen1.ui'
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
        self.inv = QPushButton(Form)
        self.inv.setObjectName(u"inv")
        self.inv.setGeometry(QRect(980, 410, 291, 251))
        self.inv.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: \n"
"#8abbca;\n"
"color:white;")
        self.inv.setIconSize(QSize(30, 30))
        self.exam = QPushButton(Form)
        self.exam.setObjectName(u"exam")
        self.exam.setGeometry(QRect(660, 410, 291, 251))
        self.exam.setStyleSheet(u"font: 17pt \"MS Shell Dlg 2\";\n"
"background-color: #3caac3;\n"
"color:white;")
        self.exam.setIconSize(QSize(30, 30))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, 0, 1931, 81))
        self.label_2.setStyleSheet(u"background-color: #274857")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(790, 20, 51, 51))
        self.label_6.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_6.setPixmap(QPixmap(u"icons/table.png"))
        self.label_6.setScaledContents(True)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(740, 290, 471, 61))
        self.textBrowser.setStyleSheet(u"background-color: transparent;\n"
"text-align:center;\n"
"border: none;\n"
"font-size: 20px;\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"color:#8D8D8D;\n"
"font-weight:lighter;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(850, 20, 301, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 30px \"MS Shell Dlg 2\" center\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(760, 470, 81, 81))
        self.label_3.setPixmap(QPixmap(u"icons/exam (2).png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(720, 560, 171, 31))
        self.label_4.setStyleSheet(u"color: white;\n"
"font-size:25px;\n"
"")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1080, 470, 81, 81))
        self.label_5.setPixmap(QPixmap(u"icons/exam (1).png"))
        self.label_5.setScaledContents(True)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1040, 560, 171, 31))
        self.label_7.setStyleSheet(u"color: white;\n"
"font-size:25px;\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.inv.setText("")
        self.exam.setText("")
        self.label_2.setText("")
        self.label_6.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">\u0627\u062e\u062a\u0631 \u0646\u0648\u0639 \u0627\u0644\u062c\u062f\u0648\u0644 \u0627\u0644\u0630\u064a \u062a\u0631\u064a\u062f \u0627\u0646\u0634\u0627\u0621\u0647</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Timetable generator", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u062c\u062f\u0648\u0644 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646\u0627\u062a", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u062c\u062f\u0648\u0644 \u0627\u0644\u0645\u0644\u0627\u062d\u0638\u064a\u0646", None))
    # retranslateUi

