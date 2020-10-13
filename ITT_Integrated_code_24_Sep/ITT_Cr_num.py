from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QWidget, QLineEdit, QLabel
from PyQt5.QtGui import QFont
import sys

from ITT_validate import *
from ITT_update_screen import *

from PyQt5.QtGui import QPalette,QImage,QPageSize,QBrush,QPixmap
from PyQt5.QtCore import QSize

class Enter_cr(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1920)
        self.setMinimumHeight(1000)
        self.setWindowTitle("View")
        self.frame = QFrame(self)
        self.frame.setFixedSize(280, 200)
        #self.frame.setFrameShape(QFrame.StyledPanel)
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

        self.frame_1 = QFrame(self)
        #self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_1 = QGridLayout(self.frame_1)
        self.frame_1.setFixedSize(240, 60)
        self.gridLayout.addWidget(self.frame_1, 1, 0)

        self.enter()

    def enter(self):
        self.enter_cr_num_label = QLabel("CR No")
        self.enter_cr_num_label.setFont(QFont('Arial', 10))
        self.enter_cr_num_label.setContentsMargins(20, 0, 0, 10)
        # entry assigne
        self.enter_cr_num_entry = QLineEdit()
        self.enter_cr_num_entry.setFixedWidth(135)
        self.enter_cr_num_entry.setFont(QFont('Arial', 10))
        self.enter_cr_num_entry.setContentsMargins(0, 0, 30, 10)
        print(self.enter_cr_num_entry.text())
        # grid
        self.gridLayout.addWidget(self.enter_cr_num_label, 0, 0)
        self.gridLayout.addWidget(self.enter_cr_num_entry, 0, 1)
        # button
        self.Submit_but = QtWidgets.QPushButton()
        self.Submit_but.setText("Submit")
        self.Submit_but.clicked.connect(self.submit_but_clicked)
        self.Submit_but.setContentsMargins(0, 10, 10, 10)
        # grid view button
        self.gridLayout_1.addWidget(self.Submit_but, 0, 0)
        self.Exit_but = QPushButton()
        self.Exit_but.setText("Exit")
        self.Exit_but.setContentsMargins(10, 10, 0, 10)
        self.Exit_but.clicked.connect(self.Exit_but_clicked)
        # grid view button
        self.gridLayout_1.addWidget(self.Exit_but, 0, 1)
        self.showMaximized()
        self.show()

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame, self.img_frame)

    def centerOnScreen(self, frame, frame2):
        frame.move(int((self.width() - self.frame.width()) / 2), int((self.height() - self.frame.height()) / 2))
        frame2.move((self.width() - self.img_frame.width()), 1)

    def Exit_but_clicked(self):
        from itt_main_ui import main_window
        self.w = main_window()
        self.w.show()
        self.hide()

    def submit_but_clicked(self):
        self.cr_no = self.enter_cr_num_entry.text()
        self.ret = validate_cr_list(self.cr_no)
        if (self.ret >= 0):
            #self.w = Update(self.enter_cr_num_entry.text())
            self.w = Update(self.ret)
            self.w.show()
            self.close()
        else:
            print("No cr exist")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = Enter_cr()
    sys.exit(app.exec_())