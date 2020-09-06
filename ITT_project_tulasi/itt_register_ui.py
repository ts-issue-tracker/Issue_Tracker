from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
import sys
import itt_credentials_file_access as file_access
from itt_login_ui import *
from PyQt5.QtGui import QFont
from validations import itt_validations
from itt_mail_sending import *
credentials_file="Credentials.csv"
from itt_utils import *

class register_window(QWidget):
    def __init__(self):
        super().__init__()
        self.values = {'Username': False, 'Password': False, 'Confirm Password': False,'Email ID': False}
        self.title = "Register"
        self.user_var = 2
        self.pwd_var = 2
        self.confirm_pwd_var=2
        self.email_id_var=2
        self.list = [self.user_var, self.pwd_var, self.confirm_pwd_var,self.email_id_var]

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

        self.util = utils()

        self.show()

    def user_name_validation(self):
        msg_to_display = ""
        msg_to_display += self.util.user_name_validtion_register \
            (self.list, credentials_file, self.user_txt.text())
        if len(msg_to_display) != 0:
            QMessageBox.about(self, 'Information', msg_to_display)

    def password_valid(self,text,number):
        msg_to_display = ""
        if number==1:
            msg_to_display += self.util.password_validation \
                (self.list, self.pwd_txt.text())
        else:
            msg_to_display += self.util.confirm_password_validation \
                (self.list,self.confirm_pwd_txt.text())
        if len(msg_to_display) != 0:
            QMessageBox.about(self, 'Information', msg_to_display)

    def email_validation(self):
        msg_to_display = ""
        msg_to_display += self.util.email_validation \
            (self.list, self.email_txt.text())
        if len(msg_to_display) != 0:
            QMessageBox.about(self, 'Information', msg_to_display)


    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self,frame):
        frame.move((self.width()-self.frame.width()) / 2, (self.height()-self.frame.height()) / 2)

    def continue_btn_click(self):
        self.open_login_window()

    def submit_btn_click(self):
        msg_to_display=""
        username=self.user_txt.text()
        lb_list = ["Usename", "Password","Confirm Password","Email ID"]
        msg_to_display += self.util.empty_fields_message(self.list, lb_list)
        invalid_msg_to_display = ""
        invalid_msg_to_display += self.util.invalid_fields_message(self.list, lb_list, username)
        if len(msg_to_display) == 0 and len(invalid_msg_to_display) == 0:
            if self.list[0] != value_chk.empty.value and self.list[1] != value_chk.empty.value \
                    and self.list[2] != value_chk.empty.value and self.list[3] !=value_chk.empty.value:
                if self.user_txt.text() != "":
                    is_duplicate = file_access.duplicates_checking(credentials_file, self.user_txt.text())
                    if is_duplicate:
                        QMessageBox.about(self, 'Information', "Username already available,please enter other Username")
                    else:
                        if self.user_txt.text() != "" and self.pwd_txt.text() != '' and self.email_txt.text() != '':
                            file_access.writing_username_and_pwd(credentials_file, self.user_txt.text(),
                                                                 self.pwd_txt.text())
                            #sending_registration_mail_to(self.email_txt.text())
                            QMessageBox.about(self, 'Information', "You are successfully register,Please click on Continue to Login")
                        else:
                            QMessageBox.about(self, 'Information', "Username/Password Empty can\'t proceed furthur")
        else:
            if len(invalid_msg_to_display) != 0:
                msg_to_display += " " + invalid_msg_to_display
            QMessageBox.about(self, 'Information', msg_to_display)

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