import xlsxwriter

def create_halls_template():
    try: 
        workbook = xlsxwriter.Workbook('نموذج القاعات.xlsx')

        groups = workbook.add_worksheet('الدفعات')
        branch1 = workbook.add_worksheet('خلفاوي')
        branch2 = workbook.add_worksheet('روض الفرج')

        header_format = workbook.add_format()
        header_format.set_align('center')
        header_format.set_text_wrap()
        header_format.set_bold()
        header_format.set_font_size(16)

        branch1.set_column('A:A', 25)
        branch1.set_column('B:D', 15)
        branch1.right_to_left()
        branch1.write(0, 0, 'اسم القاعه', header_format)
        branch1.write(0, 1, 'السعه', header_format)
        branch1.write(0, 2, 'رقم المبني', header_format)
        branch1.write(0, 3, 'رقم الدور', header_format)

        branch2.set_column('A:A', 25)
        branch2.set_column('B:D', 15)
        branch2.right_to_left()
        branch2.write(0, 0, 'اسم القاعه', header_format)
        branch2.write(0, 1, 'السعه', header_format)
        branch2.write(0, 2, 'رقم المبني', header_format)
        branch2.write(0, 3, 'رقم الدور', header_format)

        groups.set_column('A:A', 25)
        groups.set_column('B:B', 17)
        groups.set_column('C:E', 15)
        groups.right_to_left()
        groups.right_to_left()
        groups.write(0, 0, 'اسم الدفعه', header_format)
        groups.write(0, 1, 'الفرع', header_format)
        groups.write(0, 2, 'عدد الطلاب', header_format)
        groups.write(0, 3, 'من', header_format)
        groups.write(0, 4, 'الي', header_format)

        workbook.close()
        return True
    
    except: 
        return False


def create_observers_template():
    try:
        workbook = xlsxwriter.Workbook('نموذج الملاحظين.xlsx')

        observersData = workbook.add_worksheet('الملاحظين')
        examsTable = workbook.add_worksheet('جدول الامتحانات')

        header_format = workbook.add_format()
        header_format.set_align('center')
        header_format.set_text_wrap()
        header_format.set_bold()
        header_format.set_font_size(16)

        observersData.set_column('A:A', 30)
        observersData.set_column('B:D', 20)
        observersData.set_column('E:E', 30)
        observersData.set_column('F:F', 17)
        observersData.right_to_left()
        observersData.write(0, 0, 'الاسم', header_format)
        observersData.write(0, 1, 'المسمى الوظيفى', header_format)
        observersData.write(0, 2, 'مكان العمل', header_format)
        observersData.write(0, 3, 'المبنى', header_format)
        observersData.write(0, 4, 'البريد الالكتروني', header_format)
        observersData.write(0, 5, 'التكليف الحالي', header_format)

        examsTable.set_column('A:G', 25)
        examsTable.right_to_left()
        examsTable.write(0, 0, 'التاريخ', header_format)
        examsTable.write(0, 1, '0/0/0000', header_format)
        examsTable.write(0, 2, '0/0/0000', header_format)
        examsTable.write(0, 3, '0/0/0000', header_format)
        examsTable.write(0, 4, '0/0/0000', header_format)
        examsTable.write(0, 5, '0/0/0000', header_format)
        examsTable.write(0, 6, '0/0/0000', header_format)

        workbook.close()
        return True

    except:
        return False