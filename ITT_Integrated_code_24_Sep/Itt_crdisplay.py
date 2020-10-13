from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette,QImage,QPageSize,QBrush
from PyQt5.QtCore import QSize

class Windowfinal(QWidget):

    def __init__(self,ret):
        self.details = ret
        super().__init__()
        print("In final window showing details",self.details)
        self.setWindowTitle("Details of CR")
        for pair in self.details.items():
            print(pair)
        self.ret = ret
        self.gui()

    def exitbuttonData(self):
        print("exitbuttonfuntion")
        self.exitData = QPushButton("Exit", self)
        self.exitData.clicked.connect(self.on_exitdata)

    def on_exitdata(self):
        print("exit clicked")
        from Itt_data import App1
        self.w = App1(self.flist)
        self.w.show()
        self.hide()

    def gui(self):
        print("inside gui")
        self.crbox = QLineEdit()
        self.crbox.setEchoMode(QLineEdit.Normal)
        self.crboxLabel = QLabel("CR No.")
        self.crboxLabel.setBuddy(self.crbox)
#        self.crbox.setFixedWidth(400)

        self.Assigneebox = QLineEdit()
        self.Assigneebox.setEchoMode(QLineEdit.Normal)
        self.AssigneeboxLabel = QLabel("Assignee")
        self.AssigneeboxLabel.setBuddy(self.Assigneebox)
#        self.Assigneebox.setFixedWidth(400)

        self.Titlebox = QLineEdit()
        self.Titlebox.setEchoMode(QLineEdit.Normal)
        self.TitleboxLabel = QLabel("Title")
        self.TitleboxLabel.setBuddy(self.Titlebox)
#        self.Titlebox.setFixedWidth(400)

        self.Statebox = QLineEdit()
        self.Statebox.setEchoMode(QLineEdit.Normal)
        self.StateboxLabel = QLabel("State")
        self.StateboxLabel.setBuddy(self.Statebox)
#        self.Statebox.setFixedWidth(400)

        self.SoftwareImagebox = QLineEdit()
        self.SoftwareImagebox.setEchoMode(QLineEdit.Normal)
        self.SoftwareImageboxLabel = QLabel("Software Image State")
        self.SoftwareImageboxLabel.setBuddy(self.SoftwareImagebox)
#        self.SoftwareImagebox.setFixedWidth(400)

        self.Domainbox = QLineEdit()
        self.Domainbox.setEchoMode(QLineEdit.Normal)
        self.DomainboxLabel = QLabel("Domain")
        self.DomainboxLabel.setBuddy(self.Domainbox)
#        self.Domainbox.setFixedWidth(400)

        self.Issuetypebox = QLineEdit()
        self.Issuetypebox.setEchoMode(QLineEdit.Normal)
        self.IssuetypeboxLabel = QLabel("Issue Type")
        self.IssuetypeboxLabel.setBuddy(self.Issuetypebox)
#        self.Issuetypebox.setFixedWidth(400)

        self.Gitbox = QLineEdit()
        self.Gitbox.setEchoMode(QLineEdit.Normal)
        self.GitboxLabel = QLabel("GIT commit ID/Gerrit Link")
        self.GitboxLabel.setBuddy(self.Gitbox)
#        self.Gitbox.setFixedWidth(400)

        self.Bibox = QLineEdit()
        self.Bibox.setEchoMode(QLineEdit.Normal)
        self.BiboxLabel = QLabel("Build ID")
        self.BiboxLabel.setBuddy(self.Bibox)
#       self.Bibox.setFixedWidth(400)

        self.Createdonbox = QLineEdit()
        self.Createdonbox.setEchoMode(QLineEdit.Normal)
        self.CreatedonboxLabel = QLabel("Created On")
        self.CreatedonboxLabel.setBuddy(self.Createdonbox)
#       self.Createdonbox.setFixedWidth(400)

        self.lastmodifiedbox = QLineEdit()
        self.lastmodifiedbox.setEchoMode(QLineEdit.Normal)
        self.lastmodifiedboxLabel = QLabel("Last Modified")
        self.lastmodifiedboxLabel.setBuddy(self.lastmodifiedbox)
        #self.lastmodifiedbox.setFixedWidth(400)

        self.historybox = QTextBrowser()
        self.historybox.setAcceptRichText(True)
        self.historyboxLabel = QLabel("History")
        self.historyboxLabel.setBuddy(self.historybox)
        self.historybox.setOpenExternalLinks(True)
        #self.historybox.setFixedWidth(400)
        self.historybox.setFixedHeight(200)
        self.historybox.clear()
        self.fill()

        # adding frame to qvbox layout
        self.setMinimumWidth(600)
        self.setMinimumHeight(800)
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 700)
        # self.frame.setFrameShape(QFrame.StyledPanel)

        self.layout = QGridLayout(self.frame)
        self.layout.setSpacing(0)
        # self.layout.setContentsMargins(40, 40, 40, 40)
        # self.layout.heightForWidth(0)

        self.frame_one = QFrame(self)
        #self.frame_one.setFrameShape(QFrame.StyledPanel)
        self.vLayout_one = QGridLayout(self.frame_one)
        self.frame_one.setFixedSize(500, 700)
        self.frame_one.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.frame_one)

        self.vLayout_one.addWidget(self.crboxLabel,0,0)
        self.vLayout_one.addWidget(self.crbox,0,1)
        self.vLayout_one.addWidget(self.TitleboxLabel,1,0)
        self.vLayout_one.addWidget(self.Titlebox,1,1)
        self.vLayout_one.addWidget(self.AssigneeboxLabel,2,0)
        self.vLayout_one.addWidget(self.Assigneebox,2,1)
        self.vLayout_one.addWidget(self.StateboxLabel,3,0)
        self.vLayout_one.addWidget(self.Statebox,3,1)
        self.vLayout_one.addWidget(self.IssuetypeboxLabel,4,0)
        self.vLayout_one.addWidget(self.Issuetypebox,4,1)
        self.vLayout_one.addWidget(self.DomainboxLabel,5,0)
        self.vLayout_one.addWidget(self.Domainbox,5,1)
        self.vLayout_one.addWidget(self.SoftwareImageboxLabel,6,0)
        self.vLayout_one.addWidget(self.SoftwareImagebox,6,1)
        self.vLayout_one.addWidget(self.GitboxLabel,7,0)
        self.vLayout_one.addWidget(self.Gitbox,7,1)
        self.vLayout_one.addWidget(self.BiboxLabel,8,0)
        self.vLayout_one.addWidget(self.Bibox,8,1)
        self.vLayout_one.addWidget(self.CreatedonboxLabel,9,0)
        self.vLayout_one.addWidget(self.Createdonbox,9,1)
        self.vLayout_one.addWidget(self.lastmodifiedboxLabel,10,0)
        self.vLayout_one.addWidget(self.lastmodifiedbox,10,1)
        self.vLayout_one.addWidget(self.historyboxLabel,11,0)
        self.vLayout_one.addWidget(self.historybox,11,1)

        oImage = QImage("image2.jpg")
        sImage = oImage.scaled(QSize(1000, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        #self.setGeometry(330, 35, 700, 700)
        self.setLayout(self.layout)
        self.showMaximized()
        self.show()

    def fill(self):
        self.details = dict(self.details)

        #entering cr
        self.cr_no = int(self.details["CR"])
        self.crbox.setText(str(self.cr_no))
        self.crbox.setReadOnly(True)


        #entering title
        self.title = self.details["Title"]
        self.Titlebox.setText(self.title)
        self.Titlebox.setReadOnly(True)

        #entering Assignee
        self.assinee = self.details["Assignee"]
        self.Assigneebox.setText(self.assinee)
        self.Assigneebox.setReadOnly(True)

        # entering State
        self.state = self.details["State"]
        self.Statebox.setText(self.state)
        self.Statebox.setReadOnly(True)

        # entering si
        self.sim = self.details["Software Image"]
        self.SoftwareImagebox.setText(self.sim)
        self.SoftwareImagebox.setReadOnly(True)

        #entering DOmain
        self.domain = self.details["Domain"]
        self.Domainbox.setText(self.domain)
        self.Domainbox.setReadOnly(True)

        # entering Issuetype
        self.Issue = self.details["Issue Type"]
        self.Issuetypebox.setText(self.Issue)
        self.Issuetypebox.setReadOnly(True)

        # entering GIT details
        self.git = self.details["GIT commit id/Gerrit link"]#GIT commit id/Gerrit link"]
        self.Gitbox.setText(self.git)
        self.Gitbox.setReadOnly(True)

        # entering BID
        self.Build = self.details["Build ID"]
        self.Bibox.setText(self.Build)
        self.Bibox.setReadOnly(True)

        # entering Createdon
        self.details = dict(self.details)
        print("created on print",self.details.keys())
        self.Createdon = self.details["   Created    on"]
        self.Createdonbox.setText((self.Createdon))
        self.Createdonbox.setReadOnly(True)

        # entering Last modified
        self.Lastmodified = str(self.details["Last Modified"])
        self.lastmodifiedbox.setText((self.Lastmodified))
        self.lastmodifiedbox.setReadOnly(True)

        # entering history
        self.append_history()

    def append_history(self):
        self.history = str(self.details["History"])
        self.history = self.history.replace('[', '')
        self.history = self.history.replace('"', '')
        self.history = self.history.replace('"[','')
        self.history = self.history.replace(']','')
        self.history = self.history.replace("'", '')
        self.history = self.history.replace('\\', '')


        self.changes = self.history.split(",")
        for line in self.changes:
            self.historybox.append(line)
            self.historybox.append("")

