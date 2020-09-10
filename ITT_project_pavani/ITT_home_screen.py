from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QLabel, \
    QLineEdit
from PyQt5.QtWidgets import *
import sys

class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Screen")
        self.frame = QFrame(self)
        self.frame.setFixedSize(500,1000)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.home_screen()

    def home_screen(self):
        #submit button
        self.create=QPushButton()
        self.create.setText("Create")
        self.create.clicked.connect(self.create_click)

        #grid button
        self.gridLayout.addWidget(self.create,0,0)

        #submit button
        self.modify=QPushButton()
        self.modify.setText("Update")
        self.modify.clicked.connect(self.modify_click)

        #grid button
        self.gridLayout.addWidget(self.modify,1,0)

        #submit button
        self.view_record=QPushButton()
        self.view_record.setText("View")
        self.view_record.clicked.connect(self.view_record_clicked)

        #grid button
        self.gridLayout.addWidget(self.view_record,2,0)

        # submit button
        self.view_statistics = QPushButton()
        self.view_statistics.setText("Statistics")
        self.view_statistics.clicked.connect(self.Statistics_clicked)

        # grid button
        self.gridLayout.addWidget(self.view_statistics, 3, 0)

        self.show()

    def create_click(self):
        from ITT_create_issue import Create_cr
        self.w = Create_cr()
        self.w.show()
        self.hide()

    def modify_click(self):
        from ITT_Cr_num import Enter_cr
        self.w = Enter_cr()
        self.w.show()
        self.hide()

    def view_record_clicked(self):
        from ITT_cr_num_view import Enter_cr
        self.w = Enter_cr()
        self.w.show()
        self.hide()

    def Statistics_clicked(self):
        pass

if __name__ == "__main__":
    App = QApplication(sys.argv)
    main_window = Main_window()
    sys.exit(App.exec_())