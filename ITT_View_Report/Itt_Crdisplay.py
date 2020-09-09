import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDateTime

class Windowfinal(QWidget):#QMainWindow):                           # <===

    def __init__(self,ret):
        self.details = ret
        super().__init__()
        print("In final window showing details",self.details)
        self.setWindowTitle("Details of CR")
        for pair in self.details.items():
            print(pair)
        self.gridLayout = QGridLayout()
        self.setGeometry(400,100,600,600)
        self.ret = ret
        self.gui()

    def gui(self):
        print("inside gui")
        self.crbox = QLineEdit()
        self.crbox.setEchoMode(QLineEdit.Normal)
        self.crboxLabel = QLabel("&CR:")
        self.crboxLabel.setBuddy(self.crbox)

        self.Assigneebox = QLineEdit()
        self.Assigneebox.setEchoMode(QLineEdit.Normal)
        self.AssigneeboxLabel = QLabel("&Assignee:")
        self.AssigneeboxLabel.setBuddy(self.Assigneebox)

        self.Titlebox = QLineEdit()
        self.Titlebox.setEchoMode(QLineEdit.Normal)
        self.TitleboxLabel = QLabel("&Title:")
        self.TitleboxLabel.setBuddy(self.Titlebox)

        self.Statebox = QLineEdit()
        self.Statebox.setEchoMode(QLineEdit.Normal)
        self.StateboxLabel = QLabel("&State:")
        self.StateboxLabel.setBuddy(self.Statebox)

        self.SoftwareImagebox = QLineEdit()
        self.SoftwareImagebox.setEchoMode(QLineEdit.Normal)
        self.SoftwareImageboxLabel = QLabel("&Software Image:")
        self.SoftwareImageboxLabel.setBuddy(self.SoftwareImagebox)

        self.Domainbox = QLineEdit()
        self.Domainbox.setEchoMode(QLineEdit.Normal)
        self.DomainboxLabel = QLabel("&Domain:")
        self.DomainboxLabel.setBuddy(self.Domainbox)

        self.Issuetypebox = QLineEdit()
        self.Issuetypebox.setEchoMode(QLineEdit.Normal)
        self.IssuetypeboxLabel = QLabel("&Issue Type:")
        self.IssuetypeboxLabel.setBuddy(self.Issuetypebox)

        self.Gitbox = QLineEdit()
        self.Gitbox.setEchoMode(QLineEdit.Normal)
        self.GitboxLabel = QLabel("&GIT commit ID/Gerrit Link:")
        self.GitboxLabel.setBuddy(self.Gitbox)

        self.Bibox = QLineEdit()
        self.Bibox.setEchoMode(QLineEdit.Normal)
        self.BiboxLabel = QLabel("&Build ID:")
        self.BiboxLabel.setBuddy(self.Bibox)

        self.Createdonbox = QLineEdit()
        self.Createdonbox.setEchoMode(QLineEdit.Normal)
        self.CreatedonboxLabel = QLabel("&Created On:")
        self.CreatedonboxLabel.setBuddy(self.Createdonbox)

        self.lastmodifiedbox = QLineEdit()
        self.lastmodifiedbox.setEchoMode(QLineEdit.Normal)
        self.lastmodifiedboxLabel = QLabel("&Last Modified:")
        self.lastmodifiedboxLabel.setBuddy(self.lastmodifiedbox)

        self.historybox = QLineEdit()
        self.historybox.setEchoMode(QLineEdit.Normal)
        self.historyboxLabel = QLabel("&History:")
        self.historyboxLabel.setBuddy(self.historybox)

        self.fill()

        self.gridLayout.addWidget(self.crboxLabel, 0, 0,)
        self.gridLayout.addWidget(self.crbox, 0, 1)
        self.gridLayout.addWidget(self.TitleboxLabel,1 ,0)
        self.gridLayout.addWidget(self.Titlebox, 1, 1)
        self.gridLayout.addWidget(self.AssigneeboxLabel, 2, 0 )
        self.gridLayout.addWidget(self.Assigneebox, 2, 1)
        self.gridLayout.addWidget(self.StateboxLabel, 3, 0)
        self.gridLayout.addWidget(self.Statebox, 3, 1,)
        self.gridLayout.addWidget(self.IssuetypeboxLabel, 4, 0)
        self.gridLayout.addWidget(self.Issuetypebox, 4, 1)
        self.gridLayout.addWidget(self.DomainboxLabel, 5, 0)
        self.gridLayout.addWidget(self.Domainbox, 5, 1)
        self.gridLayout.addWidget(self.SoftwareImageboxLabel, 6, 0)
        self.gridLayout.addWidget(self.SoftwareImagebox, 6, 1)
        self.gridLayout.addWidget(self.GitboxLabel,7,0)
        self.gridLayout.addWidget(self.Gitbox, 7, 1)
        self.gridLayout.addWidget(self.BiboxLabel, 8, 0)
        self.gridLayout.addWidget(self.Bibox, 8, 1)
        self.gridLayout.addWidget(self.CreatedonboxLabel, 9, 0)
        self.gridLayout.addWidget(self.Createdonbox, 9, 1)
        self.gridLayout.addWidget(self.lastmodifiedboxLabel, 10, 0)
        self.gridLayout.addWidget(self.lastmodifiedbox, 10, 1)
        self.gridLayout.addWidget(self.historyboxLabel, 11, 0)
        self.gridLayout.addWidget(self.historybox, 11, 1)

        self.setLayout(self.gridLayout)
        self.show()

    def fill(self):
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
        self.git = self.details["GIT commit ID/Gerrit Link"]
        self.Gitbox.setText(self.git)
        self.Gitbox.setReadOnly(True)

        # entering BID
        self.Build = self.details["Build ID"]
        self.Bibox.setText(self.Build)
        self.Bibox.setReadOnly(True)

        # entering Createdon
        print(self.details["Created on"])
        self.Createdon = str(self.details["Created on"])
        self.Createdonbox.setText((self.Createdon))
        self.Createdonbox.setReadOnly(True)

        # entering Last modified
        self.Lastmodified = str(self.details["Created on"])
        self.lastmodifiedbox.setText((self.Lastmodified))
        self.lastmodifiedbox.setReadOnly(True)
