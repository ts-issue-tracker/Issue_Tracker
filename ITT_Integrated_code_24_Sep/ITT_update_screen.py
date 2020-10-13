from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDateTime
import sys

from ITT_Cr_num import *
from ITT_validate import *
from ITT_read_excel import *
from ITT_save_excel import *
from ITT_validate_update import *
from ITT_display import *

from PyQt5.QtCore import QDateTime,QFileInfo
from PyQt5.QtGui import QPalette,QImage,QPageSize,QBrush,QPixmap
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets

class Update(QWidget):
    def __init__(self,cr_index):
        super().__init__()
        self.setWindowTitle("Update Screen")
        self.setMinimumWidth(1920)
        self.setMinimumHeight(1000)

        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 800)
        # self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)

        oImage = QImage("image2.jpg")
        sImage = oImage.scaled(QSize(1000, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.img_frame = QFrame(self)
        self.img_frame.setFixedSize(350, 150)
        # self.img_frame.setFrameShape(QFrame.StyledPanel)
        self.img_gridLayout = QGridLayout(self.img_frame)
        self.img_gridLayout.setContentsMargins(20, 20, 20, 20)
        label = QLabel(self)
        pixmap = QPixmap('thundersoft.png')
        label.setPixmap(pixmap)
        self.img_gridLayout.addWidget(label)

        self.frame_three = QFrame(self)
        self.gridLayout_three = QGridLayout(self.frame_three)
        self.frame_three.setFixedSize(450, 60)
        self.gridLayout.addWidget(self.frame_three, 14, 0)

        self.frame_1 = QFrame(self)
        self.gridLayout_1 = QGridLayout(self.frame_1)
        self.frame_1.setFixedSize(450, 60)
        self.gridLayout.addWidget(self.frame_1, 15, 0)

        self.history_dict = {}
        self.cr_index = cr_index
        self.cr = read_cr_by_index(cr_index)
        self.si_new = ""
        self.cr_new = ""
        self.si_prev = ""
        self.si_new = ""
        self.path = ""

        self.cr_ret = ["",True]
        self.git_ret = ["",True]
        self.issue_ret= ["",True]
        self.buildid = ["",True]

        self.update()

    def update(self):
        self.crno_label = QLabel("CR")
        self.crno_label.setFont(QFont('Arial', 10))

        # entry crno
        self.crno_entry = QLineEdit()
        self.crno_entry.setText(self.cr)
        self.crno_entry.setReadOnly(True)
        self.crno_entry.setStyleSheet("QLineEdit"
                                      "{"
                                      "background-color: #DBDBDB;"
                                      "}")
        self.crno_entry.setFont(QFont('Arial', 10))
        self.crno_entry.setFixedWidth(200)

        # grid cr label
        self.gridLayout.addWidget(self.crno_label, 0, 0)
        # grid cr entry
        self.gridLayout.addWidget(self.crno_entry, 0, 1)

        # label title
        self.title_label = QLabel("Title")
        self.title_label.setFont(QFont('Arial', 10))
        # entry title
        self.title_entry = QTextEdit()
        self.title = read_title_with_cr(self.cr_index)
        self.title_entry.setPlainText(self.title)
        self.title_entry.setFixedHeight(50)
        self.title_entry.textChanged.connect(self.title_change)
        self.title_entry.setFont(QFont('Arial', 10))

        # grid label title
        self.gridLayout.addWidget(self.title_label, 1, 0)
        # grid entry assignee
        self.gridLayout.addWidget(self.title_entry, 1, 1)

        # label Description
        self.des_label = QLabel("Description")
        self.des_label.setFont(QFont('Arial', 10))
        # entry Description
        self.des_entry = QTextEdit(self)
        self.des_entry.setFont(QFont('Arial', 10))
        self.des_entry.setFixedHeight(130)
        self.des = read_des_with_cr(self.cr_index)
        self.des_entry.setPlainText(self.des)
        self.des_entry.textChanged.connect(self.des_change)
        # grid Description label
        self.gridLayout.addWidget(self.des_label, 2, 0)
        # grid Description entry
        self.gridLayout.addWidget(self.des_entry, 2, 1)

        # label assignee
        self.assignee_label = QLabel("Assignee")
        self.assignee_label.setFont(QFont('Arial', 10))
        # entry assignee
        self.assignee_entry = QLineEdit()
        self.assignee = read_asignee_with_cr(self.cr_index)
        self.assignee_entry.setText(self.assignee)
        self.assignee_entry.editingFinished.connect(self.assignee_change)
        self.assignee_entry.setFont(QFont('Arial', 10))

        # grid label assignee
        self.gridLayout.addWidget(self.assignee_label, 3, 0)
        # grid entry assignee
        self.gridLayout.addWidget(self.assignee_entry, 3, 1)

        # label cr state
        self.cr_state_label = QLabel("CR State")
        self.cr_state_label.setFont(QFont('Arial', 10))
        # entry_cr_state
        self.cr_state_entry = QComboBox(self)
        self.cr_state_entry.setFont(QFont('Arial', 10))
        self.cr_state_entry.setStyleSheet("QComboBox"
                                          "{"
                                          "background-color: white;"
                                          "}")

        self.prev_cr_state = read_cr_with_cr(self.cr_index)
        self.cr_state_entry.addItem(self.prev_cr_state)

        if(self.cr_state_entry.currentText() == "Closed"):
            self.cr_state_entry.addItem("Reopen")
            self.cr_state_entry.setEnabled(True)
        self.cr_state_entry.currentIndexChanged.connect(self.cronChanged)

        # grid cr state label
        self.gridLayout.addWidget(self.cr_state_label, 5, 0)
        # grid cr state entry
        self.gridLayout.addWidget(self.cr_state_entry, 5, 1)
        #si state
        self.si_state_label = QLabel("SI State")
        self.si_state_label.setFont(QFont('Arial', 10))
        #entry
        self.si_state = QComboBox(self)
        self.si_state.setStyleSheet("QComboBox"
                                    "{"
                                    "background-color: white;"
                                    "}")

        self.si_state.setFont(QFont('Arial', 10))
        #self.si_state.clear()
        self.si_prev_state = read_si_with_cr(self.cr_index)
        self.si_state.addItem(self.si_prev_state)
        if(self.si_state.currentText() == "Open"):
                self.si_state.addItem("Analysis")
        if(self.si_state.currentText() == "Analysis"):
            self.si_state.addItem("Fix")
            self.si_state.addItem("Withdrawn")
            self.si_state.addItem("Duplicate")
        if(self.si_state.currentText() == "Fix"):
            self.si_state.addItem("Ready")
        if(self.si_state.currentText() == "Ready"):
            self.si_state.addItem("Built")

        self.si_state.currentIndexChanged.connect(self.onChanged)
        #grid for si state
        self.gridLayout.addWidget(self.si_state_label,4,0)
        self.gridLayout.addWidget(self.si_state,4,1)
        if(self.si_state.currentText() == "Built"):
            self.si_state.setEnabled(False)

        # domain
        self.domain_label = QLabel("Domain/Tech Area")
        self.domain_label.setFont(QFont('Arial', 10))
        # domain entry
        self.domain_entry = QComboBox(self)
        self.domain_entry.setFont(QFont('Arial', 10))
        self.domain_entry.setStyleSheet("QComboBox"
                                        "{"
                                        "background-color: white;"
                                        "}")
        self.domain_entry.addItem("Audio")
        self.domain_entry.addItem("Camera")
        self.domain_entry.addItem("Video")

        self.domain = read_domain_with_cr(self.cr_index)
        self.domain_index = self.domain_entry.findText(self.domain)
        self.domain_entry.setCurrentIndex(self.domain_index)
        self.domain_entry.currentIndexChanged.connect(self.domainchange)
        # grid domain label
        self.gridLayout.addWidget(self.domain_label, 6, 0)
        # grid domain entry
        self.gridLayout.addWidget(self.domain_entry, 6, 1)


        # label Issue type
        self.issuetype_label = QLabel("Issue Type")
        self.issuetype_label.setFont(QFont('Arial', 10))

        # entry Issue type
        self.issuetype_entry = QComboBox(self)
        self.issuetype_entry.setFont(QFont('Arial', 10))
        self.issuetype_entry.setStyleSheet("QComboBox"
                                           "{"
                                           "background-color: white;"
                                           "}")
        self.issuetype_entry.addItem("Bug")
        self.issuetype_entry.addItem("Internal")
        self.issuetype_entry.addItem("Blacklisting")
        self.issue_type = read_issuetype_with_cr(self.cr_index)
        self.it_index = self.issuetype_entry.findText(self.issue_type)
        self.issuetype_entry.setCurrentIndex(self.it_index)
        self.issuetype_entry.currentIndexChanged.connect(self.onchangeissue)
        # grid Issue type label
        self.gridLayout.addWidget(self.issuetype_label, 7, 0)
        # grid issue type entry
        self.gridLayout.addWidget(self.issuetype_entry, 7, 1)

        # issue reason entry
        self.issue_reason_entry = QLineEdit(self)
        self.issue_reason_entry.setFont(QFont('Arial', 10))
        self.issue_reason_entry.setReadOnly(True)
        self.issue_reason_entry.setStyleSheet("QLineEdit"
                                              "{"
                                              "background-color: #DBDBDB;"
                                              "}")
        # grid issue reason
        self.gridLayout.addWidget(self.issue_reason_entry, 8, 1)

        # git/gerrit
        self.git_label = QLabel("Git/Gerrit link")
        self.git_label.setFont(QFont('Arial', 10))
        # git entry
        self.git_entry = QLineEdit(self)
        self.git = read_git_with_cr(self.cr_index)
        self.git_entry.setReadOnly(True)
        self.git_entry.setText(self.git)
        self.git_entry.setFont(QFont('Arial', 10))
        if (self.si_state.currentText() == 'Fix'):
            self.git = read_git_with_cr(self.cr_index)
            self.git_entry.textChanged.connect(self.git_change)
            self.git_entry.setText(self.git)
            self.git_entry.setReadOnly(False)
        else:
            self.git_entry.setStyleSheet("QLineEdit"
                                         "{"
                                         "background-color: #DBDBDB	;"
                                         "}")

        # grid git label
        self.gridLayout.addWidget(self.git_label, 9, 0)
        # grid git entry
        self.gridLayout.addWidget(self.git_entry, 9, 1)

        # build id
        self.build_label = QLabel("Build Id")
        self.build_label.setFont(QFont('Arial', 10))
        # build entry
        self.build_entry = QLineEdit(self)
        self.build = read_build_with_cr(self.cr_index)
        self.build_entry.setText(self.build)
        self.build_entry.setReadOnly(True)
        self.build_entry.setFont(QFont('Arial', 10))
        self.build_entry.setStyleSheet("QLineEdit"
                                       "{"
                                       "background-color: #DBDBDB;"
                                       "}")
        self.build_entry.editingFinished.connect(self.build_change)
        # grid git label
        self.gridLayout.addWidget(self.build_label, 10, 0)
        # grid git entry
        self.gridLayout.addWidget(self.build_entry, 10, 1)

        # Create on
        self.createon_label = QLabel("Created on")
        self.createon_label.setFont(QFont('Arial', 10))
        # create_On entry
        self.createon_entry = QLineEdit(self)
        self.datetime = read_create_date_index(self.cr_index)
        print(self.datetime)
        self.createon_entry.setText(self.datetime)
        self.createon_entry.setFont(QFont('Arial', 10))
        self.createon_entry.setReadOnly(True)
        self.createon_entry.setStyleSheet("QLineEdit"
                                          "{"
                                          "background-color: #DBDBDB	;"
                                          "}")
        # Create on
        self.gridLayout.addWidget(self.createon_label, 11, 0)
        # Create on entry
        self.gridLayout.addWidget(self.createon_entry, 11, 1)

        # last modified
        self.lastmodi_label = QLabel("Last Modified ")
        self.lastmodi_label.setFont(QFont('Arial', 10))
        # last modified entry
        self.lastmodi_entry = QLineEdit(self)
        self.lastdate = QDateTime.currentDateTime()
        self.lastmodi_entry.setText(self.lastdate.toString('dd.MM.yyyy, hh:mm:ss'))
        self.lastmodi_entry.setFont(QFont('Arial', 10))
        self.lastmodi_entry.setReadOnly(True)
        self.lastmodi_entry.setStyleSheet("QLineEdit"
                                          "{"
                                          "background-color: #DBDBDB;"
                                          "}")
        self.history_dict.update({"last date": self.lastmodi_entry.text()})

        # last modified
        self.gridLayout.addWidget(self.lastmodi_label, 12, 0)
        # last modifies entry
        self.gridLayout.addWidget(self.lastmodi_entry, 12, 1)

        # submit button
        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.setFixedWidth(100)
        self.submit.clicked.connect(self.submit_click)

        # grid button
        self.gridLayout_three.addWidget(self.submit, 0, 0)

        # view button
        self.Upload_but = QPushButton()
        self.Upload_but.setText("Attachment")
        self.Upload_but.setFixedWidth(100)

        self.Upload_but.clicked.connect(self.Upload_but_clicked)
        # grid view button
        self.gridLayout_three.addWidget(self.Upload_but, 0, 1)

        # view button
        self.Exit_but = QPushButton()
        self.Exit_but.setText("Exit")
        self.Exit_but.setFixedWidth(100)
        self.Exit_but.clicked.connect(self.Exit_but_clicked)
        # grid view button
        self.gridLayout_three.addWidget(self.Exit_but, 0, 2)

        self.showMaximized()
        self.show()

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame, self.img_frame)

    def centerOnScreen(self, frame, frame2):
        frame.move(int((self.width() - self.frame.width()) / 2), int((self.height() - self.frame.height()) / 2))
        frame2.move((self.width() - self.img_frame.width()), 1)

    def Upload_but_clicked(self):
        try:
            filename = QFileDialog.getOpenFileName()
            if filename[0].endswith(('.doc', '.docx', '.txt', '.xlsx', '.csv', '.log', '.xls')):
                info = QFileInfo(filename[0])
                size = info.size()
                if (size > 5000000):
                    msg = QMessageBox()
                    msg.setWindowTitle("Information")
                    msg.setText("Supports upto 5MB")
                    x = msg.exec_()
                else:
                    self.label = QLabel(filename[0])
                    self.label.setWordWrap(True)
                    self.gridLayout_1.addWidget(self.label, 1, 1)
                    self.path = filename[0]
            else:
                print("Does not supports")
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Only supports '.doc','.docx','.txt','.xlsx','.csv','.log','.xls")
                x = msg.exec_()
        except FileNotFoundError:
            print("Wrong file or file path")

    def git_change(self):
        print("changing git id")
        self.git_val = self.git_entry.text()
        print(self.git_val)
        ret = git_validate_update(self.git_val)
        if(ret == True):
            self.history_dict.update({"git/gerrit":self.git_val})
        else:
            print("enter valid git link")
        gitid = self.git_entry.text()
        print("print git",gitid,len(gitid))
        self.git_ret = git_validate(gitid)
        print("after validate",self.git_ret)

    def cronChanged(self):
        prev_state = self.prev_cr_state
        state = self.cr_state_entry.currentText()
        self.cr_prev = prev_state
        self.cr_new = state

        self.history_dict.update({"cr state":state})
        if(prev_state == "Closed"):
            self.cr_ret = bt_cr_validate(self.cr_prev, self.cr_new)
            print("CR main",self.cr_ret)
            if(state == "Reopen"):
                self.si_state.clear()
                self.si_state.addItem("Open")

    def domainchange(self):
        self.domain_val = self.domain_entry.currentText()
        ret = domain_validate(self.domain_entry.currentText())
        if(ret == True):
            self.history_dict.update({'domain': self.domain_val})
        else:
            print("Problem in domain")

    def assignee_change(self):
        self.assignee_val = self.assignee_entry.text()
        ret = assignee_validate_update(self.assignee_val)
        if ret == True:
            self.history_dict.update({'assignee':self.assignee_val})
        else:
            print("No Assignee")

    def build_change(self):
        self.build_prev = read_build_with_cr(self.cr_index)
        self.build_new_val = self.build_entry.text()
        ret = build_validate_update(self.build_prev,self.build_new_val)
        print(self.build_prev,self.build_new_val)
        if(self.build_prev == self.build_new_val):
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("Please change the build id")
            x = msg.exec_()
        print("build validation")
        if ret == True:
            self.history_dict.update({'buildid':self.build_new_val})
        else:
            print("Build id is not valid")
        print("button build validate")
        self.buildid = bt_build_validate_update(self.build_prev,self.build_new_val)
        print(self.buildid)

    def title_change(self):
        self.title_val = self.title_entry.toPlainText()
        ret = title_validate_update(self.title_val)
        print(self.title_val)
        if ret == True:
            self.history_dict.update({'title': self.title_val})
        else:
            print("Title not valid")

    def des_change(self):
        self.des_val = self.des_entry.toPlainText()
        ret = des_validate_update(self.des_val)
        if(ret == True):
            self.history_dict.update({'description': self.des_val})
        else:
            print("Description not valid")

    def onchangeissue(self):
        prev_state = self.issue_type
        state = self.issuetype_entry.currentText()
        self.history_dict.update({"issue type": state})

        if(prev_state == "Internal"):
            if(state == "Bug"):
                self.issue_reason_entry.setReadOnly(False)
                self.issue_reason_entry.setStyleSheet("QLineEdit"
                                                          "{"
                                                          "background-color: white;"
                                                          "}")
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Please give the reason for change")
                x = msg.exec_()
                self.issue_reason_entry.textChanged.connect(self.issue_reason_changed)

            if (state == "Blacklisting"):
                    self.issue_reason_entry.setReadOnly(False)
                    self.issue_reason_entry.setStyleSheet("QLineEdit"
                                                          "{"
                                                          "background-color: white;"
                                                          "}")
                    msg = QMessageBox()
                    msg.setWindowTitle("Information")
                    msg.setText("Please give the reason for change")
                    x = msg.exec_()
                    self.issue_reason_entry.textChanged.connect(self.issue_reason_changed)

        if (prev_state == "Bug"):
            if (state == "Internal"):
                self.issue_reason_entry.setReadOnly(False)
                self.issue_reason_entry.setStyleSheet("QLineEdit"
                                                      "{"
                                                      "background-color: white;"
                                                      "}")
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Please give the reason for change")
                x = msg.exec_()
                self.issue_reason_entry.textChanged.connect(self.issue_reason_changed)

            if(state == "Blacklisting"):
                self.issue_reason_entry.setReadOnly(False)
                self.issue_reason_entry.setStyleSheet("QLineEdit"
                                                      "{"
                                                      "background-color: white;"
                                                      "}")
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Please give the reason for change")
                x = msg.exec_()
                self.issue_reason_entry.textChanged.connect(self.issue_reason_changed)
        if(prev_state == "Blacklisting"):
            if(state == "bug"):
                self.issue_reason_entry.setReadOnly(False)
                self.issue_reason_entry.setStyleSheet("QLineEdit"
                                                      "{"
                                                      "background-color: white;"
                                                      "}")
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Please give the reason for change")
                x = msg.exec_()
                self.issue_reason_entry.textChanged.connect(self.issue_reason_changed)
            else:
                self.issue_reason_entry.setReadOnly(False)
                self.issue_reason_entry.setStyleSheet("QLineEdit"
                                                      "{"
                                                      "background-color: white;"
                                                      "}")
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Please give the reason for change")
                x = msg.exec_()
                self.issue_reason_entry.textChanged.connect(self.issue_reason_changed)
        self.issue_ret = bt_issue_reason_validate(self.issue_reason_entry.text())
        self.issue_reason_entry.setStyleSheet("QLineEdit"
                                      "{"
                                      "background-color: white;"
                                      "}")
        print(self.issue_ret,"at up")

    def issue_reason_changed(self):
        print("issue change 1")
        self.issue_reason = self.issue_reason_entry.text()
        print("issue reason",self.issue_reason)
        ret = issue_reason_validate_update(self.issue_reason)
        if(ret == True):
            self.history_dict.update({"issue Reason":self.issue_reason})
        else:
            print("Issue at reason change")
        print("button validate issue reason")
        self.issue_ret = bt_issue_reason_validate(self.issue_reason_entry.text())
        print(self.issue_ret)
        print("issue complete")

    def onChanged(self):
        state = self.si_state.currentText()
        prev_state = self.si_prev_state
        self.si_prev = prev_state
        self.si_new = state
        if(prev_state == "Open"):
            if(state == "Analysis"):
                self.cr_state_entry.clear()
                self.cr_state_entry.addItem("Analysis")

        if(prev_state == "Analysis"):
            if(state == "Fix"):
                self.cr_state_entry.clear()
                self.cr_state_entry.addItem("In-progress")
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Please enter GIT id")
                x = msg.exec_()
                self.git_entry.setReadOnly(False)
                self.git_entry.setStyleSheet("QLineEdit"
                                                      "{"
                                                      "background-color: white;"
                                                      "}")
                #self.cr_state_entry.setEnabled(False)
                self.git_entry.setStyleSheet("QLineEdit"
                                                      "{"
                                                      "background-color: white;"
                                                      "}")
                self.git_ret = git_validate(self.issue_reason_entry.text())
                self.git_entry.textChanged.connect(self.git_change)

            elif(state == "Withdrawn" or state == "Duplicate"):
                self.cr_state_entry.clear()
                self.cr_state_entry.addItem("Closed")
                self.issue_reason_entry.setReadOnly(False)
                self.issue_reason_entry.setStyleSheet("QLineEdit"
                                             "{"
                                             "background-color: white;"
                                             "}")

                if(len(self.issue_reason_entry.text()) == 0):
                    msg = QMessageBox()
                    msg.setWindowTitle("Information")
                    msg.setText("Please enter Reason for Withdrawn or Duplicate")
                    x = msg.exec_()

        if(prev_state == "Fix"):
            if(state == "Ready"):
                self.cr_state_entry.clear()
                self.cr_state_entry.addItem("In-progress")

        if(prev_state == "Ready"):
            if(state == "Built"):
                self.cr_state_entry.clear()
                self.cr_state_entry.addItem("Closed")
                self.build_prev_val = read_build_with_cr(self.cr_index)
                self.build_new_val = self.build_entry.text()
                if(self.build_new_val == self.build_prev_val):
                    msg = QMessageBox()
                    msg.setWindowTitle("Information")
                    msg.setText("Please change the build id")
                    x = msg.exec_()
                    print("built")
                    self.build_entry.setReadOnly(False)
                    self.build_entry.setStyleSheet("QLineEdit"
                                                 "{"
                                                 "background-color: white;"
                                                 "}")
                    self.buildid = bt_build_validate_new(self.build_prev_val,self.build_new_val)
                self.cr_state_entry.setEnabled(False)
                print("complete build")
        self.history_dict.update({"si state": state})

    def Exit_but_clicked(self):
        from itt_main_ui import main_window
        self.w = main_window()
        self.w.show()
        self.hide()

    def submit_click(self):
        print("clicked")
        cr_no = self.crno_entry.text()
        print(cr_no)
        title = self.title_entry.toPlainText()
        print(title)
        des = self.des_entry.toPlainText()
        print(des)
        assignee = self.assignee_entry.text()
        print("si")
        si = self.si_state.currentText()
        print("after")
        status = self.cr_state_entry.currentText()
        domain = self.domain_entry.currentText()
        issue_type = self.issuetype_entry.currentText()
        git_id = self.git_entry.text()
        build_id = self.build_entry.text()
        create_on = self.createon_entry.text()
        last_modi = self.lastmodi_entry.text()
        print("data collected")
        combo_dict = {'CR': cr_no, 'Title': title, 'Description': des, 'Assignee': assignee, 'State': status,
                      'Software Image': si,
                      'Domain': domain, 'Issue Type': issue_type, 'GIT commit id/Gerrit link': git_id,
                      'Build ID': build_id, 'Create On': create_on, 'Last Modified On': last_modi, 'History': " "}
        print("combo",combo_dict)
        print("update")
        assignee_ret = bt_assignee_validate_update(assignee)
        print("main", assignee_ret[0], assignee_ret[1])
        title_ret = bt_title_validate_update(title)
        print("main", title_ret[0], title_ret[1])
        des_ret = bt_des_validate(des)
        print("main", des_ret[0], des_ret[1])
        build_ret = bt_build_validate(build_id)
        print("main", build_ret[0], build_ret[1])
        print("calling")
        print(self.si_prev,self.si_new,self.cr_new)
        si_ret = bt_si_validate(self.si_prev,self.si_new,self.cr_new)
        print(si_ret)
        print("main",si_ret[0],si_ret[1])
        print("main",self.git_ret[0],self.git_ret[1])
        print(type(self.cr_ret))
        domain_ret = bt_domain_validate(self.domain_entry.currentText())
        print("domain",des_ret)
        print("git at save",self.git_ret[0],self.git_ret[1])

        dis_ret = display(title_ret, des_ret, build_ret, assignee_ret,si_ret,self.cr_ret,self.git_ret,domain_ret,self.issue_ret,self.buildid)
        if (len(self.path) == 0):
            self.path = ""
        if(dis_ret == True):
            save_update_info(combo_dict,self.cr,self.cr_index,self.history_dict,self.path)
            print("call")
            self.open_cr_view_screen()
        else:
            print("something went wrong")

    def open_cr_view_screen(self):
        print("view screen")
        from ITT_view_cr_screen import view_cr_window
        print(type(self.issue_reason_entry.text()))
        self.w = view_cr_window(self.cr_index,self.cr,self.issue_reason_entry.text())
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app =QApplication(sys.argv)
    obj = Update(0)
    sys.exit(app.exec_())