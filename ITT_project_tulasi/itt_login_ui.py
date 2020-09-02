from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
import sys
from PyQt5.QtCore import Qt
from itt_register_ui import *
import itt_credentials_file_access as file_access
from validations import itt_validations

credentials_file="Credentials.csv"

class login_window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Login"
        self.setWindowTitle(self.title)
        self.setMinimumWidth(700)
        self.setMinimumHeight(700)
        self.frame =QFrame(self)
        #self.frame.setAttribute(Qt.WA_TranslucentBackground)
        self.frame.setFixedSize(280, 200)
        #self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20,20,20,20)

        usr_lb = QLabel("Username")
        usr_lb.setContentsMargins(0,0,0,10)
        usr_lb.setFont(QFont('Arial', 10))

        self.user_txt = QLineEdit()
        self.user_txt.setContentsMargins(10, 0, 0, 10)
        self.user_txt.setFont(QFont('Arial', 10))
        self.user_txt.editingFinished.connect(self.user_name_validation)

        pwd_lb = QLabel("Password")
        pwd_lb.setContentsMargins(0, 10, 10, 10)
        pwd_lb.setFont(QFont('Arial', 10))

        self.pwd_txt = QLineEdit()
        self.pwd_txt.setContentsMargins(10, 10, 0, 10)
        self.pwd_txt.setFont(QFont('Arial', 10))
        self.pwd_txt.setEchoMode(QLineEdit.Password)
        self.pwd_txt.editingFinished.connect(self.password_validation)

        chk_box=QtWidgets.QCheckBox()
        chk_box.setText("Show Password")
        chk_box.setContentsMargins(0, 10, 0, 10)
        chk_box.stateChanged.connect(self.chk_box_change_event)

        login_btn=QPushButton()
        login_btn.setText("Login")
        login_btn.setFont(QFont('Arial', 10))
        login_btn.clicked.connect(self.login_btn_click)

        register_btn = QtWidgets.QPushButton()
        register_btn.setText("Register")
        register_btn.setFont(QFont('Arial', 10))
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
        self.open_register_window()

    def login_btn_click(self):
        if self.user_txt.text() != "" and self.pwd_txt.text() != '':
            is_success=file_access.reading_and_checking_credentials(credentials_file,
                                                 self.user_txt.text(),self.pwd_txt.text())
            if is_success:
                self.open_main_window()
        else:
            QMessageBox.about(self, 'Information', "Username/Password Empty can\'t proceed furthur")

    def chk_box_change_event(self,checked):
        if checked:
            self.pwd_txt.setEchoMode(QLineEdit.Normal)
        else:
            self.pwd_txt.setEchoMode(QLineEdit.Password)

    def user_name_validation(self):
        result = itt_validations.username_check(self.user_txt.text())
        if itt_validations.SUCCESS == result:
            is_duplicate = file_access.duplicates_checking(credentials_file, self.user_txt.text())
            if not is_duplicate:
                QMessageBox.about(self, 'Information', "Please Register First,and then Login")
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