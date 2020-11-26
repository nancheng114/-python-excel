import xlwt
import random
#导入模块

workbook = xlwt.Workbook(encoding='utf-8')      #utf-8  兼容各国语言

#创建一个sheet对象
sheet = workbook.add_sheet('成绩表')

#添加表头
sheet.write(0,0,'姓名')
sheet.write(0,1,'语文')
sheet.write(0,2,'数学')
sheet.write(0,3,'英语')
for row in range(1,11):
    for col in range(4):
        sheet.write(row,col,random.randint(50,100))
#保存成excel文件
workbook.save('excel/scores.xls')






