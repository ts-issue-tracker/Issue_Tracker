from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QLabel, \
    QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

from ITT_read_excel import *

class view_window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "View Screen"
        self.setWindowTitle(self.title)
        self.setMinimumWidth(600)
        self.setMinimumHeight(800)
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 800)
        # self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)

        self.frame_three = QFrame(self)
        self.gridLayout_three = QGridLayout(self.frame_three)
        self.frame_three.setFixedSize(450, 50)
        self.gridLayout.addWidget(self.frame_three, 14, 0)

        self.view_screen()

    def view_screen(self):
        # label crno
        self.crno_label = QLabel("CR")
        self.crno_label.setFont(QFont('Arial', 10))

        # entry crno
        self.crno_entry = QLineEdit()
        self.cr_no = read_last_cr()
        self.crno_entry.setText(self.cr_no)
        self.crno_entry.setReadOnly(True)
        self.crno_entry.setFont(QFont('Arial', 10))
        self.crno_entry.setStyleSheet("QLineEdit"
                                          "{"
                                          "background-color: #DBDBDB;"
                                          "}")
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
        self.title = read_last_title()
        self.title_entry.setPlainText(self.title)
        self.title_entry.setReadOnly(True)
        self.title_entry.setFont(QFont('Arial', 10))
        self.title_entry.setFixedHeight(50)
        self.title_entry.setStyleSheet("QTextEdit"
                                          "{"
                                          "background-color: #DBDBDB;"
                                          "}")

        # grid label title
        self.gridLayout.addWidget(self.title_label, 1, 0)
        # grid entry assignee
        self.gridLayout.addWidget(self.title_entry, 1, 1)

        # label Description
        self.des_label = QLabel("Description")
        self.des_label.setFont(QFont('Arial', 10))
        # entry Description
        self.des_entry = QTextEdit(self)
        self.des_entry.setFixedHeight(130)
        self.des_entry.setStyleSheet("QTextEdit"
                                     "{"
                                     "background-color: #DBDBDB;"
                                     "}")
        self.des = read_last_des()
        self.des_entry.setFont(QFont('Arial', 10))
        self.des_entry.setReadOnly(True)
        self.des_entry.setPlainText(self.des)
        # grid Description label
        self.gridLayout.addWidget(self.des_label, 2, 0)
        # grid Description entry
        self.gridLayout.addWidget(self.des_entry, 2, 1)

        # label assignee
        self.assignee_label = QLabel("Assignee")
        self.assignee_label.setFont(QFont('Arial', 10))
        # entry assignee
        self.assignee_entry = QLineEdit()
        self.assignee = read_last_assignee()
        self.assignee_entry.setText(self.assignee)
        self.assignee_entry.setReadOnly(True)
        self.assignee_entry.setFont(QFont('Arial', 10))
        self.assignee_entry.setStyleSheet("QLineEdit"
                                          "{"
                                          "background-color: #DBDBDB;"
                                          "}")

        # grid label assignee
        self.gridLayout.addWidget(self.assignee_label, 3, 0)
        # grid entry assignee
        self.gridLayout.addWidget(self.assignee_entry, 3, 1)

        # label cr state
        self.cr_state_label = QLabel("CR State")
        self.cr_state_label.setFont(QFont('Arial', 10))
        # entry_cr_state
        self.cr_state_entry = QLineEdit(self)
        self.cr_state_entry.setFont(QFont('Arial', 10))
        self.cr_state = read_last_crstate()
        self.cr_state_entry.setStyleSheet("QLineEdit"
                                      "{"
                                      "background-color: #DBDBDB;"
                                      "}")

        self.cr_state_entry.setText(self.cr_state)

        # grid cr state label
        self.gridLayout.addWidget(self.cr_state_label, 5, 0)
        # grid cr state entry
        self.gridLayout.addWidget(self.cr_state_entry, 5, 1)

        # label Si state
        #self.si_state_label = QLabel("SI State:")
        #self.si_state_label.setFont(QFont('Arial', 10))
        # entry_si_state
        #self.si_state_entry = QLineEdit(self)
        #self.si_state_entry.setFont(QFont('Arial', 10))
        #self.si_state = "open"
        #self.si_state_entry.setStyleSheet("QLineEdit"
         #                              "{"
         #                              "background-color: #DBDBDB;"
         #                              "}")
        #self.si_state_entry.setText(self.si_state)

        # grid si state label
        #self.gridLayout.addWidget(self.si_state_label, 4, 0)
        # grid si state entry
        #self.gridLayout.addWidget(self.si_state_entry, 4, 1)

        # label Si state
        self.si_label = QLabel("SI state")
        self.si_label.setFont(QFont('Arial', 10))
        # entry_si_state
        self.si_entry = QLineEdit(self)
        self.si_entry.setFont(QFont('Arial', 10))
        self.si_state = read_last_si_state()
        self.si_entry.setStyleSheet("QLineEdit"
                                          "{"
                                          "background-color: #DBDBDB;"
                                          "}")
        self.si_entry.setText(self.si_state)
        self.si_entry.setReadOnly(True)

        # grid si state label
        self.gridLayout.addWidget(self.si_label, 4, 0)
        # grid si state entry
        self.gridLayout.addWidget(self.si_entry, 4, 1)

        # domain
        self.domain_label = QLabel("Domain")
        self.domain_label.setFont(QFont('Arial', 10))
        # domain entry
        self.domain_entry = QLineEdit(self)
        self.domain_entry.setFont(QFont('Arial', 10))
        self.domain = read_last_domain()
        self.domain_entry.setText(self.domain)
        self.domain_entry.setStyleSheet("QLineEdit"
                                        "{"
                                        "background-color: #DBDBDB;"
                                        "}")
        # grid domain label
        self.gridLayout.addWidget(self.domain_label, 6, 0)
        # grid domain entry
        self.gridLayout.addWidget(self.domain_entry, 6, 1)

        # label Issue type
        self.issuetype_label = QLabel("Issue Type")
        self.issuetype_label.setFont(QFont('Arial', 10))
        # entry Issue type
        self.issuetype_entry = QLineEdit(self)
        self.issuetype_entry.setFont(QFont('Arial', 10))
        self.issuetype = read_last_issuetype()
        self.issuetype_entry.setText(self.issuetype)
        self.issuetype_entry.setStyleSheet("QLineEdit"
                                           "{"
                                           "background-color: #DBDBDB;"
                                           "}")
        # grid Issue type label
        self.gridLayout.addWidget(self.issuetype_label, 7, 0)
        # grid issue type entry
        self.gridLayout.addWidget(self.issuetype_entry, 7, 1)

        # issue reason entry
        self.issue_reason_entry = QLineEdit(self)
        self.issue_reason_entry.setFont(QFont('Arial', 10))
        self.issue_reason_entry.setStyleSheet("QLineEdit"
                                              "{"
                                              "background-color: #DBDBDB;"
                                              "}")
        self.issue_reason_entry.setReadOnly(True)
        # grid issue reason
        self.gridLayout.addWidget(self.issue_reason_entry,8 , 1)


        # git/gerrit
        self.git_label = QLabel("Git/Gerrit link")
        self.git_label.setFont(QFont('Arial', 10))
        # git entry
        self.git_entry = QLineEdit(self)
        self.git = read_git_id()
        self.git_entry.setText(self.git)
        self.git_entry.setReadOnly(True)
        self.git_entry.setStyleSheet("QLineEdit"
                                        "{"
                                        "background-color: #DBDBDB;"
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
        self.build = read_build()
        self.build_entry.setText(self.build)
        self.build_entry.setReadOnly(True)
        self.build_entry.setFont(QFont('Arial', 10))
        self.build_entry.setStyleSheet("QLineEdit"
                                     "{"
                                     "background-color: #DBDBDB;"
                                     "}")
        # grid git label
        self.gridLayout.addWidget(self.build_label, 10, 0)
        # grid git entry
        self.gridLayout.addWidget(self.build_entry, 10, 1)

        # Create on
        self.createon_label = QLabel("Created on")
        self.createon_label.setFont(QFont('Arial', 10))
        # create_On entry
        self.createon_entry = QLineEdit(self)
        self.createon = read_create_time()
        self.createon_entry.setText(self.createon)
        self.createon_entry.setFont(QFont('Arial', 10))
        self.createon_entry.setReadOnly(True)
        self.createon_entry.setStyleSheet("QLineEdit"
                                       "{"
                                       "background-color: #DBDBDB;"
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
        self.lastmodi_time = read_lastmodi_time()
        self.lastmodi_entry.setText(self.lastmodi_time)
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

        #exit button
        self.exit= QPushButton()
        self.exit.setText("Exit")
        self.exit.clicked.connect(self.exit_clicked)

        # grid button
        self.gridLayout_three.addWidget(self.exit, 13, 3)

        self.continuebt = QPushButton()
        self.continuebt.setText("Create CR")
        self.continuebt.clicked.connect(self.continuebt_clicked)

        # grid button
        self.gridLayout_three.addWidget(self.continuebt, 13, 1)

        self.show()

    def continuebt_clicked(self):
        from ITT_create_issue import Create_cr
        self.w = Create_cr()
        self.w.show()
        self.hide()

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self,frame):
        frame.move(int((self.width()-self.frame.width()) / 2), int((self.height()-self.frame.height()) / 2))

    def exit_clicked(self):
        from itt_main_ui import main_window
        self.w = main_window()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = view_window()
    sys.exit(App.exec())