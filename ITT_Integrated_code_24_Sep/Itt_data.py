from PyQt5.QtCore import QDateTime, Qt, QTimer
from Itt_crdisplay import *
from Itt_Download import *
ENTRY_NOT_FOUND = -4
from itt_mail_sending import *
import pandas as pd
import itt_display_charts_ui as displaycharts
from Itt_fileopen import *
from itt_utils import *
from itt_validations import *
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
        self.setWhatsThis("Sends CR data to mentioned recipient")
        self.sendButton = QPushButton()
        self.sendButton.setText("Send")
        self.credential()
        global chances
        chances = 0
        self.sendButton.setDefault(False)
        self.sendButton.setAutoDefault(False)
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
        displayclass = displaycharts.Statistics_Window()
        #self.senderid.editingFinished.connect(lambda: displaycharts.Statistics_Window.email_validation_filter(displayclass, self.senderidLabel.text(), 0,self.senderid.text()))  # (self.view_senderid)

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
        self.receiverIdLabel = QLabel("Recipient Email-ID")
        self.receiverIdLabel.setBuddy(self.receiverId)
        #self.receiverId.editingFinished.connect(lambda: displaycharts.Statistics_Window.email_validation_filter(displayclass,self.receiverIdLabel.text(), 2,self.receiverId.text()))

    def view_senderid(self):
        self.smailid= self.senderid.text()
        ret = email_id_check(self.smailid)

        if ret == INVALID_INPUT_ERR:
            QMessageBox.about(self,'Information',"Sender Mail-ID is invalid")
            self.senderid.clear()
        elif ret == SUCCESS:
            if(len(self.smailid)) == 0:
                QMessageBox.about(self, 'Information', "Sender Mail-ID is empty")
                self.senderid.clear()

        print("sender id is ",self.senderid.text())

    def view_password(self):
        print("password is ",self.senderpswd.text())
        self.pswd = self.senderpswd.text()
        if(len(self.pswd)==0):
            QMessageBox.about(self, 'Information', "Password is empty")

    def view_receiver(self):
        print("receiver is ",self.receiverId.text())
        err=0
        ret=0
        self.rmailid = self.receiverId.text()
        if "," in self.receiverId.text():
            rIdlist = list(self.rmailid.split(","))
            for i in rIdlist:
                res = email_id_check(i)
                if res is not SUCCESS:
                    err = 1
            if err == 1:
                ret = INVALID_INPUT_ERR
        else:
            ret = email_id_check(self.rmailid)

        if ret == INVALID_INPUT_ERR:
            QMessageBox.about(self, 'Information', "Receiver Mail-ID is invalid")
            self.receiverId.clear()
        elif ret == SUCCESS:
            if (len(self.rmailid)) == 0:
                QMessageBox.about(self, 'Information', "Receiver Mail-ID is empty")
                self.receiverId.clear()

    def send_clicked(self):
        global chances

        mail_deliver_msg = ""
        self.mailmsg = "Hi,\n"+"<br>PFA  CR Data\n"+"\nRegards,\n"+"Issue Tracking Tool"
        print(self.mailmsg)
        self.subject = "[Issue Tracking Tool] CR Data"
        print("send clicked")
        sId = self.senderid.text()
        sPwd = self.senderpswd.text()
        rId = self.receiverId.text()
        err = 0
        ret = 0
        if "," in self.receiverId.text():
            rIdlist = list(self.rmailid.split(","))
            for i in rIdlist:
                res = email_id_check(i)
                if res is not SUCCESS:
                    err = 1
            if err == 1:
                ret = INVALID_INPUT_ERR
        else:
            ret = email_id_check(self.rmailid)
        #ret = email_id_check(rId)
        if len(sId) == 0 or len(rId) == 0 or len(sPwd) == 0:
            QMessageBox.about(self, 'Information', "Please fill all details")
        elif (ret == INVALID_INPUT_ERR) or len(rId)==0:
            QMessageBox.about(self, 'Information', "Please enter correct receiver ID")
            self.receiverId.clear()            
        else:
            mail_deliver_msg += sending_mail_with_attachment(sId, sPwd, rId, self.mailmsg,self.subject )#sending_mail(mail_id, pwd, rx_mail_id, msg_to_send, subject)
            QMessageBox.about(self, 'Information', mail_deliver_msg)

        if mail_deliver_msg != "Mail Sent Successfully":
            chances = chances + 1
            self.left = 3 - chances
            QMessageBox.about(self, 'Information',"chances left - "+str(self.left))

        if mail_deliver_msg == "Mail Sent Successfully":
            chances = 0

        if chances == 3:
            self.hide()
            return 1
            ######
        #status = sending_mail_with_attachment(sId, sPwd, rId, self.mailmsg,self.subject )
        #print(status)

class App1(QWidget):
    def __init__(self,crlist):
        super().__init__()
        self.crs = crlist
        self.dflag = 0
        self.title = 'CR Filtered List'
        #adding frame to qvbox layout
        self.setMinimumWidth(600)
        self.setMinimumHeight(800)
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 700)


        self.layout = QGridLayout(self.frame)
        self.layout.setSpacing(0)


        self.frame_one = QFrame(self)
        #self.frame_one.setFrameShape(QFrame.StyledPanel)
        self.vLayout_one = QVBoxLayout(self.frame_one)
        self.frame_one.setFixedSize(500, 600)
        self.frame_one.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.frame_one)

        self.createTable()
        self.downloadButton()
        self.sendmailButton()
        self.backbuttonFilter()
        self.tableWidget.itemSelectionChanged.connect(self.itemSelectionChangedCallback)

        self.vLayout_one.addWidget(self.tableWidget)

        self.frame_two = QFrame(self)
        #self.frame_two.setFrameShape(QFrame.StyledPanel)
        self.vLayout_two = QHBoxLayout(self.frame_two)
        self.frame_two.setFixedSize(500, 80)
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
        #self.setGeometry(330, 35, 700, 700)
        self.setWindowTitle("CR Search Results")
        self.showMaximized()
        # Show window
        self.show()


    def downloadButton(self):
        self.dbutton = QPushButton("Download",self)
        self.dbutton.clicked.connect(self.on_download_click)
        self.dbutton.setFixedHeight(40)

    def on_download_click(self):
        print("download clicked")
        ret = saveCrsData(self.crs)
        if self.dflag != 1:
            QMessageBox.about(self, 'Information', "Download success")

    def sendmailButton(self):
        self.emailbutton = QPushButton("Send Mail",self)
        self.emailbutton.clicked.connect(self.on_email_click)
        self.emailbutton.setFixedHeight(40)

    def on_email_click(self):
        print("click")
        self.dflag = 1
        self.on_download_click()
        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")
        print(dlg)
        self.dflag = 0
        if chances == 3:
            from itt_login_ui import login_window
            self.w = login_window()
            self.w.show()
            self.hide()
        #send_mail()

    def backbuttonFilter(self):
        self.backFilter = QPushButton("Back",self)
        #self.exitFilter.setToolTip("example")
        self.backFilter.setFixedHeight(40)
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
            self.tableWidget.setCurrentCell(-1, -1)
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


    sheetdata = openfile(OPEN_DATA_FILE)
    namesheetdata = openfile(OPEN_CREDENTIAL_FILE)
    data_cols=len(sheetdata[0])
    name_cols=len(namesheetdata[0])
    #sheetdata = sheet#list(sheet)

    #namesheetdata = namesheet#list(namesheet)
    for key, value in filters.items():
        for i in range(data_cols):#sheet.ncols):
            if (key == sheetdata[filrow][i]):#sheet.cell_value(filrow,i)):
                filters[key] = i

    for key, value in filters.items():
        print(key,value)

    for key1, value1 in credential.items():
        for i in range(name_cols):#len(namesheetdata)):
            print("namesheetcols")
            #print(namesheet.ncols,namesheet.cell_value(filrow,i))
            if (key1 == namesheetdata[filrow][i]):#namesheet.cell_value(filrow, i)):
                print("inside namesheet true")
                credential[key1] = i
    openfile(CLOSE_DATA_FILE)
    openfile(CLOSE_CREDENTIAL_FILE)

def namelist():
    namesheet = openfile(OPEN_CREDENTIAL_FILE)
    namesheetdata = namesheet#list(namesheet)
    index = credential["Username"]
    list1 = []
    for i in range(len(namesheetdata)):#namesheet.nrows):
        list1.append(namesheetdata[i][index])#namesheet.cell_value(i,index))
    [names.append(x) for x in list1 if x not in names]
    openfile(CLOSE_CREDENTIAL_FILE)

def bilist():
    sheet = openfile(OPEN_DATA_FILE)
    sheetdata = sheet#list(sheet)
    index = filters["Build ID"]
    list1 = []
    for i in range(len(sheetdata)):#sheet.nrows):
        list1.append(sheetdata[i][index])#sheet.cell_value(i,index))
    [bientries.append(x) for x in list1 if x not in bientries]
    openfile(CLOSE_DATA_FILE)

def getCr(cr):

    sheet = openfile(OPEN_DATA_FILE)
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
    openfile(CLOSE_DATA_FILE)
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
    sheet = openfile(OPEN_DATA_FILE)
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

    openfile(CLOSE_DATA_FILE)
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

