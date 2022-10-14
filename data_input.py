import pandas as pd
from arabic_reshaper import *
from observers_data import arabic

branch_name = dict()                    # to get the branch name with branch index
branch_index = dict()                   # to get branch index with branch name
branch = []
name_and_volume_of_halls = []           # name and volume of the halls in [branch][build][floor]
num_of_floors = []                      # number of floors in [branch][build]
num_of_builds = []                      # number of builds in [branch]
dataframes = []

def validInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def validStr(s):
    return isinstance(s, str)

def clearAll()->None:
    branch_name.clear()
    branch_index.clear()               
    branch.clear()
    name_and_volume_of_halls.clear()          
    num_of_floors.clear()                      
    num_of_builds.clear()                    
    dataframes.clear()
 
def read_inputt(filename):
    clearAll()
    excelSheet = pd.ExcelFile(filename)
    allBranches = excelSheet.sheet_names        # get the name of all branches in the input sheet
    allBranches.pop(0)                          # excepting the classes tab

    for i in range(len(allBranches)):
        # if (not (allBranches[i][0] >= 'A' and allBranches[i][0] <= 'z')):
        #     allBranches[i] =allBranches[i]
        
        # map branch name to branch index and vice versa
        branch_name[i] = allBranches[i]
        branch_index[allBranches[i]] = i

    num_of_branches = len(allBranches)
    
    for i in range(num_of_branches):
        name_and_volume_of_halls.append([])
        num_of_floors.append([])
        num_of_builds.append(0)
        sheet = excelSheet.parse(excelSheet.sheet_names[i + 1])
        ls = []

        for index, rows in sheet.iterrows():
            hall = rows.values.tolist()

            if not validStr(hall[0]) and not validInt(hall[1]) and not validInt(hall[2]) and not validInt(hall[3]):
                continue

            ls.append(hall)
            hall[1] = int(hall[1])      # volume
            hall[2] = int(hall[2])      # build number
            hall[3] = int(hall[3])      # floor number

            while len(name_and_volume_of_halls[i]) <= hall[2]:
                name_and_volume_of_halls[i].append([])
                num_of_floors[i].append(0)
            while len(name_and_volume_of_halls[i][hall[2]]) <= hall[3]:
                name_and_volume_of_halls[i][hall[2]].append([])
            name_and_volume_of_halls[i][hall[2]][hall[3]].append((hall[0], hall[1]))
            num_of_builds[i] = max(num_of_builds[i], hall[2] + 1)
            num_of_floors[i][hall[2]] = max(num_of_floors[i][hall[2]], hall[3] + 1)
        dataframes.append(ls)

    return (excelSheet, num_of_branches, allBranches)

def check_data(fileName):
    excelSheet = pd.ExcelFile(fileName)
    worksheets = excelSheet.sheet_names
    
    if len(worksheets) < 2: 
        return False

    for i in range(1, len(worksheets)):
        sheet = excelSheet.parse(worksheets[i])
        header = []

        for p, v in enumerate(sheet.keys()):
            header.append(reshape(v)[::-1])
        if sorted(header) != sorted([arabic('اسم القاعه'), arabic('السعه'), arabic('رقم المبني'), arabic('رقم الدور')]):
            return False
        
        for index, rows in sheet.iterrows():
            hall, c = rows.values.tolist(), 0
            c += (not validStr(hall[0]))
            c += (not validInt(hall[1]))
            c += (not validInt(hall[2]))
            c += (not validInt(hall[3]))
            if c == 4 or c == 0: continue
            else: return False


    sheet = excelSheet.parse(worksheets[0])
    header = []

    for p, v in enumerate(sheet.keys()):
        header.append(reshape(v)[::-1])
    if sorted(header) != sorted([arabic('اسم الدفعه'), arabic('الفرع'), arabic('عدد الطلاب'), arabic('من'), arabic('الي')]):
        return False

    for index, rows in sheet.iterrows():
        g, c = rows.values.tolist(), 0
        c += (not validStr(g[0]))
        c += (not validStr(g[1]))
        c += (not validInt(g[2]))
        c += (not validInt(g[3]))
        c += (not validInt(g[4]))
        if c == 5 or c == 0: continue
        else: return False

    return True
