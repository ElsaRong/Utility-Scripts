import os
import sys
import xlrd
from xlwt import *

if __name__ == '__main__':
    file_path = r'C:\Users\Elsa\Desktop\origin_data\origindatawindow.txt'
    f = file(file_path,'r')
    line = f.read()

    w = Workbook()
    ws = w.add_sheet('DataSheet')

    arr_line = line[1:].split('\n')
    for i in range(len(arr_line)):
        arr_cell = arr_line[i].split(' ')
        for j in range(len(arr_cell)):
            ws.write(i, j, arr_cell[j])
    fpath_excel = file_path.replace('txt','xls')
    w.save(fpath_excel)
