from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QFrame,QHBoxLayout,QGridLayout
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDateTime

import sys
import textwrap

from ITT_validate import *
from ITT_save_excel import save_in_excel
from ITT_read_excel import read_new_no

class Create_cr(QWidget):
    print("Create")
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Issue tracker")
        self.frame = QFrame(self)
        self.frame.setFixedSize(500,1000)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)

        self.gridLayout = QGridLayout(self.frame)
        self.create_an_issue()

    def create_an_issue(self):
        # label crno
        self.crno_label = QLabel("Cr.no:")
        self.crno_label.setFont(QFont('Arial', 10))

        # entry crno
        self.crno_entry = QLineEdit()
        self.cr_no = read_new_no()
        self.crno_entry.setText(self.cr_no)
        self.crno_entry.setReadOnly(True)
        self.crno_entry.setStyleSheet("QLineEdit"
                                     "{"
                                     "background-color: #DBDBDB;"
                                     "}")
        self.crno_entry.setFont(QFont('Arial', 10))

        #grid cr label
        self.gridLayout.addWidget(self.crno_label,0,0)
        #grid cr entry
        self.gridLayout.addWidget(self.crno_entry, 0, 1)

        # label assignee
        self.assignee_label = QLabel("Assignee:")
        self.assignee_label.setFont(QFont('Arial', 10))
        # entry assignee
        self.assignee_entry = QLineEdit()
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
        self.title_entry.setFont(QFont('Arial', 10))

        #grid label title
        self.gridLayout.addWidget(self.title_label,2,0)
        #grid entry assignee
        self.gridLayout.addWidget(self.title_entry,2,1)

        # label cr state
        self.cr_state_label = QLabel("Cr State:")
        self.cr_state_label.setFont(QFont('Arial', 10))
        # entry_cr_state
        self.cr_state_entry = QComboBox(self)
        self.cr_state_entry.setFont(QFont('Arial', 10))
        self.cr_state_entry.addItem("Open")

        #grid cr state label
        self.gridLayout.addWidget(self.cr_state_label,4,0)
        #grid cr state entry
        self.gridLayout.addWidget(self.cr_state_entry,4,1)

        # label Si state
        #self.si_state_label = QLabel("SI State:")
        #self.si_state_label.setFont(QFont('Arial', 10))
        # entry_si_state
        #self.si_state_entry = QComboBox(self)
        #self.si_state_entry.setFont(QFont('Arial', 10))
        #self.si_state_entry.addItem("Open")

        # grid si state label
        #self.gridLayout.addWidget(self.si_state_label, 4, 0)
        # grid si state entry
        #self.gridLayout.addWidget(self.si_state_entry, 4, 1)

        # label Si state
        self.si_label = QLabel("SI:")
        self.si_label.setFont(QFont('Arial', 10))
        # entry_si_state
        self.si_entry = QComboBox(self)
        self.si_entry.setFont(QFont('Arial', 10))
        self.si_entry.addItem("Open")
        # grid si state label
        self.gridLayout.addWidget(self.si_label, 3, 0)
        # grid si state entry
        self.gridLayout.addWidget(self.si_entry, 3, 1)

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

        # grid Issue type label
        self.gridLayout.addWidget(self.issuetype_label, 5, 0)
        # grid issue type entry
        self.gridLayout.addWidget(self.issuetype_entry, 5, 1)
        #issue reason entry
        self.issue_reason_entry = QLineEdit(self)
        self.issue_reason_entry.setFont(QFont('Arial', 10))
        self.issue_reason_entry.setReadOnly(True)
        self.issue_reason_entry.setStyleSheet("QLineEdit"
                                          "{"
                                          "background-color: #DBDBDB;"
                                          "}")
        #grid issue reason
        self.gridLayout.addWidget(self.issue_reason_entry,6,1)

        # label Description
        self.des_label = QLabel("Description:")
        self.des_label.setFont(QFont('Arial', 10))
        # entry Description
        self.des_entry = QLineEdit(self)
        self.des_entry.setFont(QFont('Arial', 10))

        self.des_entry.setFixedHeight(130)
        #my_wrap = textwrap.TextWrapper(width=30)
        my_des = self.des_entry.text()
        
        #self.des_entry.setText(my_wrap.fill(text=my_des))
        # grid Description label
        self.gridLayout.addWidget(self.des_label, 7 , 0)
        # grid Description entry
        self.gridLayout.addWidget(self.des_entry, 7, 1)

        # domain
        self.domain_label = QLabel("Domain:")
        self.domain_label.setFont(QFont('Arial', 10))
        # domain entry
        self.domain_entry = QComboBox(self)
        self.domain_entry.setFont(QFont('Arial', 10))
        self.domain_entry.setStyleSheet("QComboBox"
                                     "{"
                                      "background-color: white;"
                                     "}")

        self.domain_entry.addItem("Select")
        self.domain_entry.addItem("Audio")
        self.domain_entry.addItem("Camera")
        self.domain_entry.addItem("Video")

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
        self.build_entry.setFont(QFont('Arial', 10))

        #grid git label
        self.gridLayout.addWidget(self.build_label, 10, 0)
        # grid git entry
        self.gridLayout.addWidget(self.build_entry, 10, 1)

        # Create on
        self.createon_label = QLabel("Created on:")
        self.createon_label.setFont(QFont('Arial', 10))
        # create_On entry
        self.createon_entry = QLineEdit(self)
        self.datetime = QDateTime.currentDateTime()
        self.createon_entry.setText(self.datetime.toString('dd.MM.yyyy, hh:mm:ss'))
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
        self.datetime = QDateTime.currentDateTime()
        self.lastmodi_entry.setText(self.datetime.toString('dd.MM.yyyy, hh:mm:ss'))
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

        #submit button
        self.submit=QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_click)

        #grid button
        self.gridLayout.addWidget(self.submit,13,0)

        #view button
        self.Upload_but = QPushButton()
        self.Upload_but.setText("Upload")
        self.Upload_but.clicked.connect(self.Upload_but_clicked)
        #grid view button
        self.gridLayout.addWidget(self.Upload_but,13,1)

        #view button
        self.Exit_but = QPushButton()
        self.Exit_but.setText("Exit")
        self.Exit_but.clicked.connect(self.Exit_but_clicked)
        #grid view button
        self.gridLayout.addWidget(self.Exit_but,13,2)

        self.show()

    def Upload_but_clicked(self):
        from ITT_upload_file import Upload
        print("Upload_but_clicked")
        self.w = Upload()
        self.w.show()
        self.hide()

    def Exit_but_clicked(self):
        from ITT_home_screen import Main_window
        self.w = Main_window()
        self.w.show()
        self.hide()

    def submit_click(self):
            print("clicked")
            cr_no = self.crno_entry.text()
            title = self.title_entry.text()
            des = self.des_entry.text()
            assignee = self.assignee_entry.text()
            si = self.si_entry.currentText()
            status = self.cr_state_entry.currentText()
            domain = self.domain_entry.currentText()
            issue_type = self.issuetype_entry.currentText()
            git_id = self.git_entry.text()
            build_id = self.build_entry.text()
            create_on = self.createon_entry.text()
            last_modi = self.lastmodi_entry.text()
            print("data collected")
            combo_dict = {'CR':cr_no, 'Title':title, 'Description':des,'Assignee':assignee,'State':status,'Software Image':si,
                         'Domain':domain,'Issue Type':issue_type,'GIT/Gerrit link':git_id,
                       'Build ID':build_id,'Create On':create_on,'Last Modified On':last_modi,'History':" "}
            print(combo_dict)
            ret_title = title_validate(title)
            if(ret_title == True):
                ret_des = des_validate(des)
                if(ret_des == True):
                    save_in_excel(combo_dict)
                    print("save")
                self.open_view_screen()
            else:
                print("no")
                pass

    def open_view_screen(self):
        print("open view screen")
        from ITT_view_screen import view_window
        self.w = view_window()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app =QApplication(sys.argv)
    obj = Create_cr()
    sys.exit(app.exec_())