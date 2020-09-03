from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import xlrd
from Itt_data import *
# Give the location of the file
file_location = ("C:\\Users\\akshay\\Downloads\\projectexecl.xlsx")

wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)

import sys

class myListWidget(QListWidget):

    def Clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

class NewDialog(QWidget):
  def __init__(self, parent):
    super(NewDialog, self).__init__(parent)

def main2():
    app = QApplication(sys.argv)
    listWidget = myListWidget()

    # Resize width and height
    listWidget.resize(300, 120)


    listWidget.addItem("Item 1");
    listWidget.addItem("Item 2");
    listWidget.addItem("Item 3");
    listWidget.addItem("Item 4");

    listWidget.setWindowTitle('PyQT QListwidget Demo')
    listWidget.itemClicked.connect(listWidget.Clicked)

    listWidget.show()
    sys.exit(app.exec_())


#if __name__ == '__main__':
#    main()

