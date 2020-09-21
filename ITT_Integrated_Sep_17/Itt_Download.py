import xlwt
from datetime import datetime
from Itt_fileopen import *

import xlrd
# Give the location of the file

file_location = "cr_list_entry.xlsx"#("projectexecl.xlsx")

wb1 = xlrd.open_workbook(file_location)
sheet = wb1.sheet_by_index(0)

print(sheet.nrows)
print(sheet.ncols)

#sheet = openfile(1)
wb = xlwt.Workbook()
ws = wb.add_sheet('My Sheet',cell_overwrite_ok=True)
def getCr2(cr):
#    sheet = openfile(1)
    print("before int conv")
    print("type of real cr",type(cr))
    typein = int(cr)
    print("after int conv")
    print("called data")
    result_list1=[]
    dict1 = {}
    for n in range(sheet.nrows):
        if sheet.cell_value(n, 0) == typein:
            for i in range(sheet.ncols):
                data = sheet.cell_value(n, i)
                result_list1.append(data)
                print("getcr",data)
                dict1[sheet.cell_value(0,i)]=data
    print(result_list1)
    return dict1

def saveCrsData(crlist):
    print("in save",len(crlist),type(crlist[0]))
    i=0
    global indx
    indx=1
    for i in range(len(crlist)):
        num = (crlist[i])
        ret = getCr2(num)
        sort(ret)
        indx = indx + 1
        print("indx",indx)
    print("end of writing")
    wb.save('filterData.xls')

def sort(ret):
    print("in sort ")
    global indx
    headings = ret.keys()
    if indx == 1:
        for i,heading in enumerate(headings):
            ws.write(0, i, heading)
    print("indx in sort",indx)
    for i, heading in enumerate(headings):
        ws.write(indx, i, str(ret[heading]))
