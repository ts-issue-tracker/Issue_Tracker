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
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget,QFormLayout,QMainWindow,QCompleter)
import sys
import Itt_data

import xlrd

# Give the location of the file
file_location = ("C:\\Users\\akshay\\Downloads\\projectexecl.xlsx")

wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)
row = 0
col = 0
result_list = []
print(sheet.nrows)
print(sheet.ncols)

class View_Report(QWidget):
    def __init__(self, parent=None):
        super(View_Report, self).__init__(parent)
        #flags = Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

        self.viewDropdown()
        self.View_Search()

        mainLayout = QGridLayout()
        s = QLineEdit()
        s.setEchoMode(QLineEdit.Normal)
        s.setGeometry(0,0,30,4)
        s.resize(300,200)
        s.move(0,0)

        mainLayout.addLayout(self.topLayout, 0, 0, 1, 2)
        mainLayout.addLayout(self.secLayout, 1, 0, 1, 1)
        mainLayout.addLayout(self.thirdLayout, 2, 0)

        mainLayout.setRowStretch(1, 2)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)

        self.setLayout(mainLayout)
        self.setGeometry(400,100,600,600)

        self.setWindowTitle("CR View Report")
        self.changeStyle('Open')

    def viewDropdown(self):

        self.names = ["Santhoshi","Pavani","Tulasi","Sumalatha","Suresh"]

        statusComboBox = QComboBox(self)
        statusComboBox.addItem('Open')
        statusComboBox.addItem('Analysis')
        statusComboBox.addItem('Inprogress')
        statusComboBox.addItem('Reopen')
        statusComboBox.addItem('Closed')
        # styleComboBox.addItems(QStyleFactory.keys())

        statusComboBox.activated[str].connect(self.readStatus)
        statusComboBox.setGeometry(0, 0, 80, 20)
        statusLabel = QLabel("&Status:")
        statusLabel.setBuddy(statusComboBox)

        domainComboBox = QComboBox(self)
        domainComboBox.addItem('Audio')
        domainComboBox.addItem('Video')
        domainComboBox.addItem('Camera')

        domainComboBox.activated[str].connect(self.readDomain)
        domainComboBox.setGeometry(0,0,80,20)
        domainLabel = QLabel("&Domain:")
        domainLabel.setBuddy(domainComboBox)

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
        #self.topLayout.SizeConstraint(0)

        sibox = QLineEdit()
        sibox.setEchoMode(QLineEdit.Normal)
        sibox.textChanged.connect(self.si_entry)
        sibox.editingFinished.connect(self.view_si)
        siboxLabel = QLabel("&SoftwareImage:")
        siboxLabel.setBuddy(sibox)

        self.secLayout = QHBoxLayout()
        self.secLayout.addWidget(siboxLabel)
        self.secLayout.addWidget(sibox)
        self.secLayout.addWidget(assigneeboxLabel)
        self.secLayout.addWidget(assigneebox)

        bibox = QLineEdit()
        bibox.setEchoMode(QLineEdit.Normal)
        bibox.textChanged.connect(self.bi_entry)
        bibox.editingFinished.connect(self.view_bi)
        biboxLabel = QLabel("&BuildImage:")
        biboxLabel.setBuddy(bibox)

        self.thirdLayout = QHBoxLayout()
        self.thirdLayout.addWidget(biboxLabel)
        self.thirdLayout.addWidget(bibox)

        self.topLayout.addStretch()
        self.secLayout.addStretch()
        self.thirdLayout.addStretch()

    def nameCompleter(self):
        self.completer = QCompleter(self.names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

    def resultBar(self):
        print("result bar")

    def changeStyle(self, styleName):
        st = styleName
        print(st)

    def readDomain(self,text):
        print("Domain selected is :"+text)

    def readStatus(self,text):
        print("Status selected is :"+text)

    def readAssignee(self,text):
        print("Assignee name :"+text)

    def View_Search(self):
        global crsearchbox
        global crsearchboxLabel
        crsearchbox = QLineEdit()
        crsearchbox.setEchoMode(QLineEdit.Normal)
        crsearchbox.textChanged.connect(self.textchanged)
        crsearchbox.editingFinished.connect(self.View_Enter)
        crsearchboxLabel = QLabel("&CRNo.:")
        crsearchboxLabel.setBuddy(crsearchbox)
        global secLayout

    def textchanged(self,text):
        self.inp = text

    def View_Enter(self):
        cr = int(self.inp)
        print("before cr")
        Itt_data.getCr(cr)
        print("CR number is : ")
        print(cr)

    def assignee_Entry(self,text):
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
        print("assignee entered :"+self.biName)

#if __name__ == '__main__':
#    import sys

app = QApplication(sys.argv)
gallery = View_Report()
gallery.show()
app.exec_()
#sys.exit(app.exec_())
