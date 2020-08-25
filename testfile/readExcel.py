# -*- coding:utf-8 -*-
import os
from testfile import getpathInfo
from xlrd import open_workbook  # 调用读 Excel 的第三方库 xlrd
path = getpathInfo.get_Path()  # 拿到该项目的绝对地址

class  readExcel():
    def get_xls(self,xls_name,sheet_name):  # xls_name 填写用例的 Excel 名称，sheet_name 该 Excel 的 sheet 名称
        cls =[]
        xlspath = os.path.join(path,xls_name)
        file = open_workbook(xlspath) # 打开用例 Excel
        sheet = file.sheet_by_name(sheet_name)  #  获得打开 Excel 的 sheet
        nrows = sheet.nrows # 获取这个 sheet 内容行数
        for i in range(nrows): #根据行数做循环
            if sheet.row_values(i)[0] != u'case_name': #如果这个 Excel 的这个 sheet 的第 i行的第一列不等于 case_name，那么我们把这行数据添加到 cls[]
                cls.append(sheet.row_values(i))
        return cls
if __name__ == '__main__':
    print(readExcel().get_xls('testFile.xlsx','login'))
    print(readExcel().get_xls('testFile.xlsx','login')[0][1])
    print(readExcel().get_xls('testFile.xlsx','login')[1][2])