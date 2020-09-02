from PyQt5.QtWidgets import *
from itt_register_ui import *
from itt_view_ui import *
from itt_create_an_issue_ui import *
from PyQt5.QtGui import QFont
credentials_file="Credentials.csv"

class main_window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Issue Tracker"
        self.setWindowTitle(self.title)
        self.setMinimumWidth(700)
        self.setMinimumHeight(700)
        self.frame =QFrame(self)
        self.frame.setFixedSize(300, 250)
        self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        create_btn=QPushButton()
        create_btn.setText("Create")
        create_btn.setFixedWidth(100)
        create_btn.setFont(QFont('Arial', 10))
        create_btn.clicked.connect(self.create_an_issue_btn_click)

        update_btn = QPushButton()
        update_btn.setText("Update")
        update_btn.setFixedWidth(100)
        update_btn.move(50,0)
        update_btn.setFont(QFont('Arial', 10))
        update_btn.clicked.connect(self.update_the_record_btn_click)

        view_btn = QPushButton()
        view_btn.setText("View")
        view_btn.setFixedWidth(100)
        view_btn.setFont(QFont('Arial', 10))
        view_btn.clicked.connect(self.view_the_record_btn_click)

        display_btn = QPushButton()
        display_btn.setText("Display")
        display_btn.setFixedWidth(100)
        display_btn.setFont(QFont('Arial', 10))
        display_btn.move(50, 0)
        display_btn.clicked.connect(self.display_the_record_btn_click)

        exit_btn = QPushButton()
        exit_btn.setText("Exit")
        exit_btn.setFixedWidth(100)
        exit_btn.setFont(QFont('Arial', 10))
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
        pass
    def update_the_record_btn_click(self):
        pass
    def view_the_record_btn_click(self):
        self.open_view_window()
        pass
    def display_the_record_btn_click(self):
        pass
    def on_exit_btn_click(self):
        pass

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)
    def centerOnScreen(self,frame):
        screen = QDesktopWidget()
        frame.move((self.width()-self.frame.width()) / 2, (self.height()-self.frame.height()) / 2)

    def open_create_an_issue_window(self):
        self.w = Create_cr()
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