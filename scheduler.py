from calendar import c
import sys
from PyQt5 import QtWidgets,QtPrintSupport, QtGui, QtCore
from  PyQt5.QtPrintSupport import QPrinter ,QPrintDialog
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel, QPushButton, QFileDialog, QComboBox,  QTableWidget, QTableWidgetItem, QVBoxLayout,QFrame,QDialog,QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLineEdit
import pandas as pd
from xml.etree.ElementTree import tostring
from solver import buildDp, solve, mem, toPrint
from college import *
from display import *
from groups_input import *
from observers_data import *
from observers_solve import *
import wget

URL_EXAM = "https://drive.google.com/uc?export=download&id=1b98Hzn6F-3s2dQGSPcDlOJH_YFyLTMFl"
URL_INV = "https://drive.google.com/uc?export=download&id=1_weWkhA9x7b2zKr6NRkBbIFVxuqPLjD9"

branch_num = -1
option_num = -1


def build(branch_num, num_of_branches):
    for i in range(num_of_branches):
        branch.append(Branch(branch_name[i], i, num_of_builds[i]))

    get_and_store_groups()
    DISPLAY(branch_num, num_of_branches)
    
def get_tables(branch_num, option_num):
    print(option_num)
    options(branch_num, option_num)

    def printCollege(branch: Branch) -> None:
        for hall in branch.hallsInBranch:
            print(f"{hall.name} {hall.volume}")
        print()
        for g in branch.groupsInBranch:
            print(f"{group[g].name} {group[g].volume}")


# UI
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("screen1.ui", self)

        self.inv = self.findChild(QPushButton, "inv")
        self.exam = self.findChild(QPushButton, "exam")

        self.inv.clicked.connect(self.invScreen)
        self.exam.clicked.connect(self.exScreen)

    def invScreen(self):
        widget.setCurrentWidget(invscreen1)

    def exScreen(self):
        widget.setCurrentWidget(exscreen1)

class invScreen1(QWidget):
    def __init__(self):
        super(invScreen1, self).__init__()
        loadUi("screenInv1.ui", self)
        self.browse = self.findChild(QPushButton, "browse")
        self.generate = self.findChild(QPushButton, "generate")
        self.back = self.findChild(QPushButton, "back")
        self.label = self.findChild(QLabel, "lineEdit")
        self.help = self.findChild(QPushButton, "help")
        self.help.clicked.connect(self.help_func)
        self.label_not_enough = self.findChild(QLabel, "label_not_enough")
        self.browse.clicked.connect(self.browsefiles)
        self.generate.clicked.connect(self.generateTables)
        self.back.clicked.connect(self.goBack)
        self.linefileedit = self.findChild(QLineEdit,"lineEdit")
        self.txt = ""
        self.file_name = ""

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', '', 'Excel (*.csv *xls *xlsx )')
        self.txt = fname
        self.file_name = fname[0]
        self.linefileedit.setText(fname[0])
    
    def help_func(self):
        widget.setCurrentWidget(helpinv)

    def goBack(self):
        widget.setCurrentWidget(mainwindow)
        self.label_not_enough.setText("")

    def generateTables(self):
        if (self.txt != ""):
            good_data = read_input(self.file_name)
            if not good_data:
                self.label_not_enough.setText("البيانات المدخلة غير صحيحة")
                return
            ok1 = process_exam_day(days, colDayBranch)
            if not ok1:
                self.label_not_enough.setText("يوجد تعارض بين جدول الامتحانات وجدول القاعات")                
                return
            ok2 = process(monitors, examDays)
            if not ok2 :
                self.label_not_enough.setText("عدد الموظفين غير كافي")
                return
            self.label_not_enough.setText("")
            s2 = invScreen2()
            widget.addWidget(s2)
            widget.setCurrentWidget(s2)

current_index = -1
class invScreen2(QWidget):
    def __init__(self):
        super(invScreen2, self).__init__()
        loadUi("screenInv2.ui", self)
        self.combox = self.findChild(QComboBox, "comboBox1")

        self.list = ["...اختار"]
        for mon in monitors:
            self.list.append(mon.user_name)

        self.combox.addItems(self.list)

        self.combox.currentIndexChanged.connect(self.valueOfCombo)


        self.label_name = self.findChild(QLabel, "label_4")
        self.label_dep = self.findChild(QLabel, "label_6")

        self.table_widget = self.findChild(QTableWidget, "tableWidget")

        self.lineEdit = self.findChild(QLineEdit, "lineEdit")

        self.searchButton = self.findChild(QPushButton, "searchButton")
        self.searchButton.clicked.connect(self.search_fun)

        self.next = self.findChild(QPushButton, "next")
        self.next.clicked.connect(self.next_function)
        self.prev = self.findChild(QPushButton, "prev")
        self.prev.clicked.connect(self.prev_function)

        self.back = self.findChild(QPushButton,"back")
        self.back.clicked.connect(self.backfrominv_fun)

        self.download = self.findChild(QPushButton,"download")
        self.download.clicked.connect(self.download_function)

        self.frame = self.findChild(QFrame,"frame")

        # print one
        self.printone = self.findChild(QPushButton,"printone")
        self.printone.clicked.connect(self.printone_function)

        # print all not comp
        #self.printall = self.findChild(QPushButton,"print")
        #self.printall.clicked.connect(self.printall_function)

        self.changes = self.findChild(QPushButton,"changes")
        self.changes.clicked.connect(lambda: self.changes_function(current_index))


    def printone_function(self):
        # pdf
        self.changes.setText("")

        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        screen = self.frame.grab()
        painter.drawPixmap(100, 100, screen)
        painter.end()

        self.changes.setText("حفظ التغيرات                        ")


    def download_function(self):
        cnt = 1
        for mon in monitors:
            mon.push_info(observser_data_lst, cnt)
            cnt = cnt + 1
        dataframeout = pd.DataFrame(observser_data_lst)
        dataframeout.to_excel("observer_output.xlsx")

        QMessageBox.about(self, "", "تم التنزيل                   ")


    def set_items(self,index):
        # clear table rows
        for i in range(self.table_widget.rowCount()):
            self.table_widget.removeRow(self.table_widget.rowCount() - 1)
        # clear labels
        self.label_name.setText("")
        self.label_dep.setText("")
        index_load_function = index
        # load data
        mon = monitors[index_load_function]
        self.label_name.setText(mon.user_name)
        self.label_dep.setText(mon.branch)

        for ts in mon.task:
            row = self.table_widget.rowCount()
            self.table_widget.setRowCount(row + 1)
            # item 1
            item = QtWidgets.QTableWidgetItem(str(ts.day))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_widget.setItem(row, 0, item)
            # item 2
            item = QtWidgets.QTableWidgetItem(str(ts.type))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_widget.setItem(row, 1, item)
            # item 3
            item = QtWidgets.QTableWidgetItem(str(ts.building))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_widget.setItem(
                row, 2, item)


    def valueOfCombo(self):
        global current_index
        # clear search input
        self.lineEdit.setText("")
        # print(self.combox.currentIndex())
        if (self.combox.currentIndex()):
            current_index = self.combox.currentIndex() -1
            self.set_items(self.combox.currentIndex() -1)


    def search_fun(self):
        global current_index
        if self.lineEdit.text() in self.list:

            self.index = self.list.index(self.lineEdit.text())-1
            current_index = self.index
            self.combox.setCurrentIndex(0)

            self.set_items(self.index)

        else:
            self.combox.setCurrentIndex(0)
            self.lineEdit.setText("غير موجود")
            current_index = -1

            # clear table
            for i in range(self.table_widget.rowCount()):
                self.table_widget.removeRow(self.table_widget.rowCount()-1)
            # clear labels
            self.label_name.setText("")
            self.label_dep.setText("")


    def next_function(self):
        global current_index
        if current_index + 1 == len(self.list) - 1:
            return
        current_index += 1

        self.combox.setCurrentIndex(0)
        self.lineEdit.setText("")
        self.set_items(current_index)


    def prev_function(self):
        global current_index

        if current_index == 0:
            return
        current_index -= 1


        self.combox.setCurrentIndex(0)
        self.lineEdit.setText("")


        self.set_items(current_index)


    def backfrominv_fun(self):
        widget.setCurrentWidget(invscreen1)


    def changes_function(self,index):
        index_change_function = index
        # load data
        mon = monitors[index_change_function]
        irow = 0
        for ts in mon.task:
            item = self.table_widget.item(irow,0)
            ts.day = item.text()

            item = self.table_widget.item(irow, 1)
            ts.type = item.text()

            item = self.table_widget.item(irow, 2)
            ts.building = item.text()
            irow += 1

        # # ask for download
        # dlg = QMessageBox(self)
        # dlg.setWindowTitle("تم حفظ التغيرات")
        # dlg.setText("هل تريد اعادة تنزيل الملف")
        # dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # button = dlg.exec()
        #
        # if button == QMessageBox.Yes:
        #     self.download_function()
        QMessageBox.about(self, "", "تم حفظ التغيرات                  ")

class exScreen1(QWidget):
    def __init__(self):
        super(exScreen1, self).__init__()
        loadUi("screenEx1.ui", self)
        self.browse = self.findChild(QPushButton, "browse")
        self.generate = self.findChild(QPushButton, "generate")
        self.back = self.findChild(QPushButton, "back")
        self.label = self.findChild(QLabel, "lineEdit")
        self.help = self.findChild(QPushButton, "help")
        self.help.clicked.connect(self.help_func)
        self.label_not_enough = self.findChild(QLabel, "label_not_enough")

        self.khalafawy = self.findChild(QCheckBox, "checkBox")
        self.rod = self.findChild(QCheckBox, "checkBox_2")

        self.browse.clicked.connect(self.browsefiles)
        self.generate.clicked.connect(self.generateTables)
        self.back.clicked.connect(self.goBack)

        self.txt = ""

    def help_func(self):
        widget.setCurrentWidget(helpexam)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', '', 'Excel (*.csv *xlsx)')
        self.lineEdit.setText(fname[0])
        self.txt = fname[0]

    def goBack(self):
        widget.setCurrentWidget(mainwindow)

    def generateTables(self):
        if (self.txt != ""):
            ok = check_data(self.txt)
            if not ok:
                self.label_not_enough.setText("البيانات المدخلة غير صحيحة")
                return

            excelSheet, num_of_branches, allBranches = read_inputt(self.txt)
            read_sheet(excelSheet, num_of_branches)
            
            if (self.khalafawy.isChecked() == True and self.rod.isChecked() == False):
                global branch_num
                branch_num = 1
                build(branch_num, num_of_branches)
                global s1
                s1 = exScreen2()
                widget.addWidget(s1)
                widget.setCurrentWidget(s1)
            elif (self.rod.isChecked() == True and self.khalafawy.isChecked() == False):
                branch_num = 2
                build(branch_num, num_of_branches)
                s1 = exScreen2()
                widget.addWidget(s1)
                widget.setCurrentWidget(s1)

class exScreen2(QWidget):
    def __init__(self):
        super(exScreen2, self).__init__()
        loadUi("screenEx2.ui", self)

        self.save = self.findChild(QPushButton, "save")
        self.save.clicked.connect(self.save_func)

        self.tableWidgetexam = self.findChild(QTableWidget, "tableWidget")
        self.comboxfl = self.findChild(QComboBox, "comboBoxx1_2")
        self.comboxfl.clear()
        self.comboxfl.addItem('choose')
        cnt = 1
        # for group in uniqueGroups:
        #     self.comboxfl.addItem(f"{cnt}")
        #     # print(f"{cnt}.")
        #     cnt += 1

        self.comboxfl.currentTextChanged.connect(self.change_table)
        self.label = self.findChild(QLabel, "label1")

    def change_table(self, s):
        global option_num
        if (s != "choose"):
            option_num = int(s)
            row1 = 0
            row2 = 0
            row3 = 0
            row11 = 0
            row22 = 0
            row33 = 0
            print("Text changed:", s)

            get_tables(branch_num, option_num)

            print(len(to_print1))
            self.tableWidgetexam.setRowCount(len(to_print1))
            for res in to_print3:
                self.tableWidgetexam.setItem(
                    row1, 0, QtWidgets.QTableWidgetItem(str(res[3])))
                self.tableWidgetexam.setItem(
                    row1, 1, QtWidgets.QTableWidgetItem(str(res[2])))
                self.tableWidgetexam.setItem(
                    row1, 2, QtWidgets.QTableWidgetItem(str(res[1])))
                row1 += 1

            for res in to_print2:
                self.tableWidgetexam.setItem(
                    row2, 3, QtWidgets.QTableWidgetItem(str(res[3])))
                self.tableWidgetexam.setItem(
                    row2, 4, QtWidgets.QTableWidgetItem(str(res[2])))
                self.tableWidgetexam.setItem(
                    row2, 5, QtWidgets.QTableWidgetItem(str(res[1])))
                row2 += 1

            for res in to_print1:
                self.tableWidgetexam.setItem(
                    row3, 6, QtWidgets.QTableWidgetItem(str(res[3])))
                self.tableWidgetexam.setItem(
                    row3, 7, QtWidgets.QTableWidgetItem(str(res[2])))
                self.tableWidgetexam.setItem(
                    row3, 8, QtWidgets.QTableWidgetItem(str(res[1])))
                row3 += 1

            for res in to_print3:
                self.tableWidgetexam.setItem(
                    row11, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                self.tableWidgetexam.setItem(
                    row11, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                self.tableWidgetexam.setItem(
                    row11, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                row11 += 1

            for res in to_print2:
                self.tableWidgetexam.setItem(
                    row22, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                self.tableWidgetexam.setItem(
                    row22, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                self.tableWidgetexam.setItem(
                    row22, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                row22 += 1

            for res in to_print1:
                self.tableWidgetexam.setItem(
                    row33, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                self.tableWidgetexam.setItem(
                    row33, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                self.tableWidgetexam.setItem(
                    row33, 9, QtWidgets.QTableWidgetItem(str(res[0])))
                row33 += 1
            to_print1.clear()
            to_print2.clear()
            to_print3.clear()

            # for i in range(5):
            #    print(to_print1[i], to_print2[i], to_print3[i])

    def browsefiles(self):
        QFileDialog.getOpenFileName(
            self, 'Open file', '', 'Excel (*.csv *xls)')

    def save_func(self):
        output_the_distribution(branch_num)

    def backfromex_fun(self):
        widget.removeWidget(s1)
        exscreen1 = exScreen1()
        widget.addWidget(exscreen1)
        widget.setCurrentWidget(exscreen1)


class invHelp(QWidget):
    def __init__(self):
        super(invHelp, self).__init__()
        loadUi("helpInv.ui", self)
        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.back_func)
        self.save = self.findChild(QPushButton, "save")
        self.save.clicked.connect(self.save_func)

    def back_func(self):
        widget.setCurrentWidget(invscreen1)

    def save_func(self):
        wget.download(URL_INV)


class examHelp(QWidget):
    def __init__(self):
        super(examHelp, self).__init__()
        loadUi("helpEx.ui", self)
        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.back_func)
        self.save = self.findChild(QPushButton, "save")
        self.save.clicked.connect(self.save_func)

    def back_func(self):
        widget.setCurrentWidget(exscreen1)

    def save_func(self):
        wget.download(URL_EXAM)



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
exscreen1 = exScreen1()
invscreen1 = invScreen1()
helpinv = invHelp()
helpexam = examHelp()

widget.addWidget(mainwindow)
widget.addWidget(exscreen1)
widget.addWidget(invscreen1)
widget.addWidget(helpinv)
widget.addWidget(helpexam)

widget.move(2,2)
widget.show()
sys.exit(app.exec_())
