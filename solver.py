from distutils.command.build import build
from college import Branch,Hall
from groups_input import group
from arabic_reshaper import reshape

mem, mem2, OO = dict(), dict(), int(1e18)
wrongForBuild, wrongForFloor, wrongForHall = int(1e6), int(1e3), 1
toPrint = []

def dp(idx, msk, g, h, l)->int:
    if (idx == len(h)):
        if msk != ((1 << len(g)) - 1): return OO
        else: return 0
    
    if (idx, msk) in mem: return mem[(idx, msk)]

    mem[(idx, msk)] = OO

    for i in range(len(g)):
        if msk & (1 << i): continue
        if (i, idx) not in mem2: 
            sm, j, weight = h[idx].volume, idx + 1, 0
            while j < len(h) and sm < group[g[i]].volume:
                sm += h[j].volume
                if j // l != (j - 1) // l:
                    weight = OO
                    break
                if h[j].buildNum != h[j - 1].buildNum:
                    weight += wrongForBuild
                    j += 1
                    continue
                if h[j].floorNum != h[j - 1].floorNum:
                    weight += wrongForFloor
                    j += 1
                    continue
                weight += wrongForHall
                j += 1
            if sm < group[g[i]].volume: weight = OO
            mem2[(i, idx)] = (weight, j)

        wgt, jj = mem2[(i, idx)][0], mem2[(i, idx)][1]
        if wgt == OO: continue
        mem[(idx, msk)] = min(mem[(idx, msk)], wgt + dp(jj, msk | (1 << i), g, h, l), OO)
    
    mem[(idx, msk)] = min(mem[(idx, msk)], dp(idx + 1, msk, g, h, l), OO)
    return mem[(idx, msk)]


def buildDp(idx, msk, g, h, l)->None:
    if idx == len(h): return
    
    optimal = dp(idx, msk, g, h, l)

    for i in range(len(g)):
        if msk & (1 << i): continue

        wgt, jj = mem2[(i, idx)][0], mem2[(i, idx)][1]
        if wgt == OO: continue
   
        if (wgt + dp(jj, msk | (1 << i), g, h, l) == optimal):
            sm, j, initial = 0, idx, group[g[i]]._from
            while j < len(h) and sm < group[g[i]].volume:
                toPrint.append((h[j].name, group[g[i]].name, initial, min(initial + h[j].volume - 1, group[g[i]].to)))
                sm += h[j].volume
                initial += h[j].volume
                j += 1
            buildDp(j, msk | (1 << i), g, h, l)
            return
    
    toPrint.append((h[idx].name, 'فارغه', '       ---', '---'))
    buildDp(idx + 1, msk, g, h, l)
    return

def solve(branch :Branch):
    
    groups = branch.groupsInBranch.copy()
    allHalls = branch.hallsInBranch.copy() + branch.hallsInBranch.copy() + branch.hallsInBranch.copy()
    l = len(allHalls) // 3
    
    mem.clear()
    mem2.clear()

    if dp(0, 0, groups, allHalls, l) == OO:
        return []
    
    toPrint.clear()
    buildDp(0, 0, groups, allHalls, l)
    return toPrint.copy()








    ### version 2

    # print("1. Optimal Solution")
    # print("2. Test")

    # choice = 1
    # if choice == 1:
    #     toPrint.clear()
    #     buildDp(0, 0, groups, allHalls, l)
    #     return

    # while choice.isnumeric() == False or int(choice) < 1 or int(choice) > 2:
    #     choice = input("Enter valid number: ")
    # choice = int(choice)

    # for i in range(len(toPrint)):
    #     if i % l == 0:
    #         print('\n\n-----------------------------------------------------\n\n')
    #         print(f"Day {i // l + 1}.")
    #     hall, gro, _from, to = toPrint[i][0], toPrint[i][1], toPrint[i][2], toPrint[i][3]
    #     print(f"{hall}  {reshape(gro)[::-1]} {_from}    {to}")
    # print("\n\n==========================================================\n\n")

    # mem.clear()
    # toPrint.clear()

    # choice = input("Enter The Number of Dayes which you need to build: ")
    # while choice.isnumeric() == False or int(choice) < 1 or int(choice) > 3:
    #     choice = input("Enter valid number: ")
    # choice = int(choice)

    # choice = 2

    # if choice == 1:
    #     print('1')
    #     d1, d2 = list([0]), list([1,2,3, 4])

        # choice = input("Enter The Number of groups in that Day: ")
        # while choice.isnumeric() == False or int(choice) < 1 or int(choice) > len(groups):
        #     choice = input("Enter valid number: ")
        # choice = int(choice)

        # for i in range(choice):
        #     print('\n\n-------------------\n\n')
        #     for j in range(len(groups)):
        #         print(j + 1, '. ', reshape(group[groups[j]].name)[::-1])
        #     print('\n\n-------------------\n\n')
            # g = input(f"Choose The Group: ")
            # while g.isnumeric() == False or int(g) < 1 or int(g) > len(groups):
            #     g = input("Enter valid number: ")
            # g = int(g)
            # d1.append(groups[g - 1])
            # groups.pop(g - 1)
        # d2 = groups

    #     h1 = branch.hallsInBranch.copy()
    #     h2 = h1 + branch.hallsInBranch.copy()

    #     if dp(0, 0, d1, h1, l) == OO:
    #         print("NO Valid Option")
    #         return
    #     mem.clear()
    #     if dp(0, 0, d2, h2, l) == OO:
    #         print("NO Valid Option")
    #         return
    #     mem.clear()
    #     buildDp(0, 0, d1, h1, l)
    #     mem.clear()
    #     buildDp(0, 0, d2, h2, l)

    #     for i in range(len(toPrint)):
    #         if i % l == 0:
    #             print('\n\n-----------------------------------------------------\n\n')
    #             print(f"Day {i // l + 1}.")
    #         hall, gro, _from, to = toPrint[i][0], toPrint[i][1], toPrint[i][2], toPrint[i][3]
    #         print(f"{hall}  {reshape(gro)[::-1]} {_from}    {to}")
    #     print("\n\n==========================================================\n\n")  
    
    # elif choice == 2:
    #     print('2')
    #     d1, d2, d3 = list([0]), list([4]), list([1, 2, 3])

        # choice = input("Enter The Number of groups in that Day: ")
        # while choice.isnumeric() == False or int(choice) < 1 or int(choice) > len(groups):
        #     choice = input("Enter valid number: ")
        # choice = int(choice)

        # for i in range(choice):
        #     print('\n\n-------------------\n\n')
        #     for j in range(len(groups)):
        #         print(j + 1, '. ', reshape(group[groups[j]].name)[::-1])
        #     print('\n\n-------------------\n\n')
            # g = input(f"Choose The Group: ")
            # while g.isnumeric() == False or int(g) < 1 or int(g) > len(groups):
            #     g = input("Enter valid number: ")
            # g = int(g)
            # d1.append(groups[g - 1])
            # groups.pop(g - 1)
        # d2 = groups

        # h = branch.hallsInBranch.copy()

        # if dp(0, 0, d1, h, l) == OO:
        #     print("NO Valid Option")
        #     return
        # mem.clear()
        # if dp(0, 0, d2, h, l) == OO:
        #     print("NO Valid Option")
        #     return
        # mem.clear()
        # if dp(0, 0, d3, h, l) == OO:
        #     print("NO Valid Option")
        #     return
        # mem.clear()
        # buildDp(0, 0, d1, h, l)
        # mem.clear()
        # buildDp(0, 0, d2, h, l)
        # mem.clear()
        # buildDp(0, 0, d3, h, l)

        # for i in range(len(toPrint)):
        #     if i % l == 0:
        #         print('\n\n-----------------------------------------------------\n\n')
        #         print(f"Day {i // l + 1}.")
        #     hall, gro, _from, to = toPrint[i][0], toPrint[i][1], toPrint[i][2], toPrint[i][3]
        #     print(f"{hall}  {reshape(gro)[::-1]} {_from}    {to}")
        # print("\n\n==========================================================\n\n")  
