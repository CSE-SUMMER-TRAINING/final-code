# your code goes herefrom calendar import c
from re import I
import sys
import win32api
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import (
    QWidget,
    QCheckBox,
    QApplication,
    QLabel,
    QPushButton,
    QFileDialog,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QFrame,
    QDialog,
    QMessageBox,
    QTabWidget,
    QToolBox,
    QCompleter,
)
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLineEdit
import pandas as pd
from solver import solve
from college import *
from display import *
from groups_input import *
from observers_data import *
from observers_solve import *
import wget
from template import *
from PyQt5.QtGui import *

# year=
# month=
URL_EXAM = (
    "https://drive.google.com/uc?export=download&id=1b98Hzn6F-3s2dQGSPcDlOJH_YFyLTMFl"
)
URL_INV = (
    "https://drive.google.com/uc?export=download&id=1_weWkhA9x7b2zKr6NRkBbIFVxuqPLjD9"
)

branch_num = -1
option_num = -1
branch_sol = []


def build(num_of_branches=2):
    for i in range(num_of_branches):
        branch.append(Branch(branch_name[i], i, num_of_builds[i]))

    get_and_store_groups()

    branch_sol.clear()
    for i in range(num_of_branches):
        branch_sol.append(solve(branch[i]))


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
        loadUi("./ui/screen1.ui", self)

        self.inv = self.findChild(QPushButton, "inv")
        self.exam = self.findChild(QPushButton, "exam")

        self.inv.clicked.connect(self.invScreen)
        self.exam.clicked.connect(self.exScreen)

    def invScreen(self):
        widget.setCurrentWidget(invscreen1)

    def exScreen(self):
        widget.setCurrentWidget(exscreen1)

current_index = -1

class invScreen1(QWidget):
    def __init__(self):
        super(invScreen1, self).__init__()
        loadUi("./ui/screenInv1.ui", self)
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
            self, "Open file", "", "Excel (*.csv *xls *xlsx )"
        )
        self.txt = fname
        self.file_name = fname[0]
        self.linefileedit.setText(fname[0])

    def help_func(self):
        widget.setCurrentWidget(helpinv)

    def goBack(self):
        widget.setCurrentWidget(mainwindow)
        self.label_not_enough.setText("")

    def generateTables(self):
        global current_index
        if self.txt != "":
            good_data = read_input(self.file_name)
            if good_data:
                self.label_not_enough.setText(good_data)
                return
            ok1 = process_exam_day(days, colDayBranch)
            if not ok1:
                self.label_not_enough.setText(
                    "يوجد تعارض بين جدول الامتحانات وجدول القاعات"
                )
                return
            ok2 = process(monitors, examDays)
            if not ok2:
                self.label_not_enough.setText("عدد الموظفين غير كافي")
                return
            self.label_not_enough.setText("")
            self.linefileedit.setText("")
            self.txt = ""
            # create_observers_template()
            s2 = invScreen2()
            widget.addWidget(s2)
            widget.setCurrentWidget(s2)
            current_index = -1
        else:
            self.label_not_enough.setText("برجاء اختيار الملف")


nj = 0
solveIdx = 0


class Worker(QObject):
    finished=pyqtSignal()
    def run(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.core_fonts_encoding='utf-8'
        #1-find site-package in ur python directory then go to fpdf (after installing it) create folder with the name "font"
        #2-extrat the zip file their that's all !!!!!!!!!!!!!!!!!!!!!!!!
        pdf.add_font('FreeSerif', '', 'IBM_Plex_Sans_Arabic/IBMPlexSansArabic-Regular.ttf')
        mp = {
                    0: "الأثنين",
                    1: "الثلاثاء",
                    2: "الأربعاء",
                    3: "الخميس",
                    4: "الجمعة",
                    5: "السبت",
                    6: "الأحد",
                }

        for mon in monitors:
            
            data=[(arabic("التكليف"),arabic("المكان"),arabic( "الساعة"), arabic("التاريخ"), arabic("اليوم"))]
            for tas in mon.task:
                spliteddate = tas.day.split("/")
                dayy=arabic(mp[date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0]),).weekday()])
                data.append((arabic(tas.type),arabic(tas.building),"9:15",tas.day,dayy))
            if(len(data)==1):continue
            pdf.add_page()
            pdf.image("icons\logo.jpg",90,w=35,h=50)
            pdf.set_font('FreeSerif', size=12)
            pdf.set_fill_color(237, 240, 149)
            pdf.ln()
            pdf.cell(w=195,h=5,fill=1,new_x=XPos.RIGHT, new_y=YPos.TOP,txt="2022/2023 "+arabic(" تكليف لجان الامتحانات يناير  "),align="c")
            pdf.ln()
            pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("السيد/ %s                                                                       قسم:%s"%(mon.user_name,mon.work_place)),align="R")
            pdf.ln()
            pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("تحية طيبة وبعد ..."),align="R")
            pdf.ln()
            pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("تكليف بالحضور لجان امتحانات  فى الايام والمواعيد التالية :"),align="R")
            pdf.ln()

            line_height = pdf.font_size * 1.50
            for i in range(len(data)):
                row=data[i]
                for datum in row:
                    if(i==0):
                        pdf.multi_cell(35, line_height,datum,fill=1 , border=1,new_x=XPos.RIGHT, new_y=YPos.TOP)
                    else :pdf.multi_cell(35, line_height, datum, border=1,new_x=XPos.RIGHT, new_y=YPos.TOP)
                pdf.ln()
            x=len(data)-1
            pdf.cell(w=195,h=5,fill=1,new_x=XPos.RIGHT, new_y=YPos.TOP,txt="%d    "%(x) + arabic("اجمالى عدد ايام الملاحظة  "),align="C")
            pdf.ln()
            pdf.set_fill_color(237, 12, 61)
            pdf.cell(w=195,h=5,fill=1,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("نظرا لقرار مجلس الكليه فى حالة تبديل يوم مكان اخر لابد من ايجاد البديل "),align="C")
            pdf.ln()

            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("1-الحضور بمقر اللجنة قبل بدء الامتحان بنصف ساعة على الأقل"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("2-استلام كراسات الإجابة وتوزيعها على الطلاب قبل بدء الامتحان بخمس دقائق على الأقل"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("3-توزيع أوراق الأسئلة وعدم تدوين اى معلومات عليها أو تبادل الطلاب لها"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("4-جمع كرنيهات الطلاب ومراجعة بياناتها مع البيانات المسجلة على كراسة الإجابة والتوقيع عليها"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("5-مراجعة استمارات الغياب للطلاب الغائبين مع التأكد من توقيع جميع الطلاب الحاضرين فى كشوف الحضور والانصراف"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("6-يمنع الطالب من الخروج من اللجنه قبل نصف مده الامتحان"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("7-عدم توقيع الطالب فى كشوف الانصراف إلا بعد استلام ورقة الإجابة"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("8-إبلاغ رئيس اللجنة عن اى حالة غش أو الشروع فيه أو أى إخلال بنظام الامتحان"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("9-عدم اضافة أي اسم طالب بكشوف الحضور كتابة باليد والالتزام بكشوف الاسماء المدرجه فقط"),align="R")
            pdf.ln()
            pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("الالتزام الكامل بالاجراءات الاحترازيه وارتداء الكمامه مع عدم تداول الادوات الشخصيه داخل اللجان")+"-10",align="R")
            pdf.ln()
        pdf.output('table_with_cells.pdf')
        self.finished.emit()
       
class Worker2(QObject):
    finished=pyqtSignal()
    def run(self):
        unvalid_emails = {}
        mp_day = {
            0: "الأثنين",
            1: "الثلاثاء",
            2: "الأربعاء",
            3: "الخميس",
            4: "الجمعة",
            5: "السبت",
            6: "الأحد",
        }
        mp_month = {
            1: "يناير",
            2: "فبراير",
            3: "مارس",
            4: "إبريل",
            5: "مايو",
            6: "يونيو",
            7: "يوليو",
            8: "أغسطس",
            9: "سبتمبر",
            10: "أكتوبر",
            11: "نوفمبر",
            12: "ديسمبر"
        }
        startfile("outlook.exe")
        ok = True
        if "outlook.exe" in (i.name() for i in psutil.process_iter()) == False:
            ok = False

        for mon in monitors:
            if not is_email(mon.email):
                    unvalid_emails[mon.user_name] = mon.email
                    continue
                    
            if len(mon.task) == 0:
            #    self.label_5.setText(f"{mon.user_name} ليس لديه أيّ تكليفات")
                continue
            days = []
            dates = []
            hours = []
            types = []
            places = []
            for tas in mon.task:
                # print(tas.day," ",tas.building," ",tas.type)
                spliteddate = tas.day.split("/")
                # print(date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0])))
                days.append(
                        mp_day[
                            date(
                                int(spliteddate[2]),
                                int(spliteddate[1]),
                                int(spliteddate[0]),
                            ).weekday()
                        ]
                )
                dates.append(tas.day)
                hours.append("9:15")
                types.append(tas.type)
                places.append(tas.building)

            send_email(
                mon.email,
                mon.user_name,
                mon.branch,
                mp_month[datetime.strptime(mon.task[0].day, '%d/%m/%Y').month],
                datetime.strptime(mon.task[0].day, '%d/%m/%Y').year,
                days,
                dates,
                hours,
                types,
                places,
                len(mon.task),
                ok
            )
        self.finished.emit()

class Worker3(QObject):
    finished=pyqtSignal()
    def __init__(self,txt,parent=None):
        QThread.__init__(self,parent)
        self.txt=txt
    def run(self):
        print(self.txt)
        global num_of_branches, allBranches
        excelSheet, num_of_branches, allBranches = read_inputt(self.txt)
        read_sheet(excelSheet, num_of_branches)
        build(num_of_branches)
        self.finished.emit()
        
class invScreen2(QWidget):
    def __init__(self):
        super(invScreen2, self).__init__()
        loadUi("./ui/screenInv2.ui", self)
        self.combox = self.findChild(QComboBox, "comboBox1")

        self.list = ["...اختار"]
        for mon in monitors:
            self.list.append(mon.user_name)

        self.combox.addItems(self.list)

        self.combox.currentIndexChanged.connect(self.valueOfCombo)

        self.label_name = self.findChild(QLabel, "name")
        self.label_dep = self.findChild(QLabel, "dap")
        self.label_dep0 = self.findChild(QLabel, "dap0")
        self.label_name0 = self.findChild(QLabel, "name0")
        self.label_ = self.findChild(QLabel, "label_2")
        # self.label_5 = self.findChild(QLabel, "label_5")
        self.table_widget = self.findChild(QTableWidget, "tableWidget")
        table_ho = self.table_widget.horizontalHeader()
        
        for i in range(6):
            table_ho.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        self.lineEdit = self.findChild(QLineEdit, "lineEdit")

        self.searchButton = self.findChild(QPushButton, "searchButton")
        self.searchButton.clicked.connect(self.search_fun)

        self.prev = self.findChild(QPushButton, "prev")
        self.prev.clicked.connect(self.prev_function)
        self.next = self.findChild(QPushButton, "next")
        self.next.clicked.connect(self.next_function)

        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.backfrominv_fun)

        self.download = self.findChild(QPushButton, "download")
        self.download.clicked.connect(self.download_function)


        # print one
        self.printone = self.findChild(QPushButton, "printone")
        self.printone.clicked.connect(self.printone_function)

        self.printone_2 = self.findChild(QPushButton, "printone_2")
        self.printone_2.clicked.connect(self.printone_2_function)
        self.print_2 = self.findChild(QPushButton, "print_2")
        self.print_2.clicked.connect(self.print_2_function)
        # print all not comp
        self.printall = self.findChild(QPushButton,"print")
        self.printall.clicked.connect(self.printall_function)

        self.changes = self.findChild(QPushButton, "changes")
        self.changes.clicked.connect(lambda: self.changes_function(current_index))

        # auto complete
        self.completer = QCompleter(self.list)
        self.lineEdit.setCompleter(self.completer)
    
    def msg(self):
        QMessageBox.about(self, "", "تم التنزيل                   ")
        self.print.setText("طباعة الكل")
        self.print_2.setEnabled(True)
        self.print.setEnabled(True)
        
    def printall_function(self):
        try:
            QMessageBox.about(self, "", "سوف يتم التنزيل بعد لحظات                   ")
            self.print.setEnabled(False)
            self.print_2.setEnabled(False)

            self.print.setText("...يتم التنزيل")
            self.thread=QThread()
            self.worker=Worker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.msg)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        except:
            QMessageBox.about(
                self, "", "لا يمكن تنزيل الملف اثناء تشغيله برجاء قفل table_with_cells.pdf"
            )  # needed to be errorbox
    def printone_function(self):
        # pdf
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.core_fonts_encoding='utf-8'
        #1-find site-package in ur python directory then go to fpdf (after installing it) create folder with the name "font"
        #2-extrat the zip file their that's all !!!!!!!!!!!!!!!!!!!!!!!!
        pdf.add_font('FreeSerif', '', 'IBM_Plex_Sans_Arabic/IBMPlexSansArabic-Regular.ttf')
        mp = {
                    0: "الأثنين",
                    1: "الثلاثاء",
                    2: "الأربعاء",
                    3: "الخميس",
                    4: "الجمعة",
                    5: "السبت",
                    6: "الأحد",
                }

        mon=monitors[current_index]
        data=[(arabic("التكليف"),arabic("المكان"),arabic( "الساعة"), arabic("التاريخ"), arabic("اليوم"))]
        for tas in mon.task:
            spliteddate = tas.day.split("/")
            dayy=arabic(mp[date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0]),).weekday()])
            data.append((arabic(tas.type),arabic(tas.building),"9:15",tas.day,dayy))
        pdf.add_page()
        pdf.image("icons\logo.jpg",90,w=35,h=50)
        pdf.set_font('FreeSerif', size=12)
        pdf.set_fill_color(237, 240, 149)
        pdf.ln()
        pdf.cell(w=195,h=5,fill=1,new_x=XPos.RIGHT, new_y=YPos.TOP,txt="2022/2023 "+arabic(" تكليف  لجان الامتحانات يناير  "),align="c")
        pdf.ln()
        pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("السيد/ %s                                                                       قسم:%s"%(mon.user_name,mon.work_place)),align="R")
        pdf.ln()
        pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("تحية طيبة وبعد ..."),align="R")
        pdf.ln()
        pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("تكليف بالحضور  لجان امتحانات  فى الايام والمواعيد التالية :"),align="R")
        pdf.ln()

        line_height = pdf.font_size * 1.50
        for i in range(len(data)):
            row=data[i]
            for datum in row:
                if(i==0):
                    pdf.multi_cell(39, line_height,datum,fill=1 , border=1,new_x=XPos.RIGHT, new_y=YPos.TOP)
                else :pdf.multi_cell(39, line_height, datum, border=1,new_x=XPos.RIGHT, new_y=YPos.TOP)
            pdf.ln()
        x=len(data)-1
        pdf.cell(w=195,h=5,fill=1,new_x=XPos.RIGHT, new_y=YPos.TOP,txt="%d    "%(x) + arabic("اجمالى عدد ايام الملاحظة  "),align="C")
        pdf.ln()
        pdf.set_fill_color(237, 12, 61)
        pdf.cell(w=195,h=5,fill=1,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("نظرا لقرار مجلس الكليه فى حالة تبديل يوم مكان اخر لابد من ايجاد البديل "),align="C")
        pdf.ln()

        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("1-الحضور بمقر اللجنة قبل بدء الامتحان بنصف ساعة على الأقل"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("2-استلام كراسات الإجابة وتوزيعها على الطلاب قبل بدء الامتحان بخمس دقائق على الأقل"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("3-توزيع أوراق الأسئلة وعدم تدوين اى معلومات عليها أو تبادل الطلاب لها"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("4-جمع كرنيهات الطلاب ومراجعة بياناتها مع البيانات المسجلة على كراسة الإجابة والتوقيع عليها"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("5-مراجعة استمارات الغياب للطلاب الغائبين مع التأكد من توقيع جميع الطلاب الحاضرين فى كشوف الحضور والانصراف"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("6-يمنع الطالب من الخروج من اللجنه قبل نصف مده الامتحان"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("7-عدم توقيع الطالب فى كشوف الانصراف إلا بعد استلام ورقة الإجابة"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("8-إبلاغ رئيس اللجنة عن اى حالة غش أو الشروع فيه أو أى إخلال بنظام الامتحان"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("9-عدم اضافة أي اسم طالب بكشوف الحضور كتابة باليد والالتزام بكشوف الاسماء المدرجه فقط"),align="R")
        pdf.ln()
        pdf.cell(w=195,h=4,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("الالتزام الكامل بالاجراءات الاحترازيه وارتداء الكمامه مع عدم تداول الادوات الشخصيه داخل اللجان")+"-10",align="R")
        pdf.ln()
        pdf.output(f'{mon.user_name}.pdf')
        
        try: 
            win32api.ShellExecute(0, "print", f'{mon.user_name}.pdf', None,".",0)
        except:
            pass
        
    def msg2(self):
        QMessageBox.about(self, "", "تم الارسال                   ")
        self.print_2.setText("ارسال ايميل للكل")
        self.print.setEnabled(True)
        self.print_2.setEnabled(True)
        
    def print_2_function(self):
        try:
            QMessageBox.about(self, "", "سوف يتم الارسال بعد لحظات                   ")
            self.print.setEnabled(False)
            self.print_2.setEnabled(False)
            self.print_2.setText("...يتم الارسال")
            self.thread=QThread()
            self.worker=Worker2()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.msg2)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        except:
            QMessageBox.about(
                self, "", "لا يمكن الارسال الان حاول مجددا في وقت لاحق"  
            )  # needed to be errorbox 
            
    def printone_2_function(self):
        if(current_index==-1):
            QMessageBox.about(self,"","من فضلك اختار شخص")
           
        elif len(monitors[current_index].task) == 0:
            QMessageBox.about(self,"",f"{monitors[current_index].user_name} ليس لديه أيّ تكليفات")
        
        elif not is_email(monitors[current_index].email):
                 QMessageBox.about(self,"","البريد الإلكتروني غير صالح\nالبريد يجب أن يكون على هذا النحو:\n'example@feng.bu.edu.eg'\n'أو: example@example.example'")
        else:
            ok = True
            if "outlook.exe" in (i.name() for i in psutil.process_iter()) == False:
                ok = False
            mp_day = {
            0: "الأثنين",
            1: "الثلاثاء",
            2: "الأربعاء",
            3: "الخميس",
            4: "الجمعة",
            5: "السبت",
            6: "الأحد",
            }
            mp_month = {
                1: "يناير",
                2: "فبراير",
                3: "مارس",
                4: "إبريل",
                5: "مايو",
                6: "يونيو",
                7: "يوليو",
                8: "أغسطس",
                9: "سبتمبر",
                10: "أكتوبر",
                11: "نوفمبر",
                12: "ديسمبر"
            }
            tmplst=monitors[current_index]
            days=[]
            dates=[]
            hours=[]
            types = []
            places=[]
            for tas in tmplst.task:
                spliteddate=tas.day.split("/")
                days.append(mp_day[date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0])).weekday()])
                dates.append(tas.day)
                hours.append("9:15")
                types.append(tas.type)
                places.append(tas.building)

            send_email(tmplst.email,tmplst.user_name,tmplst.branch, mp_month[datetime.strptime(tmplst.task[0].day, '%d/%m/%Y').month], datetime.strptime(tmplst.task[0].day, '%d/%m/%Y').year, days,dates,hours,types,places,len(tmplst.task),ok)
    def download_function(self):
        cnt = 0
        lst = []
        for i in observser_data_lst:
            lst.append(i.copy())
        for mon in monitors:
            mon.push_info(lst, cnt)
            cnt = cnt + 1

        try:
            
            dataframeout = pd.DataFrame(lst, columns=excelhead)
            dataframeout.to_excel("observer_output.xlsx")
            QMessageBox.about(self, "", "تم التنزيل                   ")
        except:
            QMessageBox.about(
                self, "", "لا يمكن تنزيل الملف اثناء تشغيله"
            )  # needed to be errorbox

    def set_items(self, index):
        # clear table rows
       # self.label_5.setText("")
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
                self.table_widget.setItem(row, 2, item)

            else:
                item = QtWidgets.QTableWidgetItem(str(ts.day))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_widget.setItem(row - 1, 3, item)
                item = QtWidgets.QTableWidgetItem(str(ts.type))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_widget.setItem(row - 1, 4, item)
                item = QtWidgets.QTableWidgetItem(str(ts.building))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_widget.setItem(row - 1, 5, item)
            i += 1

    def valueOfCombo(self):
        global current_index
        # clear search input
        self.lineEdit.setText("")
        if self.combox.currentIndex():
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
            # current_index = -1

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

        if current_index <= 0:
            return
        current_index -= 1

        self.combox.setCurrentIndex(0)
        self.lineEdit.setText("")

        self.set_items(current_index)

    def backfrominv_fun(self):
        widget.setCurrentWidget(invscreen1)
    
    def valid_day(self,s):
        s= s.split('/')
        if len(s)!= 3 :
            return False
        def is_int(s):
            try: 
                int(s)
                return True
            except ValueError:
                return False
        cnt = 0 
        for it in s:
            if not is_int(it):
                return False
            if cnt ==2 and len(it)!= 4:
                return False
            if cnt <2 and (len(it) <1 or len(it)>2):
                return False
            cnt+=1
        return True
        
    def current_day(self,day):
        v=str(day).split(".")[0].split("/")
        v[0]=str(int(v[0]))
        v[1]=str(int(v[1]))
        v[2]=str(int(v[2]))
        x = tuple(v)
        return daynumber[x]
    def changes_function(self, index):
        # load data
        mon = monitors[index]
        i, j, ok = 0, 0, 0
        for ts in mon.task:
            if ok == 0:
                day_change= -1
                item = self.table_widget.item(i, 0)
                if not self.valid_day(item.text()):
                    QMessageBox.about(self, "", "صيغة التاريخ غير صحيحة\nاكتب التاريخ كالتالى 10/10/2000")
                    return
                else :
                    if ts.day != item.text():
                        day_change = ts.day
                    ts.day = item.text()
                item = self.table_widget.item(i, 1)
                if item.text() not in tasks_known_names.keys():
                    QMessageBox.about(self, "", "هذا التكليف غير معروف يمكنك اختيار احدى التكاليف التالية\n1-رئيس لجنة\n2-مراقب دور\n3-ملاحظ\n4-احتياطى")
                    return
                ts.type = item.text()
                item = self.table_widget.item(i, 2)
                if item.text() not in is_bransh.keys():
                    msg= "هذا الفرع غير موجود بالكلية، يمكنك اختيار احد الاختيارات التالية\n"
                    cnt= 1 
                    for k in is_bransh.keys():
                        msg += str(cnt)+ ' - '+ (k) + '\n'
                        cnt+=1 
                    QMessageBox.about(self, "", msg)
                    return
                ts.building = item.text()
                if day_change!= -1:
                    mon.accupied_days[self.current_day(day_change)] = [0,""]
                try :
                    ts.current_day()
                except:
                    ts.day= day_change
                    QMessageBox.about(self, "", "هذا اليوم ليس من ضمن ايام الامتحانات\nلا يمكن تنفيذ العملية")
                    return
                if ts.current_day() in mon.accupied_days.keys():
                    mon.accupied_days[ts.current_day()][1] = ts.building
                else :
                    mon.accupied_days[ts.current_day()] = [1,ts.building]
                i += 1
                ok = 1
            else:
                day_change= -1
                item = self.table_widget.item(j, 3)
                if not self.valid_day(item.text()):
                    QMessageBox.about(self, "", "صيغة التاريخ غير صحيحة\nاكتب التاريخ كالتالى 10/10/2000")
                    return
                else :
                    if ts.day != item.text():
                        day_change = ts.day
                    ts.day = item.text()
                item = self.table_widget.item(j, 4)
                if item.text() not in tasks_known_names.keys():
                    QMessageBox.about(self, "", "هذا التكليف غير معروف يمكنك اختيار احدى التكاليف التالية\n1-رئيس لجنة\n2-مراقب دور\n3-ملاحظ\n4-احتياطى")
                    return
                ts.type = item.text()
                item = self.table_widget.item(j, 5)
                if (item.text()) not in is_bransh.keys():
                    msg= "هذا الفرع غير موجود بالكلية، يمكنك اختيار احد الاختيارات التالية\n"
                    cnt= 1 
                    for k in is_bransh.keys():
                        msg += str(cnt)+ ' - '+ (k) + '\n'
                        cnt+=1 
                    QMessageBox.about(self, "", msg)
                    return
                ts.building = item.text()
                if day_change!= -1:
                    mon.accupied_days[self.current_day(day_change)] = [0,""]
                try :
                    ts.current_day()
                except:
                    ts.day= day_change
                    QMessageBox.about(self, "", "هذا اليوم ليس من ضمن ايام الامتحانات\nلا يمكن تنفيذ العملية")
                    return
                if ts.current_day() in mon.accupied_days.keys():
                    mon.accupied_days[ts.current_day()][1] = ts.building
                else :
                    mon.accupied_days[ts.current_day()] = [1,ts.building]
                j += 1
                ok = 0
        monitors[index] = mon
        QMessageBox.about(self, "", "تم حفظ التغيرات                  ")

#  global __txt 
class exScreen1(QWidget):
    def __init__(self):

        super(exScreen1, self).__init__()
        loadUi("./ui/screenEx1.ui", self)
        self.browse = self.findChild(QPushButton, "browse")
        self.generate = self.findChild(QPushButton, "generate")
        self.back = self.findChild(QPushButton, "back")
        self.label = self.findChild(QLabel, "lineEdit")
        self.help = self.findChild(QPushButton, "help")
        self.label_2=self.findChild(QLabel, "label_2")
        self.label_3=self.findChild(QLabel, "label_3")
        self.pixmap =QPixmap(r"icons\uploadFile.png")
        self.help.clicked.connect(self.help_func)
        self.label_not_enough = self.findChild(QLabel, "label_not_enough")
        self.browse.clicked.connect(self.browsefiles)
        self.generate.clicked.connect(self.generateTables)
        self.back.clicked.connect(self.goBack)
        

        self.txt = ""

    def help_func(self):
        self.label_not_enough.setText("")
        widget.setCurrentWidget(helpexam)

    def browsefiles(self):
        self.label_not_enough.setText("")
        fname = QFileDialog.getOpenFileName(
            self, "Open file", "", "Excel (*.csv *xlsx)"
        )
        self.lineEdit.setText(fname[0])
        self.txt = fname[0]
        # global num_of_branches
        # excelSheet, num_of_branches, allBranches = read_inputt(self.txt)
        # read_sheet(excelSheet, num_of_branches)

    def goBack(self):
        self.label_not_enough.setText("")
        self.lineEdit.setText("")
        widget.setCurrentWidget(mainwindow)

    def msg(self):
        exs2 = exScreen2(self.txt)
        widget.addWidget(exs2)
        widget.setCurrentWidget(exs2)
        self.lineEdit.setText("")
        self.txt = ""
        self.label_2.clear()
        self.label_2.setPixmap(self.pixmap)
        self.browse.setEnabled(True)
        self.generate.setEnabled(True)
        self.back.setEnabled(True)
     
    def generateTables(self):
        if self.txt != "":
            msg = check_data(self.txt)
            if msg:
                self.label_not_enough.setText(msg)
                return

            self.label_not_enough.setText("")
            
            # global __txt
            # __txt=self.txt
            # print(__txt)
            self.thread=QThread()
            self.worker=Worker3(self.txt)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.msg)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
            self.browse.setEnabled(False)
            self.generate.setEnabled(False)
            self.back.setEnabled(False)
            self.label_2.clear()
            self.movie=QMovie("icons\loading4.gif")
            self.label_2.setMovie(self.movie)
            self.movie.start()
            
        else:
            self.label_not_enough.setText("برجاء اختيار ملف")
            return


class exScreen2(QWidget):
    def __init__(self, file):
        super(exScreen2, self).__init__()
        loadUi("./ui/hallsTable.ui", self)

        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.backfromex_fun)
        self.saveBtn = self.findChild(QPushButton, "save")
        self.saveBtn.clicked.connect(self.saveSol)
        
        # khal but
        self.khal = self.findChild(QPushButton, "khal")
        self.khal.clicked.connect(lambda :self.fill(0))
        self.rod = self.findChild(QPushButton, "rod")
        self.rod.clicked.connect(lambda :self.fill(1))

        self.table = self.findChild(QTableWidget,"tableWidget")
        self.table.setColumnCount(4)
        
        self.but1 = self.findChild(QPushButton, "but1")

        self.but2 = self.findChild(QPushButton, "but2")
        self.but3 = self.findChild(QPushButton, "but3")

        # get name of halls
        
  
        self.fill(0)

    def fill(self, index=0):
        global nj, solveIdx
        index = index
        solveIdx = index
        print(index)
        if index==0 :
            self.khal.setStyleSheet("background-color: #F5F8FA;border-radius: 5px;color: black;margin-bottom: 20px;")
            self.rod.setStyleSheet("color:#F5F8FA;margin-bottom: 20px")

            
        else:
            self.rod.setStyleSheet("background-color: #F5F8FA;border-radius: 5px;color: black;margin-bottom: 20px;")
            self.khal.setStyleSheet("color:#F5F8FA;margin-bottom: 20px")

        # table optimal solution
        # DISPLAY(index, num_of_branches)

        vertical = []
        self.toPrint = []
        #toPrint = branch_sol[index].copy()
        self.toPrint = branch_sol[index].copy()
        
        # print(len(self.toPrint))

        # print("\n\n\n")
        
        

        # for i in range(len(self.toPrint) // 3):
        #     vertical.append(self.toPrint[i][0])

        self.but1.clicked.connect(lambda: self.day1(len(self.toPrint) // 3))
        self.but2.clicked.connect(lambda: self.day2(len(self.toPrint) // 3))
        self.but3.clicked.connect(lambda: self.day3(len(self.toPrint) // 3))
        self.day1(len(self.toPrint) // 3)
        
    def day1(self,halls):


        self.but1.setStyleSheet("""
                        background-color: #006aff;
                        border-radius: 6px;
                        """)

        self.but2.setStyleSheet("""
                       background-color: #F5F8FA;
                        border-radius: 6px;
                        """)
        self.but3.setStyleSheet("""
                               background-color: #F5F8FA;
                                border-radius: 6px;
                                """)
        # delete data 
        for i in range(self.table.rowCount()):
            self.table.removeRow(self.table.rowCount() - 1)
        
        
        # set new
        for i in range(-1,halls):
            row = self.table.rowCount()
            self.table.setRowCount(row + 1)
            if i == -1:
                # header 
                item = QtWidgets.QTableWidgetItem(str("القاعه"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 0, item)
                item = QtWidgets.QTableWidgetItem(str("الدفعه"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 1, item)
                item = QtWidgets.QTableWidgetItem(str("من"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 2, item)
                item = QtWidgets.QTableWidgetItem(str("الي"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 3, item)
            else:
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
    
                self.table.setItem(row, 0, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
    
                self.table.setItem(row, 1, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
    
                self.table.setItem(row, 2, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][3]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
    
                self.table.setItem(row, 3, item)
                row += 1
              
    def day2(self,halls):
        self.but2.setStyleSheet("""
                                background-color: #006aff;
                                border-radius: 6px;
                                """)

        self.but1.setStyleSheet("""
                               background-color: #F5F8FA;
                                border-radius: 6px;
                                """)
        self.but3.setStyleSheet("""
                                       background-color: #F5F8FA;
                                        border-radius: 6px;
                                        """)
        # delete data 
        for i in range(self.table.rowCount()):
            self.table.removeRow(self.table.rowCount() - 1)

        # set new
        for i in range(halls-1,(halls*2)):
            row = self.table.rowCount()
            self.table.setRowCount(row + 1)
            if i == halls-1:
                # header 
                item = QtWidgets.QTableWidgetItem(str("القاعه"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 0, item)
                item = QtWidgets.QTableWidgetItem(str("الدفعه"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 1, item)
                item = QtWidgets.QTableWidgetItem(str("من"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 2, item)
                item = QtWidgets.QTableWidgetItem(str("الي"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 3, item)
            else:
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(row, 0, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(row, 1, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(row, 2, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][3]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(row, 3, item)
                row += 1

    def day3(self, halls):

        self.but3.setStyleSheet("""
                        background-color: #006aff;
                        border-radius: 6px;
                        """)

        self.but2.setStyleSheet("""
                       background-color: #F5F8FA;
                        border-radius: 6px;
                        """)
        self.but1.setStyleSheet("""
                               background-color: #F5F8FA;
                                border-radius: 6px;
                                """)
        # delete data 
        for i in range(self.table.rowCount()):
            self.table.removeRow(self.table.rowCount() - 1)

        # set new
        for i in range(halls*2-1, halls*3):
            # print(i, halls * 2 - 1, halls * 3, len(self.toPrint))
            row = self.table.rowCount()
            self.table.setRowCount(row + 1)
            if i == halls*2-1:
                # header 
                item = QtWidgets.QTableWidgetItem(str("القاعه"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 0, item)
                item = QtWidgets.QTableWidgetItem(str("الدفعه"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 1, item)
                item = QtWidgets.QTableWidgetItem(str("من"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 2, item)
                item = QtWidgets.QTableWidgetItem(str("الي"))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(0, 3, item)
            else:
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(row, 0, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(row, 1, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(row, 2, item)
                item = QtWidgets.QTableWidgetItem(str(self.toPrint[i][3]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                self.table.setItem(row, 3, item)
                row += 1
    def backfromex_fun(self):
        widget.setCurrentWidget(exscreen1)
    def saveSol(self):
        ok = output_the_distribution(branch_sol.copy())
        if not ok:
            QMessageBox.about(self, "", "لا يمكن تنزيل الملف اثناء تشغيله")


class invHelp(QWidget):
    def __init__(self):
        super(invHelp, self).__init__()
        loadUi("./ui/helpInv.ui", self)
        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.back_func)
        self.save = self.findChild(QPushButton, "save")
        self.save.clicked.connect(self.save_func)

    def back_func(self):
        widget.setCurrentWidget(invscreen1)

    def save_func(self):
        ok = create_observers_template()
        if not ok:
            QMessageBox.about(self, "", "لا يمكن تنزيل الملف اثناء تشغيله")


class examHelp(QWidget):
    def __init__(self):
        super(examHelp, self).__init__()
        loadUi("./ui/helpEx.ui", self)
        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.back_func)
        self.save = self.findChild(QPushButton, "save")
        self.save.clicked.connect(self.save_func)

    def back_func(self):
        widget.setCurrentWidget(exscreen1)

    def save_func(self):
        ok = create_halls_template()
        if not ok:
            QMessageBox.about(self, "", "لا يمكن تنزيل الملف اثناء تشغيله")


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
widget.setMinimumWidth(1200)
widget.setMinimumHeight(850)
widget.move(300, 0)
widget.show()
sys.exit(app.exec_())
