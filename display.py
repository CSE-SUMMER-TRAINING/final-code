import xlsxwriter
from data_input import *
from solver import solve

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

def output_the_distribution(sol):
    
    try:
        workbook = xlsxwriter.Workbook("القاعات.xlsx")
        general_format = workbook.add_format()
        general_format.set_align('center')
        general_format.set_text_wrap()

        header_format = workbook.add_format()
        header_format.set_bg_color('red')
        header_format.set_align('center')
        header_format.set_font_size(20)
        header_format.set_text_wrap()
        header_format.set_bold()

        sub_header_format = workbook.add_format()
        sub_header_format.set_align('center')
        sub_header_format.set_bg_color('silver')
        sub_header_format.set_text_wrap()
        sub_header_format.set_font_size(16)

        global toPrint
        toPrint = sol.copy()

        for b in range(len(toPrint)):
            worksheet = workbook.add_worksheet(branch_name[b])

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
            l = len(branch[b].hallsInBranch)

            for i in range(l):
                worksheet.write(R + i, 0, toPrint[b][i][0], sub_header_format)
                worksheet.write(R + i, 1, toPrint[b][i][1], general_format)
                worksheet.write(R + i, 2, toPrint[b][i][2], general_format)
                worksheet.write(R + i, 3, toPrint[b][i][3], general_format)

            for i in range(l):
                worksheet.write(R + i, 4, toPrint[b][i + l][1], general_format)
                worksheet.write(R + i, 5, toPrint[b][i + l][2], general_format)
                worksheet.write(R + i, 6, toPrint[b][i + l][3], general_format)

            for i in range(l):
                worksheet.write(R + i, 7, toPrint[b][i + 2 * l][1], general_format)
                worksheet.write(R + i, 8, toPrint[b][i + 2 * l][2], general_format)
                worksheet.write(R + i, 9, toPrint[b][i + 2 * l][3], general_format)

        workbook.close()
        output_the_distribution_with_halls_data()
        return True
    
    except:
        return False

    

def output_the_distribution_with_halls_data():
    workbook = xlsxwriter.Workbook('icons/hallsWithAllData.xlsx')

    general_format = workbook.add_format()
    general_format.set_align('center')
    general_format.set_text_wrap()

    header_format = workbook.add_format()
    header_format.set_bg_color('red')
    header_format.set_align('center')
    header_format.set_font_size(20)
    header_format.set_text_wrap()
    header_format.set_bold()

    sub_header_format = workbook.add_format()
    sub_header_format.set_align('center')
    sub_header_format.set_bg_color('silver')
    sub_header_format.set_text_wrap()
    sub_header_format.set_font_size(16)

    for b in range(len(toPrint)):
        worksheet = workbook.add_worksheet(branch_name[b])

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
        l = len(branch[b].hallsInBranch)

        for i in range(l):
            worksheet.write(R + i, 0, toPrint[b][i][0], sub_header_format)
            worksheet.write(R + i, 1, toPrint[b][i][1], general_format)
            worksheet.write(R + i, 2, toPrint[b][i][2], general_format)
            worksheet.write(R + i, 3, toPrint[b][i][3], general_format)


        for i in range(l):
            worksheet.write(R + i, 4, toPrint[b][i + l][1], general_format)
            worksheet.write(R + i, 5, toPrint[b][i + l][2], general_format)
            worksheet.write(R + i, 6, toPrint[b][i + l][3], general_format)


        for i in range(l):
            worksheet.write(R + i, 7, toPrint[b][i + 2 * l][1], general_format)
            worksheet.write(R + i, 8, toPrint[b][i + 2 * l][2], general_format)
            worksheet.write(R + i, 9, toPrint[b][i + 2 * l][3], general_format)

        for i in range(l):
            worksheet.write(R + i, 10, dataframes[b][i][1], general_format)
            worksheet.write(R + i, 11, dataframes[b][i][2], general_format)
            worksheet.write(R + i, 12, dataframes[b][i][3], general_format)
    
    # worksheet2 = workbook.add_worksheet(str(len(branch_name)))
    # worksheet2.right_to_left()
    workbook.close()
