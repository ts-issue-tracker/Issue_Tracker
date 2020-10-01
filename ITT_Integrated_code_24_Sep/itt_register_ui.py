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

from PyQt5.QtGui import QPalette,QImage,QPageSize,QBrush
from PyQt5.QtCore import QSize

class register_window(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.max = 4
        self.title = "Register"
        self.user_var = value_chk.empty.value
        self.pwd_var = value_chk.empty.value
        self.confirm_pwd_var=value_chk.empty.value
        self.email_id_var=value_chk.empty.value
        self.email_pwd_var=value_chk.empty.value
        self.rx_email_id=value_chk.empty.value
        self.list = [self.user_var, self.pwd_var, self.confirm_pwd_var,self.email_id_var,self.email_pwd_var,self.rx_email_id]

        self.title_frame = QFrame(self)
        # self.frame.setAttribute(Qt.WA_TranslucentBackground)
        self.title_frame.setFixedSize(650, 100)
        # self.title_frame.setFrameShape(QFrame.StyledPanel)

        self.title_lb = QLabel("ISSUE TRACKING TOOL")

        self.title_gridLayout = QGridLayout(self.title_frame)
        self.title_gridLayout.setContentsMargins(20, 20, 20, 20)
        self.title_gridLayout.addWidget(self.title_lb, 0, 0)

        myFont = QFont()
        myFont.setBold(True)
        self.title_lb.setFont(myFont)

        self.title_lb.setAlignment(Qt.AlignCenter)
        self.title_lb.setFont(QFont('Arial', 30))

        self.setWindowTitle(self.title)
        self.setMinimumWidth(600)

        self.setMinimumHeight(800)
        self.frame =QFrame(self)
        self.frame.setFixedSize(350,350)
        #self.frame.setFrameShape(QFrame.StyledPanel)

        oImage = QImage("image2.jpg")
        sImage = oImage.scaled(QSize(1000, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20,20,20,20)

        usr_lb = QLabel("Username")
        usr_lb.setFixedWidth(140)
        usr_lb.setFont(QFont('Arial', 10))

        self.user_txt = QLineEdit()

        self.user_txt.setFixedWidth(180)
        self.user_txt.setFont(QFont('Arial', 10))
        self.user_txt.textChanged.connect(self.user_name_validation)

        pwd_lb = QLabel("Password")
        pwd_lb.setFixedWidth(140)
        pwd_lb.setFont(QFont('Arial', 10))

        self.pwd_txt = QLineEdit()
        self.pwd_txt.setFixedWidth(180)
        self.pwd_txt.setFont(QFont('Arial', 10))
        self.pwd_txt.setEchoMode(QLineEdit.Password)
        self.pwd_txt.textChanged.connect(lambda: self.password_valid(pwd_lb.text(), 1))

        confirm_pwd_lb = QLabel("Confirm Password")
        confirm_pwd_lb.setFixedWidth(140)
        confirm_pwd_lb.setFont(QFont('Arial', 10))

        self.confirm_pwd_txt = QLineEdit()
        self.confirm_pwd_txt.setFixedWidth(180)
        self.confirm_pwd_txt.setFont(QFont('Arial', 10))
        self.confirm_pwd_txt.setEchoMode(QLineEdit.Password)
        self.confirm_pwd_txt.editingFinished.connect(lambda: self.password_valid(confirm_pwd_lb.text(),2))

        chk_box=QtWidgets.QCheckBox()

        chk_box.setText("Show Password")

        chk_box.stateChanged.connect(self.chk_box_change_event)

        email_lb1 = QLabel("Mail ID")
        email_lb1.setFixedWidth(140)
        email_lb1.setFont(QFont('Arial', 10))

        self.mail_txt = QLineEdit()
        self.mail_txt.setFixedWidth(180)
        self.mail_txt.setFont(QFont('Arial', 10))
        self.mail_txt.editingFinished.connect(lambda: self.email_validation(email_lb1.text(), 3))

        email_pwd = QLabel("Password")
        email_pwd.setFixedWidth(140)
        email_pwd.setFont(QFont('Arial', 10))

        self.mail_pwd_txt = QLineEdit()
        self.mail_pwd_txt.setFixedWidth(180)
        self.mail_pwd_txt.setFont(QFont('Arial', 10))
        self.mail_pwd_txt.textChanged.connect(self.password_validation)
        self.mail_pwd_txt.setEchoMode(QLineEdit.Password)

        rx_email_lb = QLabel("Recipient Mail ID")
        rx_email_lb.setFixedWidth(140)
        rx_email_lb.setFont(QFont('Arial', 10))

        self.rx_email_txt = QLineEdit()
        self.rx_email_txt.setFixedWidth(180)
        self.rx_email_txt.setFont(QFont('Arial', 10))
        self.rx_email_txt.editingFinished.connect(lambda: self.email_validation(rx_email_lb.text(), 5))

        submit_btn=QPushButton()
        submit_btn.setFixedWidth(80)
        submit_btn.setText("Submit")
        submit_btn.setFont(QFont('Arial', 10))
        submit_btn.clicked.connect(self.submit_btn_click)

        continue_btn = QtWidgets.QPushButton()
        continue_btn.setFixedWidth(80)
        continue_btn.setText("Continue")
        continue_btn.setFont(QFont('Arial', 10))
        continue_btn.clicked.connect(self.continue_btn_click)

        self.gridLayout.addWidget(usr_lb,0,0)
        self.gridLayout.addWidget(self.user_txt, 0, 1)

        self.gridLayout.addWidget(pwd_lb, 1, 0)
        self.gridLayout.addWidget(self.pwd_txt, 1, 1)

        self.gridLayout.addWidget(confirm_pwd_lb, 2, 0)
        self.gridLayout.addWidget(self.confirm_pwd_txt, 2, 1)

        self.gridLayout.addWidget(email_lb1, 3, 0)
        self.gridLayout.addWidget(self.mail_txt, 3, 1)

        self.gridLayout.addWidget(email_pwd, 4, 0)
        self.gridLayout.addWidget(self.mail_pwd_txt, 4, 1)

        self.gridLayout.addWidget(rx_email_lb, 5, 0)
        self.gridLayout.addWidget(self.rx_email_txt, 5, 1)


        self.gridLayout.addWidget(chk_box, 6, 1)

        self.gridLayout.addWidget(submit_btn, 7, 0)
        self.gridLayout.addWidget(continue_btn, 7, 1)

        self.util = utils()

        self.show()
    def init_fields(self):
        self.user_txt.setText("")
        self.pwd_txt.setText("")
        self.confirm_pwd_txt.setText("")
        self.mail_txt.setText("")
        self.mail_pwd_txt.setText("")
        self.rx_email_txt.setText("")

    def password_validation(self):
        self.count += 1
        remaining = self.max - self.count
        remaining = str(remaining)
        if(self.count < self.max):
            msg_to_display = ""
            if self.mail_pwd_txt.text()=="":
                self.list[4]=value_chk.empty.value
            else:
                self.list[4] = value_chk.valid.value
            if len(msg_to_display)!=0:
                QMessageBox.about(self, 'Information', msg_to_display + remaining + " attempts left")
        else:
            from itt_login_ui import login_window
            self.w = login_window()
            self.w.show()
            self.hide()

    def user_name_validation(self):
        self.count += 1
        remaining = self.max - self.count
        remaining = str(remaining)
        if(self.count <= self.max):
            msg_to_display = ""
            msg_to_display += self.util.user_name_validtion_register \
                (self.list, credentials_file, self.user_txt.text())
            if len(msg_to_display) != 0:
                QMessageBox.about(self, 'Information', msg_to_display + remaining + " attempts left")
        else:
            from itt_login_ui import login_window
            self.w = login_window()
            self.w.show()
            self.hide()

    def password_valid(self,text,number):
        self.count += 1
        remaining = self.max - self.count
        remaining = str(remaining)
        msg_to_display = ""
        if(self.count < self.max):
            if number==1:
                msg_to_display += self.util.password_validation \
                    (self.list, self.pwd_txt.text())
            else:
                msg_to_display += self.util.confirm_password_validation \
                    (self.list,self.pwd_txt.text(),self.confirm_pwd_txt.text())
            if len(msg_to_display) != 0:
                QMessageBox.about(self, 'Information', msg_to_display + remaining + " attempts left")
        else:
            from itt_login_ui import login_window
            self.w = login_window()
            self.w.show()
            self.hide()

    def email_validation(self,mail_label,index):
        self.count += 1
        remaining = self.max - self.count
        remaining = str(remaining)
        if (self.count < self.max):
            if mail_label.__contains__("Recipient"):
                self.rmailid = self.rx_email_txt.text()
                if(self.rmailid == self.mail_txt.text()):
                    self.IDlist = list(self.rmailid.split(","))
                else:
                    msg_to_display = "Please enter same mail id & receipent mail id"
                    if len(msg_to_display) != 0:
                        QMessageBox.about(self, 'Information', msg_to_display + remaining + " attempts left")
                #mail=self.rx_email_txt.text()
            else:
                self.smailid=self.mail_txt.text()
                #mail=self.mail_txt.text()
                self.IDlist = list(self.smailid.split(","))
            """
            else:
                mail=self.mail_txt.text()
            """
            msg_to_display = ""
            if mail_label.__contains__("Recipient"):
                msg_to_display += self.email_rx_validation_with_msg(self.list, self.IDlist, mail_label,self.mail_txt.text(),index)
            else:
                msg_to_display += self.email_validation_with_msg(self.list, self.IDlist,mail_label,index)
            if len(msg_to_display) != 0:
                QMessageBox.about(self, 'Information', msg_to_display+ remaining + " attempts left")
        else:
            from itt_login_ui import login_window
            self.w = login_window()
            self.w.show()
            self.hide()

    def email_rx_validation_with_msg(self,list,mail_id_list,mail_label,mail,index):
        msg_to_return = ""
        # result = valid.email_id_check(mail_id)
        err = 0
        result = 0
        if len(mail_id_list) == 0:
            result = valid.INVALID_INPUT_ERR

        if len(mail_id_list) == 1:
            result = valid.email_id_check(mail_id_list[0])
            if mail_label == mail:
                msg_to_return += "Please enter mail id and receipent mail id"
                list[index] = value_chk.invalid.value
                return msg_to_return

        elif len(mail_id_list) > 1:
            for i in mail_id_list:
                res = valid.email_id_check(i)
                if res is not valid.SUCCESS:
                    err = 1
            if err == 1:
                result = valid.INVALID_INPUT_ERR
            else:
                result = valid.SUCCESS
        if result == valid.SUCCESS:
            if len(mail_id_list) == 0:  # if mail_id == "":
                list[index] = value_chk.empty.value
            else:
                list[index] = value_chk.valid.value
        else:
            msg_to_return += "Invalid {}".format(mail_label)
            list[index] = value_chk.invalid.value
        return msg_to_return

    def email_validation_with_msg(self,list,mail_id_list,mail_label,index):
        msg_to_return = ""
        #result = valid.email_id_check(mail_id)
        err = 0
        result = 0
        if len(mail_id_list) == 1:
            result = valid.email_id_check(mail_id_list[0])
        elif len(mail_id_list) > 1:
            for i in mail_id_list:

                res = valid.email_id_check(i)
                if res is not valid.SUCCESS:
                    err = 1
            if err == 1:
                result = valid.INVALID_INPUT_ERR
            else:
                result = valid.SUCCESS
        elif len(mail_id_list) == 0:
            result = valid.INVALID_INPUT_ERR

        if result == valid.SUCCESS:
            if len(mail_id_list) == 0:#if mail_id == "":
                list[index] = value_chk.empty.value
            else:
                list[index] = value_chk.valid.value
        else:
            msg_to_return += "Invalid {}".format(mail_label)
            list[index] = value_chk.invalid.value
        return msg_to_return

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame,self.title_frame)

    def centerOnScreen(self, frame,frame1):
        frame.move((self.width() - self.frame.width()) / 2, (self.height() - self.frame.height()) / 2)
        frame1.move((self.width() - self.title_frame.width()) / 2, self.title_frame.height())

    def continue_btn_click(self):
        self.open_login_window()

    def submit_btn_click(self):
        msgtxt = "Congratulations, you are successfully registered with \"Thundersoft Issue Tracking Tool\""\
                 + "\n your username and password: " + self.user_txt.text()+" and " + self.pwd_txt.text()
        subject="Thundersoft Issue Tracking Tool Registration"
        msg_to_display=""
        username=self.user_txt.text()
        lb_list = ["Username", "Password","Confirm Password","Email ID","Password","Recipient Mail ID"]
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
                        if self.user_txt.text() != "" and self.pwd_txt.text() != '' and self.mail_txt.text() != '':
                            file_access.writing_username_and_pwd(credentials_file, self.user_txt.text(),
                                                                 self.pwd_txt.text())
                            result_msg=sending_mail(self.mail_txt.text(),self.mail_pwd_txt.text(),
                                                         self.rx_email_txt.text(),msgtxt,subject)
                            if result_msg != "Mail Sent Successfully":
                                QMessageBox.about(self, 'Information', result_msg+",Registered credentials not sent.\nPlease click on Continue to Login")#"You have successfully registered\nPlease click on Continue to Login")
                                self.init_fields()
                            else:
                                QMessageBox.about(self, 'Information',
                                                  result_msg +",You have successfully registered.\nPlease click on Continue to Login")
                                self.init_fields()
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