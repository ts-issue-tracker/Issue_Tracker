import xlrd
from View_Report_Validation import *
from crdisplay import *
from Itt_Download import *
from ITT_mail import *
from PyQt5.QtCore import Qt
from itt_mail_sending import *
ENTRY_NOT_FOUND = -4
# Give the location of the file
data_file_location = ("C:\\Users\\akshay\\Downloads\\projectexecl.xlsx")
credential_file_location = ("")
wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)

wb2 = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)

row = 0
col = 0
result_list = []
names = []
bientries = []
sientries = []
filters = {"CR":'nil',"Title":'nil',"Assignee":'nil',"State":'nil',"Software Image":'nil',"Domain":'nil',"Issue Type":'nil',"GIT commit ID/Gerrit Link":'nil',"Build ID":'nil',"Created on":'nil',"Last Modified":'nil',"History":'nil'}
filrow = 0


class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)
        #setWindowFlags(windowFlags() & ~Qt::WindowContextHelpButtonHint)
        #flags = (Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle("Send Email")

        #QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.sendButton = QPushButton("Send",self)
        self.credential()
        #self.buttonBox = QDialogButtonBox(QBtn)
        #self.buttonBox.accepted.connect(self.accept)
        #self.buttonBox.rejected.connect(self.reject)
        self.sendButton.clicked.connect(self.send_clicked)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.senderidLabel)
        self.layout.addWidget(self.senderid)
        self.layout.addWidget(self.senderpswdLabel)
        self.layout.addWidget(self.senderpswd)
        self.layout.addWidget(self.receiverIdLabel)
        self.layout.addWidget(self.receiverId)
        self.layout.addWidget(self.sendButton)
        self.setLayout(self.layout)

    def credential(self):
        #self.senderid = QLineEdit()
        #self.nameCompleter()
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
        #send_mail(self.senderid.text(),self.senderpswd.text(),self.receiverId.text())
        text = "mail content"

        if (self.senderid.text() == '') and (self.senderpswd.text() == '') and (self.receiverId.text()):
            QMessageBox.about(self,'Information',"Enter the details")

        if (self.senderid.text() == '') or (self.senderpswd.text() == '') or (self.receiverId.text()):
            if self.senderid.text()=='':
                QMessageBox.about(self, 'Information', "sender Mail-ID empty")
            elif self.senderpswd.text()=='':
                QMessageBox.about(self, 'Information', "Password empty")
            elif self.receiverId.text()=='':
                QMessageBox.about(self, 'Information', "Receiver Mail-ID empty")

            ret = email_id_check(self.senderid.text())
            if ret == -2:
                QMessageBox.about(self, 'Information', "Invalid Sender Mail-ID")

            ret = email_id_check(self.receiverId)
            if ret == -2:
                QMessageBox.about(self, 'Information', "Invalid Receiver Mail-ID")
        else:
            sending_mail_with_selected_statistics_info(self.senderid.text(), self.senderpswd.text(), self.receiverId.text(),text)

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
        self.sendmailButton()
        self.tableWidget.itemSelectionChanged.connect(self.itemSelectionChangedCallback)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.dbutton)
        self.layout.addWidget(self.emailbutton)
        self.setLayout(self.layout)

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

        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")
        #send_mail()

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
        self.header = QTableWidgetItem("Search results")
        #self.header.setFont()
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Search results"))
        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        #self.tableWidget.setAutoScroll(True)#VerticalScrollBar()
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


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
