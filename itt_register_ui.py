from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QLabel, \
    QLineEdit
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)
        print("hi")
    def __init__(self):
        super().__init__()
        self.title = "Register"
        #self.top = 200
        #self.left = 500
        #self.width = 400
        #self.height = 300
        #self.setWindowIcon(QtGui.QIcon("TS_logo.png"))

        self.setWindowTitle(self.title)
        self.frame =QFrame(self)
        self.frame.setFixedSize(250,200)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(0.6)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0,0,0,0)

        usr_lb = QLabel("Username")
        usr_lb.setContentsMargins(10,10,10,10)
        usr_lb.setFont(QFont('Arial', 10))
        user_txt = QLineEdit()
        user_txt.setContentsMargins(0, 10, 10, 10)
        user_txt.setFont(QFont('Arial', 10))

        pwd_lb = QLabel("Password")
        pwd_lb.setContentsMargins(10, 10, 10, 10)
        pwd_lb.setFont(QFont('Arial', 10))
        self.pwd_txt = QLineEdit()

        self.pwd_txt.setContentsMargins(0, 10, 10, 10)
        self.pwd_txt.setFont(QFont('Arial', 10))
        self.pwd_txt.setEchoMode(QLineEdit.Password)

        confirm_pwd_lb = QLabel("Confirm Password")
        confirm_pwd_lb.setContentsMargins(10, 10, 10, 10)
        confirm_pwd_lb.setFont(QFont('Arial', 10))

        self.confirm_pwd_txt = QLineEdit()
        self.confirm_pwd_txt.setContentsMargins(0, 10, 10, 10)
        self.confirm_pwd_txt.setFont(QFont('Arial', 10))
        self.confirm_pwd_txt.setEchoMode(QLineEdit.Password)

        chk_box=QtWidgets.QCheckBox()
        chk_box.setText("Show Password")
        chk_box.setContentsMargins(0, 0, 0, 0)
        chk_box.stateChanged.connect(self.chk_box_chnage_event)

        submit_btn=QPushButton()
        submit_btn.setText("Submit")
        submit_btn.clicked.connect(self.submit_btn_click)

        continue_btn = QtWidgets.QPushButton()
        continue_btn.setText("Continue")
        continue_btn.clicked.connect(self.continue_btn_click)


        self.gridLayout.addWidget(usr_lb,0,0)
        self.gridLayout.addWidget(user_txt, 0, 1)

        self.gridLayout.addWidget(pwd_lb, 1, 0)
        self.gridLayout.addWidget(self.pwd_txt, 1, 1)

        self.gridLayout.addWidget(confirm_pwd_lb, 2, 0)
        self.gridLayout.addWidget(self.confirm_pwd_txt, 2, 1)

        self.gridLayout.addWidget(chk_box, 3, 1)

        self.gridLayout.addWidget(submit_btn, 4, 0)
        self.gridLayout.addWidget(continue_btn, 4, 1)

        self.show()

    def continue_btn_click(self):
        print("Continue clicked")

    def submit_btn_click(self):
        print("Submit clicked")

    def chk_box_chnage_event(self,checked):
        if checked:
            self.pwd_txt.setEchoMode(QLineEdit.Normal)
            self.confirm_pwd_txt.setEchoMode(QLineEdit.Normal)
        else:
            self.pwd_txt.setEchoMode(QLineEdit.Password)
            self.confirm_pwd_txt.setEchoMode(QLineEdit.Password)

    def centerOnScreen(self,frame):
        screen = QDesktopWidget()
        frame.move((self.width()-self.frame.width()) / 2, (self.height()-self.frame.height()) / 2)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())