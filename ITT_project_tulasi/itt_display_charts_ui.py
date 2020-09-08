from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame, QGridLayout
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from itt_main_file_access import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Display Statistics"
        top = 400
        left = 400
        width = 900
        height = 500

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.frame = QFrame(self)
        # self.frame.setAttribute(Qt.WA_TranslucentBackground)
        self.frame.setFixedSize(500, 500)
        # self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)

        self.MyUI()

    def MyUI(self):

        canvas = Canvas(self, width=8, height=4)
        #canvas.move(0,0)
        self.gridLayout.addWidget(canvas, 0, 0)

        button = QPushButton("Click Me", self)
        button.move(100, 450)

        button2 = QPushButton("Click Me Two", self)
        button2.move(250, 450)


class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()

    def plot(self):
        ax = self.figure.add_subplot(111)
        column_name = "Domain"
        label_list = []
        label_list.extend(return_label_list(column_name))
        pie_chart_list = []
        pie_chart_list.extend(list_to_display_on_pie(column_name))
        ax.pie(pie_chart_list, explode=None, labels=label_list, colors=['b', 'g', 'r', 'y', 'm'], autopct='% 1d %%')

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()