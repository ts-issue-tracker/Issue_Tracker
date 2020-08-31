import sys
from PyQt5.QtWidgets import QMainWindow, QApplication ,QLineEdit, QMessageBox,QLabel,QComboBox,QPushButton
import sys
from PyQt5.QtCore import QDateTime

class Create_cr(QMainWindow):
     def __init__(self):
          super().__init__()
          self.title = "Create New Cr"
          self.left = 200
          self.right = 200
          self.width = 500
          self.height = 500
          self.create_new_cr()

     def create_new_cr(self):
          self.setWindowTitle(self.title)
          self.setGeometry(self.left,self.right,self.width,self.height)
          #label cr_no
          self.label_crno = QLabel(self)
          self.label_crno.setText("Cr no")
          self.label_crno.move(100, 200)
          #entry Cr_no
          self.entry_crno = QLineEdit(self)
          self.entry_crno.setText("try")
          #self.cr_no = read_excel_file()
          self.entry_crno.setReadOnly(True)
          self.entry_crno.resize(200,25)
          self.entry_crno.move(200,200)
          # title
          self.label_title = QLabel(self)
          self.label_title.setText("Title")
          self.label_title.move(100, 250)
          # title entry
          self.title_entry = QLineEdit(self)
          self.title_entry.resize(200,25)
          self.title_entry.move(200, 250)
          # Assignee
          self.label_assignee = QLabel(self)
          self.label_assignee.setText("Assignee")
          self.label_assignee.move(100, 300)
          # Assignee entry
          self.assignee_entry = QLineEdit(self)
          self.assignee_entry.resize(200,25)
          self.assignee_entry.move(200, 300)
          # state
          self.label_state = QLabel(self)
          self.label_state.setText("Cr State")
          self.label_state.move(100, 350)
          # state entry
          self.state_drop = QComboBox(self)
          self.state_drop.addItem("Open")
          self.state_drop.addItem("Closed")
          self.state_drop.addItem("Inprogress")
          self.state_drop.addItem("Reopened")
          self.state_drop.move(200, 350)
          # Si_state
          self.label_si_state = QLabel(self)
          self.label_si_state.setText("SI State")
          self.label_si_state.resize(200,25)
          self.label_si_state.move(100, 400)
          # SI entry
          self.si_state_drop = QComboBox(self)
          self.si_state_drop.addItem("Open")
          self.si_state_drop.addItem("Closed")
          self.si_state_drop.addItem("Duplicate")
          self.si_state_drop.addItem("Fix")
          self.si_state_drop.addItem("Ready")
          self.si_state_drop.addItem("Withdraw")
          self.si_state_drop.resize(200,25)
          self.si_state_drop.move(200, 400)
          #Issue_tyepe
          self.techarea = QLabel(self)
          self.techarea.setText("Issue Type")
          self.techarea.resize(200,25)
          self.techarea.move(100,450)
          #Issue_type entry
          self.techarea = QComboBox(self)
          self.techarea.addItem("Bug")
          self.techarea.addItem("Internal")
          self.techarea.addItem("Blacklisting")
          self.techarea.resize(200,25)
          self.techarea.move(200,450)
          # Description
          self.label_des = QLabel(self)
          self.label_des.setText("Description")
          self.label_des.setWordWrap(True)
          self.label_des.move(100, 500)
          # Description entry
          self.Des_entry = QLineEdit(self)
          self.Des_entry.resize(250, 150)
          self.Des_entry.move(200, 500)
          # Git/Gerrit
          self.label_git = QLabel(self)
          self.label_git.setText("Git/Gerrit")
          self.label_git.move(100,700)
          # Git/Gerrit
          self.entry_git = QLineEdit(self)
          self.entry_git.setReadOnly(True)
          self.entry_git.resize(200, 25)
          self.entry_git.move(200,700)
          #Build_Id
          self.build_id_label = QLabel(self)
          self.build_id_label.setText("Build id")
          self.build_id_label.move(100,750)
          #Build_Id
          self.entry_buildid = QLineEdit(self)
          self.entry_buildid.resize(200,25)
          self.entry_buildid.move(200,750)
          #create on
          self.create_on_label = QLabel(self)
          self.create_on_label.setText("Create On")
          self.create_on_label.move(100,800)
          #entry create on
          self.create_on_entry = QLineEdit(self)
          self.datetime = QDateTime.currentDateTime()
          self.create_on_entry.setText(self.datetime.toString('dd.MM.yyyy, hh:mm:ss'))
          self.create_on_entry.setReadOnly(True)
          self.create_on_entry.resize(200,25)
          self.create_on_entry.move(200,800)
          # last modified on
          self.last_modi_label = QLabel(self)
          self.last_modi_label.setText("Create On")
          self.last_modi_label.move(100, 850)
          # entry last modified on
          self.last_modi_entry = QLineEdit(self)
          self.datetime = QDateTime.currentDateTime()
          self.last_modi_entry.setText(self.datetime.toString('dd.MM.yyyy, hh:mm:ss'))
          self.last_modi_entry.setReadOnly(True)
          self.last_modi_entry.resize(200, 25)
          self.last_modi_entry.move(200, 850)
          #upload button
          self.Upload_button = QPushButton('Upload', self)
          self.Upload_button.move(50, 900)
          self.Upload_button.clicked.connect(self.upload_click)
          #submit button
          self.Upload_button = QPushButton('Submit', self)
          self.Upload_button.move(200, 900)
          self.Upload_button.clicked.connect(self.submit_click)
          #Exit button
          self.Upload_button = QPushButton('Exit', self)
          self.Upload_button.move(350, 900)
          self.Upload_button.clicked.connect(self.Exit_click)

          self.show()
     def upload_click(self):
          print("upload clicked")

     def submit_click(self):
          assignee = self.assignee_entry.text()

     def Exit_click(self):
          print("Exit clicked")

if __name__ == '__main__':
     app = QApplication(sys.argv)
     Create_cr_obj = Create_cr()
     sys.exit(app.exec_())