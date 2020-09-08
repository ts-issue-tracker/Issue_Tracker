import xlrd
from crdisplay import *
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
#result_list=[]
#filters = {"CR":0,"Title":1,"Assignee":2,"State":3,"Domain":5,"Issue Type":6,"Build ID":8}
#filters =  {"Crno":0,"Assignee":2, "State":3, "Domain":5, "IssueType":6, "Build ID":8}
filters = {"CR":'nil',"Title":'nil',"Assignee":'nil',"State":'nil',"Software Image":'nil',"Domain":'nil',"Issue Type":'nil',"GIT commit ID/Gerrit Link":'nil',"Build ID":'nil',"Created on":'nil',"Last Modified":'nil',"History":'nil'}
filrow = 0

class App1(QWidget):
    def __init__(self,crlist):
        super().__init__()
        self.crs = crlist
        self.title = 'CR Filtered List'
        self.left = 400
        self.top = 100
        self.width =600
        self.height = 600

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()
        #print("before table clicked")
        #self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        #print("after table clicked")
        #self.itemSelectionChanged.connect(self.itemSelectionChangedCallback)
        self.tableWidget.itemSelectionChanged.connect(self.itemSelectionChangedCallback)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show window
        self.show()



    def itemSelectionChangedCallback(self):
        #print('#' * 80)
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            #print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            request = currentQTableWidgetItem.text()
            ret = getCr(request)
            self.finalwindow(ret)

    def finalwindow(self,ret):
        print("in window three")
        self.v = Windowfinal(ret)#Window3(ret)  # Window2()
        self.v.show()

    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.itemAt(row, column)
        self.ID = item.text()
        print("item selected is",self.ID)

    # Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
        #print("in table",self.crs)
        # Row count
        #self.tableWidget.setRowCount(4)
        self.tableWidget.setRowCount(len(self.crs))
        # Column count
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("CR No.s"))
        i=1
        for i in range(len(self.crs)):
            #data = str(self.crs)
            self.tableWidget.setItem(i,0,QTableWidgetItem(str(self.crs[i])))

        """
        #self.tableWidget.setItem(0, 1, QTableWidgetItem("City"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Aloysius"))
        #self.tableWidget.setItem(1, 1, QTableWidgetItem("Indore"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Alan"))
        #self.tableWidget.setItem(2, 1, QTableWidgetItem("Bhopal"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Arnavi"))
        #self.tableWidget.setItem(3, 1, QTableWidgetItem("Mandsaur"))
        """
        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)


def getcols():
    for key, value in filters.items():
        for i in range(sheet.ncols):
            if (key == sheet.cell_value(filrow,i)):
                filters[key] = i

    for key, value in filters.items():
        print(key,value)

def namelist():
    index = filters["Assignee"]
    for i in range(sheet.nrows):
        names.append(sheet.cell_value(i,index))

    #names = list(dict.fromkeys(names))

def bilist():
    index = filters["Build ID"]
    for i in range(sheet.nrows):
        bientries.append(sheet.cell_value(i,index))

    #bientries = list(dict.fromkeys(bientries))
        
def getCr(cr):
    print("before int conv")
    typein = int(cr)
    print("after int conv")
    print("called data")
    result_list=[]
    dict = {}
    for n in range(sheet.nrows):
        if sheet.cell_value(n, 0) == typein:
            for i in range(sheet.ncols):
                #print(sheet.cell_value(n, i))
                data = sheet.cell_value(n, i)
                result_list.append(data)
                dict[sheet.cell_value(0,i)]=data
    print(result_list)
    #l1.append(data)
    return dict #result_list
    #window3(result_list)

def search(userFilter):
    global l1
    l1 = []
    global l2
    l2 = []

    default = "None"
    #uList = dict.fromkeys(["Crno","Assignee", "State", "Domain", "IssueType", "Build ID"],default)
    uList = dict.fromkeys(["CR","Assignee","State","Domain","Issue Type","Build ID"],default)
    for key in userFilter :
        if userFilter[key] != "None":
            uList[key]=userFilter[key]
    print("printing ulist : ",uList)
    l1.clear()
    #print("before filling",l1[0])
    for key in uList :
        if uList[key] != "None":
            if key == "CR":
                res = searchCr(key,uList[key])
                if res == 0:
                    #print("Invalid",key)
                    print("Search Not available")
                    return
                break
            else:
                res = searchCr(key, uList[key])
                if res == 0:
                    #print("Invalid",key)
                    print("Search Not available")
                    return

    print("final l1: ",l1)
    return l1
    #window2()
    #print("after win2")


def searchCr(field,entry):
    global l1
    global l2
    index = filters[field]
    crindx = filters["CR"]
    print("called searchCr")
    if field == "CR":
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
