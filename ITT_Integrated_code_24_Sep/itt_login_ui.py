from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QFocusEvent
import sys
from PyQt5.QtCore import Qt
from itt_register_ui import *
import itt_credentials_file_access as file_access
from validations import itt_validations
from itt_utils import *
from PyQt5.QtGui import QPalette,QImage,QPageSize,QBrush,QPixmap
from PyQt5.QtCore import QSize

credentials_file = "Credentials.csv"

is_registered=False
class login_window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Login"

        self.user_var=value_chk.empty.value
        self.pwd_var=value_chk.empty.value
        self.list=[self.user_var,self.pwd_var]
        self.lb_list=["Usename","Password"]
        self.non_exising_user=False
        self.setWindowTitle(self.title)
        self.setMinimumWidth(1920)
        self.setMinimumHeight(1000)

        oImage = QImage("image2.jpg")
        sImage = oImage.scaled(QSize(1000, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.img_frame = QFrame(self)
        self.img_frame.setFixedSize(350,150)
        #self.img_frame.setFrameShape(QFrame.StyledPanel)
        self.img_gridLayout = QGridLayout(self.img_frame)
        self.img_gridLayout.setContentsMargins(20, 20, 20, 20)
        label = QLabel(self)
        pixmap = QPixmap('thundersoft.png')
        label.setPixmap(pixmap)
        self.img_gridLayout.addWidget(label)

        self.title_frame = QFrame(self)
        self.title_frame.setFixedSize(650, 100)
        #self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_lb = QLabel("ISSUE TRACKING TOOL")

        self.title_gridLayout = QGridLayout(self.title_frame)
        self.title_gridLayout.setContentsMargins(20, 20, 20, 20)
        self.title_gridLayout.addWidget(self.title_lb,0,0)

        myFont = QFont()
        myFont.setBold(True)
        self.title_lb.setFont(myFont)

        self.title_lb.setAlignment(Qt.AlignCenter)
        self.title_lb.setFont(QFont('Arial', 30))

        self.frame = QFrame(self)
        # self.frame.setAttribute(Qt.WA_TranslucentBackground)
        self.frame.setFixedSize(280, 200)
        # self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)

        usr_lb = QLabel("Username")
        usr_lb.setContentsMargins(0, 0, 0, 10)
        usr_lb.setFont(QFont('Arial', 10))

        self.user_txt = QLineEdit()
        self.user_txt.setContentsMargins(10, 0, 0, 10)
        self.user_txt.setFont(QFont('Arial', 10))
        #self.user_txt.focusOutEvent()
        self.user_txt.editingFinished.connect(self.user_name_validation)

        pwd_lb = QLabel("Password")
        pwd_lb.setContentsMargins(0, 10, 10, 10)
        pwd_lb.setFont(QFont('Arial', 10))

        self.pwd_txt = QLineEdit()
        self.pwd_txt.setContentsMargins(10, 10, 0, 10)
        self.pwd_txt.setFont(QFont('Arial', 10))
        self.pwd_txt.setEchoMode(QLineEdit.Password)
        self.pwd_txt.editingFinished.connect(self.password_validation)

        chk_box = QtWidgets.QCheckBox()
        chk_box.setText("Show Password")
        chk_box.setContentsMargins(0, 10, 0, 10)
        chk_box.stateChanged.connect(self.chk_box_change_event)

        login_btn = QPushButton()
        login_btn.setText("Login")
        login_btn.setFont(QFont('Arial', 10))
        login_btn.clicked.connect(self.login_btn_click)

        register_btn = QtWidgets.QPushButton()
        register_btn.setText("Register")
        register_btn.setFont(QFont('Arial', 10))
        register_btn.clicked.connect(self.register_btn_click)

        self.gridLayout.addWidget(usr_lb, 0, 0)
        self.gridLayout.addWidget(self.user_txt, 0, 1)

        self.gridLayout.addWidget(pwd_lb, 1, 0)
        self.gridLayout.addWidget(self.pwd_txt, 1, 1)

        self.gridLayout.addWidget(chk_box, 2, 1)

        self.gridLayout.addWidget(login_btn, 3, 0)
        self.gridLayout.addWidget(register_btn, 3, 1)

        self.util=utils()

        self.show()

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame,self.title_frame,self.img_frame)

    def centerOnScreen(self, frame,frame1,frame2):
        frame.move((self.width() - self.frame.width()) / 2, (self.height() - self.frame.height()) / 2)
        frame1.move((self.width() - self.title_frame.width()) / 2, self.title_frame.height())
        frame2.move((self.width()-self.img_frame.width()) , 1)

    def open_register_window(self):
        from itt_register_ui import register_window
        self.w = register_window()
        self.w.show()
        self.hide()

    def open_main_window(self):
        from itt_main_ui import main_window
        self.w = main_window()
        self.w.show()
        self.hide()

    def register_btn_click(self):
        self.open_register_window()

    def login_btn_click(self):
        final_msg = ""
        msg_to_display=""
        username = self.user_txt.text()
        password = self.pwd_txt.text()
        msg_to_display+=self.util.empty_fields_message(self.list,self.lb_list)
        invalid_msg_to_display = ""
        invalid_msg_to_display += self.util.invalid_fields_message(self.list,self.lb_list,username)
        if invalid_msg_to_display.__contains__("Not a Registered User"):
            msg_to_display=""
        if len(msg_to_display)==0 and len(invalid_msg_to_display)==0:
            if username != "" and password != '':
                if self.list[0]==value_chk.valid.value:
                    pwd = file_access.return_password_for_user(credentials_file, username)
                    if pwd == password :
                        QMessageBox.about(self, 'Information', "Logged in as "+username)
                        self.open_main_window()
                        pwd_var=value_chk.valid.value
                    else:
                        if pwd!="":
                            QMessageBox.about(self, 'Information', "Incorrect Password")
                            pwd_var=value_chk.incorrect.value
                            return
                        else:
                            QMessageBox.about(self, 'Information', "Not a Registered User")
                else:
                    if self.list[0]==value_chk.incorrect.value:
                        QMessageBox.about(self, 'Information', "Not a Registered User")
        else:
            if len(invalid_msg_to_display)!=0:
                 msg_to_display+=" "+invalid_msg_to_display
            QMessageBox.about(self, 'Information', msg_to_display)

    def chk_box_change_event(self, checked):
        if checked:
            self.pwd_txt.setEchoMode(QLineEdit.Normal)
        else:
            self.pwd_txt.setEchoMode(QLineEdit.Password)

    def user_name_validation(self):
        msg_to_display=""
        msg_to_display+=self.util.user_name_validtion\
            (self.list,credentials_file,self.user_txt.text())
        if len(msg_to_display)!=0:
            QMessageBox.about(self, 'Information', msg_to_display)
        if msg_to_display.__contains__("Not a Registered User"):
            self.user_txt.setText("")
            self.list[0]=value_chk.empty.value
            self.user_txt.setFocus()

    def password_validation(self):
        msg_to_display = ""
        msg_to_display+=self.util.password_validation_login\
            (self.list,self.pwd_txt.text())
        if len(msg_to_display)!=0:
            QMessageBox.about(self, 'Information', msg_to_display)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = login_window()
    sys.exit(App.exec())