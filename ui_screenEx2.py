# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenEx2.ui'
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
        self.label.setGeometry(QRect(1600, 10, 241, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 129, 139);\n"
"font: 20px \"MS Shell Dlg 2\" center\n"
"")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1850, 10, 41, 31))
        self.label_5.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_5.setPixmap(QPixmap(u"icons/table.png"))
        self.label_5.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 1951, 51))
        self.label_2.setStyleSheet(u"background-color: rgb(18, 129, 139)")
        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(120, 10, 93, 28))
        self.label_2.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.back.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u062c\u062f\u0648\u0644 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646\u0627\u062a", None))
        self.label_5.setText("")
        self.label_2.setText("")
        self.back.setText(QCoreApplication.translate("Form", u"\u0631\u062c\u0648\u0639", None))
    # retranslateUi

