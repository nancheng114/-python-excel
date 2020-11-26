import xlrd

#打开excel文件
workbook = xlrd.open_workbook('excel/成绩表.xlsx')


#获取目标sheet对象
sheet = workbook.sheet_by_index(0)      #获取第一个sheet表格
cell = sheet.cell(0,0)
print(cell.ctype)           #1
print(xlrd.XL_CELL_TEXT)    #1
print(xlrd.XL_CELL_NUMBER)  #2
print(xlrd.XL_CELL_DATE)    #3
print(xlrd.XL_CELL_BOOLEAN) #4
print(xlrd.XL_CELL_BLANK)   #6