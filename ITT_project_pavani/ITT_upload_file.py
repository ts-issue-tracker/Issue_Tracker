from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QWidget,QFrame,QGridLayout,QPushButton,QFileDialog
import sys
import shutil

class Upload(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Upload screen")
        self.setMinimumWidth(700)
        self.setMinimumHeight(700)
        self.frame = QFrame(self)
        self.frame.setFixedSize(330, 250)
        # self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.upload_file()

    def upload_file(self):

        #submit button
        self.upload=QPushButton()
        self.upload.setText("Browse")
        self.upload.clicked.connect(self.upload_click)

        #grid button
        self.gridLayout.addWidget(self.upload,1,0)

        self.exit = QPushButton()
        self.exit.setText("Exit")
        self.exit.clicked.connect(self.exit_click)

        # grid button
        self.gridLayout.addWidget(self.upload, 2, 1)
        self.show()

    def exit_click(self):
        from ITT_home_screen import Main_window
        self.w = Main_window()
        self.w.show()
        self.hide()

    def upload_click(self):
        destpath = "C:\\Users\\lenovo\\Desktop"
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        shutil.copy(path,destpath)

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self,frame):
        frame.move(int((self.width()-self.frame.width()) / 2), int((self.height()-self.frame.height()) / 2))

if __name__ == "__main__":
    app =QApplication(sys.argv)
    obj = Upload()
    sys.exit(app.exec_())