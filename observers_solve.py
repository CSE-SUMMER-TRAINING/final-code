from cmath import nan
from observers_data import *
from college import *
import math

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
            tsk = Task(day.current_day(), day.work_place(), observer)
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

            tsk = Task(day.current_day(), day.work_place(), monitor0)

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

            tsk = Task(day.current_day(), day.work_place(), manager)
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
    col = ["الاسم", "المسمى الوظيفى", "مكان العمل", "المبنى","البريد الالكتروني", "التكليف الحالي"]
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
        if len(x.split(".")[0].split("/"))==1:
            continue
        day.append(tuple(x.split(".")[0].split("/")))
        removeNAN=y.values.tolist()
        newlist=[]
        temp=[]
        for a in removeNAN:
            if not pd.isnull(a):
                newlist.append(a)
        temp.append(newlist)
        temp.insert(0, x.split(".")[0])
        print(temp)
        days.append(temp)
    print(day)
    day = sorted(day, key=srt)
    for x in day:
        if x not in daynumber.keys():
            cnt += 1
            daynumber[x] = cnt
    for i in range(len(days)):
        days[i] = ExamDay(*days[i])
    # days.clear()
    return True


# these two lists must be cleared and have the data from excel sheeets before start the process
# then pass these lists as arguements to function => process_exam_day(exam_day_input,collage_day_input)
exam_day_input = [
    ExamDay( "12/11/2020", ["e3dady", "1st etisalat"]),
    ExamDay( "14/10/2020", ["e3dady", "1st etisalat"]),
]
collage_day_input = [
    collageDay(
        {
            "اعدادي هندسه": [Hall(0, 1, 1, 75, "sb4-1"),Hall(0, 2, 2, 55, "sb7-1")],
        }
    ),
    collageDay(
        {
            "اولي اتصالات": [Hall(0, 1, 1, 25, "sb4-1"), Hall(0, 2, 2, 55, "sb7-1")],
            "تالته حاسبات": [Hall(1, 1, 1, 25, "sb4-1"), Hall(1, 2, 2, 55, "sb7-1")],
        }
    ),
    collageDay(
        {
            "رابعه حاسبات": [Hall(1, 1, 1, 25, "sb4-1"), Hall(1, 2, 2, 55, "sb7-1")],
        }
    ),
]


def process_exam_day(exam_days, collage_days):
    for i in range(len(exam_days)):
        cur_day=exam_days[i]
        my_data = {}
        collge_day_idx = (cur_day.day_number() - 1) % len(collage_days)
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
                    my_data[hall.branchNum]=tmp
                # for every 14 student having an observer
        for key, val in my_data.items():
            exam_days[i] = Day(
                cur_day.date,
                val.observers,
                len(val.floor),
                len(val.building),
                khalafawy if key else road_el_farag,
            )
            print(i,key,val.observers)
    return True
# نحسب كثافة المراقبين على عدد الطلاب
def observers_on_volume(volume, size):
    return (volume + size - 1) // size


# شيل كل ده
read_input("observers_data_input.xlsx")
ok = process_exam_day(days,collage_day_input)
print(ok)
for i in days:
    print(f"day = {i.day} obs = {i.obs} mon = {i.monit} man = {i.manager} build = {arabic(i.building)}")
# ok &= process(monitors, days)
# if not ok:
#     print("not enough")
# else:
#     print(ok)
#     for mon in monitors:
#         mon.print_info()
