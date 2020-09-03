import xlrd
from Itt_Display_list import *
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

#filters = {"CR":0,"Title":1,"Assignee":2,"State":3,"Domain":5,"Issue Type":6,"Build ID":8}
filters =  {"Crno":0,"Assignee":2, "State":3, "Domain":5, "IssueType":6, "Build ID":8}



def namelist():
    index = filters["Assignee"]
    for i in range(sheet.nrows):
        names.append(sheet.cell_value(i,index))

def bilist():
    index = filters["Build ID"]
    for i in range(sheet.nrows):
        bientries.append(sheet.cell_value(i,index))

def getCr(cr):
    print("before int conv")
    typein = int(cr)
    print("after int conv")
    print("called data")
    result_list=[]
    for n in range(sheet.nrows):
        if sheet.cell_value(n, 0) == typein:
            for i in range(sheet.ncols):
                #print(sheet.cell_value(n, i))
                data = sheet.cell_value(n, i)
                result_list.append(data)
    print(result_list)
                #l1.append(data)

def search(userFilter):
    global l1
    l1 = []
    global l2
    l2 = []

    default = "None"
    uList = dict.fromkeys(["Crno","Assignee", "State", "Domain", "IssueType", "Build ID"],default)

    for key in userFilter :
        if userFilter[key] != "None":
            uList[key]=userFilter[key]
    print("printing ulist : ",uList)
    l1.clear()
    #print("before filling",l1[0])
    for key in uList :
        if uList[key] != "None":
            if key == "Crno":
                res = searchCr(key,uList[key])
                if res == 0:
                    print("Invalid",key)
                    return
                break
            else:
                res = searchCr(key, uList[key])
                if res == 0:
                    print("Invalid",key)
                    return

    print("final l1: ",l1)

def searchCr(field,entry):
    global l1
    global l2
    index = filters[field]
    crindx = filters["Crno"]
    print("called searchCr")
    if field == "Crno":
        print("in field")
        getCr(entry)
    if len(l1) == 0:
        print("in l1")
        for n in range(sheet.nrows):
            if sheet.cell_value(n, index) == entry:
                l1.append(int(sheet.cell_value(n,crindx)))
    else:
        print("in loop l1")
        for n in range(sheet.nrows):
            print(n)
            if sheet.cell_value(n, index) == entry:
                print(sheet.cell_value(n, index))
                crVar=int(sheet.cell_value(n, crindx))
                searchInl1(crVar)
        #print("l2 is",l2)
        l2 = list(dict.fromkeys(l2))
        #print("after removing dupes l2 :", l2)
        #overwrite()
        l1 = list(l2)
        l2.clear()
    #if len(l2) > 0:
    #    l1 = list(l2)
    if len(l1) == 0:
        return 0
    print("before l1")
    print(l1)
    #print("over")
    #overwrite()
    #print("l2 is :",l2)
    #print("l1 after copy of l2:",l1)
    #createList(l1)
    # main2()

def overwrite():
    for i in range(len(l2)):
        l1.insert(i,l2[i])

    """
    if len(l2) < len(l1):
        x = len(l2)
        y = len(l1)-1
        while x is not y:
            l1.pop(x)
            x=x+1
    """
    #print("l1 in for :",l1)

def searchInl1(cri):
    print("in searchinl1")
    if cri in l1:
        l2.append(cri)
