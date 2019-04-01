# -*- coding: utf-8 -*-
import xlrd
import xlwt
import pandas
import numpy

from datetime import date, datetime
import types


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\tianruixi\Desktop\0329\项目汇总+执行明细 - 2019-03-29.xlsx')
    wb_result = xlwt.Workbook()
    sheet_result = wb_result.add_sheet('result', cell_overwrite_ok=True)
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    # sheet2_name = workbook.sheet_names()[2]
    #
    # # 根据sheet索引或者名称获取sheet内容
    # sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    # sheet2 = workbook.sheet_by_name('效果导出')


    #获取工作表
    a =[]
    table = workbook.sheets()[2]
    nrow = table.nrows
    # sum = 0
    # for i in range(1,nrow):
    #     cell = table.cell_value(i,27)
    #     id = table.cell_value(i,0)
    #     a.append(cell)
    # a.to_excel("C:\\Users\\tianruixi\\Desktop\\test.xls")
    # # print(a)
    # # df_sum = table.groupby('订单ID')['金额'].sum()
    # # print(df_sum)
    id = table.cell_value(1, 0)
    sum = float(0)
    for i in range(1,nrow):
        id_i = table.cell_value (i, 0)
        print (id_i)
        if id_i == id:
            cell = table.cell_value(i, 27)
            # print(type(cell))
            # sum = sum + cell
            print(int(id), intcell)
        else:
            sum = 0
            id_i = table.cell_value(i, 0)
            print(id_i)
            print(sum)
        id = id_i

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