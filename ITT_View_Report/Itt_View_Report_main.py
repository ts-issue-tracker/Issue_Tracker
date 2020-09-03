#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import *
import sys
from Itt_data import *
from View_Report_Validation import *
from Itt_Display_list import *

class View_Report(QWidget):
    def __init__(self, parent=None):
        super(View_Report, self).__init__(parent)
        #flags = Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

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
        #self.changeStyle('Open')
        self.selectedFilter = {"Crno":"None","Assignee": "None", "State": "None", "Domain": "None", "IssueType": "None",
                               "Build ID": "None"}

    def open_new_dialog(self):
        self.nd = NewDialog(self)
        self.nd.show()

    def viewSearch(self):
        search(self.selectedFilter)

    def Searchbutton(self):
        self.button = QPushButton("Search",self)
        self.button.setToolTip("example")
        self.button.move(100,200)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        #self.open_new_dialog()
        self.viewSearch()


    def viewWidgets(self):

        namelist()
        bilist()

        statusComboBox = QComboBox(self)
        statusComboBox.addItem('None')
        statusComboBox.addItem('Open')
        statusComboBox.addItem('Analysis')
        statusComboBox.addItem('Inprogress')
        statusComboBox.addItem('Reopen')
        statusComboBox.addItem('Closed')

        statusComboBox.activated[str].connect(self.readStatus)
        statusComboBox.setGeometry(0, 0, 80, 20)
        statusLabel = QLabel("&Status:")
        statusLabel.setBuddy(statusComboBox)

        domainComboBox = QComboBox(self)
        domainComboBox.addItem('None')
        domainComboBox.addItem('Audio')
        domainComboBox.addItem('Video')
        domainComboBox.addItem('Camera')

        domainComboBox.activated[str].connect(self.readDomain)
        domainComboBox.setGeometry(0,0,80,20)
        domainLabel = QLabel("&Domain:")
        domainLabel.setBuddy(domainComboBox)

        issuetypeComboBox = QComboBox(self)
        issuetypeComboBox.addItem('None')
        issuetypeComboBox.addItem('Bug')
        issuetypeComboBox.addItem('Internal')
        issuetypeComboBox.addItem('Blacklisting')

        issuetypeComboBox.activated[str].connect(self.readIssuetype)
        issuetypeComboBox.setGeometry(0, 0, 80, 20)
        issuetypeLabel = QLabel("&IssueType:")
        issuetypeLabel.setBuddy(issuetypeComboBox)

        global topLayout
        global crsearchbox
        global crsearchboxLabel

        crsearchbox = QLineEdit()
        crsearchbox.setEchoMode(QLineEdit.Normal)
        crsearchbox.textChanged.connect(self.textchanged)
        crsearchbox.editingFinished.connect(self.View_Enter)
        crsearchboxLabel = QLabel("&CRNo.:")
        crsearchboxLabel.setBuddy(crsearchbox)

        self.nameCompleter()
        assigneebox = QLineEdit()
        assigneebox.setEchoMode(QLineEdit.Normal)
        assigneebox.textChanged.connect(self.assignee_Entry)
        assigneebox.setCompleter(self.completer)
        assigneebox.editingFinished.connect(self.view_assignee)
        assigneeboxLabel = QLabel("&Assignee:")
        assigneeboxLabel.setBuddy(assigneebox)

        self.topLayout = QHBoxLayout()
        self.topLayout.alignment()
        self.topLayout.addWidget(crsearchboxLabel)
        self.topLayout.addWidget(crsearchbox)
        self.topLayout.addWidget(statusLabel)
        self.topLayout.addWidget(statusComboBox)
        self.topLayout.addWidget(domainLabel)
        self.topLayout.addWidget(domainComboBox)
        self.topLayout.addWidget(issuetypeLabel)
        self.topLayout.addWidget(issuetypeComboBox)

        self.biCompleter()
        bibox = QLineEdit()
        bibox.setEchoMode(QLineEdit.Normal)
        bibox.textChanged.connect(self.bi_entry)
        bibox.setCompleter(self.bicompleter)
        bibox.editingFinished.connect(self.view_bi)
        biboxLabel = QLabel("&BuildImage:")
        biboxLabel.setBuddy(bibox)

        self.secLayout = QHBoxLayout()
        self.secLayout.addWidget(assigneeboxLabel)
        self.secLayout.addWidget(assigneebox)
        self.secLayout.addWidget(biboxLabel)
        self.secLayout.addWidget(bibox)

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

        #report_show(domain,dno)

    def readStatus(self,text):
        sno = "status"
        self.selectedFilter["State"] = text
        print("Status selected is :"+text)
        #report_show(status,sno)

    def readIssuetype(self,text):
        ino = "issuetype"
        self.selectedFilter["IssueType"] = text
        print("Issuetype is :"+text)
        #report_show(issuetype,ino)

    def textchanged(self,text):
        global l
        l=1
        self.inp = text
        print("Cr entered is :",text)

    def View_Enter(self):
        global l
        if l != 1:
            return
        print("in cr enter")
        res = validateCr(self.inp)
        if res == 0:
            return 0
        if res == 1:
            self.seletedFilter["Crno"] = "None"
        else:
            self.selectedFilter["Crno"] = self.inp
        #cr = int(self.inp)
        print("before cr")
        #getCr(cr)

        print("CR number is : ")
        #print(cr)

    def assignee_Entry(self,text):
        self.selectedFilter["Assignee"] = text
        self.assigneeName=text

    def view_assignee(self):
        print("assignee entered :"+self.assigneeName)

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

