import xlrd

# Give the location of the file
file_location = ("C:\\Users\\akshay\\Downloads\\projectexecl.xlsx")

wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)
row = 0
col = 0
result_list = []
print(sheet.nrows)
print(sheet.ncols)


def getCr(cr):
    print("called data")
    result_list=[]
    for n in range(sheet.nrows):
        typein = int(cr)
        if sheet.cell_value(n, 0) == typein:
            for i in range(sheet.ncols):
                print(sheet.cell_value(n, i))
                data = sheet.cell_value(n, i)
                result_list.append(data)
                # crvar.set("option is :"+(e1.get()))
    ips = len(result_list) / sheet.ncols
    if ips > 1:
        print("more than one entry")


