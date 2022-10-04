from sre_compile import isstring
import pandas as pd
import arabic_reshaper


def arabic(str):
    return arabic_reshaper.reshape(str)[::-1]


daynumber = {}
khalafawy = "خلفاوي"
road_el_farag = "روض الفرج"
professor = "ا.د"
Adoctor = "ا.م"
doctor = "دكتور"
manager = "رئيس لجنة"
observer = "ملاحظ"
monitor0 = "مراقب دور"
dss = []
mp = {
    "professor": 0,
    professor: 0,
    Adoctor: 1,
    doctor: 2,
    "Adoctor": 1,
    "doctor": 2,
    "other": 3,
    "road el farag": 1,
    "khalafawy": 0,
    road_el_farag: 1,
    khalafawy: 0,
}


class Task(object):
    def __init__(self, day=0, building=0, type=observer):
        self.day = day
        self.building = building
        self.type = type

    def select_day(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def print_info(self):
        print(
            arabic(
                f"اليوم رقم : {self.day} ، التكليف: {self.type} ، المينى:  {self.building}"
            )
        )

    def task_place(self):
        return mp[self.building]

    def work_place(self):
        return self.building


class Monitor:
    def __init__(
        self,
        user_name="unkhown",
        title="employee",
        work_place="college",
        branch="main",
        mail="m@m",
        max_days=0,
    ):
        self.user_name = user_name
        self.title = title
        self.work_place = work_place
        self.branch = branch
        self.max_days = max_days
        self.email=mail
        self.task = []
        self.accupied_days = {}

    def append_task(self, new_task):
        self.task.append(new_task)

    def print_info(self):
        print()
        print(arabic("بيانات المكلف"))
        print(arabic(f"الاسم : {self.user_name.capitalize()} "))
        print(arabic(f" المسمى الوظيفى: {self.title}"))
        print(arabic(f"مكان العمل: {self.work_place} "))
        print(arabic(f"المبنى: {self.branch} "))
        print()
        print(arabic("التكليفات: "))

        for task in self.task:
            task.print_info()
        print()
        print("#" * 20)
        print()

    def push_info(self, dt, cnt):
        numofworkdays = 0
        for i in range(50):
            dt[cnt].append(" ")
            if i in self.accupied_days.keys():
                dt[cnt].append(self.accupied_days[i][1])
                numofworkdays += 1
            else:
                dt[cnt].append(" ")
        dt[cnt][4] = numofworkdays

    def Work_place(self):
        return mp[self.branch]

    def Title(self):
        if self.title in mp.keys():
            return mp[self.title]
        return 3


class Day:
    def __init__(self, day=0, obs=0, monit=0, manager=0, building=0):
        self.day = day
        self.obs = obs
        self.manager = manager
        self.monit = monit
        self.building = building

    def current_day(self):
        x = tuple(self.day.split("/"))
        return daynumber[x]

    def observers(self):
        return self.obs

    def Manager(self):
        return self.manager

    def monitor(self):
        return self.monit

    def work_place(self):
        return self.building


# from exam table
class ExamDay: # str - list of classes have exam => ["e3dady","1st etisalat"] O(days*classes)
    def __init__(self,date, study_class_list):
        self.date = date
        self.study_class_list = study_class_list
    def day_number(self):
        return daynumber[tuple(self.date.split(".")[0].split("/"))]
    def date(self):
        return self.date

#solution from hawara
class collageDay:   # dict of list {"e3dady":[sb4-1,sb4-2]}
    def __init__(self,hall_class_map):
        self.hall_class_map = hall_class_map


class brachDayTasks:
    def __init__(self):
        self.floor  = set()
        self.building = set()
        self.observers = 0  