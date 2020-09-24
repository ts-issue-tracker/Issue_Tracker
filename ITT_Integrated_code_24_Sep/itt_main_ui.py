from PyQt5.QtWidgets import *
from itt_register_ui import *
from Itt_View_Report_main import *
from ITT_create_issue import *
from ITT_Cr_num import *
from ITT_update_screen import *
from itt_display_charts_ui import *
from PyQt5.QtGui import QFont

from PyQt5.QtGui import QPalette,QImage,QPageSize,QBrush
from PyQt5.QtCore import QSize

credentials_file="Credentials.csv"

class main_window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Issue Tracker"
        self.setWindowTitle(self.title)
        self.setMinimumWidth(600)
        self.setMinimumHeight(800)
        self.frame =QFrame(self)
        self.frame.setFixedSize(300, 500)
        #self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        oImage = QImage("image2.jpg")
        sImage = oImage.scaled(QSize(1000, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        create_btn=QPushButton()
        create_btn.setText("Create")
        create_btn.setFixedHeight(50)
        create_btn.setFixedWidth(200)
        create_btn.setFont(QFont('Arial', 15))
        create_btn.clicked.connect(self.create_an_issue_btn_click)

        update_btn = QPushButton()
        update_btn.setText("Update")
        update_btn.setFixedHeight(50)
        update_btn.setFixedWidth(200)
        update_btn.move(50,0)
        update_btn.setFont(QFont('Arial', 15))
        update_btn.clicked.connect(self.update_the_record_btn_click)

        view_btn = QPushButton()
        view_btn.setText("View")
        view_btn.setFixedHeight(50)
        view_btn.setFixedWidth(200)
        view_btn.setFont(QFont('Arial', 15))
        view_btn.clicked.connect(self.view_the_record_btn_click)

        display_btn = QPushButton()
        display_btn.setText("Statistics")
        display_btn.setFixedHeight(50)
        display_btn.setFixedWidth(200)
        display_btn.setFont(QFont('Arial', 15))
        display_btn.move(50, 0)
        display_btn.clicked.connect(self.display_statistics_btn_click)

        exit_btn = QPushButton()
        exit_btn.setText("Exit")
        exit_btn.setFixedHeight(50)
        exit_btn.setFixedWidth(200)
        exit_btn.setFont(QFont('Arial', 15))
        exit_btn.move(50, 0)
        exit_btn.clicked.connect(self.on_exit_btn_click)

        self.gridLayout.addWidget(create_btn, 1, 0)
        self.gridLayout.addWidget(update_btn, 2, 0)
        self.gridLayout.addWidget(view_btn, 3, 0)
        self.gridLayout.addWidget(display_btn, 4, 0)
        self.gridLayout.addWidget(exit_btn, 5, 0)
        self.show()

    def create_an_issue_btn_click(self):
        self.open_create_an_issue_window()

    def update_the_record_btn_click(self):
        self.open_update_window()

    def view_the_record_btn_click(self):
        self.open_view_window()
    def display_statistics_btn_click(self):
        self.open_display_statistics_window()
    def on_exit_btn_click(self):
        self.open_login_window()
    def open_login_window(self):
        from itt_login_ui import login_window
        self.w = login_window()
        self.w.show()
        self.hide()
    def open_display_statistics_window(self):
        self.w = Statistics_Window()
        self.w.show()
        self.hide()

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)
    def centerOnScreen(self,frame):
        screen = QDesktopWidget()
        frame.move((self.width()-self.frame.width()) / 2, (self.height()-self.frame.height()) / 2)

    def open_create_an_issue_window(self):
        self.w = Create_cr()
        self.w.show()
        self.hide()
    def open_update_window(self):
        from ITT_Cr_num import Enter_cr
        self.w = Enter_cr()
        self.w.show()
        self.hide()

    def open_view_window(self):
        self.w =  View_Report()
        self.w.show()
        self.hide()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = main_window()
    sys.exit(App.exec())