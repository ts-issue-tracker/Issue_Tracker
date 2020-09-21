from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Itt_data import *
from View_Report_Validation import *

"""
class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent=parent)
        #QPaintEvent()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("picture.png"))
        QStackedWidget.paintEvent(self, event)
"""
class View_Report(QWidget):
    def __init__(self, parent=None):
        #super(View_Report, self).__init__(parent)
        super().__init__()
        self.viewWidgets()
        self.Searchbutton()
        self.Exitbutton()

        self.setMinimumWidth(700)
        self.setMinimumHeight(700)
        self.frame = QFrame(self)
        self.frame.setFixedSize(900, 700)
        self.frame.setFrameShape(QFrame.StyledPanel)

        self.mainLayout = QGridLayout(self.frame)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(40, 40, 40, 40)
        self.mainLayout.heightForWidth(0)

        #mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        """n
        mainLayout.addLayout(self.topLayout, 0, 0,Qt.AlignCenter)
        #mainLayout.addLayout(self.topform, 0, 0, 1, 2)
        mainLayout.addLayout(self.secLayout, 1, 0,Qt.AlignCenter)
        mainLayout.addWidget(self.button,2,0,Qt.AlignCenter)
        #mainLayout.setRowStretch(1, 2)
        #mainLayout.setRowStretch(2, 1)
        #mainLayout.setColumnStretch(0, 1)
        #mainLayout.setColumnStretch(1, 1)
        """
        self.frame_one = QFrame(self)
        self.frame_one.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_one = QGridLayout(self.frame_one)
        self.frame_one.setFixedSize(700, 80)
        #self.frame_one.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.frame_one, 2, 0)

        self.gridLayout_one.addWidget(self.crsearchboxLabel, 0, 0)
        self.gridLayout_one.addWidget(self.crsearchbox, 0, 1)
        self.gridLayout_one.addWidget(self.statusLabel, 0, 2)
        self.gridLayout_one.addWidget(self.statusComboBox, 0, 3)

        self.frame_two = QFrame(self)
        self.frame_two.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_two = QGridLayout(self.frame_two)
        self.frame_two.setFixedSize(700, 80)
        #self.frame_two.setContentsMargins(0,0,0,0)
        self.mainLayout.addWidget(self.frame_two, 3, 0)

        self.gridLayout_two.addWidget(self.domainLabel, 0, 0)
        self.gridLayout_two.addWidget(self.domainComboBox, 0, 1)
        self.gridLayout_two.addWidget(self.issuetypeLabel, 0, 2)
        self.gridLayout_two.addWidget(self.issuetypeComboBox, 0, 3)

        self.frame_three = QFrame(self)
        self.frame_three.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_three = QGridLayout(self.frame_three)
        self.frame_three.setFixedSize(700, 80)
        #self.frame_two.setContentsMargins(0,0,0,0)
        self.mainLayout.addWidget(self.frame_three, 4, 0)

        self.gridLayout_three.addWidget(self.assigneeboxLabel, 0, 0)
        self.gridLayout_three.addWidget(self.assigneebox, 0, 1)
        self.gridLayout_three.addWidget(self.biboxLabel, 0, 2)
        self.gridLayout_three.addWidget(self.bibox, 0, 3)
        self.gridLayout_three.addWidget(self.button, 1, 0)
        self.gridLayout_three.addWidget(self.exitbutton, 1, 1)
        #self.gridLayout_three.setContentsMargins(0,0,0,0)

        self.frame_four = QFrame(self)
        self.frame_four.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_four = QGridLayout(self.frame_four)
        self.frame_four.setFixedSize(700, 80)
        #self.frame_two.setContentsMargins(0,0,0,0)
        self.mainLayout.addWidget(self.frame_four, 5, 0)
        self.gridLayout_four.addWidget(self.button, 0, 0)
        self.gridLayout_four.addWidget(self.exitbutton, 0, 3)
        self.gridLayout_four.setHorizontalSpacing(10)
        self.gridLayout_four.setRowStretch(0,0)
        """
        self.gridLayout_three.addWidget(self.issuetypeLabel, 3, 0)
        self.gridLayout_three.addWidget(self.issuetypeComboBox, 3, 1)
        self.gridLayout_three.addWidget(self.assigneeboxLabel, 4, 0)
        self.gridLayout_three.addWidget(self.assigneebox, 4, 1)
        self.gridLayout_three.addWidget(self.biboxLabel, 5, 0)
        self.gridLayout_three.addWidget(self.bibox, 5, 1)
        self.gridLayout_three.addWidget(self.button, 6, 0)
        self.gridLayout_three.addWidget(self.exitbutton, 6, 1)
        """
        """
        self.mainLayout.addWidget(self.crsearchboxLabel,0,0)
        self.mainLayout.addWidget(self.crsearchbox,0,1)
        self.mainLayout.addWidget(self.statusLabel,1,0)
        self.mainLayout.addWidget(self.statusComboBox,1,1)
        self.mainLayout.addWidget(self.domainLabel,2,0)
        self.mainLayout.addWidget(self.domainComboBox,2,1)
        self.mainLayout.addWidget(self.issuetypeLabel,3,0)
        self.mainLayout.addWidget(self.issuetypeComboBox,3,1)
        self.mainLayout.addWidget(self.assigneeboxLabel,4,0)
        self.mainLayout.addWidget(self.assigneebox, 4, 1)
        self.mainLayout.addWidget(self.biboxLabel, 5, 0)
        self.mainLayout.addWidget(self.bibox, 5, 1)
        self.mainLayout.addWidget(self.button,6,0)
        self.mainLayout.addWidget(self.exitbutton,6,1)
        """
        #verticalSpacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        #self.mainLayout.addItem(verticalSpacer, 3, 0, Qt.AlignCenter)
        self.mainLayout.heightForWidth(10)
        self.setLayout(self.mainLayout)
        self.setGeometry(250,40,900,900)
        self.setWindowTitle("CR View Report")
        #self.setStyleSheet("{background-image: url(picture.png);}")

        # Create widget
        #label = QLabel(self)
        #pixmap = QPixmap('picture.png')
        #label.setPixmap(pixmap)
        self.selectedFilter = {"CR":"None","Assignee":"None","State":"None","Domain":"None","Issue Type":"None","Build ID":"None"}


    def viewSearch(self):
        result = search(self.selectedFilter)
        self.flist = result[0]
        self.flag = result[1]
        print("li list from main: and crflag",self.flist,self.flag)

    def Searchbutton(self):
        self.button = QPushButton("Search",self)
        self.button.setToolTip("example")
        self.button.setGeometry(10,80,6,1)
        self.button.clicked.connect(self.on_click)

    def Exitbutton(self):
        self.exitbutton = QPushButton("Exit",self)
        self.exitbutton.setToolTip("example")
        self.exitbutton.clicked.connect(self.on_exit)

    def on_exit(self):
        from itt_main_ui import main_window
        from crdisplay import Windowfinal
        self.w = main_window()
        self.w.show()
        #Windowfinal().hide()
        self.hide()


    def on_click(self):

        # using all() + dictionary comprehension
        # Check if all values are 0 in dictionary
        #openfile(3)
        #openfile(1)
        #openfile(2)
        res = all(x == "None" for x in self.selectedFilter.values())
        if (res == 1):
            QMessageBox.about(self, 'Information', "No selection made!")
        else:
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
            #self.hide()

        elif(self.flag == -4):
            msg = "Search not available. "+self.flist[0]+" not found"
            QMessageBox.about(self, 'Information', msg)

        else:
            print("in cr flag false")
            self.w = App1(self.flist)
            self.w.show()
            self.hide()

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
        #self.statusComboBox.setFixedWidth(10)
        #self.statusComboBox.resize(90,10)

        self.statusComboBox.activated[str].connect(self.readStatus)
        self.statusComboBox.setGeometry(0, 0, 80, 20)
        self.statusLabel = QLabel("Status")
        self.statusLabel.setBuddy(self.statusComboBox)

        self.statusComboBox.setFixedWidth(130)
        #self.statusComboBox(QFont('Arial', 10))
        #self.statusComboBox.move(50, 0)

        self.statusLabel.setFixedWidth(80)
        #self.statusLabel.resize(10,1)
        #self.statusLabel(QFont('Arial', 10))
        #self.statusLabel.move(50, 0)

        self.domainComboBox = QComboBox(self)
        self.domainComboBox.addItem('None')
        self.domainComboBox.addItem('Audio')
        self.domainComboBox.addItem('Video')
        self.domainComboBox.addItem('Camera')

        self.domainComboBox.activated[str].connect(self.readDomain)
        #self.domainComboBox.setGeometry(0,0,80,20)
        self.domainLabel = QLabel("Domain")
        self.domainLabel.setBuddy(self.domainComboBox)

        self.domainComboBox.setFixedWidth(130)
        #self.domainComboBox(QFont('Arial', 10))
        #self.domainComboBox.move(50, 0)

        self.domainLabel.setFixedWidth(80)
        #self.domainLabel(QFont('Arial', 10))
        #self.domainLabel.move(50, 0)

        self.issuetypeComboBox = QComboBox(self)
        self.issuetypeComboBox.addItem('None')
        self.issuetypeComboBox.addItem('Bug')
        self.issuetypeComboBox.addItem('Internal')
        self.issuetypeComboBox.addItem('Blacklisting')

        self.issuetypeComboBox.activated[str].connect(self.readIssuetype)
        #self.issuetypeComboBox.setGeometry(0, 0, 80, 20)
        self.issuetypeLabel = QLabel("IssueType")
        self.issuetypeLabel.setBuddy(self.issuetypeComboBox)

        self.issuetypeComboBox.setFixedWidth(130)
        #self.issuetypeComboBox(QFont('Arial', 10))
        #self.issuetypeComboBox.move(50, 0)

        self.issuetypeLabel.setFixedWidth(80)
        #self.issuetypeLabel(QFont('Arial', 10))
        #self.issuetypeLabel.move(50, 0)

        global topLayout
        global crsearchbox
        global crsearchboxLabel

        self.crsearchbox = QLineEdit()
        self.crsearchbox.setEchoMode(QLineEdit.Normal)
        self.crsearchbox.editingFinished.connect(self.View_Enter)
        self.crsearchboxLabel = QLabel("CRNo.")
        self.crsearchboxLabel.setFixedWidth(80)
        self.crsearchboxLabel.setBuddy(self.crsearchbox)

        self.crsearchbox.setFixedWidth(130)
        #self.crsearchbox(QFont('Arial', 10))
        #self.crsearchbox.move(50, 0)

        self.crsearchboxLabel.setFixedWidth(80)
        #self.crsearchboxLabel(QFont('Arial', 10))
        #self.crsearchboxLabel.move(50, 0)

        self.nameCompleter()
        self.assigneebox = QLineEdit()
        self.assigneebox.setEchoMode(QLineEdit.Normal)
        self.assigneebox.setCompleter(self.completer)
        self.assigneebox.editingFinished.connect(self.view_assignee)
        self.assigneeboxLabel = QLabel("Assignee")
        self.assigneeboxLabel.setBuddy(self.assigneebox)

        self.assigneebox.setFixedWidth(130)
        #self.assigneebox(QFont('Arial', 10))
        #self.assigneebox.move(50, 0)

        self.assigneeboxLabel.setFixedWidth(80)
        #self.assigneeboxLabel(QFont('Arial', 10))
        #self.assigneeboxLabel.move(50, 0)

        self.biCompleter()
        self.bibox = QLineEdit()
        self.bibox.setEchoMode(QLineEdit.Normal)
        #self.bibox.textChanged.connect(self.bi_entry)
        self.bibox.setCompleter(self.bicompleter)
        self.bibox.editingFinished.connect(self.view_bi)
        self.biboxLabel = QLabel("BuildImage")
        self.biboxLabel.setBuddy(self.bibox)

        self.bibox.setFixedWidth(130)
        #self.bibox(QFont('Arial', 10))
        #self.bibox.move(50, 0)

        self.biboxLabel.setFixedWidth(80)
        #self.biboxLabel(QFont('Arial', 10))
        #self.biboxLabel.move(50, 0)

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
        print("in view build id")
        buildidText = self.bibox.text()
        result = buildid_check(buildidText)
        if result == 0:
            self.selectedFilter["Build ID"] = buildidText
        elif result == -3:
            self.selectedFilter["Build ID"] = "None"
        elif result == -2:
            QMessageBox.about(self, 'Information', "Invalid entry")
        elif result == -1:
            QMessageBox.about(self, 'Information', "Maximum limit is 6")

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self,frame):
        screen = QDesktopWidget()
        frame.move((self.width()-self.frame.width()) / 2, (self.height()-self.frame.height()) / 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gallery = View_Report()
    gallery.show()
    app.exec_()
