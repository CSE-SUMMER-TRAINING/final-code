import string
import pandas as pd
from arabic_reshaper import *

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


def read_inputt(filename):
    excelSheet = pd.ExcelFile(filename)
    allBranches = excelSheet.sheet_names        # get the name of all branches in the input sheet
    allBranches.pop()                           # excepting the classes tab

    for i in range(len(allBranches)):
        if (not (allBranches[i][0] >= 'A' and allBranches[i][0] <= 'z')):
            allBranches[i] = reshape(allBranches[i])[::-1]
        
        # map branch name to branch index and vice versa
        branch_name[i] = allBranches[i]

        dataframe = excelSheet.parse(excelSheet.sheet_names[i])
        ls = []
        for ind, row in dataframe.iterrows():
            temp=row.values.tolist()
            ls.append(temp)
        dataframes.append(ls)
        branch_index[allBranches[i]] = i

    num_of_branches = len(allBranches)

    for i in range(num_of_branches):
        name_and_volume_of_halls.append([])
        num_of_floors.append([])
        num_of_builds.append(0)
        sheet = excelSheet.parse(excelSheet.sheet_names[i])
        for index, rows in sheet.iterrows():
            hall = rows.values.tolist()
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

    return (excelSheet, num_of_branches, allBranches)

def check_data(fileName):
    excelSheet = pd.ExcelFile(fileName)
    allBranches = excelSheet.sheet_names
    num_of_branches = len(allBranches)
    
    if num_of_branches < 2: 
        return False

    for i in range(num_of_branches - 1):
        sheet = excelSheet.parse(allBranches[i])
        for index, rows in sheet.iterrows():
            hall = rows.values.tolist()
            if(not validStr(hall[0]) or not validInt(hall[1]) or not validInt(hall[2]) or not validInt(hall[3])):
                return False

    sheet = excelSheet.parse(allBranches[num_of_branches - 1])
    for index, rows in sheet.iterrows():
        g = rows.values.tolist()
        if(not validStr(g[0]) or not validStr(g[1]) or not validInt(g[2]) or not validInt(g[3]) or not validInt(g[4])):
            return False

    return True