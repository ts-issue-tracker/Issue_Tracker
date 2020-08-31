from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QLabel, \
    QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import sys
from ITT_read_excel import *

class view_window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "View"
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 1000)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)

        self.gridLayout = QGridLayout(self.frame)
        self.view_screen()

    def view_screen(self):
        print("in viewscreen")
        self.setWindowTitle("view screen")
        # label crno
        self.crno_label = QLabel("Cr.no:")
        self.crno_label.setFont(QFont('Arial', 10))
        # entry crno
        self.crno_entry = QLineEdit()
        self.cr_no = read_last_cr()
        print(self.cr_no)
        self.crno_entry.setText(self.cr_no)
        self.crno_entry.setReadOnly(True)
        self.crno_entry.setFont(QFont('Arial', 10))
        # grid cr label
        self.gridLayout.addWidget(self.crno_label, 0, 0)
        # grid cr entry
        self.gridLayout.addWidget(self.crno_entry, 0, 1)

        # label Description
        self.des_label = QLabel("Description:")
        self.des_label.setFont(QFont('Arial', 10))
        # entry Description
        self.des_entry = QLineEdit(self)
        self.des = read_last_des()
        self.des_entry.setReadOnly(True)
        self.des_entry.setFont(QFont('Arial', 10))

        # grid Description label
        self.gridLayout.addWidget(self.des_label, 1, 0)
        # grid Description entry
        self.gridLayout.addWidget(self.des_entry, 1, 1)

        # label title
        self.title_label = QLabel("Title:")
        self.title_label.setFont(QFont('Arial', 10))
        # entry title
        self.title_entry = QLineEdit()
        self.title = read_last_title()
        print(self.title)
        self.title_entry.setText(self.title)
        self.title_entry.setReadOnly(True)
        self.title_entry.setFont(QFont('Arial', 10))

        #grid label assignee
        self.gridLayout.addWidget(self.title_label,2,0)
        #grid entry assignee
        self.gridLayout.addWidget(self.title_entry,2,1)

        # label assignee
        self.assignee_label = QLabel("Assignee:")
        self.assignee_label.setFont(QFont('Arial', 10))
        # entry title
        self.assignee_entry = QLineEdit()
        self.assignee = read_last_assignee()
        print(self.assignee)
        self.assignee_entry.setText(self.title)
        self.assignee_entry.setReadOnly(True)
        self.assignee_entry.setFont(QFont('Arial', 10))


        #grid label assignee
        self.gridLayout.addWidget(self.assignee_label,3,0)
        #grid entry assignee
        self.gridLayout.addWidget(self.assignee_entry,3,1)





if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = view_window()
    sys.exit(App.exec())
