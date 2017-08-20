# coding:utf-8
import xlrd
import codecs


def readxls(path):
    xl = xlrd.open_workbook(path)
    sheet = xl.sheets()[0]
    data = []
    for i in range(0, sheet.nrows):
        data.append(list(sheet.row_values(i)))
    return data


def readxls_col(path):
    xl = xlrd.open_workbook(path)
    sheet = xl.sheets()[0]
    data = []
    for i in range(0, sheet.ncols):
        data.append(list(sheet.col_values(i)))
    return data


def readtxt(path, code):
    with codecs.open(path, 'r', encoding=code)as f:
        txt_lines = f.readlines()
    return txt_lines


def writetxt(path, content, code):
    with codecs.open(path, 'a', encoding=code)as f:
        f.write(content)
    return path+' is ok!'


from tempfile import TemporaryFile
from xlwt import Workbook


def wryxls(wry_path, out_list):
    book = Workbook()
    sheet1 = book.add_sheet('Sheet 1')
    for i in range(len(out_list)):
        row = sheet1.row(i)
        for j in range(len(out_list[i])):
            row.write(j, out_list[i][j])
    book.save(wry_path)
    book.save(TemporaryFile())
    return wry_path+' is ok!'
