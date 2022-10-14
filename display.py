from secrets import choice
from xml.etree.ElementTree import tostring
import xlsxwriter
from data_input import *
from solver import buildDp, solve, mem, toPrint
from observers_data import arabic

to_print1 = []
to_print2 = []
to_print3 = []


def DISPLAY(branch_num, num_of_branches):
    choice = branch_num
    solve(branch[choice])
    # output_the_distribution(branch_num)


def options(choice, choice2):
    print_output(choice - 1, choice2)


def print_output(choice1, choice2):
    cnt, R = 1, 2

    # for group in uniqueGroups:
    #     if cnt < choice2:
    #         cnt += 1
    #         continue
    #     print("\n\n")
    #     mem.clear()
    #     buildDp(0, 0, group[0], branch[choice1].hallsInBranch)
    #     to_print1.extend(list(toPrint))
    #     print("\n")
    #     toPrint.clear()
    #     mem.clear()
    #     buildDp(0, 0, group[1], branch[choice1].hallsInBranch)
    #     to_print2.extend(list(toPrint))
    #     print("\n")
    #     toPrint.clear()
    #     mem.clear()
    #     buildDp(0, 0, group[2], branch[choice1].hallsInBranch)
    #     to_print3.extend(list(toPrint))
    #     print("\n")
    #     toPrint.clear()
    #     mem.clear()
        # break

def hasSpace(str):
    return True if ' ' in str else False

def output_the_distribution(choice1):
    name = branch_name[choice1]
    workbook = xlsxwriter.Workbook(f"قاعات {arabic(name)[::-1]}.xlsx")
    if hasSpace(name): name = arabic(branch_name[choice1])
    worksheet = workbook.add_worksheet(name)

    general_format = workbook.add_format()
    general_format.set_align('center')
    general_format.set_text_wrap()
    # general_format.set_border_color('black')

    header_format = workbook.add_format()
    # header_format.set_border_color('black')
    header_format.set_bg_color('red')
    header_format.set_align('center')
    header_format.set_font_size(20)
    header_format.set_text_wrap()
    header_format.set_bold()

    sub_header_format = workbook.add_format()
    # sub_header_format.set_border_color('black')
    sub_header_format.set_align('center')
    sub_header_format.set_bg_color('silver')
    sub_header_format.set_text_wrap()
    sub_header_format.set_font_size(16)

    del_format = workbook.add_format()
    del_format.set_diag_border()

    worksheet.set_column('A:J', 20)
    worksheet.set_column('C:D', 13)
    worksheet.set_column('F:G', 13)
    worksheet.set_column('I:J', 13)

    worksheet.right_to_left()

    worksheet.merge_range(0, 1, 0, 3, 'اليوم الاول', header_format)
    worksheet.merge_range(0, 4, 0, 6, 'اليوم الثاني', header_format)
    worksheet.merge_range(0, 7, 0, 9, 'اليوم الثالث', header_format)
    worksheet.write(1, 0, 'اسم القاعه', header_format)

    worksheet.write(1, 1, 'اسم الدفعه', sub_header_format)
    worksheet.write(1, 4, 'اسم الدفعه', sub_header_format)
    worksheet.write(1, 7, 'اسم الدفعه', sub_header_format)
    worksheet.write(1, 2, 'من', sub_header_format)
    worksheet.write(1, 5, 'من', sub_header_format)
    worksheet.write(1, 8, 'من', sub_header_format)
    worksheet.write(1, 3, 'الي', sub_header_format)
    worksheet.write(1, 6, 'الي', sub_header_format)
    worksheet.write(1, 9, 'الي', sub_header_format)

    cnt, R = 1, 2
    l = len(branch[choice1].hallsInBranch)
    

    for i in range(l):
        worksheet.write(R + i, 0, toPrint[i][0], sub_header_format)
        worksheet.write(R + i, 1, toPrint[i][1], general_format)
        worksheet.write(R + i, 2, toPrint[i][2], general_format)
        worksheet.write(R + i, 3, toPrint[i][3], general_format)

    # to_print2.extend(list(toPrint))

    for i in range(l):
        worksheet.write(R + i, 4, toPrint[i + l][1], general_format)
        worksheet.write(R + i, 5, toPrint[i + l][2], general_format)
        worksheet.write(R + i, 6, toPrint[i + l][3], general_format)

    # to_print3.extend(list(toPrint))

    for i in range(l):
        worksheet.write(R + i, 7, toPrint[i + 2 * l][1], general_format)
        worksheet.write(R + i, 8, toPrint[i + 2 * l][2], general_format)
        worksheet.write(R + i, 9, toPrint[i + 2 * l][3], general_format)
    workbook.close()
    output_the_distribution_with_halls_data(choice1)

def output_the_distribution_with_halls_data(choice1):
    name = branch_name[choice1]
    workbook = xlsxwriter.Workbook(f'hallsWithAllData{choice1}.xlsx')
    if hasSpace(name): name = arabic(branch_name[choice1])
    worksheet = workbook.add_worksheet(name)

    general_format = workbook.add_format()
    general_format.set_align('center')
    general_format.set_text_wrap()
    # general_format.set_border_color('black')

    header_format = workbook.add_format()
    # header_format.set_border_color('black')
    header_format.set_bg_color('red')
    header_format.set_align('center')
    header_format.set_font_size(20)
    header_format.set_text_wrap()
    header_format.set_bold()

    sub_header_format = workbook.add_format()
    # sub_header_format.set_border_color('black')
    sub_header_format.set_align('center')
    sub_header_format.set_bg_color('silver')
    sub_header_format.set_text_wrap()
    sub_header_format.set_font_size(16)

    del_format = workbook.add_format()
    del_format.set_diag_border()

    worksheet.set_column('A:J', 20)
    worksheet.set_column('C:D', 13)
    worksheet.set_column('F:G', 13)
    worksheet.set_column('I:J', 13)

    worksheet.right_to_left()

    worksheet.merge_range(0, 1, 0, 3, 'اليوم الاول', header_format)
    worksheet.merge_range(0, 4, 0, 6, 'اليوم الثاني', header_format)
    worksheet.merge_range(0, 7, 0, 9, 'اليوم الثالث', header_format)
    worksheet.write(1, 0, 'اسم القاعه', header_format)

    worksheet.write(1, 1, 'اسم الدفعه', sub_header_format)
    worksheet.write(1, 4, 'اسم الدفعه', sub_header_format)
    worksheet.write(1, 7, 'اسم الدفعه', sub_header_format)
    worksheet.write(1, 2, 'من', sub_header_format)
    worksheet.write(1, 5, 'من', sub_header_format)
    worksheet.write(1, 8, 'من', sub_header_format)
    worksheet.write(1, 3, 'الي', sub_header_format)
    worksheet.write(1, 6, 'الي', sub_header_format)
    worksheet.write(1, 9, 'الي', sub_header_format)
    worksheet.write(1, 10, 'السعه', sub_header_format)
    worksheet.write(1, 11, 'رقم المبنى', sub_header_format)
    worksheet.write(1, 12, 'رقم الدور', sub_header_format)

    cnt, R = 1, 2

    # print("\n\n")
    # print(len(toPrint))
    # to_print1.extend(list(toPrint))
    l = len(branch[choice1].hallsInBranch)
    

    for i in range(l):
        worksheet.write(R + i, 0, toPrint[i][0], sub_header_format)
        worksheet.write(R + i, 1, toPrint[i][1], general_format)
        worksheet.write(R + i, 2, toPrint[i][2], general_format)
        worksheet.write(R + i, 3, toPrint[i][3], general_format)

    # to_print2.extend(list(toPrint))

    for i in range(l):
        worksheet.write(R + i, 4, toPrint[i + l][1], general_format)
        worksheet.write(R + i, 5, toPrint[i + l][2], general_format)
        worksheet.write(R + i, 6, toPrint[i + l][3], general_format)

    # to_print3.extend(list(toPrint))

    for i in range(l):
        worksheet.write(R + i, 7, toPrint[i + 2 * l][1], general_format)
        worksheet.write(R + i, 8, toPrint[i + 2 * l][2], general_format)
        worksheet.write(R + i, 9, toPrint[i + 2 * l][3], general_format)
    for i in range(l):
        worksheet.write(R + i, 10, dataframes[choice1][i][1], general_format)
        worksheet.write(R + i, 11, dataframes[choice1][i][2], general_format)
        worksheet.write(R + i, 12, dataframes[choice1][i][3], general_format)
    worksheet2 = workbook.add_worksheet(str(len(branch_name)))
    worksheet2.right_to_left()
    workbook.close()
