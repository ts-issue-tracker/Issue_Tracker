from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
import sys
from itt_register_ui import *
import itt_credentials_file_access as file_access
from validations import itt_validations

credentials_file="Credentials.csv"

class login_window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Login"
        self.setWindowTitle(self.title)
        self.frame =QFrame(self)
        self.frame.setFixedSize(250, 200)
        self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        usr_lb = QLabel("Username")
        usr_lb.setContentsMargins(10,10,10,10)
        usr_lb.setFont(QFont('Arial', 10))
        self.user_txt = QLineEdit()
        self.user_txt.setContentsMargins(0, 10, 10, 10)
        self.user_txt.setFont(QFont('Arial', 10))
        self.user_txt.editingFinished.connect(self.user_name_validation)

        pwd_lb = QLabel("Password")
        pwd_lb.setContentsMargins(10, 10, 10, 10)
        pwd_lb.setFont(QFont('Arial', 10))

        self.pwd_txt = QLineEdit()
        self.pwd_txt.setContentsMargins(0, 10, 10, 10)
        self.pwd_txt.setFont(QFont('Arial', 10))
        self.pwd_txt.setEchoMode(QLineEdit.Password)
        self.pwd_txt.editingFinished.connect(self.password_validation)

        chk_box=QtWidgets.QCheckBox()
        chk_box.setText("Show Password")
        chk_box.setContentsMargins(0, 0, 0, 0)
        chk_box.stateChanged.connect(self.chk_box_chnage_event)

        login_btn=QPushButton()
        login_btn.setText("Login")
        login_btn.setFixedWidth(70)
        #login_btn.setDisabled(True)
        login_btn.clicked.connect(self.login_btn_click)

        register_btn = QtWidgets.QPushButton()
        register_btn.setText("Register")
        register_btn.setFixedWidth(70)

        register_btn.move(50,0)
        #register_btn.setGeometry(200, 150, 100, 40)
        #register_btn.setContentsMargins(20, 0, 0, 0)
        register_btn.clicked.connect(self.register_btn_click)


        self.gridLayout.addWidget(usr_lb,0,0)
        self.gridLayout.addWidget(self.user_txt, 0, 1)

        self.gridLayout.addWidget(pwd_lb, 1, 0)
        self.gridLayout.addWidget(self.pwd_txt, 1, 1)

        self.gridLayout.addWidget(chk_box, 2, 1)

        self.gridLayout.addWidget(login_btn, 3, 0)
        self.gridLayout.addWidget(register_btn, 3, 1)

        self.show()

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self,frame):
        frame.move((self.width()-self.frame.width()) / 2, (self.height()-self.frame.height()) / 2)

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
        print("Register Clicked")
        self.open_register_window()

    def login_btn_click(self):
        print("Login Clicked")
        if self.user_txt.text() != "" and self.pwd_txt.text() != '':
            is_success=file_access.reading_and_checking_credentials(credentials_file,
                                                 self.user_txt.text(),self.pwd_txt.text())
            if is_success:
                self.open_main_window()
        else:
            QMessageBox.about(self, 'Information', "Username/Password Empty can\'t proceed furthur")

    def chk_box_chnage_event(self,checked):
        if checked:
            self.pwd_txt.setEchoMode(QLineEdit.Normal)
        else:
            self.pwd_txt.setEchoMode(QLineEdit.Password)

    def user_name_validation(self):
        result = itt_validations.username_check(self.user_txt.text())
        if itt_validations.SUCCESS == result:
            pass
        elif itt_validations.EXCEED_LIMIT_ERR == result:
            QMessageBox.about(self, 'Information', "Max 15 characters are allowed")
        elif itt_validations.INVALID_INPUT_ERR == result:
            QMessageBox.about(self, 'Error', "Invalid Username,Only alphabets are allowed")

    def password_validation(self):
        result = itt_validations.password_check(self.pwd_txt.text())
        if itt_validations.SUCCESS == result:
            pass
        elif itt_validations.EXCEED_LIMIT_ERR == result:
            QMessageBox.about(self, 'Information', "Max 15 characters are allowed")
        elif itt_validations.INVALID_INPUT_ERR == result:
            QMessageBox.about(self, 'Error', "Invalid Password,Only alphanumerics are allowed")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = login_window()
    sys.exit(App.exec())