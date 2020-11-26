import xlwt
import xlrd

rwb = xlrd.open_workbook('excel/成绩表.xlsx')
mysheet = rwb.sheet_by_index(0)

#添加总分单元格
mysheet.put_cell(0,4,xlrd.XL_CELL_TEXT,'总分',None)
mysheet.put_cell(19,0,xlrd.XL_CELL_TEXT,'平均分',None)

for row in range(1,19):
    score = mysheet.row_values(row,1,4)
    mysheet.put_cell(row,4,xlrd.XL_CELL_NUMBER,sum(score),None)
    #行，列，类型，数据
    # mysheet.put_cell(row,4,xlrd.XL_CELL_NUMBER,sum(),None)
    # mysheet.put_cell(row,4,xlrd.XL_CELL_NUMBER,sum(),None)

for lie in range(1,5):
    scores = mysheet.col_values(lie,1,19)  #将调用的值赋值给scores
    mysheet.put_cell(19,lie,xlrd.XL_CELL_NUMBER,sum(scores)/len(scores),None)
    # mysheet.put_cell(行，列，写入的格式，写入的数据，None)


#编辑的实质是   读取 编辑   先写入一个新的excel文件

wwb = xlwt.Workbook(encoding='utf-8')

new_sheet = wwb.add_sheet('一班')
for row in range(mysheet.nrows):
    for col in range(mysheet.ncols):
        value = mysheet.cell_value(row,col)
        new_sheet.write(row,col,value)

wwb.save('excel/xinbiao.xls')







