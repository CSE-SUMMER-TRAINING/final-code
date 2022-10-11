from reportlab.lib import colors  
from reportlab.lib.pagesizes import letter, inch  
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle   
# creating a pdf file to add tables  
my_doc = SimpleDocTemplate("table.pdf", pagesize = letter)  
my_obj = []  
# defining Data to be stored on table  
my_data = [  
   ["ID", "1234"],  
   ["Name", "Den Arthur"],  
   ["Profession", "Software Developer"],  
   ["Age", "28"],  
   ["Sex", "Male"]  
]  
# Creating the table with 5 rows  
my_table = Table(my_data, 1 * [1.6 * inch], 5 * [0.5 * inch])  
# setting up style and alignments of borders and grids  
my_table.setStyle(  
   TableStyle(  
       [  
           ("ALIGN", (1, 1), (0, 0), "LEFT"),  
           ("VALIGN", (-1, -1), (-1, -1), "TOP"),  
           ("ALIGN", (-1, -1), (-1, -1), "RIGHT"),  
           ("VALIGN", (-1, -1), (-1, -1), "TOP"),  
           ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),  
           ("BOX", (0, 0), (-1, -1), 2, colors.black),  
       ]  
   )  
)  
my_obj.append(my_table)  
my_doc.build(my_obj)  