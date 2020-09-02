from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
import sys
import itt_credentials_file_access as file_access
from itt_login_ui import *
from PyQt5.QtGui import QFont
from validations import itt_validations
from itt_mail_sending import *
credentials_file="Credentials.csv"

class register_window(QWidget):
    def __init__(self):
        super().__init__()
        self.values = {'Username': False, 'Password': False, 'Confirm Password': False,'Email ID': False}
        self.title = "Register"

        self.setWindowTitle(self.title)
        self.setMinimumWidth(700)
        self.setMinimumHeight(700)
        self.frame =QFrame(self)
        self.frame.setFixedSize(330,250)
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
        self.pwd_txt.setContentsMargins(10, 0, 0, 10)
        self.pwd_txt.setFont(QFont('Arial', 10))
        self.pwd_txt.setEchoMode(QLineEdit.Password)
        self.pwd_txt.editingFinished.connect(lambda: self.password_valid(pwd_lb.text(), 1))

        confirm_pwd_lb = QLabel("Confirm Password")
        confirm_pwd_lb.setContentsMargins(0, 0, 0, 10)
        confirm_pwd_lb.setFont(QFont('Arial', 10))

        self.confirm_pwd_txt = QLineEdit()
        self.confirm_pwd_txt.setContentsMargins(10, 0, 0, 10)
        self.confirm_pwd_txt.setFont(QFont('Arial', 10))
        self.confirm_pwd_txt.setEchoMode(QLineEdit.Password)
        self.confirm_pwd_txt.editingFinished.connect(lambda: self.password_valid(confirm_pwd_lb.text(),2))

        chk_box=QtWidgets.QCheckBox()
        chk_box.setText("Show Password")

        #chk_box.setContentsMargins(0, 0, 0, 0)
        chk_box.stateChanged.connect(self.chk_box_change_event)

        email_lb = QLabel("Email ID")
        email_lb.setContentsMargins(0, 0, 0, 10)
        email_lb.setFont(QFont('Arial', 10))

        self.email_txt = QLineEdit()
        self.email_txt.setContentsMargins(10, 0, 0, 10)
        self.email_txt.setFont(QFont('Arial', 10))
        self.email_txt.editingFinished.connect(self.email_validation)

        submit_btn=QPushButton()
        submit_btn.setText("Submit")
        submit_btn.setFont(QFont('Arial', 10))
        submit_btn.clicked.connect(self.submit_btn_click)

        continue_btn = QtWidgets.QPushButton()
        continue_btn.setText("Continue")
        continue_btn.setFont(QFont('Arial', 10))
        continue_btn.clicked.connect(self.continue_btn_click)

        self.gridLayout.addWidget(usr_lb,0,0)
        self.gridLayout.addWidget(self.user_txt, 0, 1)

        self.gridLayout.addWidget(pwd_lb, 1, 0)
        self.gridLayout.addWidget(self.pwd_txt, 1, 1)

        self.gridLayout.addWidget(confirm_pwd_lb, 2, 0)
        self.gridLayout.addWidget(self.confirm_pwd_txt, 2, 1)

        self.gridLayout.addWidget(email_lb, 3, 0)
        self.gridLayout.addWidget(self.email_txt, 3, 1)

        self.gridLayout.addWidget(chk_box, 4, 1)

        self.gridLayout.addWidget(submit_btn, 5, 0)
        self.gridLayout.addWidget(continue_btn, 5, 1)

        self.show()

    def user_name_validation(self):
        result = itt_validations.username_check(self.user_txt.text())
        if itt_validations.SUCCESS == result:
            self.values["Username"]=True
        elif itt_validations.EXCEED_LIMIT_ERR == result:
            QMessageBox.about(self, 'Information', "Max 15 characters are allowed")
        elif itt_validations.INVALID_INPUT_ERR == result:
            QMessageBox.about(self, 'Error', "Invalid Username,Only alphabets are allowed")

    def password_valid(self,text,number):
        if number==1:
            result = itt_validations.password_check(self.pwd_txt.text())
        else:
            result = itt_validations.password_check(self.confirm_pwd_txt.text())
        if itt_validations.SUCCESS == result:
            self.values[text] = True
        elif itt_validations.EXCEED_LIMIT_ERR == result:
            QMessageBox.about(self, 'Information', "Max 15 characters are allowed")
        elif itt_validations.INVALID_INPUT_ERR == result:
            QMessageBox.about(self, 'Error', "Invalid {},Only alphanumerics are allowed".format(text))

    def email_validation(self):
        result = itt_validations.email_id_check(self.email_txt.text())
        if result == itt_validations.SUCCESS:
            self.values["Email ID"] = True
        else:
            QMessageBox.about(self, 'Error', "Invalid Email ID")

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self,frame):
        frame.move((self.width()-self.frame.width()) / 2, (self.height()-self.frame.height()) / 2)

    def continue_btn_click(self):
        self.open_login_window()

    def submit_btn_click(self):
        print("Submit clicked")
        print(self.user_txt.text())
        print(self.pwd_txt.text())
        print(self.confirm_pwd_txt.text())
        if self.user_txt.text()!="":
            is_duplicate=file_access.duplicates_checking(credentials_file, self.user_txt.text())
            if is_duplicate:
                QMessageBox.about(self,'Information', "Username already available,please enter other Username")
            else:
                if self.user_txt.text()!="" and self.pwd_txt.text()!='':
                    file_access.writing_username_and_pwd(credentials_file,self.user_txt.text(),self.pwd_txt.text())
                    #sending_registration_mail_to(self.email_txt.text())
                else:
                    QMessageBox.about(self, 'Information', "Username/Password Empty can\'t proceed furthur")

    def chk_box_change_event(self,checked):
        if checked:
            self.pwd_txt.setEchoMode(QLineEdit.Normal)
            self.confirm_pwd_txt.setEchoMode(QLineEdit.Normal)
        else:
            self.pwd_txt.setEchoMode(QLineEdit.Password)
            self.confirm_pwd_txt.setEchoMode(QLineEdit.Password)

    def open_login_window(self):
        from itt_login_ui import login_window
        self.w = login_window()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = register_window()
    sys.exit(App.exec())