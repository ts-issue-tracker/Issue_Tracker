import xlrd
from crdisplay import *
from Itt_Display_list import *
from Itt_Download import *
ENTRY_NOT_FOUND = -4
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
        self.downloadButton()
        self.tableWidget.itemSelectionChanged.connect(self.itemSelectionChangedCallback)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.dbutton)
        self.setLayout(self.layout)

        # Show window
        self.show()


    def downloadButton(self):
        self.dbutton = QPushButton("Download",self)
        self.dbutton.clicked.connect(self.on_download_click)

    def on_download_click(self):
        print("download clicked")
        saveCrsData(self.crs)

    def itemSelectionChangedCallback(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            request = currentQTableWidgetItem.text()
            ret = getCr(request)
            print("type of request",type(request))
            self.finalwindow(ret)

    def finalwindow(self,ret):
        print("in window three")
        self.v = Windowfinal(ret)
        self.v.show()

    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.itemAt(row, column)
        self.ID = item.text()
        print("item selected is",self.ID)

    # Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.crs))
        # Column count
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("CR No.s"))
        i=1
        for i in range(len(self.crs)):
            self.tableWidget.setItem(i,0,QTableWidgetItem(str(self.crs[i])))

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

def bilist():
    index = filters["Build ID"]
    for i in range(sheet.nrows):
        bientries.append(sheet.cell_value(i,index))
        
def getCr(cr):
    print("before int conv")
    print("type of real cr",type(cr))
    typein = int(cr)
    print("after int conv")
    print("called data")
    result_list=[]
    dict = {}
    for n in range(sheet.nrows):
        if sheet.cell_value(n, 0) == typein:
            for i in range(sheet.ncols):
                data = sheet.cell_value(n, i)
                result_list.append(data)
                print("getcr",data)
                dict[sheet.cell_value(0,i)]=data
    print(result_list)
    return dict


def search(userFilter):
    global l1
    l1 = []
    global l2
    l2 = []

    default = "None"
    uList = dict.fromkeys(["CR","Assignee","State","Domain","Issue Type","Build ID"],default)
    for key in userFilter :
        if userFilter[key] != "None":
            uList[key]=userFilter[key]
    print("printing ulist : ",uList)
    l1.clear()

    for key in uList :
        if uList[key] != "None":
            if key == "CR":
                res = searchCr(key,uList[key])
                if res == 0:
                    #print("Invalid",key)
                    print("Search Not available")
                    l1.append(key)
                    return l1,ENTRY_NOT_FOUND
                return l1,2
                break
            else:
                res = searchCr(key, uList[key])
                if res == 0:
                    print("Search Not available")
                    l1.append(key)
                    return l1,ENTRY_NOT_FOUND

    print("final l1: ",l1)
    return l1,0


def searchCr(field,entry):
    global l1
    global l2
    index = filters[field]
    crindx = filters["CR"]
    print("called searchCr")
    if field == "CR":
        print("in field")
        for n in range(sheet.nrows):
            print("n and indeex and entry and sheet.cell_value(n,index)",n,index,type(entry),type(sheet.cell_value(n, index)))
            if sheet.cell_value(n, index) == float(entry):
                l1.append(int(sheet.cell_value(n,crindx)))
                return
        #getCr(entry)

    if len(l1) == 0:
        print("in l1")
        for n in range(sheet.nrows):
            print("n and indeex and entry and sheet.cell_value(n,index)",n,index,type(entry),type(sheet.cell_value(n, index)))
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

        l2 = list(dict.fromkeys(l2))
        l1 = list(l2)
        l2.clear()
    if len(l1) == 0:
        return 0
    print("before l1")
    print(l1)

def overwrite():
    for i in range(len(l2)):
        l1.insert(i,l2[i])


def searchInl1(cri):
    print("in searchinl1")
    if cri in l1:
        l2.append(cri)
