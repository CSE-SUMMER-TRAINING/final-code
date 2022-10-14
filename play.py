from csv import excel
import pandas as pd
import arabic_reshaper

excl=pd.ExcelFile("halls_data_input.xlsx")
print(excl.sheet_names)