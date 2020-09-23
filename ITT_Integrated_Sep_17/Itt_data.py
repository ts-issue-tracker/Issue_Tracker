from PyQt5.QtCore import QDateTime, Qt, QTimer
from crdisplay import *
from Itt_Download import *
ENTRY_NOT_FOUND = -4
from itt_mail_sending import *
import pandas as pd
from Itt_fileopen import *
import numpy as np
from PyQt5.QtGui import QPalette,QImage,QPageSize,QBrush
from PyQt5.QtCore import QSize


row = 0
col = 0
result_list = []
names = []
bientries = []
sientries = []
filters = {"CR":'nil',"Title":'nil',"Assignee":'nil',"State":'nil',"Software Image":'nil',"Domain":'nil',"Issue Type":'nil',"GIT commit ID/Gerrit Link":'nil',"Build ID":'nil',"Created on":'nil',"Last Modified":'nil',"History":'nil'}
credential = {"Username":'nil',"Password":'nil'}
filrow = 0


class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Email Sending")

        self.sendButton = QPushButton("Send",self)
        self.credential()

        self.sendButton.clicked.connect(self.send_clicked)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.senderidLabel)
        self.layout.addWidget(self.senderid)
        self.layout.addWidget(self.senderpswdLabel)
        self.layout.addWidget(self.senderpswd)
        self.layout.addWidget(self.receiverIdLabel)
        self.layout.addWidget(self.receiverId)
        self.layout.addWidget(self.sendButton)
        oImage = QImage("image2.jpg")
        sImage = oImage.scaled(QSize(1000, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.setLayout(self.layout)

    def credential(self):
        self.senderid = QLineEdit()
        self.senderid.setEchoMode(QLineEdit.Normal)
        #self.senderid.setCompleter(self.completer)
        self.senderid.editingFinished.connect(self.view_senderid)
        self.senderidLabel = QLabel("User Email-ID")
        self.senderidLabel.setBuddy(self.senderid)

        self.senderpswd = QLineEdit()
        self.senderpswd.setEchoMode(QLineEdit.Password)
        # self.senderid.setCompleter(self.completer)
        self.senderpswd.editingFinished.connect(self.view_password)
        self.senderpswdLabel = QLabel("Password")
        self.senderpswdLabel.setBuddy(self.senderpswd)

        self.receiverId = QLineEdit()
        self.receiverId.setEchoMode(QLineEdit.Normal)
        # self.senderid.setCompleter(self.completer)
        self.receiverId.editingFinished.connect(self.view_receiver)
        self.receiverIdLabel = QLabel("Receiver Email-ID")
        self.receiverIdLabel.setBuddy(self.receiverId)

    def view_senderid(self):
        print("sender id is ",self.senderid.text())

    def view_password(self):
        print("password is ",self.senderpswd.text())

    def view_receiver(self):
        print("receiver is ",self.receiverId.text())

    def send_clicked(self):

        self.mailmsg = "PFA of filtered data"
        self.subject = "[Issue Tracker Tool] Filtered data"
        print("send clicked")
        sId = self.senderid.text()
        sPwd = self.senderpswd.text()
        rId = self.receiverId.text()
        status = sending_mail_with_attachment(sId, sPwd, rId, self.mailmsg,self.subject )
        print(status)

class App1(QWidget):
    def __init__(self,crlist):
        super().__init__()
        self.crs = crlist
        self.title = 'CR Filtered List'
        #adding frame to qvbox layout
        self.setMinimumWidth(600)
        self.setMinimumHeight(800)
        self.frame = QFrame(self)
        self.frame.setFixedSize(600, 600)


        self.layout = QGridLayout(self.frame)
        self.layout.setSpacing(0)


        self.frame_one = QFrame(self)
        self.frame_one.setFrameShape(QFrame.StyledPanel)
        self.vLayout_one = QVBoxLayout(self.frame_one)
        self.frame_one.setFixedSize(600, 600)
        self.frame_one.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.frame_one)

        self.createTable()
        self.downloadButton()
        self.sendmailButton()
        self.backbuttonFilter()
        self.tableWidget.itemSelectionChanged.connect(self.itemSelectionChangedCallback)

        self.vLayout_one.addWidget(self.tableWidget)

        self.frame_two = QFrame(self)
        self.frame_two.setFrameShape(QFrame.StyledPanel)
        self.vLayout_two = QHBoxLayout(self.frame_two)
        self.frame_two.setFixedSize(600, 80)
        self.frame_two.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.frame_two)

        self.vLayout_two.addWidget(self.dbutton)
        self.vLayout_two.addWidget(self.emailbutton)
        self.vLayout_two.addWidget(self.backFilter)

        oImage = QImage("image2.jpg")
        sImage = oImage.scaled(QSize(1000, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        verticalSpacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(verticalSpacer, 3, 0, Qt.AlignCenter)

        self.setLayout(self.layout)
        self.setGeometry(330, 35, 700, 700)
        self.setWindowTitle("CR Search Results")

        # Show window
        self.show()


    def downloadButton(self):
        self.dbutton = QPushButton("Download",self)
        self.dbutton.clicked.connect(self.on_download_click)

    def on_download_click(self):
        print("download clicked")
        saveCrsData(self.crs)

    def sendmailButton(self):
        self.emailbutton = QPushButton("Send Mail",self)
        self.emailbutton.clicked.connect(self.on_email_click)

    def on_email_click(self):
        print("click")
        self.on_download_click()
        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")
        #send_mail()

    def backbuttonFilter(self):
        self.backFilter = QPushButton("Back",self)
        #self.exitFilter.setToolTip("example")
        self.backFilter.clicked.connect(self.on_backfilter)

    def on_backfilter(self):
        #openfile(3)
        from Itt_View_Report_main import View_Report
        self.w = View_Report()
        self.w.show()
        self.hide()

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
        #self.hide()

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
        self.header = QTableWidgetItem("Search results")
        #self.header.setFont()
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Search results"))
        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def getcols():
    data_cols = 13
    sheet = openfile(1)
    namesheet = openfile(2)

    sheetdata = sheet#list(sheet)

    namesheetdata = namesheet#list(namesheet)
    for key, value in filters.items():
        for i in range(data_cols):#sheet.ncols):
            if (key == sheetdata[filrow][i]):#sheet.cell_value(filrow,i)):
                filters[key] = i

    for key, value in filters.items():
        print(key,value)

    for key1, value1 in credential.items():
        for i in range(2):#len(namesheetdata)):
            print("namesheetcols")
            #print(namesheet.ncols,namesheet.cell_value(filrow,i))
            if (key1 == namesheetdata[filrow][i]):#namesheet.cell_value(filrow, i)):
                print("inside namesheet true")
                credential[key1] = i
    openfile(3)
    openfile(4)

def namelist():
    namesheet = openfile(2)
    namesheetdata = namesheet#list(namesheet)
    index = credential["Username"]
    list1 = []
    for i in range(len(namesheetdata)):#namesheet.nrows):
        list1.append(namesheetdata[i][index])#namesheet.cell_value(i,index))
    [names.append(x) for x in list1 if x not in names]
    openfile(4)

def bilist():
    sheet = openfile(1)
    sheetdata = sheet#list(sheet)
    index = filters["Build ID"]
    list1 = []
    for i in range(len(sheetdata)):#sheet.nrows):
        list1.append(sheetdata[i][index])#sheet.cell_value(i,index))
    [bientries.append(x) for x in list1 if x not in bientries]
    openfile(3)

def getCr(cr):

    sheet = openfile(1)
    sheetdata = sheet#list(sheet)
    data_cols = 13
    print("before int conv")
    print("type of real cr",type(cr))
    typein = int(cr)
    print("after int conv")
    print("called data")
    result_list=[]
    dict = {}

    for n in range(len(sheetdata)):#sheet.nrows):
        print(type(sheetdata[n][0]))
        if sheetdata[n][0]==str(typein):#sheet.cell_value(n, 0) == typein:
            for i in range(data_cols):#sheet.ncols):
                data = sheetdata[n][i]#sheet.cell_value(n, i)
                result_list.append(data)
                print("getcr",data)
                dict[sheetdata[0][i]]=data#sheet.cell_value(0,i)]=data
    print(result_list)
    openfile(3)
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
    sheet = openfile(1)
    sheetdata = sheet#list(sheet)
    index = filters[field]
    crindx = filters["CR"]
    print("called searchCr")
    if field == "CR":
        print("in field")
        for n in range(len(sheetdata)):#sheet.nrows):
            #print("n and indeex and entry and sheet.cell_value(n,index)",n,index,type(entry),type(sheet.cell_value(n, index)))
            if sheetdata[n][index] == float(entry):#sheet.cell_value(n, index) == float(entry):
                l1.append(int(sheetdata[n][crindx]))#sheet.cell_value(n,crindx)))
                return
        #getCr(entry)

    if len(l1) == 0:
        print("in l1")
        for n in range(len(sheetdata)):#sheet.nrows):
            if sheetdata[n][index] == entry:#sheet.cell_value(n, index) == entry:
                l1.append(int(sheetdata[n][crindx]))#sheet.cell_value(n,crindx)))
    else:
        print("in loop l1")
        for n in range(len(sheetdata)):#sheet.nrows):
            print(n)
            if sheetdata[n][index] == entry:#sheet.cell_value(n, index) == entry:
                crVar=int((sheetdata[n][crindx]))#sheet.cell_value(n, crindx))
                searchInl1(crVar)

        l2 = list(dict.fromkeys(l2))
        l1 = list(l2)
        l2.clear()

    openfile(3)
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

