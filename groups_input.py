import arabic_reshaper
from data_input import  branch_index, branch, validStr, validInt

group = []

class Group:
    def __init__(self, d, v, f, t, brn, s):
        self.id = d
        self.volume = v
        self._from = f
        self.to = t
        self.branchNum = brn
        self.name = s

def read_sheet(excelSheet, num_of_branches):
    global sheet
    sheet = excelSheet.parse(excelSheet.sheet_names[0])

def get_and_store_groups():
    for index, rows in sheet.iterrows():
        g = rows.values.tolist()

        if(not validStr(g[0]) and not validStr(g[1]) and not validInt(g[2]) and not validInt(g[3]) and not validInt(g[4])):
            continue

        g[2] = int(g[2])                                                    # number
        g[3] = int(g[3])                                                    # from
        g[4] = int(g[4])                                                    # to
        # g[0] = arabic_reshaper.reshape(g[0])[::-1]                        # group name
        g[1] = arabic_reshaper.reshape(g[1])[::-1]                          # branch name 
        brn = branch_index[g[1]]
        branch[brn].groupsInBranch.append(len(group))
        group.append(Group(len(group), g[2], g[3], g[4], brn, g[0]))