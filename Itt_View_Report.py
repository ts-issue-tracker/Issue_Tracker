# app.py
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import(QWidget, QHBoxLayout, QGridLayout, QApplication, QLineEdit, QFormLayout, QStyleFactory,QLabel, QComboBox)

class View_MainWindow(QWidget):

    def __init__(self,parent = None):
        #global win
        #win = QWidget()
        super(View_MainWindow, self).__init__(parent)

        global flo
        self.originalPalette = QApplication.palette()
        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        styleComboBox.activated[str].connect(self.changeStyle)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        self.View_Search()
        #topLayout.addWidget(self.setLayout(flo))

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)

        self.setLayout(mainLayout)

        #self.setWindowTitle("Styles")
        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('View')
        #self.show()
        self.View_Search()
        self.initUI()


    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        #self.changePalette()

    def View_Search(self):
        global flo
        flo = QFormLayout()
        #global win
        global e5
        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Normal)
        flo.addRow("CRNo.", e5)
        e5.textChanged.connect(self.textchanged)
        e5.editingFinished.connect(self.View_Enter)
        #win.setLayout(flo)
        #win.setWindowTitle("PyQt")
        #win.show()
        self.setLayout(flo)
        self.setWindowTitle("PyQt")
        self.show()

    def textchanged(self,text):
        global inp
        inp = text
        #print("contents of text box: " + text)

    def View_Enter(self):
        global inp
        cr = int(inp)
        print(cr)

    def initUI(self):
        super().__init__()
        self.lbl = QLabel('Open', self)

        combo = QComboBox(self)
        combo.addItem('Open')
        combo.addItem('Analysis')
        combo.addItem('Inprogress')
        combo.addItem('Reopen')
        combo.addItem('Closed')

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


"""
app = QApplication(sys.argv)
w = View_MainWindow()
#w.show()
sys.exit(app.exec_())
"""
"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel('Ubuntu', self)

        combo = QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Mandriva')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
"""

def main():

    app = QApplication(sys.argv)

    w = View_MainWindow()
   # exo = Example()
    #w.resize(250, 150)
    #w.move(300, 300)
    #w.setWindowTitle('Simple')
    #w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()