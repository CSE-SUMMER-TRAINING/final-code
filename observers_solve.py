from cmath import nan
from operator import indexOf
from pickle import GLOBAL
from tokenize import triple_quoted
from observers_data import *
from college import *
import math
from datetime import date

import win32com.client as client
from tabulate import tabulate
from os import startfile
from pretty_html_table import build_table
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import psutil
import re
colDayBranch=[{},{},{}]
excelhead=[]
is_bransh={}


def process_single_task(day, tsk, monitors, lst):

    if not monitors:
        return False

    try:
        if day.current_day() in monitors[lst[0]].accupied_days.keys():
            return False
    except KeyError:
        pass

    monitors[lst[0]].accupied_days[day.current_day()] = [1, tsk.work_place()]

    if not monitors[lst[0]].max_days:
        lst[1] = lst[0]
        lst[0] = 0

    if not lst[1]:
        return False
    monitors[lst[0]].append_task(tsk)
    monitors[lst[0]].max_days -= 1
    lst[0] = (lst[0] + 1) % lst[1]
    return True


def process(monitors, days):

    monitors = sorted(monitors, key=lambda monitor: monitor.max_days, reverse=True)

    employees = {
        0: {
            2: [[], []],
            3: [[], []],
            1: [[], []],
            0: [[], []],
        },
        1: {
            2: [[], []],
            3: [[], []],
            1: [[], []],
            0: [[], []],
        },
    }
    for monitor in monitors:
        employees[monitor.Work_place()][monitor.Title()][1].append(monitor)

    for i in employees:
        for j in employees[i]:
            employees[i][j][0] = [0, len(employees[i][j][1])]

    done, ok = 1, 0
    for day in days:
        for i in range(1, day.observers() + 1):
            tsk = Task(day.day, day.work_place(), observer)
            ok = process_single_task(
                day,
                tsk,
                employees[tsk.task_place()][3][1],
                employees[tsk.task_place()][3][0],
            )
            if ok:
                continue
            ok = process_single_task(
                day,
                tsk,
                employees[(tsk.task_place() + 1) % 2][3][1],
                employees[(tsk.task_place() + 1) % 2][3][0],
            )
            if ok:
                continue
            return False

        for i in range(1, day.monitor() + 1):

            tsk = Task(day.day, day.work_place(), monitor0)

            ok = process_single_task(
                day,
                tsk,
                employees[tsk.task_place()][2][1],
                employees[tsk.task_place()][2][0],
            )
            if ok:
                continue
            ok = process_single_task(
                day,
                tsk,
                employees[tsk.task_place()][1][1],
                employees[tsk.task_place()][1][0],
            )
            if ok:
                continue
            ok = process_single_task(
                day,
                tsk,
                employees[tsk.task_place()][0][1],
                employees[tsk.task_place()][0][0],
            )
            if ok:
                continue
            return False

        for i in range(1, day.Manager() + 1):

            tsk = Task(day.day, day.work_place(), manager)
            employees[tsk.task_place()][0]
            ok = process_single_task(
                day,
                tsk,
                employees[tsk.task_place()][0][1],
                employees[tsk.task_place()][0][0],
            )
            if ok:
                continue
            ok = process_single_task(
                day,
                tsk,
                employees[tsk.task_place()][1][1],
                employees[tsk.task_place()][1][0],
            )
            if ok:
                continue

            ok = process_single_task(
                day,
                tsk,
                employees[tsk.task_place()][2][1],
                employees[tsk.task_place()][2][0],
            )
            if ok:
                continue
            return False

        monitors = []
        for i in employees:
            for j in employees[i]:
                for k in employees[i][j][1]:
                    monitors.append(k)
    return True


monitors, days, observser_data_lst = [], [], []


def read_input(exel_name):
    monitors.clear()
    days.clear()
    excelhead.clear()
    observser_data_lst.clear()
    colDayBranch.clear()
    examDays.clear()
    colDayBranch.append({})
    colDayBranch.append({})
    colDayBranch.append({})
    # check weather the sheet name exist
    try:
        allExcelFile = pd.ExcelFile(exel_name)
        sheets = allExcelFile.sheet_names
        if len(sheets) != 2:
            return "الملف غير مطابق للمواصفات يجب ان يحتوي علي اثنين شيت واحد للمراقبين و الاخر لجدول الامتحانات"

    except:
        return "الملف غير قابل للفتح"
    dataframe1 = allExcelFile.parse(sheets[0])
    col = [
        "الاسم",
        "المسمى الوظيفى",
        "مكان العمل",
        "المبنى",
        "البريد الالكتروني",
        "التكليف الحالي",
    ]
    excelhead.append(col.copy())
    excelhead.append(col.copy())
    excelhead.append(col.copy())
    ok = True
    values = []
    if(len(dataframe1.columns)!=6):return "يجب ان يكون الشيت الاول من 6 اعمدة"
    for i in range(6):        
        values.append(dataframe1.columns[i])
    ok &= values == ["الاسم", "المسمى الوظيفى", "مكان العمل", "المبنى", "البريد الالكتروني", "التكليف الحالي"]
    if not ok:
        return "اسماء الاعمدة غير صحيحة"
    for index, rows in dataframe1.iterrows():
        my_list = rows.values.tolist()
        observser_data_lst.append(my_list)
    for x in observser_data_lst:
        if x[3]!= khalafawy and x[3]!= road_el_farag:
            return "البيانات المدخلة تحتوى على قيم غير معروفة فى خانة المبنى،القيم المتاحة: خلفاوي، روض الفرج"
        monitors.append(Monitor(*x))

    def srt(elem):
        return (elem[2], elem[1], elem[0])

    dataframe2 = allExcelFile.parse(sheets[1])
    day = []
    cnt = 0
    for x, y in dataframe2.items():
        if len(x.split(".")[0].split("/")) == 1:
            continue
        day.append(tuple(x.split(".")[0].split("/")))
        removeNAN = y.values.tolist()
        newlist = []
        temp = []
        for a in removeNAN:
            if not pd.isnull(a):
                newlist.append(a)
        temp.append(newlist)
        temp.insert(0, x.split(".")[0])
        days.append(temp)
    day = sorted(day, key=srt)
    for x in day:
        if x not in daynumber.keys():
            cnt += 1
            daynumber[x] = cnt
    for i in range(len(days)):
        days[i] = ExamDay(*days[i])
    try:
        excel=pd.ExcelFile("hallsWithAllData.xlsx")
    except:
        return "يجب تشغيل جزء القاعات قبل هذا الجزء"
    br=0
    ok=0
    while 1:
        try:
            excel=pd.ExcelFile(f"hallsWithAllData{br}.xlsx")
        except:
            break
        excel=pd.ExcelFile(f"hallsWithAllData{br}.xlsx")
        for i in range(len(excel.sheet_names)-1):
            dataframe=excel.parse(excel.sheet_names[i])
            is_bransh[excel.sheet_names[i]]=True
            for ind,row in dataframe.iterrows():
                if(ind==0):continue
                if(row[1]!="فارغه"):
                    if row[1] not in colDayBranch[0].keys():
                        colDayBranch[0][row[1]]=[]
                    print(row[3],row[2])
                    colDayBranch[0][row[1]].append((Hall(br,row[-1],row[-2],row[-3],row[0]),int(row[3])-int(row[2])+1))
                if(row[4]!="فارغه"):
                    if row[4] not in colDayBranch[1].keys():
                        colDayBranch[1][row[4]]=[]
                    colDayBranch[1][row[4]].append((Hall(br,row[-1],row[-2],row[-3],row[0]),int(row[6])-int(row[5])+1))
                if(row[7]!="فارغه"):
                    if row[7] not in colDayBranch[2].keys():
                        colDayBranch[2][row[7]]=[]
                    colDayBranch[2][row[7]].append((Hall(br,row[-1],row[-2],row[-3],row[0]),int(row[9])-int(row[8])+1))
        br+=1
        if br==int(excel.sheet_names[1]):
            ok=1
            break
    if(not ok):
        return "يجب تنزيل القاعات لكل الفروع قبل تشغيل جزء الملاحظين"
    seen = set()
    seen_add = seen.add
    res= [x for x in day if not (x in seen or seen_add(x))]
    for i in res:
        x=''
        for ele in i:
            x = x + str(ele) + '/'
        y=x.split("/")
        y.pop()
        dd, mm, yy = y
        x=x[:-1:]
        day_name = date(int(yy), int(mm), int(dd)).strftime("%A")
        excelhead[0].append(x)
        excelhead[0].append(x)
        excelhead[1].append(arabicWeekDays[day_name])
        excelhead[1].append(arabicWeekDays[day_name])
        excelhead[2].append("الساعة")
        excelhead[2].append("المكان")

    colDayBranch[0]=collageDay(colDayBranch[0])
    colDayBranch[1]=collageDay(colDayBranch[1])
    colDayBranch[2]=collageDay(colDayBranch[2])
    return 0


WeekDays = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]
arabicWeekDays = {
    "Saturday" :'السبت',
    "Sunday":'الاحد',
    "Monday":'الاثنين',
    "Tuesday":"الثلاثاء",
    "Wednesday":" الاربع",
    "Thursday":"الخميس",
    "Friday":"الجمعة",
}
examDays=[]
def sync_day(dy):
    if dy == "Friday":
        return "Friday"
    return WeekDays[(WeekDays.index(dy) + 3) % 6]


def process_exam_day(exam_days, collage_days):
    visited_days = {}
    taken_collge_pairs = {}

    for i in range(len(exam_days)):
        cur_day = exam_days[i]
        dd, mm, yy = cur_day.date.split("/")
        day_name = date(int(yy), int(mm), int(dd)).strftime("%A")
        collge_day_idx = 6
        if day_name in visited_days.keys():
            collge_day_idx = visited_days[day_name]
        else:
            ok = False
            for j in range(len(collage_days)):
                if j in taken_collge_pairs.keys():
                    continue
                check = 1
                for study_class in exam_days[i].study_class_list:
                    if study_class in collage_days[j].hall_class_map.keys():
                        continue
                    check = 0
                if check:
                    ok = True
                    collge_day_idx = j
                    visited_days[day_name] = visited_days[sync_day(day_name)] = j
                    taken_collge_pairs[j] = True
                    break
            if not ok:
                return False
        my_data = {}

        for cur_class in cur_day.study_class_list:
            if cur_class not in collage_days[collge_day_idx].hall_class_map.keys():
                return False
            for hall in collage_days[collge_day_idx].hall_class_map[cur_class]:
                if hall[0].branchNum in my_data.keys():
                    my_data[hall[0].branchNum].floor.add(hall[0].floorNum)
                    my_data[hall[0].branchNum].building.add(hall[0].buildNum)
                    my_data[hall[0].branchNum].observers += observers_on_volume(
                        hall[0].volume, 14
                    )
                else:
                    tmp = brachDayTasks()
                    tmp.floor.add(hall[0].floorNum)
                    tmp.building.add(hall[0].buildNum)
                    tmp.observers = observers_on_volume(hall[1], 14)
                    my_data[hall[0].branchNum] = tmp
        for key, val in my_data.items():
            examDays.append( Day(
                cur_day.date,
                val.observers,
                len(val.floor),
                len(val.building),
                road_el_farag if key else khalafawy,
            ))
    return True


def observers_on_volume(volume, size):
    return (volume + size - 1)*130 // (size*100)

# days dates hours places
def email_content(days,dates,hours,places):
    dic = {
        "اليوم": [],
        "التاريخ": [],
        "حضور الساعة": [],
        "مكان اللجان": [],
    }
    # days = ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس"]
    # dates = ["20/10/2022", "21/10/2022", "22/10/2022", "23/10/2022", "24/10/2022", "25/10/2022"]
    # hours = ["9:15", "9:15", "9:15", "9:15", "9:15", "9:15"]
    # places = ["روض الفرج", "روض الفرج", "روض الفرج", "روض الفرج", "روض الفرج", "روض الفرج"]

    for a in days:
        dic["اليوم"].append(a)

    for a in dates:
        dic["التاريخ"].append(a)

    for a in hours:
        dic["حضور الساعة"].append(a)

    for a in places:
        dic["مكان اللجان"].append(a)

    df = pd.DataFrame(dic)
    table = build_table(df, "blue_light", text_align='right', font_size="large")
    return table


def send_email(address, name, section, month, year,days,dates,hours,places,no_of_days,ok):
   
    outlook = client.Dispatch('outlook.application')  # create a Outlook instance
    mail = outlook.CreateItem(0)  # create Mail Message item
    mail.To = address
    mail.Subject = 'تكليف ملاحظة لجان الامتحانات'
    mail.HTMLBody = f"""
        <!DOCTYPE html>
        <html dir="rtl">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                <h2>تكليف ملاحظة لجان الامتحانات {month} {year}</h2>
                <table style="border-collapse: collapse;border-spacing: 0; font-size:auto">
                    <thead>
                        <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">السيد</th>
                        <th style="padding: 10px 20px;border: 1px solid #000;">{name}</th>
                        <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">قسم</th>
                        <th style="padding: 10px 20px;border: 1px solid #000;">{section}</th>
                    </thead>
                </table>

                <p style="font-size:120%;">تحية طيبة وبعد....</p>
                <p style="font-size:120%;">تكليف بالحضور لملاحظة لجان امتحانات  دور {month} لعام {year} فى الايام والمواعيد التالية :</p>
                <div>
                    {email_content(days,dates,hours,places)}
                </div>
                <table style="border-collapse: collapse;border-spacing: 0; font-size:auto">
                    <thead>
                        <th style="padding: 10px 20px;border: 1px solid #000;">إجمالي عدد أيام الملاحظة</th>
                        <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">{no_of_days}</th>
                    </thead>
                </table>
                <p style="font-size:120%;font-weight:bold; border-style:dotted;border-width: medium; width:fit-content;border-color:rgb(7, 105, 105);padding:0.5rem;">نظرًا لقرار مجلس الكلية فى حالة تبديل يوم مكان أخر لابد من إيجاد البديل</p>
                <ol style="font-size:120%;font-weight:bold; border-style:dotted;border-width: medium; width:fit-content;border-color:rgb(7, 105, 105);padding:0.5rem 2rem;">
                    <li style="padding:0.5rem;">الحضور بمقر اللجنة قبل بدء الامتحان بنصف ساعة على الأقل</li>
                    <li style="padding:0.5rem;">استلام كراسات الإجابة وتوزيعها على الطلاب قبل بدء الامتحان بخمس دقائق على الأقل</li>
                    <li style="padding:0.5rem;">توزيع أوراق الأسئلة وعدم تدوين اى معلومات عليها أو تبادل الطلاب لها</li>
                    <li style="padding:0.5rem;">جمع كرنيهات الطلاب ومراجعة بياناتها مع البيانات المسجلة على كراسة الإجابة والتوقيع عليها</li>
                    <li style="padding:0.5rem;">مراجعة استمارات الغياب للطلاب الغائبين مع التأكد من توقيع جميع الطلاب الحاضرين فى كشوف الحضور والانصراف</li>
                    <li style="padding:0.5rem;">يمنع الطالب من الخروج من اللجنه قبل نصف مده الامتحان</li>
                    <li style="padding:0.5rem;">عدم توقيع الطالب فى كشوف الانصراف إلا بعد استلام ورقة الإجابة</li>
                    <li style="padding:0.5rem;">إبلاغ رئيس اللجنة عن اى حالة غش أو الشروع فيه أو أى إخلال بنظام الامتحان</li>
                    <li style="padding:0.5rem;">عدم اضافة أي اسم طالب بكشوف الحضور كتابة باليد والالتزام بكشوف الاسماء المدرجه فقط</li>
                    <li style="padding:0.5rem;">الالتزام الكامل بالاجراءات الاحترازيه وارتداء الكمامه مع عدم تداول الادوات الشخصيه داخل اللجان</li>
                  </ol>
                  <div style="font-size: 130%;font-weight:bold;margin-right:40vw;">
                    <p style="padding:0.5rem; background-color:rgb(7, 105, 105); border-radius:20%; width:fit-content; color:white;">إدارة شئون الطلاب</p>
                    <p style="margin:0 auto;"><img src="https://upload.wikimedia.org/wikipedia/ar/e/e9/%D8%B4%D8%B9%D8%A7%D8%B1_%D8%AC%D8%A7%D9%85%D8%B9%D8%A9_%D8%A8%D9%86%D9%87%D8%A7.png" alt="شعار جامعة بنها" width="130vw" height="80vw"></p>
                    <p style="margin:0 auto;">كلية الهندسة بشبرا</p>
                  </div>
                  
            </body>
        </html>
"""
    # check if outlook is open
    if ok == False:
        startfile("outlook.exe")
    mail.send
    

def is_email(address):
    #this is function is used  to validate the email addess using regex
    check1 = re.search("^[A-z0-9\.]+@[A-z0-9]+\.[A-z]+$", address)
    check2 = re.search("^[A-z0-9\.]+@feng.bu.edu.eg$", address)
    
    return check1 or check2
