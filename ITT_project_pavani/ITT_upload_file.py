from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QWidget,QFrame,QGridLayout,QPushButton,QFileDialog
import sys
import shutil

class Upload(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Upload screen")
        self.frame = QFrame(self)
        self.frame.setFixedSize(500,1000)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.upload_file()

    def upload_file(self):

        #submit button
        self.upload=QPushButton()
        self.upload.setText("Browse")
        self.upload.clicked.connect(self.upload_click)

        #grid button
        self.gridLayout.addWidget(self.upload,1,0)
        self.show()

    def upload_click(self):
        destpath = "C:\\Users\\lenovo\\Desktop"
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        shutil.copy(path,destpath)

if __name__ == "__main__":
    app =QApplication(sys.argv)
    obj = Upload()
    sys.exit(app.exec_())