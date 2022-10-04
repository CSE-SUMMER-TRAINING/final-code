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
        self.save = QPushButton(Form)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(860, 910, 171, 41))
        self.save.setStyleSheet(u"background-color: rgb(18, 129, 139);font-size:20px;color:white;")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(350, 250, 1271, 601))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1850, 10, 41, 31))
        self.label_5.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_5.setPixmap(QPixmap(u"../../../Downloads/table.png"))
        self.label_5.setScaledContents(True)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(840, 100, 241, 41))
        self.textBrowser.setStyleSheet(u"background-color: transparent;\n"
"text-align:center;\n"
"border: none;\n"
"font-size: 10px;\n"
"color:#8D8D8D;\n"
"font-weight:lighter;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 1951, 51))
        self.label_2.setStyleSheet(u"background-color: rgb(18, 129, 139)")
        self.comboBoxx1_2 = QComboBox(Form)
        self.comboBoxx1_2.addItem("")
        self.comboBoxx1_2.setObjectName(u"comboBoxx1_2")
        self.comboBoxx1_2.setGeometry(QRect(810, 150, 251, 31))
        self.label_2.raise_()
        self.label.raise_()
        self.save.raise_()
        self.tableWidget.raise_()
        self.label_5.raise_()
        self.textBrowser.raise_()
        self.comboBoxx1_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u062c\u062f\u0648\u0644 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646\u0627\u062a", None))
        self.save.setText(QCoreApplication.translate("Form", u"\u062a\u062d\u0645\u064a\u0644", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u0625\u0644\u0649", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0645\u0646", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0627\u0633\u0645 \u0627\u0644\u062f\u0641\u0639\u0629", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0625\u0644\u0649", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0645\u0646", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0627\u0633\u0645 \u0627\u0644\u062f\u0641\u0639\u0629", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u0625\u0644\u0649", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u0645\u0646", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u0627\u0633\u0645 \u0627\u0644\u062f\u0641\u0639\u0629", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u0627\u0633\u0645 \u0627\u0644\u0642\u0627\u0639\u0629", None));
        self.label_5.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">choose one option </span></p></body></html>", None))
        self.label_2.setText("")
        self.comboBoxx1_2.setItemText(0, QCoreApplication.translate("Form", u"choose", None))

    # retranslateUi

