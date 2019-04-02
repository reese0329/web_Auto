# -*- coding: utf-8 -*-
import xlrd
import xlwt



from datetime import date, datetime
import types


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\tianruixi\Desktop\0329\项目汇总+执行明细 - 2019-03-29 (2).xlsx')
    result = xlwt.Workbook() #创建xlsx文件
    sheet = result.add_sheet('result', cell_overwrite_ok=True)  #表名为result
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    # sheet2_name = workbook.sheet_names()[2]
    #
    # # 根据sheet索引或者名称获取sheet内容
    # sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    # sheet2 = workbook.sheet_by_name('效果导出')


    #获取工作表
    a =[]
    b =[]
    table = workbook.sheets()[0]
    nrow = table.nrows
    print(nrow)
    for i in range(nrow):
        cell = table.cell_value(i,27)
        id = table.cell_value(i, 0)
        # if i>0:
        #     id = int(id)
        b.append(cell)
        a.append(id)
    print(a)
    c=[]

    for i in a:
        if not i in c:
            c.append(i)

    #
    # # c = c.sort(reverse=True)
    #
    # a = set(a)
    # print(a)
    #




        # a.append(cell)
    # a.to_excel("C:\\Users\\tianruixi\\Desktop\\test.xls")
    # # print(a)
    # # df_sum = table.groupby('订单ID')['金额'].sum()
    # # print(df_sum)
    id = table.cell_value(1, 0)
    sum = float(0)
    a =0
    z =['金额']
    for i in range(1,nrow):
        id_i = table.cell_value (i, 0)
        # print(id_i)
        if id_i == id:
            if a!=0:
                cell = float(table.cell_value(i, 27))
                # print(cell)
                # print(type(cell))
                sum = sum + cell
                print(int(id), cell)
            a +=1
        else:
            a =0
            print(sum)
            z.append(sum)
            sum = 0
            id = table.cell_value(i, 0)
            print(id_i)
            print(sum)

    for i in range(1,nrow):
        id_i = table.cell_value(i, 0)
        # print(id_i)
        if id_i != id:
            a = 0
            print(sum)
            z.append(sum)
            sum = 0
            id = table.cell_value (i, 0)
            print(id_i)
            print(sum)
        else:
            if a!=0:
                cell = float(table.cell_value(i, 27))
                # print(cell)
                # print(type(cell))
                sum = sum + cell
                print(int(id), cell)
            a +=1
    z.append(sum)



    print(z)
    print(c)
    for i in range(0,len(c)):
            sheet.write(i,0,c[i])
    for i in range(0,len(z)):
            sheet.write(i,1,z[i])



    result.save("C://Users//tianruixi//Desktop//0329//result.xls")


    # sheet的名称，行数，列数
    # print(sheet2.name, sheet2.nrows, sheet2.ncols)

    # # 获取整行和整列的值（数组）
    # # rows = sheet2.row_values(3)  # 获取第四行内容
    # cols = sheet2.col_values(1)  # 获取第三列内容
    # # print(rows)
    # print(cols)
    # #
    # 获取单元格内容
    # print(sheet2.cell(1, 0).value.encode('utf-8'))
    # print(sheet2.cell_value(1, 0).encode('utf-8'))
    # print(sheet2.row(1)[0].value.encode('utf-8'))
    # # 获取单元格内容的数据类型
    # print(sheet2.cell(1, 0).ctype)


if __name__ == '__main__':
    read_excel()