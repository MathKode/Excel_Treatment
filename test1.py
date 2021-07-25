import xlsxwriter

#Créer une feuille Excel
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

worksheet.name = "Ma première feuille"

worksheet.write("A1","Hello")
worksheet.write("B2","World")

worksheet2 = workbook.add_worksheet()

worksheet2.write(0,0,"Hello")
worksheet2.write(1,0,"World")

workbook.close()