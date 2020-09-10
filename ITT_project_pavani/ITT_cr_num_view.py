from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QWidget, QLineEdit, QLabel
from PyQt5.QtGui import QFont
import sys

from ITT_validate import *
from ITT_view_cr import *

class Enter_cr(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Screen")
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 1000)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.enter()

    def enter(self):
        self.enter_cr_num_label = QLabel("Cr.No:")
        self.enter_cr_num_label.setFont(QFont('Arial', 10))
        # entry assignee
        self.enter_cr_num_entry = QLineEdit()
        self.enter_cr_num_entry.setFont(QFont('Arial', 10))
        print(self.enter_cr_num_entry.text())
        # grid
        self.gridLayout.addWidget(self.enter_cr_num_label, 0, 0)
        self.gridLayout.addWidget(self.enter_cr_num_entry, 0, 1)
        # button
        self.Submit_but = QtWidgets.QPushButton()
        self.Submit_but.setText("Submit")
        self.Submit_but.clicked.connect(self.submit_but_clicked)
        # grid view button
        self.gridLayout.addWidget(self.Submit_but, 0, 2)

        self.show()
    def submit_but_clicked(self):
        self.cr_no = self.enter_cr_num_entry.text()
        self.ret = validate_cr_list(self.cr_no)
        if (self.ret >= 0):
            #self.w = Update(self.enter_cr_num_entry.text())
            self.w = View(self.ret)
            self.w.show()
            self.close()
        else:
            print("No cr exist")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = Enter_cr()
    sys.exit(app.exec_())
