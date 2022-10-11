# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenInv2.ui'
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
        Form.resize(1920, 1000)
        Form.setMinimumSize(QSize(1920, 1000))
        Form.setMaximumSize(QSize(1920, 1000))
        Form.setLayoutDirection(Qt.RightToLeft)
        Form.setStyleSheet(u"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1590, 10, 241, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: #005580;\n"
"font: 20px \"MS Shell Dlg 2\" center\n"
"")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(2600, 30, 41, 31))
        self.label_7.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_7.setPixmap(QPixmap(u"../../Downloads/table.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(-330, 0, 2251, 51))
        self.label_8.setStyleSheet(u"background-color:  #005580")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1840, 10, 41, 31))
        self.label_9.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_9.setPixmap(QPixmap(u"../../Downloads/table.png"))
        self.label_9.setScaledContents(True)
        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(60, 10, 93, 28))
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.download = QPushButton(Form)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(180, 10, 93, 28))
        self.download.setCursor(QCursor(Qt.PointingHandCursor))
        self.print = QPushButton(Form)
        self.print.setObjectName(u"print")
        self.print.setGeometry(QRect(300, 10, 93, 28))
        self.print.setCursor(QCursor(Qt.PointingHandCursor))
        self.print.setStyleSheet(u"")
        self.cover = QFrame(Form)
        self.cover.setObjectName(u"cover")
        self.cover.setGeometry(QRect(0, 54, 1920, 1030))
        self.cover.setStyleSheet(u"")
        self.cover.setFrameShape(QFrame.StyledPanel)
        self.cover.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.cover)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(270, 80, 1551, 781))
        self.frame.setStyleSheet(u"background-color:white;\n"
"border:1px solid #005580;\n"
"border-radius:10px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 170, 1471, 561))
        self.tableWidget.setStyleSheet(u"color:black;font-size:16px;")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(240)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(31)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 10, 1061, 41))
        self.label_2.setStyleSheet(u"font-size:30px;\n"
"border:none;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(640, 80, 121, 30))
        self.label_3.setStyleSheet(u"border:none;font-size:15px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(820, 80, 361, 30))
        self.label_4.setStyleSheet(u"border:none;font-size:15px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 80, 470, 30))
        self.label_10.setStyleSheet(u"border:none;font-size:15px;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1320, 80, 141, 31))
        self.label_6.setStyleSheet(u"border:none;font-size:15px;")
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.changes = QPushButton(self.frame)
        self.changes.setObjectName(u"changes")
        self.changes.setGeometry(QRect(1290, 740, 93, 28))
        self.changes.setCursor(QCursor(Qt.PointingHandCursor))
        self.changes.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"\n"
"font-size:15px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #005580;\n"
"background-color:#005580;\n"
"color:white;\n"
"font-size:16px;\n"
"}\n"
"")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(650, 380, 341, 101))
        self.label_5.setStyleSheet(u"border:none;font-size:22px;color:red;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.prev = QPushButton(self.cover)
        self.prev.setObjectName(u"prev")
        self.prev.setGeometry(QRect(440, 890, 93, 28))
        self.prev.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color:#005580;\n"
"color:white;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #6699ff;\n"
"color:white;\n"
"font-size:16px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev.setIcon(icon)
        self.next = QPushButton(self.cover)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(1570, 880, 91, 28))
        self.next.setCursor(QCursor(Qt.PointingHandCursor))
        self.next.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color:#005580;\n"
"color:white;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #6699ff;\n"
"color:white;\n"
"font-size:16px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon1)
        self.printone = QPushButton(self.cover)
        self.printone.setObjectName(u"printone")
        self.printone.setGeometry(QRect(1110, 880, 141, 41))
        self.printone.setCursor(QCursor(Qt.PointingHandCursor))
        self.printone.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: #005580;\n"
"color:white;\n"
"font-size:15px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #6699ff;\n"
"color:white;\n"
"font-size:16px;\n"
"}\n"
"")
        self.searchButton = QPushButton(self.cover)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(1630, 30, 93, 31))
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: #005580;\n"
"color:white;\n"
"font-size:15px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #6699ff;\n"
"color:white;\n"
"font-size:16px;\n"
"}\n"
"")
        self.lineEdit = QLineEdit(self.cover)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1260, 30, 341, 31))
        self.lineEdit.setStyleSheet(u"background-color:white;")
        self.comboBox1 = QComboBox(self.cover)
        self.comboBox1.setObjectName(u"comboBox1")
        self.comboBox1.setGeometry(QRect(290, 30, 381, 31))
        self.comboBox1.setFocusPolicy(Qt.ClickFocus)
        self.comboBox1.setStyleSheet(u"background-color:white;")
        self.comboBox1.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox1.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.printone_2 = QPushButton(self.cover)
        self.printone_2.setObjectName(u"printone_2")
        self.printone_2.setGeometry(QRect(830, 880, 211, 41))
        self.printone_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.printone_2.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: #005580;\n"
"color:white;\n"
"font-size:15px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: #6699ff;\n"
"color:white;\n"
"font-size:16px;\n"
"}\n"
"")
        self.print_2 = QPushButton(Form)
        self.print_2.setObjectName(u"print_2")
        self.print_2.setGeometry(QRect(420, 10, 251, 28))
        self.print_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.print_2.setStyleSheet(u"")
        self.label_8.raise_()
        self.label.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.back.raise_()
        self.download.raise_()
        self.print.raise_()
        self.cover.raise_()
        self.print_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u062c\u062f\u0648\u0644 \u0627\u0644\u0645\u0644\u0627\u062d\u0638\u064a\u0646", None))
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.back.setText(QCoreApplication.translate("Form", u"\u0631\u062c\u0648\u0639", None))
        self.download.setText(QCoreApplication.translate("Form", u"\u062a\u0646\u0632\u064a\u0644", None))
        self.print.setText(QCoreApplication.translate("Form", u"\u0637\u0628\u0627\u0639\u0629 \u0627\u0644\u0643\u0644", None))
#if QT_CONFIG(shortcut)
        self.print.setShortcut(QCoreApplication.translate("Form", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u064a\u0648\u0645", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u062a\u0643\u0644\u064a\u0641", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u0644\u062c\u0627\u0646", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u064a\u0648\u0645", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u062a\u0643\u0644\u064a\u0641", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u0644\u062c\u0627\u0646", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"\u062a\u0643\u0644\u064a\u0641 \u0645\u0644\u0627\u062d\u0638\u0629 \u0644\u062c\u0627\u0646", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u0642\u0633\u0645 :", None))
        self.label_4.setText("")
        self.label_10.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u0633\u064a\u062f/", None))
        self.changes.setText(QCoreApplication.translate("Form", u"\u062d\u0641\u0638 \u0627\u0644\u062a\u063a\u064a\u0631\u0627\u062a", None))
        self.label_5.setText("")
        self.prev.setText("")
#if QT_CONFIG(shortcut)
        self.prev.setShortcut(QCoreApplication.translate("Form", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.next.setText("")
#if QT_CONFIG(shortcut)
        self.next.setShortcut(QCoreApplication.translate("Form", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.printone.setText(QCoreApplication.translate("Form", u"\u0637\u0628\u0627\u0639\u0647", None))
        self.searchButton.setText(QCoreApplication.translate("Form", u"\u0628\u062d\u062b", None))
        self.printone_2.setText(QCoreApplication.translate("Form", u"\u0627\u0631\u0633\u0627\u0644 \u0627\u064a\u0645\u064a\u0644 \u0644\u0644\u0634\u062e\u0635", None))
        self.print_2.setText(QCoreApplication.translate("Form", u"\u0627\u0631\u0633\u0627\u0644 \u0627\u064a\u0645\u064a\u0644 \u0644\u0644\u0643\u0644", None))
#if QT_CONFIG(shortcut)
        self.print_2.setShortcut(QCoreApplication.translate("Form", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

