from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDateTime
import sys

from ITT_Cr_num import *
from ITT_validate import *
from ITT_read_excel import *
from ITT_cr_num_view import *
from ITT_home_screen import *

class View(QWidget):
    def __init__(self,cr_index):
        super().__init__()
        self.setWindowTitle("Update Screen")
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 1000)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)

        self.gridLayout = QGridLayout(self.frame)
        self.cr_index = cr_index
        self.cr = read_cr_by_index(cr_index)
        self.view()

    def view(self):
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
        # label assignee
        self.assignee_label = QLabel("Assignee:")
        self.assignee_label.setFont(QFont('Arial', 10))
        # entry assignee
        self.assignee_entry = QLineEdit()
        self.assignee = read_asignee_with_cr(self.cr_index)
        self.assignee_entry.setText(self.assignee)
        self.assignee_entry.setReadOnly(True)
        self.assignee_entry.setStyleSheet("QLineEdit"
                                      "{"
                                      "background-color: #DBDBDB;"
                                      "}")
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
        self.title_entry.setReadOnly(True)
        self.title_entry.setFont(QFont('Arial', 10))

        # grid label title
        self.gridLayout.addWidget(self.title_label, 2, 0)
        # grid entry assignee
        self.gridLayout.addWidget(self.title_entry, 2, 1)

        # label cr state
        self.cr_state_label = QLabel("Cr State:")
        self.cr_state_label.setFont(QFont('Arial', 10))
        # entry_cr_state
        self.cr_state_entry = QLineEdit(self)
        self.cr_state_entry.setFont(QFont('Arial', 10))
        self.prev_cr_state = read_cr_with_cr(self.cr_index)
        self.cr_state_entry.setText(self.prev_cr_state)
        self.cr_state_entry.setReadOnly(True)

        # grid cr state label
        self.gridLayout.addWidget(self.cr_state_label, 4, 0)
        # grid cr state entry
        self.gridLayout.addWidget(self.cr_state_entry, 4, 1)

        # si state
        self.si_state_label = QLabel("SI State")
        self.si_state_label.setFont(QFont('Arial', 10))
        # entry
        self.si_state = QLineEdit(self)
        self.si_state.setFont(QFont('Arial', 10))
        self.si_prev_state = read_si_with_cr(self.cr_index)
        self.si_state.setText(self.si_prev_state)
        self.si_state.setReadOnly(True)

        # grid for si state
        self.gridLayout.addWidget(self.si_state_label, 3, 0)
        self.gridLayout.addWidget(self.si_state, 3, 1)
        # label Issue type
        self.issuetype_label = QLabel("Issue Type:")
        self.issuetype_label.setFont(QFont('Arial', 10))

        # entry Issue type
        self.issuetype_entry = QLineEdit(self)
        self.issuetype_entry.setFont(QFont('Arial', 10))
        self.issue_type = read_issuetype_with_cr(self.cr_index)
        self.issuetype_entry.setText(self.issue_type)
        self.issuetype_entry.setReadOnly(True)

        # grid Issue type label
        self.gridLayout.addWidget(self.issuetype_label, 5, 0)
        # grid issue type entry
        self.gridLayout.addWidget(self.issuetype_entry, 5, 1)
        # label Description
        self.des_label = QLabel("Description:")
        self.des_label.setFont(QFont('Arial', 10))
        # entry Description
        self.des_entry = QLineEdit(self)
        self.des_entry.setFont(QFont('Arial', 10))
        self.des = read_des_with_cr(self.cr_index)
        self.des_entry.setText(self.des)
        self.des_entry.setReadOnly(True)

        # grid Description label
        self.gridLayout.addWidget(self.des_label, 6, 0)
        # grid Description entry
        self.gridLayout.addWidget(self.des_entry, 6, 1)

        # domain
        self.domain_label = QLabel("Domain/Tech Area:")
        self.domain_label.setFont(QFont('Arial', 10))
        # domain entry
        self.domain_entry = QLineEdit(self)
        self.domain_entry.setFont(QFont('Arial', 10))
        self.domain_entry.setStyleSheet("QComboBox"
                                        "{"
                                        "background-color: white;"
                                        "}")
        self.domain =  read_domain_with_cr(self.cr_index)
        self.domain_entry.setText(self.domain)
        self.domain_entry.setReadOnly(True)

        # grid domain label
        self.gridLayout.addWidget(self.domain_label, 7, 0)
        # grid domain entry
        self.gridLayout.addWidget(self.domain_entry, 7, 1)

        # git/gerrit
        self.git_label = QLabel("Git/Gerrit link:")
        self.git_label.setFont(QFont('Arial', 10))
        # git entry
        self.git_entry = QLineEdit(self)
        self.git = read_git_with_cr(self.cr_index)
        self.git_entry.setText(self.git)
        self.git_entry.setReadOnly(True)
        self.git_entry.setStyleSheet("QLineEdit"
                                     "{"
                                     "background-color: #DBDBDB	;"
                                     "}")

        # grid git label
        self.gridLayout.addWidget(self.git_label, 8, 0)
        # grid git entry
        self.gridLayout.addWidget(self.git_entry, 8, 1)

        # build id
        self.build_label = QLabel("Build Id:")
        self.build_label.setFont(QFont('Arial', 10))
        # build entry
        self.build_entry = QLineEdit(self)
        self.build = read_build_with_cr(self.cr_index)
        self.build_entry.setText(self.build)
        self.build_entry.setReadOnly(True)
        self.build_entry.setFont(QFont('Arial', 10))

        # grid git label
        self.gridLayout.addWidget(self.build_label, 9, 0)
        # grid git entry
        self.gridLayout.addWidget(self.build_entry, 9, 1)

        # Create on
        self.createon_label = QLabel("Created on:")
        self.createon_label.setFont(QFont('Arial', 10))
        # create_On entry
        self.createon_entry = QLineEdit(self)
        self.datetime = read_create_date_index(self.cr_index)
        self.createon_entry.setText(self.datetime)
        self.createon_entry.setFont(QFont('Arial', 10))
        self.createon_entry.setReadOnly(True)
        self.createon_entry.setStyleSheet("QLineEdit"
                                          "{"
                                          "background-color: #DBDBDB	;"
                                          "}")
        # Create on
        self.gridLayout.addWidget(self.createon_label, 10, 0)
        # Create on entry
        self.gridLayout.addWidget(self.createon_entry, 10, 1)

        # last modified
        self.lastmodi_label = QLabel("Last Modified: ")
        self.lastmodi_label.setFont(QFont('Arial', 10))
        # last modified entry
        self.lastmodi_entry = QLineEdit(self)
        self.lastdate = read_late_date_index(self.cr_index)
        self.lastmodi_entry.setText(self.lastdate)
        self.lastmodi_entry.setFont(QFont('Arial', 10))
        self.lastmodi_entry.setReadOnly(True)
        self.lastmodi_entry.setStyleSheet("QLineEdit"
                                          "{"
                                          "background-color: #DBDBDB;"
                                          "}")

        # last modified
        self.gridLayout.addWidget(self.lastmodi_label, 11, 0)
        # last modifies entry
        self.gridLayout.addWidget(self.lastmodi_entry, 11, 1)

        self.exit = QPushButton()
        self.exit.setText("Exit")
        self.exit.clicked.connect(self.exit_clicked)

        # grid button
        self.gridLayout.addWidget(self.exit, 12, 2)

        self.show()

    def exit_clicked(self):
        self.w = Main_window()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app =QApplication(sys.argv)
    obj = View(0)
    sys.exit(app.exec_())