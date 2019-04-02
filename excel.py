# -*- coding: utf-8 -*-
import xlrd
import xlwt


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook (r'C:*****\项目汇总+执行明细 - 2019-03-29 (2).xlsx')
    result = xlwt.Workbook ()  # 创建xlsx文件
    sheet = result.add_sheet ('result', cell_overwrite_ok=True)  # 表名为result
    # 获取所有sheet
    print (workbook.sheet_names ())  # [u'sheet1', u'sheet2']

    # 获取工作表
    a = []
    b = []
    table = workbook.sheets ()[0]
    nrow = table.nrows
    print (nrow)
    for i in range (nrow):
        cell = table.cell_value (i, 27)
        id = table.cell_value (i, 0)
        # if i>0:
        #     id = int(id)
        b.append (cell)
        a.append (id)
    print (a)
    c = []

    for i in a:
        if not i in c:
            c.append (i)

    id = table.cell_value (1, 0)
    sum = float (0)
    a = 0
    z = ['金额']
    for i in range (1, nrow):
        id_i = table.cell_value (i, 0)
        # print(id_i)
        if id_i == id:
            if a != 0:
                cell = float (table.cell_value (i, 27))
                # print(cell)
                # print(type(cell))
                sum = sum + cell
                print (int (id), cell)
            a += 1
        else:
            a = 0
            print (sum)
            z.append (sum)
            sum = 0
            id = table.cell_value (i, 0)
            print (id_i)
            print (sum)


    z.append (sum)

    print (z)
    print (c)
    for i in range (0, len (c)):
        sheet.write (i, 0, c[i])
    for i in range (0, len (z)):
        sheet.write (i, 1, z[i])

    result.save ("***//result.xls")

if __name__ == '__main__':
    read_excel ()