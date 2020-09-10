from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import *
import sys
import Itt_data
from Itt_data import *
from View_Report_Validation import *
from Itt_Display_list import *

class View_Report(QWidget):
    def __init__(self, parent=None):
        super(View_Report, self).__init__(parent)
        
        self.viewWidgets()
        self.Searchbutton()
        mainLayout = QGridLayout()

        mainLayout.addLayout(self.topLayout, 0, 0, 1, 2)
        mainLayout.addLayout(self.secLayout, 1, 0, 1, 2)
        mainLayout.addWidget(self.button,2,0,1,2)
        mainLayout.setRowStretch(1, 2)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)

        self.setLayout(mainLayout)
        self.setGeometry(400,100,600,600)

        self.setWindowTitle("CR View Report")
        self.selectedFilter = {"CR":"None","Assignee":"None","State":"None","Domain":"None","Issue Type":"None","Build ID":"None"}

    def open_new_dialog(self):
        self.nd = NewDialog(self)
        self.nd.show()

    def viewSearch(self):
        result = search(self.selectedFilter)
        self.flist = result[0]
        self.flag = result[1]
        print("li list from main: and crflag",self.flist,self.flag)

    def Searchbutton(self):
        self.button = QPushButton("Search",self)
        self.button.setToolTip("example")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.viewSearch()
        self.window2()

    def window2(self):
        print("in window 2")

        if (self.flag == 2):
            print("in cr flag true")
            print("type of ret ", type(self.flist[0]))
            ret = getCr(self.flist[0])
            self.w = Windowfinal(ret)
            self.w.show()
        elif(self.flag == -4):
            msg = self.flist[0]+" not found"
            QMessageBox.about(self, 'Information', msg)
        else:
            print("in cr flag false")
            self.w = App1(self.flist)
            self.w.show()

    def viewWidgets(self):
        getcols()
        namelist()
        bilist()
        self.statusComboBox = QComboBox(self)
        self.statusComboBox.addItem('None')
        self.statusComboBox.addItem('Open')
        self.statusComboBox.addItem('Analysis')
        self.statusComboBox.addItem('Inprogress')
        self.statusComboBox.addItem('Reopen')
        self.statusComboBox.addItem('Closed')

        self.statusComboBox.activated[str].connect(self.readStatus)
        self.statusComboBox.setGeometry(0, 0, 80, 20)
        self.statusLabel = QLabel("&Status:")
        self.statusLabel.setBuddy(self.statusComboBox)

        self.domainComboBox = QComboBox(self)
        self.domainComboBox.addItem('None')
        self.domainComboBox.addItem('Audio')
        self.domainComboBox.addItem('Video')
        self.domainComboBox.addItem('Camera')

        self.domainComboBox.activated[str].connect(self.readDomain)
        self.domainComboBox.setGeometry(0,0,80,20)
        self.domainLabel = QLabel("&Domain:")
        self.domainLabel.setBuddy(self.domainComboBox)

        self.issuetypeComboBox = QComboBox(self)
        self.issuetypeComboBox.addItem('None')
        self.issuetypeComboBox.addItem('Bug')
        self.issuetypeComboBox.addItem('Internal')
        self.issuetypeComboBox.addItem('Blacklisting')

        self.issuetypeComboBox.activated[str].connect(self.readIssuetype)
        self.issuetypeComboBox.setGeometry(0, 0, 80, 20)
        self.issuetypeLabel = QLabel("&IssueType:")
        self.issuetypeLabel.setBuddy(self.issuetypeComboBox)

        global topLayout
        global crsearchbox
        global crsearchboxLabel

        self.crsearchbox = QLineEdit()
        self.crsearchbox.setEchoMode(QLineEdit.Normal)
        self.crsearchbox.editingFinished.connect(self.View_Enter)
        self.crsearchboxLabel = QLabel("&CRNo.:")
        self.crsearchboxLabel.setBuddy(self.crsearchbox)

        self.nameCompleter()
        self.assigneebox = QLineEdit()
        self.assigneebox.setEchoMode(QLineEdit.Normal)
        self.assigneebox.setCompleter(self.completer)
        self.assigneebox.editingFinished.connect(self.view_assignee)
        self.assigneeboxLabel = QLabel("&Assignee:")
        self.assigneeboxLabel.setBuddy(self.assigneebox)

        self.topLayout = QHBoxLayout()
        self.topLayout.alignment()
        self.topLayout.addWidget(self.crsearchboxLabel)
        self.topLayout.addWidget(self.crsearchbox)
        self.topLayout.addWidget(self.statusLabel)
        self.topLayout.addWidget(self.statusComboBox)
        self.topLayout.addWidget(self.domainLabel)
        self.topLayout.addWidget(self.domainComboBox)
        self.topLayout.addWidget(self.issuetypeLabel)
        self.topLayout.addWidget(self.issuetypeComboBox)

        self.biCompleter()
        self.bibox = QLineEdit()
        self.bibox.setEchoMode(QLineEdit.Normal)
        self.bibox.textChanged.connect(self.bi_entry)
        self.bibox.setCompleter(self.bicompleter)
        self.bibox.editingFinished.connect(self.view_bi)
        self.biboxLabel = QLabel("&BuildImage:")
        self.biboxLabel.setBuddy(self.bibox)

        self.secLayout = QHBoxLayout()
        self.secLayout.addWidget(self.assigneeboxLabel)
        self.secLayout.addWidget(self.assigneebox)
        self.secLayout.addWidget(self.biboxLabel)
        self.secLayout.addWidget(self.bibox)

        self.topLayout.addStretch()
        self.secLayout.addStretch()

    def nameCompleter(self):
        self.completer = QCompleter(names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

    def siCompleter(self):
        self.sicompleter = QCompleter(sientries)
        self.sicompleter.setCaseSensitivity(Qt.CaseInsensitive)

    def biCompleter(self):
        self.bicompleter = QCompleter(bientries)
        self.bicompleter.setCaseSensitivity(Qt.CaseInsensitive)

    def resultBar(self):
        print("result bar")

    def changeStyle(self, styleName):
        st = styleName
        print(st)

    def readDomain(self,text):
        self.selectedFilter["Domain"] = text
        print("Domain selected is :"+text)

    def readStatus(self,text):
        sno = "status"
        self.selectedFilter["State"] = text
        print("Status selected is :"+text)

    def readIssuetype(self,text):
        ino = "issuetype"
        self.selectedFilter["Issue Type"] = text
        print("Issuetype is :"+text)

    def textchanged(self,text):
        global l
        l=1
        self.inp = text
        print("Cr entered is :",text)

    def View_Enter(self):
        inttext = self.crsearchbox.text()
        result = cr_check(inttext) #self.crsearchbox.text())
        if result == 0:
            self.selectedFilter["CR"] = self.crsearchbox.text()
        elif result == -3:
            self.selectedFilter["CR"] = "None"
        elif result == -2:
            QMessageBox.about(self, 'Information', "Invalid entry,Only numbers are accepted")
        elif result == -1:
            QMessageBox.about(self, 'Information', "Maximum limit is 6 numbers")

    def assignee_Entry(self,text):
        self.selectedFilter["Assignee"] = text
        self.assigneeName=text

    def view_assignee(self):
        print("in view assignee")
        assigneeText = self.assigneebox.text()
        result = assigneename_check(assigneeText)
        if result == 0:
            self.selectedFilter["Assignee"] = assigneeText
        elif result == -3:
            self.selectedFilter["Assignee"] = "None"
        elif result == -2:
            QMessageBox.about(self, 'Information', "Invalid entry only alphabets are allowed")
        elif result == -1:
            QMessageBox.about(self, 'Information', "Maximum limit is 15 characters")

    def si_entry(self,text):
        self.siName=text

    def view_si(self):
        print("si entered :"+self.siName)

    def bi_entry(self,text):
        self.biName=text

    def view_bi(self):
        self.selectedFilter["Build ID"] = self.biName
        print("BI entered :"+self.biName)


app = QApplication(sys.argv)
gallery = View_Report()
gallery.show()
app.exec_()

