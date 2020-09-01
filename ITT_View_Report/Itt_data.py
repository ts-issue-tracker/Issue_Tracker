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
names = []
bientries = []
sientries = []

filters = {"CR":0,"Title":1,"Assignee":2,"State":3,"Domain":5,"Issue Type":6,"Build ID":8}

def namelist():
    index = filters["Assignee"]
    for i in range(sheet.nrows):
        names.append(sheet.cell_value(i,index))

def bilist():
    index = filters["Build ID"]
    for i in range(sheet.nrows):
        bientries.append(sheet.cell_value(i,index))

def getCr(cr):
    typein = int(cr)
    print("called data")
    result_list=[]
    for n in range(sheet.nrows):
        if sheet.cell_value(n, 0) == typein:
            for i in range(sheet.ncols):
                print(sheet.cell_value(n, i))
                data = sheet.cell_value(n, i)
                result_list.append(data)
