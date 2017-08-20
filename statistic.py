# -*- coding: utf-8 -*-
# @Date    : 2017-03-28 00:10:51
# @Author  : Alan Lau (rlalan@outlook.com)
from tempfile import TemporaryFile
from xlwt import Workbook

# you can count word's frequency by using collections.Count


def wryxls(wry_path, out_list):
    book = Workbook()
    sheet1 = book.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'Word')
    sheet1.write(0, 1, 'Frequency')
    for i in range(len(out_list)):
        row = sheet1.row(i+1)
        for j in range(len(out_list[i])):
            row.write(j, out_list[i][j])
    book.save(wry_path)
    book.save(TemporaryFile())
    return wry_path+' is ok!'


def orderdic(dic, reverse):
    ordered_list = sorted(
        dic.items(), key=lambda item: item[1], reverse=reverse)
    return ordered_list
