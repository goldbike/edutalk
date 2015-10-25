__author__ = 'dustinlee'


from openpyxl import load_workbook


fileName = '.\\DATA\\chat\\주1반.xlsx'

wb = load_workbook(filename=fileName)
sheet = wb['Table2']
for row in sheet.rows[5:]:
    print(row[1].value, row[4].value)


