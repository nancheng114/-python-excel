import xlrd

#开始读取
myexcle = xlrd.open_workbook('excel/123.xlsx')
# mysheetname = myexcle.sheet_names()          获取所有
# mysheetname = myexcle.sheet_by_index(3)      从下标开始获取
# mysheetname = myexcle.sheet_by_name('123')     #根据名字获取
# mysheet = myexcle.sheets()
# # print(mysheet)
# for x in mysheet:   #挨个吧表格从列表（可以理解为从箱子里往外拿东西，挨个拿）
#     print(x.name)   #打印该sheet的名字
#
# # print(mysheetname.name)     #打印这个整体的名字

sheet0 = myexcle.sheet_by_index(0)
print("行数:%d" % sheet0.nrows)#123.xlsx(你导入的表格1的行数）
print("列数:%d" % sheet0.ncols)#123.xlsx(你导入的表格1的列数）
