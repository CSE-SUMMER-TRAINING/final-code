# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hallsTable.ui'
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
        Form.resize(1005, 800)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QWidget(Form)
        self.main.setObjectName(u"main")
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.body = QWidget(self.main)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background-color: #F5F8FA;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setSpacing(35)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(35, 0, 0, 0)
        self.widget_2 = QWidget(self.body)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(35)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 80))
        self.widget_3.setMaximumSize(QSize(16777215, 80))
        self.widget_3.setStyleSheet(u"box-shadow: 10px 10px 5px lightblue;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 80))
        self.label.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setFamily(u"Urdu Typesetting")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: #006aff;\n"
"color: white;\n"
"border-radius: 7px;")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setSpacing(35)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 50))
        self.widget_7.setMaximumSize(QSize(16777215, 50))
        self.widget_7.setToolTipDuration(0)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setSpacing(40)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.back = QPushButton(self.widget_7)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(170, 45))
        font1 = QFont()
        font1.setFamily(u"Simplified Arabic")
        font1.setPointSize(16)
        self.back.setFont(font1)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #000;\n"
"color: white;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#000;\n"
"color:#f4eade;\n"
"font-size:22px;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.back)

        self.save = QPushButton(self.widget_7)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(170, 45))
        self.save.setMaximumSize(QSize(120, 45))
        self.save.setFont(font1)
        self.save.setCursor(QCursor(Qt.PointingHandCursor))
        self.save.setLayoutDirection(Qt.LeftToRight)
        self.save.setStyleSheet(u"background-color: #006aff;\n"
"color: white;\n"
"border-radius: 7px;\n"
"")

        self.horizontalLayout_5.addWidget(self.save)


        self.verticalLayout_6.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 7px;")
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 20)
        self.widget_6 = QWidget(self.widget_8)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.tableWidget = QTableWidget(self.widget_6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(700, 500))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget.setStyleSheet(u"border: none;\n"
" text-align: left;\n"
" background-color: #fff;\n"
"\n"
"th {\n"
"  height: 50px;\n"
"  vertical-align: bottom;\n"
"}\n"
"\n"
"tr:hover {background-color: coral;}\n"
"")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setTextElideMode(Qt.ElideNone)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.NoPen)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addWidget(self.widget_6)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.but3 = QPushButton(self.widget_11)
        self.but3.setObjectName(u"but3")
        self.but3.setMinimumSize(QSize(12, 12))
        self.but3.setMaximumSize(QSize(12, 12))
        self.but3.setCursor(QCursor(Qt.PointingHandCursor))
        self.but3.setStyleSheet(u"background-color: #006aff;\n"
"border-radius: 6px;")

        self.horizontalLayout_7.addWidget(self.but3)

        self.but2 = QPushButton(self.widget_11)
        self.but2.setObjectName(u"but2")
        self.but2.setMinimumSize(QSize(12, 12))
        self.but2.setMaximumSize(QSize(12, 12))
        self.but2.setCursor(QCursor(Qt.PointingHandCursor))
        self.but2.setStyleSheet(u"background-color: #F5F8FA;\n"
"border-radius: 6px;")

        self.horizontalLayout_7.addWidget(self.but2)

        self.but1 = QPushButton(self.widget_11)
        self.but1.setObjectName(u"but1")
        self.but1.setMinimumSize(QSize(12, 12))
        self.but1.setMaximumSize(QSize(12, 12))
        self.but1.setCursor(QCursor(Qt.PointingHandCursor))
        self.but1.setStyleSheet(u"background-color: #F5F8FA;\n"
"border-radius: 6px;")

        self.horizontalLayout_7.addWidget(self.but1)


        self.horizontalLayout_8.addWidget(self.widget_11)

        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_6.addWidget(self.widget_10)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_7.addWidget(self.widget_9)


        self.verticalLayout_6.addWidget(self.widget_8)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.body)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(170, 0))
        self.widget.setMaximumSize(QSize(170, 16777215))
        self.widget.setStyleSheet(u"\n"
"background-color: #006aff;\n"
"color: white;\n"
"border-radius: 7px;")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(35)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 25, 0)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 80))
        self.label_2.setMaximumSize(QSize(200, 80))
        font2 = QFont()
        font2.setFamily(u"Urdu Typesetting")
        font2.setPointSize(38)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: red\n"
"")
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 100))
        self.scrollArea.setStyleSheet(u"border: none;\n"
"padding: 0;")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 145, 685))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.khal = QPushButton(self.scrollAreaWidgetContents)
        self.khal.setObjectName(u"khal")
        self.khal.setMinimumSize(QSize(145, 65))
        font3 = QFont()
        font3.setFamily(u"Harrington")
        font3.setPointSize(12)
        self.khal.setFont(font3)
        self.khal.setCursor(QCursor(Qt.PointingHandCursor))
        self.khal.setStyleSheet(u"background-color: #F5F8FA;\n"
"border-radius: 5px;\n"
"color: black;\n"
"margin-bottom: 20px;")

        self.verticalLayout_5.addWidget(self.khal)

        self.rod = QPushButton(self.scrollAreaWidgetContents)
        self.rod.setObjectName(u"rod")
        self.rod.setMinimumSize(QSize(0, 65))
        self.rod.setFont(font3)
        self.rod.setCursor(QCursor(Qt.PointingHandCursor))
        self.rod.setStyleSheet(u"color:#F5F8FA;\n"
"margin-bottom: 20px")

        self.verticalLayout_5.addWidget(self.rod)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.body)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u062c\u062f\u0648\u0644 \u0627\u0644\u0642\u0627\u0639\u0627\u062a", None))
        self.back.setText(QCoreApplication.translate("Form", u"\u0631\u062c\u0648\u0639", None))
#if QT_CONFIG(shortcut)
        self.back.setShortcut(QCoreApplication.translate("Form", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.save.setText(QCoreApplication.translate("Form", u"\u062a\u0646\u0632\u064a\u0644", None))
        self.label_3.setText("")
        self.but3.setText("")
        self.but2.setText("")
        self.but1.setText("")
        self.label_4.setText("")
        self.label_2.setText("")
        self.khal.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u062e\u0644\u0641\u0627\u0648\u064a", None))
        self.rod.setText(QCoreApplication.translate("Form", u"\u0631\u0648\u0636 \u0627\u0644\u0641\u0631\u062c", None))
    # retranslateUi

