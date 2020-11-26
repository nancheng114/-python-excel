import xlrd

#打开excel文件
workbook = xlrd.open_workbook('excel/成绩表.xlsx')


#获取目标sheet对象
sheet = workbook.sheet_by_index(0)      #获取第一个sheet表格

#获取cell相关内容
# cell = sheet.cell(0,0)         #获取第一行第一列    下标从0开始
# print(cell)             #输出

# cell1 = sheet.row_slice(1,1,3)       #获取第一行的第一到第二个  包含第一不包含第三
# print(cell)[number:78.0,  number:99.0]

# for x in cell1:
#     print(x.value)


# cell2 = sheet.col_slice(1,1,3)
# print(cell2)
# for x in cell2:
#     print(x.value)

# print(sum([x.value for x in cell2])/len(cell2))

# print(sheet.cell_value(2,2))    #直接获取第二行第二列单元格的值

# print(sheet.row_values(3,1,3))      #第三行的第一列到第三列的值
                                    #包含第一列不包含第三列

# print(sheet.nrows)  #19行    先输出一共有几行
# print(sheet.col_values(1,1,sheet.nrows)) #[78.0, 98.0, 94.0, 90.0, 95.0, 99.0, 96.0, 96.0, 93.0, 90.0, 95.0, 96.0, 92.0, 90.0, 96.0, 98.0, 92.0, 99.0]
#
# scores = sheet.col_values(1,1,sheet.nrows)  #将调用的值赋值给scores
# result = sum(scores)/len(scores)    #用sum让scores相加然后用len求scores的长度，然后相除
# print(result)       #输出result

# print(sheet.cell(0，1).ctype)#1  姓名
# print(sheet.cell(2,2).ctype)#2  100

