from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect
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
        self.title = "Login"
        #self.top = 200
        #self.left = 200
        #self.width = 690
        #self.height = 4

        #self.setWindowIcon(QtGui.QIcon("TS_logo.png"))
        self.setWindowTitle(self.title)
        self.frame =QFrame(self)
        self.frame.setFixedSize(250, 200)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(0.6)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

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

        chk_box=QtWidgets.QCheckBox()
        chk_box.setText("Show Password")
        chk_box.setContentsMargins(0, 0, 0, 0)
        chk_box.stateChanged.connect(self.chk_box_chnage_event)

        login_btn=QPushButton()
        login_btn.setText("Login")
        login_btn.setFixedWidth(70)
        login_btn.clicked.connect(self.login_btn_click)

        register_btn = QtWidgets.QPushButton()
        register_btn.setText("Register")
        register_btn.setFixedWidth(70)

        register_btn.move(50,0)
        #register_btn.setGeometry(200, 150, 100, 40)
        #register_btn.setContentsMargins(20, 0, 0, 0)
        register_btn.clicked.connect(self.register_btn_click)


        self.gridLayout.addWidget(usr_lb,0,0)
        self.gridLayout.addWidget(user_txt, 0, 1)

        self.gridLayout.addWidget(pwd_lb, 1, 0)
        self.gridLayout.addWidget(self.pwd_txt, 1, 1)

        self.gridLayout.addWidget(chk_box, 2, 1)

        self.gridLayout.addWidget(login_btn, 3, 0)
        self.gridLayout.addWidget(register_btn, 3, 1)

        self.show()

    def centerOnScreen(self,frame):
        screen = QDesktopWidget()
        #screenGeom = QRect(screen.screenGeometry(frame))
        #screenCenterX = screenGeom.center().x()
        #screenCenterY = screenGeom.center().y()
        frame.move((self.width()-self.frame.width()) / 2, (self.height()-self.frame.height()) / 2)

    def register_btn_click(self):
        print("Register Clicked")
    def login_btn_click(self):
        print("Login Clicked")

    def chk_box_chnage_event(self,checked):
        if checked:
            self.pwd_txt.setEchoMode(QLineEdit.Normal)
        else:
            self.pwd_txt.setEchoMode(QLineEdit.Password)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())