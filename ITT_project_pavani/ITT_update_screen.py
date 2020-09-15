from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDateTime
import sys

from ITT_Cr_num import *
from ITT_validate import *
from ITT_read_excel import *
from ITT_save_excel import *

class Update(QWidget):
    def __init__(self,cr_index):
        super().__init__()
        self.setWindowTitle("Update Screen")
        self.setMinimumWidth(600)
        self.setMinimumHeight(600)
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 1000)
        # self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)

        self.cr_index = cr_index
        self.cr = read_cr_by_index(cr_index)
        self.update()

    def update(self):
        self.crno_label = QLabel("Cr.no:")
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

        # grid cr label
        self.gridLayout.addWidget(self.crno_label, 0, 0)
        # grid cr entry
        self.gridLayout.addWidget(self.crno_entry, 0, 1)

        # grid cr label
        self.gridLayout.addWidget(self.crno_label, 0, 0)
        # grid cr entry
        self.gridLayout.addWidget(self.crno_entry, 0, 1)

        # label assignee
        self.assignee_label = QLabel("Assignee:")
        self.assignee_label.setFont(QFont('Arial', 10))
        # entry assignee
        self.assignee_entry = QLineEdit()
        self.assignee = read_asignee_with_cr(self.cr_index)
        self.assignee_entry.setText(self.assignee)
        self.assignee_entry.setFont(QFont('Arial', 10))

        # grid label assignee
        self.gridLayout.addWidget(self.assignee_label, 1, 0)
        # grid entry assignee
        self.gridLayout.addWidget(self.assignee_entry, 1, 1)

        # label title
        self.title_label = QLabel("Title:")
        self.title_label.setFont(QFont('Arial', 10))
        # entry title
        self.title_entry = QLineEdit()
        self.title = read_title_with_cr(self.cr_index)
        self.title_entry.setText(self.title)
        self.title_entry.setFont(QFont('Arial', 10))

        # grid label title
        self.gridLayout.addWidget(self.title_label, 2, 0)
        # grid entry assignee
        self.gridLayout.addWidget(self.title_entry, 2, 1)

        # label cr state
        self.cr_state_label = QLabel("Cr State:")
        self.cr_state_label.setFont(QFont('Arial', 10))
        # entry_cr_state
        self.cr_state_entry = QComboBox(self)
        self.cr_state_entry.setFont(QFont('Arial', 10))
        self.cr_state_entry.setStyleSheet("QComboBox"
                                      "{"
                                      "background-color: white;"
                                      "}")
        self.cr_state_entry.addItem("Open")
        self.cr_state_entry.addItem("Analysis")
        self.cr_state_entry.addItem("Closed")
        self.cr_state_entry.addItem("In-progress")
        self.cr_state_entry.addItem("Reopen")
        self.prev_cr_state = read_cr_with_cr(self.cr_index)
        self.crindex = self.cr_state_entry.findText(self.prev_cr_state)
        self.cr_state_entry.setCurrentIndex(self.crindex)

        self.cr_state_entry.currentIndexChanged.connect(self.cronChanged)

        # grid cr state label
        self.gridLayout.addWidget(self.cr_state_label, 4, 0)
        # grid cr state entry
        self.gridLayout.addWidget(self.cr_state_entry, 4, 1)
        #si state
        self.si_state_label = QLabel("SI State")
        self.si_state_label.setFont(QFont('Arial', 10))
        #entry
        self.si_state = QComboBox(self)
        self.si_state.setStyleSheet("QComboBox"
                                          "{"
                                          "background-color: white;"
                                          "}")
        self.si_state.addItem("Open")
        self.si_state.addItem("Analysis")
        self.si_state.addItem("Fix")
        self.si_state.addItem("Withdrawn")
        self.si_state.addItem("Duplicate")
        self.si_state.addItem("Ready")
        self.si_state.addItem("Built")
        self.si_state.setFont(QFont('Arial', 10))
        self.si_prev_state = read_si_with_cr(self.cr_index)
        self.si_index = self.si_state.findText(self.si_prev_state)
        self.si_state.setCurrentIndex(self.si_index)
        self.si_state.currentIndexChanged.connect(self.onChanged)

        #grid for si state
        self.gridLayout.addWidget(self.si_state_label,3,0)
        self.gridLayout.addWidget(self.si_state,3,1)

        # label Issue type
        self.issuetype_label = QLabel("Issue Type:")
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
        self.gridLayout.addWidget(self.issuetype_label, 5, 0)
        # grid issue type entry
        self.gridLayout.addWidget(self.issuetype_entry, 5, 1)

        # issue reason entry
        self.issue_reason_entry = QLineEdit(self)
        self.issue_reason_entry.setFont(QFont('Arial', 10))
        self.issue_reason_entry.setReadOnly(True)
        self.issue_reason_entry.setStyleSheet("QLineEdit"
                                              "{"
                                              "background-color: #DBDBDB;"
                                              "}")
        # grid issue reason
        self.gridLayout.addWidget(self.issue_reason_entry, 6, 1)

        # label Description
        self.des_label = QLabel("Description:")
        self.des_label.setFont(QFont('Arial', 10))
        # entry Description
        self.des_entry = QTextEdit(self)
        self.des_entry.setFont(QFont('Arial', 10))
        self.des_entry.setFixedHeight(130)
        self.des = read_des_with_cr(self.cr_index)
        print(self.des)
        self.des_entry.setText(self.des)

        # grid Description label
        self.gridLayout.addWidget(self.des_label, 7, 0)
        # grid Description entry
        self.gridLayout.addWidget(self.des_entry, 7, 1)

        # domain
        self.domain_label = QLabel("Domain/Tech Area:")
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
        print(self.domain)
        self.domain_index = self.domain_entry.findText(self.domain)
        print(self.domain_index)
        self.domain_entry.setCurrentIndex(self.domain_index)
        self.domain_entry.currentIndexChanged.connect(self.onchangeissue)

        # grid domain label
        self.gridLayout.addWidget(self.domain_label, 8, 0)
        # grid domain entry
        self.gridLayout.addWidget(self.domain_entry, 8, 1)

        # git/gerrit
        self.git_label = QLabel("Git/Gerrit link:")
        self.git_label.setFont(QFont('Arial', 10))
        # git entry
        self.git_entry = QLineEdit(self)
        self.git_entry.setReadOnly(True)
        self.git_entry.setStyleSheet("QLineEdit"
                                     "{"
                                     "background-color: #DBDBDB	;"
                                     "}")

        # grid git label
        self.gridLayout.addWidget(self.git_label, 9, 0)
        # grid git entry
        self.gridLayout.addWidget(self.git_entry, 9, 1)

        # build id
        self.build_label = QLabel("Build Id:")
        self.build_label.setFont(QFont('Arial', 10))
        # build entry
        self.build_entry = QLineEdit(self)
        self.build = read_build_with_cr(self.cr_index)
        self.build_entry.setText(self.build)
        self.build_entry.setFont(QFont('Arial', 10))

        # grid git label
        self.gridLayout.addWidget(self.build_label, 10, 0)
        # grid git entry
        self.gridLayout.addWidget(self.build_entry, 10, 1)

        # Create on
        self.createon_label = QLabel("Created on:")
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
        self.lastmodi_label = QLabel("Last Modified: ")
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

        # last modified
        self.gridLayout.addWidget(self.lastmodi_label, 12, 0)
        # last modifies entry
        self.gridLayout.addWidget(self.lastmodi_entry, 12, 1)

        # submit button
        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_click)

        # grid button
        self.gridLayout.addWidget(self.submit, 13, 0)

        # view button
        self.Exit_but = QPushButton()
        self.Exit_but.setText("Exit")
        self.Exit_but.clicked.connect(self.Exit_but_clicked)
        # grid view button
        self.gridLayout.addWidget(self.Exit_but, 13, 2)

        self.show()

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self,frame):
        frame.move(int((self.width()-self.frame.width()) / 2), int((self.height()-self.frame.height()) / 2))

    def cronChanged(self):
        prev_state = self.prev_cr_state
        state = self.cr_state_entry.currentText()

        if(prev_state == "Closed"):
            if(state == "Reopen"):
                self.si_state.setCurrentIndex(0)

    def onchangeissue(self):
        prev_state = self.issue_type
        state = self.issuetype_entry.currentText()
        if(prev_state == "Internal"):
            if(state == "Bug"):
                self.issue_reason_entry.setReadOnly(False)
                self.issue_reason_entry.setStyleSheet("QLineEdit"
                                                          "{"
                                                          "background-color: white;"
                                                          "}")

    def onChanged(self):
        state = self.si_state.currentText()
        prev_state = self.si_prev_state

        if(prev_state == "Open"):
            if(state == "Analysis"):
                self.cr_state_entry.setCurrentIndex(1)

        if(prev_state == "Analysis"):
            if(state == "Fix"):
                self.cr_state_entry.setCurrentIndex(3)
                self.git_entry.setReadOnly(False)
                self.git_entry.setStyleSheet("QLineEdit"
                                                  "{"
                                                  "background-color: white;"
                                                  "}")

            if(state == "Withdrawn" or state == "Duplicate"):
                self.issue_reason_entry.setReadOnly(False)
                self.issue_reason_entry.setStyleSheet("QLineEdit"
                                                      "{"
                                                      "background-color: white;"
                                                      "}")
                self.cr_state_entry.setCurrentIndex(2)

        if(prev_state == "Fix"):
            if(state == "Ready"):
                self.cr_state_entry.setCurrentIndex(4)

        if(prev_state == "Ready"):
            if (state == "Build"):
                self.cr_state_entry.setCurrentIndex(2)

    def Exit_but_clicked(self):
            from ITT_home_screen import Main_window
            self.w = Main_window()
            self.w.show()
            self.hide()

    def submit_click(self):
        print("clicked")
        cr_no = self.crno_entry.text()
        print(cr_no)
        title = self.title_entry.text()
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
                      'Domain': domain, 'Issue Type': issue_type, 'GIT/Gerrit link': git_id,
                      'Build ID': build_id, 'Create On': create_on, 'Last Modified On': last_modi, 'History': " "}
        #title_ret = title_validate(title)
        # assignee_ret = assignee_validate(assignee)
        #des_ret = des_validate(des)
        #cr_ret = cr_state_validate(status)
        #domain_ret = domain_validate(domain)
        #build_ret = build_validation(build_id)
        print("update")
        save_update_info(combo_dict,self.cr,self.cr_index)

if __name__ == "__main__":
    app =QApplication(sys.argv)
    obj = Update(0)
    sys.exit(app.exec_())