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
        QVBoxLayout, QWidget,QFormLayout,QMainWindow)
import sys

class View_Report(QWidget):
    def __init__(self, parent=None):
        super(View_Report, self).__init__(parent)
        #flags = Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

        self.originalPalette = QApplication.palette()
        self.viewDropdown()
        self.View_Search()
        global topLayout
        global secLayout
        global thirdLayout
        global sibox
        mainLayout = QGridLayout()
        #saw = QVBoxLayout()
        s = QLineEdit()
        s.setEchoMode(QLineEdit.Normal)
        s.setGeometry(0,0,30,4)
        s.resize(300,200)
        s.move(0,0)
        #saw.addWidget(s)
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addLayout(secLayout, 1, 0, 1, 1)
        mainLayout.addLayout(thirdLayout, 2, 0)
        mainLayout.addWidget(s,3,0)
        #mainLayout.addLayout(secLayout,1,0,1,1)
        mainLayout.setRowStretch(1, 2)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)




        self.setLayout(mainLayout)
        self.setGeometry(300,300,400,400)

        self.setWindowTitle("CR View Report")
        self.changeStyle('Open')

    def viewDropdown(self):
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
        ##flo.addRow("CRNo.", e5)
        crsearchbox.textChanged.connect(self.textchanged)
        crsearchbox.editingFinished.connect(self.View_Enter)
        crsearchboxLabel = QLabel("&CRNo.:")
        crsearchboxLabel.setBuddy(crsearchbox)

        topLayout = QHBoxLayout()
        #topLayout.setContentsMargins(1, 1, 1, 1)

        topLayout.alignment()
        topLayout.addWidget(crsearchboxLabel)
        topLayout.addWidget(crsearchbox)
        topLayout.addWidget(statusLabel)
        topLayout.addWidget(statusComboBox)
        topLayout.addWidget(domainLabel)
        topLayout.addWidget(domainComboBox)
        topLayout.SizeConstraint(1)
        #topLayout.setSpacing(1)
        global sibox
        sibox = QLineEdit()
        sibox.setEchoMode(QLineEdit.Normal)
        ##flo.addRow("CRNo.", e5)
        sibox.textChanged.connect(self.textchanged)
        sibox.editingFinished.connect(self.View_Enter)
        siboxLabel = QLabel("&SoftwareImage:")
        siboxLabel.setBuddy(sibox)

        global secLayout
        secLayout = QHBoxLayout()
        secLayout.addWidget(siboxLabel)
        secLayout.addWidget(sibox)

        bibox = QLineEdit()
        bibox.setEchoMode(QLineEdit.Normal)
        ##flo.addRow("CRNo.", e5)
        bibox.textChanged.connect(self.textchanged)
        bibox.editingFinished.connect(self.View_Enter)
        biboxLabel = QLabel("&BuildImage:")
        biboxLabel.setBuddy(bibox)

        global thirdLayout
        thirdLayout = QHBoxLayout()
        thirdLayout.addWidget(biboxLabel)
        thirdLayout.addWidget(bibox)

        topLayout.addStretch()
        secLayout.addStretch()
        thirdLayout.addStretch()

    def changeStyle(self, styleName):
        st = styleName
        print(st)

    def readDomain(self,text):
        print("Domain selected is :"+text)

    def readStatus(self,text):
        print("Status selected is :"+text)

    def View_Search(self):
        """global flo
        flo = QFormLayout()
        #global win
        """
        global crsearchbox
        global crsearchboxLabel
        crsearchbox = QLineEdit()
        crsearchbox.setEchoMode(QLineEdit.Normal)
        ##flo.addRow("CRNo.", e5)
        crsearchbox.textChanged.connect(self.textchanged)
        crsearchbox.editingFinished.connect(self.View_Enter)
        crsearchboxLabel = QLabel("&CRNo.:")
        crsearchboxLabel.setBuddy(crsearchbox)
        global secLayout
        #secLayout = QHBoxLayout()
        #secLayout.addWidget(crsearchboxLabel)
        #secLayout.addWidget(crsearchbox)
        #win.setLayout(flo)
        #win.setWindowTitle("PyQt")
        #win.show()
        #self.setLayout(flo)
        #self.setWindowTitle("PyQt")
        #self.show()

    def textchanged(self,text):
        global inp
        inp = text
        #print("contents of text box: " + text)

    def View_Enter(self):
        global inp
        cr = int(inp)
        print("CR number is : ")
        print(cr)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gallery = View_Report()
    gallery.show()
    app.exec_()