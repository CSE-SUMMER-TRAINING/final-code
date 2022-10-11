from calendar import c
import sys
from PyQt5 import QtWidgets,QtPrintSupport, QtGui, QtCore
from  PyQt5.QtPrintSupport import QPrinter ,QPrintDialog
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel, QPushButton, QFileDialog, QComboBox,\
    QTableWidget, QTableWidgetItem, QVBoxLayout,QFrame,QDialog,QMessageBox,QTabWidget,QToolBox,QCompleter
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
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
from template import *
# year=
# month=
URL_EXAM = "https://drive.google.com/uc?export=download&id=1b98Hzn6F-3s2dQGSPcDlOJH_YFyLTMFl"
URL_INV = "https://drive.google.com/uc?export=download&id=1_weWkhA9x7b2zKr6NRkBbIFVxuqPLjD9"

branch_num = -1
option_num = -1


def build( num_of_branches=2):
    for i in range(num_of_branches):
        branch.append(Branch(branch_name[i], i, num_of_builds[i]))

    get_and_store_groups()
    DISPLAY(branch_num, num_of_branches)
    
def get_tables(branch_num, option_num):
    # print(option_num)
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
        self.label_not_enough.setWordWrap(True)
        self.browse.clicked.connect(self.browsefiles)
        self.generate.clicked.connect(self.generateTables)
        self.back.clicked.connect(self.goBack)
        self.linefileedit = self.findChild(QLineEdit, "lineEdit")
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
            if good_data:
                self.label_not_enough.setText(good_data)
                return
            ok1 = process_exam_day(days, colDayBranch)
            if not ok1:
                self.label_not_enough.setText("يوجد تعارض بين جدول الامتحانات وجدول القاعات")
                return
            ok2 = process(monitors, examDays)
            if not ok2:
                self.label_not_enough.setText("عدد الموظفين غير كافي")
                return
            self.label_not_enough.setText("")
            self.linefileedit.setText("")
            self.txt=""
            # create_observers_template()
            s2 = invScreen2()
            widget.addWidget(s2)
            widget.setCurrentWidget(s2)
        else :
            self.label_not_enough.setText("برجاء اختيار الملف")

current_index = -1
nj = 0

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
        self.label_dep = self.findChild(QLabel, "label_10")
        self.label_dep0 = self.findChild(QLabel, "label_3")
        self.label_name0 = self.findChild(QLabel, "label_6")
        self.label_ = self.findChild(QLabel, "label_2")

        self.table_widget = self.findChild(QTableWidget, "tableWidget")

        self.lineEdit = self.findChild(QLineEdit, "lineEdit")

        self.searchButton = self.findChild(QPushButton, "searchButton")
        self.searchButton.clicked.connect(self.search_fun)

        self.next = self.findChild(QPushButton, "next")
        self.next.clicked.connect(self.next_function)
        self.prev = self.findChild(QPushButton, "prev")
        self.prev.clicked.connect(self.prev_function)

        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.backfrominv_fun)

        self.download = self.findChild(QPushButton, "download")
        self.download.clicked.connect(self.download_function)

        self.frame = self.findChild(QFrame, "frame")

        # print one
        self.printone = self.findChild(QPushButton, "printone")
        self.printone.clicked.connect(self.printone_function)

        self.printone_2 = self.findChild(QPushButton, "printone_2")
        self.printone_2.clicked.connect(self.printone_2_function)
        # print all not comp
        # self.printall = self.findChild(QPushButton,"print")
        # self.printall.clicked.connect(self.printall_function)

        self.changes = self.findChild(QPushButton, "changes")
        self.changes.clicked.connect(lambda: self.changes_function(current_index))

        # auto complete
        self.completer = QCompleter(self.list)
        self.lineEdit.setCompleter(self.completer)

    def printone_function(self):
        # pdf
        self.changes.setText("")

        self.frame.resize(1000, 780)

        self.table_widget.setGeometry(20, 170, 850, 560)

        self.label_dep.setGeometry(100, 80, 200, 30)
        self.label_name.setGeometry(550, 80, 200, 30)
        self.label_dep0.setGeometry(250, 80, 200, 30)
        self.label_name0.setGeometry(800, 80, 50, 30)
        self.label_.setGeometry(330, 20, 400, 50)
        self.frame.setStyleSheet("border:none;background-color:white;")
        self.table_widget.setStyleSheet("border:1px solid black;background-color:white;")

        header = self.table_widget.horizontalHeader()
        for i in range(6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        screen = self.frame.grab()
        painter.drawPixmap(100, 100, screen)
        painter.end()

        self.frame.resize(1550, 780)

        self.table_widget.setGeometry(40, 170, 1470, 560)

        self.label_dep.setGeometry(150, 80, 470, 30)
        self.label_name.setGeometry(820, 80, 360, 30)
        self.label_dep0.setGeometry(640, 80, 121, 30)
        self.label_name0.setGeometry(1320, 80, 141, 30)
        self.label_.setGeometry(270, 10, 1060, 40)
        self.frame.setStyleSheet("border:1px solid #005580;border-radius:10px;background-color:white;")

        self.changes.setText("حفظ التغيرات ")
        
    def printone_2_function(self): 
        mp={
            0:"الأثنين",
            1:"الثلاثاء",
            2:"الأربعاء",
            3:"الخميس",
            4:"الجمعة",
            5:"السبت",
            6:"الأحد",
        }        
        for mon in monitors:
            days=[]
            dates=[]
            hours=[]
            places=[]
            for tas in mon.task:
                # print(tas.day," ",tas.building," ",tas.type)
                spliteddate=tas.day.split("/")
                # print(date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0])))
                days.append(arabic(mp[date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0])).weekday()]))
                dates.append(tas.day)
                hours.append("9:15")
                places.append(arabic(tas.building))
                
            send_email(mon.email,arabic(mon.user_name),arabic(mon.branch),11,2020,days,dates,hours,places)
        pass

    def download_function(self):
        cnt = 0
        print(observser_data_lst)
        lst=[]
        for i in observser_data_lst:
            lst.append(i.copy())
        for mon in monitors:
            mon.push_info(lst, cnt)
            cnt = cnt + 1
        
       try:
            dataframeout = pd.DataFrame(lst,columns=excelhead)
            dataframeout.to_excel("observer_output.xlsx")
            QMessageBox.about(self, "", "تم التنزيل                   ")

        except:
            QMessageBox.about(self, "", "لا يمكن تنزيل الملف اثناء تشغيله") #needed to be errorbox
        

    def set_items(self, index):
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
        countOfDays = len(mon.task)
        i = 0
        for ts in mon.task:
            row = self.table_widget.rowCount()

            if i % 2 == 0:
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

            else:
                item = QtWidgets.QTableWidgetItem(str(ts.day))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_widget.setItem(
                    row - 1, 3, item)
                item = QtWidgets.QTableWidgetItem(str(ts.type))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_widget.setItem(
                    row - 1, 4, item)
                item = QtWidgets.QTableWidgetItem(str(ts.building))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_widget.setItem(
                    row - 1, 5, item)
            i += 1

    def valueOfCombo(self):
        global current_index
        # clear search input
        self.lineEdit.setText("")
        # print(self.combox.currentIndex())
        if (self.combox.currentIndex()):
            current_index = self.combox.currentIndex() - 1
            self.set_items(self.combox.currentIndex() - 1)

    def search_fun(self):
        global current_index
        if self.lineEdit.text() in self.list:

            self.index = self.list.index(self.lineEdit.text()) - 1
            current_index = self.index
            self.combox.setCurrentIndex(0)

            self.set_items(self.index)

        else:
            self.combox.setCurrentIndex(0)
            self.lineEdit.setText("غير موجود")
            current_index = -1

            # clear table
            for i in range(self.table_widget.rowCount()):
                self.table_widget.removeRow(self.table_widget.rowCount() - 1)
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

    def changes_function(self, index):
        index_change_function = index
        # load data
        mon = monitors[index_change_function]
        i, j, ok = 0, 0, 0

        for ts in mon.task:
            
            if ok == 0:
                item = self.table_widget.item(i, 0)
                print(item.text())
                ts.day = item.text()

                item = self.table_widget.item(i, 1)
                print(item.text())
                ts.type = item.text()

                item = self.table_widget.item(i, 2)
                print(item.text())
                ts.building = item.text()
                i += 1
                ok = 1
                
            else:
                item = self.table_widget.item(j, 3)
                print(item.text())
                ts.day = item.text()

                item = self.table_widget.item(j, 4)
                print(item.text())
                ts.type = item.text()

                item = self.table_widget.item(j, 5)
                print(item.text())
                ts.building = item.text()
                j += 1
                ok = 0
            
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
        # global num_of_branches
        # excelSheet, num_of_branches, allBranches = read_inputt(self.txt)
        # read_sheet(excelSheet, num_of_branches)

    def goBack(self):
        widget.setCurrentWidget(mainwindow)

    def generateTables(self):
        if (self.txt != ""):
            ok = check_data(self.txt)
            if not ok:
                self.label_not_enough.setText("البيانات المدخلة غير صحيحة")
                return

            self.label_not_enough.setText("")
            # create_halls_template()
            global num_of_branches
            excelSheet, num_of_branches, allBranches = read_inputt(self.txt)
            read_sheet(excelSheet, num_of_branches)
            build(num_of_branches)

            exs2 = exScreen2(self.txt)
            widget.addWidget(exs2)
            widget.setCurrentWidget(exs2)
            self.lineEdit.setText("")
            self.txt = ""


        else:
            self.label_not_enough.setText("برجاء اختيار ملف")
            return

class exScreen2(QWidget):

    def __init__(self, file):

        super(exScreen2, self).__init__()

        loadUi("screenEx2.ui", self)

        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.backfromex_fun)
        # set tabs of branches
        self.add_tab_widget = QTabWidget(self)
        self.add_tab_widget.move(200, 100)  # position
        self.add_tab_widget.resize(1480, 800)  # size
        # get name of branches
        excelSheet = pd.ExcelFile(file)
        self.listOfBranches = excelSheet.sheet_names
        self.listOfBranches.pop(0)

        self.listOfFrames = []

        # self.save_func()
        for i in range(len(self.listOfBranches)):
            frame = QFrame(self)
            # frame.setStyleSheet("background-color:#c6ebd9;")
            self.listOfFrames.append(frame)

        for i in range(len(self.listOfBranches)):

            self.add_tab_widget.addTab(self.listOfFrames[i], self.listOfBranches[i])
            # self.add_tab_widget.setTabPosition(QTabWidget.South)
            # change direction
            self.add_tab_widget.setLayoutDirection(Qt.RightToLeft)

        self.add_tab_widget.setStyleSheet(
            """
                QTabBar::tab {
                    width: 300px;
                    height:50px;
                }
               QTabBar::tab:selected {
                    font-family: Roboto;
                    font-size: 18px;
                    background: rgb(175,175,175,255);
                    color: rgb(0,0,0,255);
                    border-top-left-radius: 8px;
                    border-top-right-radius: 8px;
                    border:1px solid rgb(197,197,199,255);
                    padding: 10px 30px 10px 24px;
               }
               QTabBar::tab:!selected{
                    font-family: Roboto;
                    font-size: 18px;
                    font: italic;
                    background: rgb(234,234,234,255);
                    color: rgb(0,0,0,255);
                    border-top-left-radius: 8px;
                    border-top-right-radius: 8px;

                    border:1px solid rgb(197,197,199,255);
                    padding: 10px 30px 10px 24px;
                }
            """)

        self.f(0)
        self.add_tab_widget.tabBarClicked.connect(self.f)


    def f(self, index=0):
        global nj
        index = index
        self.tabs = QTabWidget(self.listOfFrames[index])
        print(index)
        DISPLAY(index, num_of_branches)
        # print(toPrint)
        vertical = ["  القاعه"]


        for i in range(len(toPrint)):
            if toPrint[i][0] not in vertical:
                vertical.append(toPrint[i][0])

        table = QTableWidget(len(vertical),9)

        header = ["الدفعه","من","الي","الدفعه","من","الي","الدفعه","من","الي"]
        table.setHorizontalHeaderLabels(header)
        table_ho = table.horizontalHeader()
        for i in range(9):
            table_ho.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        table.setVerticalHeaderLabels(vertical)
        table_ve = table.verticalHeader()
        table_ve.setStyleSheet("font-size:20px;")
        # print(len(toPrint))
        for i in range(3):
            for j in range(len(vertical)-1):
                item = QtWidgets.QTableWidgetItem(str(toPrint[j][i+1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                table.setItem(j+1, i, item)

        for i in range(3):
            for j in range(len(vertical)-1):
                item = QtWidgets.QTableWidgetItem(str(toPrint[j+len(vertical)-1][i+1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                table.setItem(j+1, i+3, item)
        
        nj = 2*len(vertical)-2
        for i in range(3):
            for j in range(len(vertical)-1):
                item = QtWidgets.QTableWidgetItem(str(toPrint[j+nj][i+1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                table.setItem(j+1, i+6, item)

        l0 = QLabel("lab2")
        if index == 0:
            l0 = QLabel("lab11")

        self.tabs.addTab(table, "حل مقترح")
        self.tabs.addTab(l0, "اضافة حل؟")

        self.tabs.move(10, 10)  # position
        self.tabs.resize(1450, 700)  # size
        self.tabs.setTabPosition(QTabWidget.South)

        self.tabs.setStyleSheet('''QTabWidget::tab-bar
            {
                alignment: center;
            }
              QTabBar::tab {
                width: 100px;
                height:50px;
            }
            QTabBar::tab:selected {
                 font-family: Roboto;
                 font-size: 18px;
                 color: rgb(0,0,0,255);
                 background: rgb(175,175,175,255);
                 border-top-left-radius: 8px;
                 border-top-right-radius: 8px;
                 border:1px solid rgb(197,197,199,255);
                 padding: 10px 30px 10px 24px;
            }
            QTabBar::tab:!selected{
                 font-family: Roboto;
                 font-size: 18px;
                 font: italic;
                color: rgb(0,0,0,255);
                 border-top-left-radius: 8px;
                 border-top-right-radius: 8px;          
                 border:1px solid rgb(197,197,199,255);
                 padding: 10px 30px 10px 24px;
                 background: rgb(234,234,234,255);
             }
            ''')


    def backfromex_fun(self):
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
