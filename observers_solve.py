from cmath import nan
from operator import indexOf
from pickle import GLOBAL
from observers_data import *
from college import *
import math
from datetime import date

import win32com.client as client
from tabulate import tabulate
from os import startfile
from pretty_html_table import build_table

colDayBranch=[{},{},{}]

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
        if len(sheets) != 3:
            print(len(sheets))
            return 0
    except:
        print(3)
        return False
    dataframe1 = allExcelFile.parse(sheets[0])
    col = [
        "الاسم",
        "المسمى الوظيفى",
        "مكان العمل",
        "المبنى",
        "البريد الالكتروني",
        "التكليف الحالي",
    ]
    for i in range(50):
        if not i:
            col.append(" ")
            col.append(" ")
        else:
            col.append(f"يوم {i} وقت")
            col.append(f"يوم {i}")
    observser_data_lst.append(col)
    ok = True
    values = []
    for i in range(6):
        values.append(dataframe1.columns[i])
    ok &= values == ["nameNN", "nik", "job", "place", "email", "num"]
    if not ok:
        return False
    for index, rows in dataframe1.iterrows():
        my_list = rows.values.tolist()
        observser_data_lst.append(my_list)
    for x in observser_data_lst:
        if x == observser_data_lst[0]:
            continue
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
        # print(temp)
        days.append(temp)
    # print(day)
    day = sorted(day, key=srt)
    for x in day:
        if x not in daynumber.keys():
            cnt += 1
            daynumber[x] = cnt
    for i in range(len(days)):
        days[i] = ExamDay(*days[i])
    excel=pd.ExcelFile("hallsWithAllData.xlsx")
    for i in range(len(excel.sheet_names)):
        dataframe=excel.parse(excel.sheet_names[i])
        print (dataframe)
        for ind,row in dataframe.iterrows():
            if(row[1]!="فارغه"):
                if row[1] not in colDayBranch[0].keys():
                    colDayBranch[0][row[1]]=[]
                colDayBranch[0][row[1]].append(Hall(i,row[-1],row[-2],row[-3],row[0]))
            if(row[4]!="فارغه"):
                if row[4] not in colDayBranch[1].keys():
                    colDayBranch[1][row[4]]=[]
                colDayBranch[1][row[4]].append(Hall(i,row[-1],row[-2],row[-3],row[0]))
            if(row[7]!="فارغه"):
                if row[7] not in colDayBranch[2].keys():
                    colDayBranch[2][row[7]]=[]
                colDayBranch[2][row[7]].append(Hall(i,row[-1],row[-2],row[-3],row[0]))
    # days.clear()
    print(colDayBranch)
    colDayBranch[0]=collageDay(colDayBranch[0])
    colDayBranch[1]=collageDay(colDayBranch[1])
    colDayBranch[2]=collageDay(colDayBranch[2])
    return True


# these two lists must be cleared and have the data from excel sheeets before start the process
# then pass these lists as arguements to function => process_exam_day(exam_day_input,collage_day_input)
# collage_day_input = [
#     collageDay(
#         {
#             "اعدادي هندسه": [Hall(0, 1, 1, 75, "sb4-1"), Hall(0, 2, 2, 55, "sb7-1")],
#         }
#     ),
#     collageDay(
#         {
#             "اولي اتصالات": [Hall(0, 1, 1, 25, "sb4-1"), Hall(0, 2, 2, 55, "sb7-1")],
#             "تالته حاسبات": [Hall(1, 1, 1, 25, "sb4-1"), Hall(1, 2, 2, 55, "sb7-1")],
#         }
#     ),
#     collageDay(
#         {
#             "رابعه حاسبات": [Hall(1, 1, 1, 25, "sb4-1"), Hall(1, 2, 2, 55, "sb7-1")],
#         }
#     ),
# ]colday is up their ready for use
WeekDays = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]
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
            # print(cur_day.date)
            # print(day_name)
            # print(visited_days.items())
            # print(taken_collge_pairs.items())
            ok = False
            for j in range(len(collage_days)):
                if j in taken_collge_pairs.keys():
                    continue
                check = 1
                # print(exam_days[i].study_class_list)
                # print(collage_days[j].hall_class_map.keys())
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
            # print(ok)
            if not ok:
                return False
        # print(f"this is idx= {collge_day_idx}")
        my_data = {}

        for cur_class in cur_day.study_class_list:
            if cur_class not in collage_days[collge_day_idx].hall_class_map.keys():
                return False
            for hall in collage_days[collge_day_idx].hall_class_map[cur_class]:
                if hall.branchNum in my_data.keys():
                    my_data[hall.branchNum].floor.add(hall.floorNum)
                    my_data[hall.branchNum].building.add(hall.buildNum)
                    my_data[hall.branchNum].observers += observers_on_volume(
                        hall.volume, 14
                    )
                else:
                    tmp = brachDayTasks()
                    tmp.floor.add(hall.floorNum)
                    tmp.building.add(hall.buildNum)
                    tmp.observers = observers_on_volume(hall.volume, 14)
                    my_data[hall.branchNum] = tmp
                # for every 14 student having an observer
        for key, val in my_data.items():
            examDays.append( Day(
                cur_day.date,
                val.observers,
                len(val.floor),
                len(val.building),
                road_el_farag if key else khalafawy,
            ))
            # print(i, key, val.observers)
    return True


def observers_on_volume(volume, size):
    return (volume + size - 1) // size


def email_content():
    dic = {
        "اليوم": [],
        "التاريخ": [],
        "حضور الساعة": [],
        "مكان اللجان": [],
    }
    days = ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس"]
    dates = ["20/10/2022", "21/10/2022", "22/10/2022", "23/10/2022", "24/10/2022", "25/10/2022"]
    hours = ["9:15", "9:15", "9:15", "9:15", "9:15", "9:15"]
    places = ["روض الفرج", "روض الفرج", "روض الفرج", "روض الفرج", "روض الفرج", "روض الفرج"]

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


def send_email(address, name, section, month, year):
    outlook = client.Dispatch('outlook.application')  # create a Outlook instance
    mail = outlook.CreateItem(0)  # create Mail Message item
    mail.To = address
    mail.Subject = 'تكليف ملاحظة لجان الامتحانات'
    mail.HTMLBody = f"""
        <!DOCTYPE html>
        <html dir="rtl">
            <head>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1>تكليف ملاحظة لجان الامتحانات {month} {year}</h1>
                <table style="border-collapse: collapse;border-spacing: 0; font-size:150%">
                    <thead>
                        <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">السيد</th>
                        <th style="padding: 10px 20px;border: 1px solid #000;">{name}</th>
                        <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">قسم</th>
                        <th style="padding: 10px 20px;border: 1px solid #000;">{section}</th>
                    </thead>
                </table>
                <p style="font-size:150%;">تحية طيبة وبعد....</p>
                <p style="font-size:150%;">تكليف بالحضور لملاحظة لجان امتحانات  دور {month} لعام {year} فى الايام والمواعيد التالية :</p>
                <div>
                    {email_content()}
                </div>
                <table style="border-collapse: collapse;border-spacing: 0; font-size:150%">
                    <thead>
                        <th style="padding: 10px 20px;border: 1px solid #000;">إجمالي عدد أيام الملاحظة</th>
                        <th style="padding: 10px 20px;border: 1px solid #000; background-color:rgb(7, 105, 105); color :white">6</th>
                    </thead>
                </table>
            </body>
        </html>

"""
    startfile("outlook.exe")
    mail.send

# شيل كل ده
# read_input("observers_data_input.xlsx")
# ok = process_exam_day(days, collage_day_input)
# if not ok:
#     print(arabic("البيانات اللى انت حاطتها ف الجدول مش بتتماشى مع المطلوب ، روح بص على جدول القاعات والجدول اللى انت عامله واتاكد ان مفيش فرقة مش بتنزل فاليوم ده وانت منزلها"))
# else:
#     ok &= process(monitors, days)
#     if not ok:
#         print("not enough")
#     else:
#         print(ok)
#         for mon in monitors:
#             mon.print_info()
