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
        else:
            self.label_not_enough.setText("برجاء اختيار الملف")


current_index = -1
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
            
            data=[(arabic("المكان"),arabic( "الساعة"), arabic("التاريخ"), arabic("اليوم"))]
            for tas in mon.task:
                spliteddate = tas.day.split("/")
                dayy=arabic(mp[date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0]),).weekday()])
                data.append((arabic(tas.building),"9:15",tas.day,dayy))
            if(len(data)==1):continue
            pdf.add_page()
            pdf.image("icons\download.png",90,w=35,h=30)
            pdf.set_font('FreeSerif', size=12)
            pdf.set_fill_color(237, 240, 149)
            pdf.cell(w=195,h=5,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("كلية الهندسة بشبرا"),align="C")
            pdf.ln()
            pdf.cell(w=195,h=5,fill=1,new_x=XPos.RIGHT, new_y=YPos.TOP,txt="2020/2021 "+arabic(" تكليف ملاحظة لجان الامتحانات يناير  "),align="c")
            pdf.ln()
            pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("السيد/ %s                                                                       قسم:%s"%(mon.user_name,mon.work_place)),align="R")
            pdf.ln()
            pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("تحية طيبة وبعد ..."),align="R")
            pdf.ln()
            pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("تكليف بالحضور لملاحظة لجان امتحانات  فى الايام والمواعيد التالية :"),align="R")
            pdf.ln()

            line_height = pdf.font_size * 1.50
            for i in range(len(data)):
                row=data[i]
                for datum in row:
                    if(i==0):
                        pdf.multi_cell(50, line_height,datum,fill=1 , border=1,new_x=XPos.RIGHT, new_y=YPos.TOP)
                    else :pdf.multi_cell(50, line_height, datum, border=1,new_x=XPos.RIGHT, new_y=YPos.TOP)
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
            if len(mon.task) == 0:
            #    self.label_5.setText(f"{mon.user_name} ليس لديه أيّ تكليفات")
               continue
            days = []
            dates = []
            hours = []
            places = []
            for tas in mon.task:
                # print(tas.day," ",tas.building," ",tas.type)
                spliteddate = tas.day.split("/")
                # print(date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0])))
                days.append(
                        mp[
                            date(
                                int(spliteddate[2]),
                                int(spliteddate[1]),
                                int(spliteddate[0]),
                            ).weekday()
                        ]
                )
                dates.append(tas.day)
                hours.append("9:15")
                places.append(tas.building)
            address=mon.email
            name=mon.user_name
            section=mon.branch
            month=11
            year=mon.task[0].day[-4:]
            
            print (f"\n{address}  {name}  {section}  {month}  {year} ")
            print ("days: ",end=" ")
            for i in days:
                print(i,end=" ")
            print ("\ndates: ")
            for i in dates :
                print (i,end=" ")
            
            print("\nhours: ",end=" ")
            for i in hours :
                print(i,end=" ")
            print("\nplaces: ",end=" ")
            for i in places :
                print (i,end=" ")
        #     outlook = client.Dispatch('outlook.application')  # create a Outlook instance
        #     mail = outlook.CreateItem(0)  # create Mail Message item
        #     mail.To = address
        #     mail.Subject = 'تكليف ملاحظة لجان الامتحانات'
        #     mail.HTMLBody = f"""
        #         <!DOCTYPE html>
        #         <html dir="rtl">
        #             <head>
        #                 <meta charset="UTF-8">
        #                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
        #             </head>
        #             <body>
        #                 <h2>تكليف ملاحظة لجان الامتحانات {month} {year}</h2>
        #                 <table style="border-collapse: collapse;border-spacing: 0; font-size:auto">
        #                     <thead>
        #                         <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">السيد</th>
        #                         <th style="padding: 10px 20px;border: 1px solid #000;">{name}</th>
        #                         <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">قسم</th>
        #                         <th style="padding: 10px 20px;border: 1px solid #000;">{section}</th>
        #                     </thead>
        #                 </table>

        #                 <p style="font-size:120%;">تحية طيبة وبعد....</p>
        #                 <p style="font-size:120%;">تكليف بالحضور لملاحظة لجان امتحانات  دور {month} لعام {year} فى الايام والمواعيد التالية :</p>
        #                 <div>
        #                     {email_content(days,dates,hours,places)}
        #                 </div>
        #                 <table style="border-collapse: collapse;border-spacing: 0; font-size:auto">
        #                     <thead>
        #                         <th style="padding: 10px 20px;border: 1px solid #000;">إجمالي عدد أيام الملاحظة</th>
        #                         <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">6</th>
        #                     </thead>
        #                 </table>
        #                 <p style="font-size:120%;font-weight:bold; border-style:dotted;border-width: medium; width:fit-content;border-color:rgb(7, 105, 105);padding:0.5rem;">نظرًا لقرار مجلس الكلية فى حالة تبديل يوم مكان أخر لابد من إيجاد البديل</p>
        #                 <ol style="font-size:120%;font-weight:bold; border-style:dotted;border-width: medium; width:fit-content;border-color:rgb(7, 105, 105);padding:0.5rem 2rem;">
        #                     <li style="padding:0.5rem;">الحضور بمقر اللجنة قبل بدء الامتحان بنصف ساعة على الأقل</li>
        #                     <li style="padding:0.5rem;">استلام كراسات الإجابة وتوزيعها على الطلاب قبل بدء الامتحان بخمس دقائق على الأقل</li>
        #                     <li style="padding:0.5rem;">توزيع أوراق الأسئلة وعدم تدوين اى معلومات عليها أو تبادل الطلاب لها</li>
        #                     <li style="padding:0.5rem;">جمع كرنيهات الطلاب ومراجعة بياناتها مع البيانات المسجلة على كراسة الإجابة والتوقيع عليها</li>
        #                     <li style="padding:0.5rem;">مراجعة استمارات الغياب للطلاب الغائبين مع التأكد من توقيع جميع الطلاب الحاضرين فى كشوف الحضور والانصراف</li>
        #                     <li style="padding:0.5rem;">يمنع الطالب من الخروج من اللجنه قبل نصف مده الامتحان</li>
        #                     <li style="padding:0.5rem;">عدم توقيع الطالب فى كشوف الانصراف إلا بعد استلام ورقة الإجابة</li>
        #                     <li style="padding:0.5rem;">إبلاغ رئيس اللجنة عن اى حالة غش أو الشروع فيه أو أى إخلال بنظام الامتحان</li>
        #                     <li style="padding:0.5rem;">عدم اضافة أي اسم طالب بكشوف الحضور كتابة باليد والالتزام بكشوف الاسماء المدرجه فقط</li>
        #                     <li style="padding:0.5rem;">الالتزام الكامل بالاجراءات الاحترازيه وارتداء الكمامه مع عدم تداول الادوات الشخصيه داخل اللجان</li>
        #                   </ol>
        #                   <div style="font-size: 130%;font-weight:bold;margin-right:40vw;">
        #                     <p style="padding:0.5rem; background-color:rgb(7, 105, 105); border-radius:20%; width:fit-content; color:white;">إدارة شئون الطلاب</p>
        #                     <p style="margin:0 auto;"><img src="https://u...content-available-to-author-only...a.org/wikipedia/ar/e/e9/%D8%B4%D8%B9%D8%A7%D8%B1_%D8%AC%D8%A7%D9%85%D8%B9%D8%A9_%D8%A8%D9%86%D9%87%D8%A7.png" alt="شعار جامعة بنها" width="130vw" height="80vw"></p>
        #                     <p style="margin:0 auto;">كلية الهندسة بشبرا</p>
        #                   </div>
                        
        #             </body>
        #         </html>
        # """
        #     # check if outlook is open
        #     if "outlook.exe" in (i.name() for i in psutil.process_iter()) == False:
        #         startfile("outlook.exe")
        #     mail.send
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

        self.label_name = self.findChild(QLabel, "label_4")
        self.label_dep = self.findChild(QLabel, "label_10")
        self.label_dep0 = self.findChild(QLabel, "label_3")
        self.label_name0 = self.findChild(QLabel, "label_6")
        self.label_ = self.findChild(QLabel, "label_2")
        self.label_5 = self.findChild(QLabel, "label_5")
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
        data=[(arabic("المكان"),arabic( "الساعة"), arabic("التاريخ"), arabic("اليوم"))]
        for tas in mon.task:
            spliteddate = tas.day.split("/")
            dayy=arabic(mp[date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0]),).weekday()])
            data.append((arabic(tas.building),"9:15",tas.day,dayy))
        pdf.add_page()
        pdf.image("icons\download.png",90,w=35,h=30)
        pdf.set_font('FreeSerif', size=12)
        pdf.set_fill_color(237, 240, 149)
        pdf.cell(w=195,h=5,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("كلية الهندسة بشبرا"),align="C")
        pdf.ln()
        pdf.cell(w=195,h=5,fill=1,new_x=XPos.RIGHT, new_y=YPos.TOP,txt="2020/2021 "+arabic(" تكليف ملاحظة لجان الامتحانات يناير  "),align="c")
        pdf.ln()
        pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("السيد/ %s                                                                       قسم:%s"%(mon.user_name,mon.work_place)),align="R")
        pdf.ln()
        pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("تحية طيبة وبعد ..."),align="R")
        pdf.ln()
        pdf.cell(w=195,h=10,new_x=XPos.RIGHT, new_y=YPos.TOP,txt=arabic("تكليف بالحضور لملاحظة لجان امتحانات  فى الايام والمواعيد التالية :"),align="R")
        pdf.ln()

        line_height = pdf.font_size * 1.50
        for i in range(len(data)):
            row=data[i]
            for datum in row:
                if(i==0):
                    pdf.multi_cell(50, line_height,datum,fill=1 , border=1,new_x=XPos.RIGHT, new_y=YPos.TOP)
                else :pdf.multi_cell(50, line_height, datum, border=1,new_x=XPos.RIGHT, new_y=YPos.TOP)
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
        pdf.output('fl.pdf')
        
        try: 
            win32api.ShellExecute(0, "print", 'fl.pdf', None,".",0)
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
            self.label_5.setText("من فضلك اختار شخص")
           
        elif len(monitors[current_index].task) == 0:
            self.label_5.setText(f"{monitors[current_index].user_name} ليس لديه أيّ تكليفات")
            
        else:
            mp={
                0:"الأثنين",
                1:"الثلاثاء",
                2:"الأربعاء",
                3:"الخميس",
                4:"الجمعة",
                5:"السبت",
                6:"الأحد",
            }
            tmplst=monitors[current_index]
            days=[]
            dates=[]
            hours=[]
            places=[]
            for tas in tmplst.task:
                spliteddate=tas.day.split("/")
                days.append(mp[date(int(spliteddate[2]),int(spliteddate[1]),int(spliteddate[0])).weekday()])
                dates.append(tas.day)
                hours.append("9:15")
                places.append(tas.building)

            send_email(tmplst.email,tmplst.user_name,tmplst.branch,11,tmplst.task[0].day[-4:],days,dates,hours,places)
    def download_function(self):
        cnt = 0
        lst = []
        for i in observser_data_lst:
            lst.append(i.copy())
        for mon in monitors:
            mon.push_info(lst, cnt)
            cnt = cnt + 1

        try:
            # print(excelhead)
            dataframeout = pd.DataFrame(lst, columns=excelhead)
            # print(dataframeout)
            dataframeout.to_excel("observer_output.xlsx")
            QMessageBox.about(self, "", "تم التنزيل                   ")
        except:
            QMessageBox.about(
                self, "", "لا يمكن تنزيل الملف اثناء تشغيله"
            )  # needed to be errorbox

    def set_items(self, index):
        # clear table rows
        self.label_5.setText("")
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
        # print(self.combox.currentIndex())
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

        if current_index == 0:
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
        x = tuple(day.split("/"))
        return daynumber[x]
    def changes_function(self, index):
        # load data
        mon = monitors[index]
        i, j, ok = 0, 0, 0
        print("###############################")
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
                print(item.text())
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
            print(mon.accupied_days[ts.current_day()])
        monitors[index] = mon
        QMessageBox.about(self, "", "تم حفظ التغيرات                  ")


class exScreen1(QWidget):
    def __init__(self):

        super(exScreen1, self).__init__()
        loadUi("./ui/screenEx1.ui", self)
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

    def generateTables(self):
        if self.txt != "":
            ok = check_data(self.txt)
            if not ok:
                self.label_not_enough.setText("البيانات المدخلة غير صحيحة")
                return

            self.label_not_enough.setText("")
            # create_halls_template()
            global num_of_branches, allBranches
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
        loadUi("./ui/screenEx2.ui", self)

        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.backfromex_fun)
        self.saveBtn = self.findChild(QPushButton, "save")
        self.saveBtn.clicked.connect(self.saveSol)

        # set tabs of branches
        self.add_tab_widget = QTabWidget(self)
        self.add_tab_widget.move(200, 100)  # position
        self.add_tab_widget.resize(1480, 800)  # size
        # get name of branches
        excelSheet = pd.ExcelFile(file)
        self.listOfBranches = excelSheet.sheet_names
        # groups
        self.groups = pd.read_excel(file, usecols='A')
        self.groups.head()

        self.listOfBranches.pop(0)
        self.listOfFrames = []

        for i in range(len(self.listOfBranches)):
            frame = QFrame(self)
            self.listOfFrames.append(frame)

        for i in range(len(self.listOfBranches)):
            self.add_tab_widget.addTab(self.listOfFrames[i], self.listOfBranches[i])
            # change direction
            # self.add_tab_widget.setTabPosition(QTabWidget.South)
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
                    background: #407991;
                    color: white;
                    border-top-left-radius: 8px;
                    border-top-right-radius: 8px;
                    border:1px solid rgb(197,197,199,255);
                    padding: 10px 30px 10px 24px;
               }
               QTabBar::tab:!selected{
                    font-family: Roboto;
                    font-size: 18px;
                    font: italic;
                    background: #305a6c;
                    color: white;
                    border-top-left-radius: 8px;
                    border-top-right-radius: 8px;
                    border:1px solid rgb(197,197,199,255);
                    padding: 10px 30px 10px 24px;
                }
            """
        )

        self.fill_tabs(0)
        self.add_tab_widget.tabBarClicked.connect(self.fill_tabs)

    def fill_tabs(self, index=0):
        global nj, solveIdx
        index = index
        solveIdx = index
        
        # two tabs for each branch
        self.tabs = QTabWidget(self.listOfFrames[index])

        # table optimal solution
        # DISPLAY(index, num_of_branches)

        vertical = ["  القاعه"]
        toPrint = branch_sol[index].copy()

        for i in range(len(toPrint) // 3):
            # if toPrint[i][0] not in vertical:
            vertical.append(toPrint[i][0])

        table = QTableWidget(len(vertical), 9)

        header = ["الدفعه", "من", "الي", "الدفعه", "من", "الي", "الدفعه", "من", "الي"]
        table.setHorizontalHeaderLabels(header)
        table_ho = table.horizontalHeader()
        for i in range(9):
            table_ho.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        table.setVerticalHeaderLabels(vertical)
        table_ve = table.verticalHeader()
        table_ve.setStyleSheet("font-size:20px;")

        for i in range(3):
            for j in range(len(vertical) - 1):
                item = QtWidgets.QTableWidgetItem(str(toPrint[j][i + 1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                table.setItem(j + 1, i, item)

        for i in range(3):
            for j in range(len(vertical) - 1):
                item = QtWidgets.QTableWidgetItem(
                    str(toPrint[j + len(vertical) - 1][i + 1])
                )
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                table.setItem(j + 1, i + 3, item)

        nj = 2 * len(vertical) - 2
        for i in range(3):
            for j in range(len(vertical) - 1):
                item = QtWidgets.QTableWidgetItem(str(toPrint[j + nj][i + 1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                table.setItem(j + 1, i + 6, item)

        # suggest tab
        self.suggest = QWidget()

        # for day1
        self.but1 = QPushButton("اليوم الاول", self.suggest)
        self.but1.setStyleSheet("""
                QPushButton{
                background-color:#305a6c;
                border-radius:20px;
                width:300px;
                height:80px;
                color:white;
                font-size:20px;
                }
                QPushButton:hover{
                        background-color:#407991;
                }
                """)
        self.but1.clicked.connect(self.day1)
        self.but1.move(1180, 100)
        self.but1.setCursor(Qt.PointingHandCursor)

        # for day 2
        self.but2 = QPushButton("اليوم الثاني", self.suggest)
        self.but2.setStyleSheet("""
                        QPushButton{
                        background-color:#305a6c;
                        border-radius:20px;
                        width:300px;
                        height:80px;
                        color:white;
                        font-size:20px;
                        }
                        QPushButton:hover{
                                background-color:#407991;
                        }

                        """)
        self.but2.move(1180, 200)
        self.but2.clicked.connect(self.day2)
        self.but2.setCursor(Qt.PointingHandCursor)

        # groups area
        self.frame1 = QFrame(self.suggest)
        self.frame1.move(40, 30)

        # choose from label 
        self.labelgroubs = QLabel(self.frame1)
        self.labelgroubs.resize(800, 40)
        self.labelgroubs.move(180, 10)
        self.labelgroubs.setAlignment(QtCore.Qt.AlignCenter)

        # names of groups
        self.checkboxlist = []

        # after saving data for day1 or both
        self.buttonsendall = QPushButton(self.suggest)
        self.buttonsendall.resize(0, 0)
        self.buttonsendall.clicked.connect(self.send)
        self.buttonsendall.setCursor(Qt.PointingHandCursor)

        # return checkboxes not checked
        self.buttonback = QPushButton(self.suggest)
        self.buttonback.resize(0, 0)
        self.buttonback.clicked.connect(self.return_data)
        self.buttonback.setCursor(Qt.PointingHandCursor)

        # get groups
        for i in self.groups.values:
            self.checkboxlist.append(i[0])

        # for each check box
        self.choosegroup = []
        xch = 800
        ych = 100
        for x in range(len(self.checkboxlist)):
            c = QCheckBox(self.frame1)
            c.move(xch, ych)
            c.resize(0, 0)
            c.setStyleSheet("font-size:24px;")
            self.choosegroup.append(c)
            if xch >= 300:
                xch -= 300

            else:
                xch = 800
                ych += 50

        self.button1_send = QPushButton(self.frame1)
        self.button1_send.setStyleSheet("border:none;")
        self.button1_send.move(100, 500)
        self.button2_send = QPushButton(self.frame1)
        self.button2_send.setStyleSheet("border:none;")
        self.button2_send.move(100, 500)

        self.button2_send.setCursor(Qt.PointingHandCursor)
        self.button1_send.setCursor(Qt.PointingHandCursor)

        # frame table by person 
        self.frame2 = QFrame(self.suggest)
        self.frame2.move(40, 30)
        self.frame2.resize(0, 0)
        
        # self.closeframe2btn = QPushButton(self.frame2)
        # self.closeframe2btn.resize(0, 0)
        # self.closeframe2btn.setCursor(Qt.PointingHandCursor)
        # self.closeframe2btn.clicked.connect(self.closeframe2fun)

        self.table_suggest = QTableWidget(self.frame2)
        self.table_suggest.move(5, 30)

        self.tabs.addTab(table, "حل مقترح")
        self.tabs.addTab(self.suggest, "اضافة حل؟")

        # groups choosen
        self.day1list = []
        self.day2list = []

        # return from frame1
        self.backToFrame0 = QPushButton(self.frame1)
        self.backToFrame0.setIcon(QIcon("icons\go-back-arrow.png"))
        self.backToFrame0.setCursor(Qt.PointingHandCursor)
        self.backToFrame0.setStyleSheet("background-color:white;border:none;")
        size = QSize(0, 0)
        self.backToFrame0.resize(0, 0)
        self.backToFrame0.setIconSize(size)
        self.backToFrame0.clicked.connect(self.backToFrame0Function)
        self.backToFrame0.setToolTip("رجوع")
        self.backToFrame0.move(0, 0)

        self.tabs.move(10, 10)  # position
        self.tabs.resize(1450, 700)  # size
        self.tabs.setTabPosition(QTabWidget.South)

        self.tabs.setStyleSheet(
            """QTabWidget::tab-bar
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
                 color: white;
                 background: #407991;
                 border-top-left-radius: 8px;
                 border-top-right-radius: 8px;
                 border:1px solid rgb(197,197,199,255);
                 padding: 10px 30px 10px 24px;
            }
            QTabBar::tab:!selected{
                 font-family: Roboto;
                 font-size: 18px;
                 font: italic;
                color: white;
                 border-top-left-radius: 8px;
                 border-top-right-radius: 8px;          
                 border:1px solid rgb(197,197,199,255);
                 padding: 10px 30px 10px 24px;
                 background: #305a6c;
             }
            """
        )

    def day1(self):
        self.frame1.resize(1200, 800)
        self.button2_send.resize(0, 0)
        self.but1.move(1220, 100)
        self.but1.setStyleSheet("""
                        background-color:#407991;
                        border-radius:20px;
                        color:white;
                        font-size:20px;
                        """)
        self.but2.move(1180, 200)
        self.but2.setStyleSheet("""
                        QPushButton{
                        background-color:#305a6c;
                        border-radius:20px;
                        width:300px;
                        height:80px;
                        color:white;
                        font-size:20px;
                        }
                        QPushButton:hover{
                                background-color:#407991;
                        }
                        """)

        size = QSize(30, 30)
        self.backToFrame0.setIconSize(size)
        self.backToFrame0.resize(50, 30)

        self.labelgroubs.setText("اختار من هذه الدفعات")
        self.labelgroubs.setStyleSheet("font-size:25px;background-color:#e6e6e6;color:#141414;padding:3px;border-radius:10px;")

        # show checkbox
        for i in range(len(self.choosegroup)):
            if self.choosegroup[i].isChecked() != True and self.choosegroup[i].text() not in self.day2list:
                self.choosegroup[i].resize(230, 100)
                self.choosegroup[i].setText(self.checkboxlist[i])
            else:
                if self.choosegroup[i].text() in self.day1list:
                    self.choosegroup[i].resize(230, 100)
                    self.choosegroup[i].setText(self.checkboxlist[i])
                    self.choosegroup[i].setChecked(True)
                else:
                    self.choosegroup[i].resize(0, 0)

        self.button1_send.setText("حفظ لليوم الاول")
        # self.button1_send.move(500, 500)
        self.button1_send.clicked.connect(self.send_data1)
        self.button1_send.resize(200, 40)
        self.button1_send.setStyleSheet("""
        QPushButton {
            border:1px solid #255;
            color:white;
            background-color:#305a6c;
            padding:5px;
            border-radius:10px;
            font-size:17px;
        }
        QPushButton:hover {
            background-color:#407991;
            font-size:18px;
        }
        """)

        self.buttonsendall.move(1200, 400)
        self.buttonsendall.resize(200, 60)
        self.buttonsendall.setText("ارسال ")
        self.buttonsendall.setStyleSheet("""
        QPushButton {
            border:1px solid #255;
            color:white;
            background-color:#305a6c;
            padding:5px;
            border-radius:10px;
            font-size:17px;
        }
        QPushButton:hover {
            background-color:#407991;
            font-size:18px;
        }
        """)

        self.buttonback.move(1200, 500)
        self.buttonback.resize(200, 60)
        self.buttonback.setText("تراجع")
        self.buttonback.setStyleSheet("""
        QPushButton {
            border:1px solid #255;
            color:white;
            background-color:#305a6c;
            padding:5px;
            border-radius:10px;
            font-size:17px;
        }
        QPushButton:hover {
            background-color:#407991;
            font-size:18px;
        }
        """)

    def day2(self):
        self.frame1.resize(1200, 800)
        self.button1_send.resize(0, 0)
        self.but1.move(1180, 100)
        self.but1.setStyleSheet("""
                        QPushButton{
                        background-color:#305a6c;
                        border-radius:20px;
                        width:300px;
                        height:80px;
                        color:white;
                        font-size:20px;
                        }
                        QPushButton:hover{
                                background-color:#407991;
                        }
                        """)
        self.but2.move(1220, 200)
        self.but2.setStyleSheet("""
                        background-color:#407991;
                        border-radius:20px;
                        color:white;
                        font-size:20px;
                        """)
        size = QSize(30, 30)
        self.backToFrame0.setIconSize(size)
        self.backToFrame0.resize(50, 30)

        self.labelgroubs.setText("اختار من هذه الدفعات")
        self.labelgroubs.setStyleSheet("font-size:25px;background-color:#e6e6e6;color:#141414;padding:3px;border-radius:10px;")

        for i in range(len(self.choosegroup)):
            if self.choosegroup[i].isChecked() != True and self.choosegroup[i].text() not in self.day1list:
                self.choosegroup[i].resize(230, 100)
                self.choosegroup[i].setText(self.checkboxlist[i])

            else:
                if self.choosegroup[i].text() in self.day2list:
                    self.choosegroup[i].resize(230, 100)
                    self.choosegroup[i].setText(self.checkboxlist[i])
                    self.choosegroup[i].setChecked(True)
                else:
                    self.choosegroup[i].resize(0, 0)

        self.button2_send.setText("حفظ لليوم الثاني")
        # self.button2_send.move(500, 400)
        self.button2_send.clicked.connect(self.send_data2)
        self.button2_send.resize(200, 40)
        self.button2_send.setStyleSheet("""
        QPushButton {
            border:1px solid #255;
            color:white;
            background-color:#305a6c;
            padding:5px;
            border-radius:10px;
            font-size:17px;
        }
        QPushButton:hover {
            background-color:#407991;
            font-size:18px;
        }
        """)

        self.buttonsendall.move(1200, 400)
        self.buttonsendall.resize(200, 60)
        self.buttonsendall.setText("ارسال ")
        self.buttonsendall.setStyleSheet("""
        QPushButton {
            border:1px solid #255;
            color:white;
            background-color:#305a6c;
            padding:5px;
            border-radius:10px;
            font-size:17px;
        }
        QPushButton:hover {
            background-color:#407991;
            font-size:18px;
        }
        """)

        self.buttonback.move(1200, 500)
        self.buttonback.resize(200, 60)
        self.buttonback.setText("تراجع")
        self.buttonback.setStyleSheet("""
        QPushButton {
            border:1px solid #255;
            color:white;
            background-color:#305a6c;
            padding:5px;
            border-radius:10px;
            font-size:17px;
        }
        QPushButton:hover {
            background-color:#407991;
            font-size:18px;
        }
        """)

    def send(self):
        print(self.day1list)
        print(self.day2list)

        ret = QMessageBox.question(self, 'MessageBox', "هل تريد عرض الجدول",
                                   QMessageBox.Yes | QMessageBox.No)

        if ret == QMessageBox.Yes:
            self.show_table()

        self.return_data()

    def show_table(self):
        # self.frame2.setStyleSheet("background-color:black;")
        self.frame2.resize(1420, 700)
        self.frame2.setStyleSheet("background-color:white;")
        self.table_suggest.resize(1300, 450)
        # self.closeframe2btn.resize(200, 50)
        # self.closeframe2btn.setText("اغلاق")
        # self.closeframe2btn.move(1000, 520)
        # self.closeframe2btn.setStyleSheet("background-color:#305a6c;color:white;")

        # first tab
        DISPLAY(0, num_of_branches)
        # print(toPrint)
        vertical = ["  القاعه"]

        for i in range(len(toPrint)):
            if toPrint[i][0] not in vertical:
                vertical.append(toPrint[i][0])

        self.table_suggest.setColumnCount(9)
        self.table_suggest.setRowCount(len(vertical))

        header = ["الدفعه", "من", "الي", "الدفعه", "من", "الي", "الدفعه", "من", "الي"]
        self.table_suggest.setHorizontalHeaderLabels(header)
        table_ho = self.table_suggest.horizontalHeader()
        for i in range(9):
            table_ho.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        self.table_suggest.setVerticalHeaderLabels(vertical)
        table_ve = self.table_suggest.verticalHeader()
        table_ve.setStyleSheet("font-size:20px;")
        # print(len(toPrint))
        for i in range(3):
            for j in range(len(vertical) - 1):
                item = QtWidgets.QTableWidgetItem(str(toPrint[j][i + 1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_suggest.setItem(j + 1, i, item)

        for i in range(3):
            for j in range(len(vertical) - 1):
                item = QtWidgets.QTableWidgetItem(str(toPrint[j + len(vertical) - 1][i + 1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_suggest.setItem(j + 1, i + 3, item)

        nj = 2 * len(vertical) - 2
        for i in range(3):
            for j in range(len(vertical) - 1):
                item = QtWidgets.QTableWidgetItem(str(toPrint[j + nj][i + 1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_suggest.setItem(j + 1, i + 6, item)

    # def closeframe2fun(self):
    #     self.frame2.resize(0, 0)
    #     self.closeframe2btn.resize(0, 0)
    #     self.table_suggest.resize(0, 0)

    def saveSol(self):
        output_the_distribution(solveIdx, branch_sol[solveIdx].copy())

    def return_data(self):
        for i in range(len(self.choosegroup)):
            self.choosegroup[i].setChecked(False)
            self.choosegroup[i].resize(230, 100)

        self.day2list.clear()
        self.day1list.clear()

    def send_data2(self):

        for i in range(len(self.choosegroup)):
            if self.choosegroup[i].isChecked() == True and self.choosegroup[i].text() not in self.day1list and \
                self.choosegroup[i].text() not in self.day2list:
                self.day2list.append(self.choosegroup[i].text())

        print(self.day2list)

    def send_data1(self):
        for i in range(len(self.choosegroup)):
            if self.choosegroup[i].isChecked() == True and self.choosegroup[i].text() not in self.day2list and \
                self.choosegroup[i].text() not in self.day1list:
                self.day1list.append(self.choosegroup[i].text())
        print(self.day1list)

    def backToFrame0Function(self):
        self.frame1.resize(0, 0)
        self.backToFrame0.resize(0, 0)
        self.but2.move(1180, 200)
        self.but1.move(1180, 100)
        self.but2.setStyleSheet("""
                        QPushButton{
                        background-color:#305a6c;
                        border-radius:20px;
                        width:300px;
                        height:80px;
                        color:white;
                        font-size:20px;
                        }
                        QPushButton:hover{
                                background-color:#407991;
                        }
                        """)
        self.but1.setStyleSheet("""
                        QPushButton{
                        background-color:#305a6c;
                        border-radius:20px;
                        width:300px;
                        height:80px;
                        color:white;
                        font-size:20px;
                        }
                        QPushButton:hover{
                                background-color:#407991;
                        }
                        """)
        self.buttonsendall.resize(0, 0)
        self.buttonback.resize(0, 0)

    def backfromex_fun(self):
        widget.setCurrentWidget(exscreen1)


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
        create_observers_template()


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
        create_halls_template()


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

widget.move(2, 2)
widget.show()
sys.exit(app.exec_())
