#from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame, QGridLayout, QComboBox, QLabel, QLineEdit
import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from itt_main_file_access import *
from PyQt5.QtWidgets import QMessageBox
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
        self.frame.setFixedSize(900, 500)
        self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)

        self.frame_one = QFrame(self)
        self.frame_one.setFrameShape(QFrame.StyledPanel)
        self.frame_one.setFixedSize(850, 60)

        self.gridLayout_one = QGridLayout(self.frame_one)
        self.gridLayout.addWidget(self.frame_one,0,0)
        #self.gridLayout_one.setContentsMargins(20, 20, 20, 20)

        self.MyUI()

    def MyUI(self):
        self.TypeCombo = QComboBox(self)
        self.TypeCombo.addItem('State')
        self.TypeCombo.addItem('Domain')
        self.TypeCombo.addItem('IssueType')

        self.TypeCombo.activated[str].connect(self.readType)
        self.TypeCombo.setFixedWidth(100)
        statusLabel = QLabel("&Type:")
        statusLabel.setFixedWidth(50)
        statusLabel.setBuddy(self.TypeCombo)

        self.AssigneeCombo = QComboBox(self)
        self.AssigneeCombo.addItem('Tulasi')
        self.AssigneeCombo.addItem('Santhoshi')
        self.AssigneeCombo.addItem('Pavani')
        self.AssigneeCombo.addItem('Sumalatha')
        self.AssigneeCombo.addItem('Suresh')
        self.AssigneeCombo.addItem('Swetha')
        self.AssigneeCombo.setCurrentText("hi")

        self.AssigneeCombo.activated[str].connect(self.readAssignee)
        self.AssigneeCombo.setFixedWidth(100)
        AssigneeLabel = QLabel("&Assignee && &Type:")
        AssigneeLabel.setFixedWidth(100)
        AssigneeLabel.setBuddy(self.AssigneeCombo)

        self.DomianCombo = QComboBox(self)
        self.DomianCombo.addItem('Audio')
        self.DomianCombo.addItem('Camera')
        self.DomianCombo.addItem('Video')

        self.DomianCombo.activated[str].connect(self.readDomain)
        self.DomianCombo.setFixedWidth(100)
        DomainLabel = QLabel("&Domain && &Type:")
        DomainLabel.setFixedWidth(100)
        DomainLabel.setBuddy(self.DomianCombo)

        self.ChartTypeCombo = QComboBox(self)
        self.ChartTypeCombo.addItem('Pie Chart')
        self.ChartTypeCombo.addItem('Bar Chart')

        self.ChartTypeCombo.activated[str].connect(self.readChartType)
        self.ChartTypeCombo.setFixedWidth(100)
        ChartTypeLabel = QLabel("&ChartType:")
        ChartTypeLabel.setFixedWidth(100)
        ChartTypeLabel.setBuddy(self.ChartTypeCombo)

        self.gridLayout_one.addWidget(statusLabel,0,0)
        self.gridLayout_one.addWidget(self.TypeCombo,0,1)

        self.gridLayout_one.addWidget(AssigneeLabel,0,2)
        self.gridLayout_one.addWidget(self.AssigneeCombo,0,3)

        self.gridLayout_one.addWidget(DomainLabel, 0, 4)
        self.gridLayout_one.addWidget(self.DomianCombo, 0, 5)

        self.gridLayout_one.addWidget(ChartTypeLabel, 0, 6)
        self.gridLayout_one.addWidget(self.ChartTypeCombo, 0, 7)

        self.pie_chart_for_specified_type(self.TypeCombo.currentText())


    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self, frame):
        frame.move((self.width() - self.frame.width()) / 2, (self.height() - self.frame.height()) / 2)

    def readType(self, text):
        if self.ChartTypeCombo.currentText()=="Pie Chart":
            self.pie_chart_for_specified_type(text)
        else:
            self.bar_chart_for_specified_type(text)

    def readChartType(self, text):
        pass

    def readDomain(self, text):
        type = self.TypeCombo.currentText()
        domain = self.DomianCombo.currentText()
        if self.ChartTypeCombo.currentText()=="Pie Chart":
            self.readDomain_for_pie_chart(type,domain,text)
        else:
            self.readDomain_for_bar_chart(type,domain,text)

    def readAssignee(self, text):
        type = self.TypeCombo.currentText()
        assignee = self.AssigneeCombo.currentText()
        if self.ChartTypeCombo.currentText()=="Pie Chart":
            self.readAssignee_for_pie_chart(type,assignee,text)
        else:
            self.readAssignee_for_bar_chart(type,assignee,text)

    def readAssignee_for_bar_chart(self, type, assignee, text):
        self.read_assignee_or_domain_for_bar_char(type, assignee, text)

    def readDomain_for_bar_chart(self, type, domain, text):

        self.read_assignee_or_domain_for_bar_char(type, domain, text)

    def readDomain_for_pie_chart(self, type, domain, text):
        self.read_assignee_or_domain_for_pie_chart(type, domain, text)

    def readAssignee_for_pie_chart(self,type,assignee,text):
        self.read_assignee_or_domain_for_pie_chart(type,assignee,text)

    def read_assignee_or_domain_for_pie_chart(self, type, assignee_or_domain, text):
        self.canvas = Canvas(self, width=8, height=4)
        self.gridLayout.addWidget(self.canvas, 1, 0)
        ax = self.canvas.figure.add_subplot(111)
        col = return_col_of_specified_col_name(assignee_or_domain)
        label_list = []
        label_list.extend(return_label_list(type))
        list = []
        list.extend(list_to_display_on_pie_for_assignee(col, assignee_or_domain, type))
        wedges, texts, autotexts = ax.pie(list, explode=None, colors=['b', 'g', 'r', 'y', 'm'], autopct='% 1d %%')
        ax.legend(wedges, label_list,
                  title=type,
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

    def read_assignee_or_domain_for_bar_char(self,type,assignee_or_domain,text):
        canvas = Canvas(self, width=8, height=6)
        self.gridLayout.addWidget(canvas, 1, 0)
        ax = canvas.figure.add_subplot(111)
        col = return_col_of_specified_col_name(assignee_or_domain)
        label_list = []
        label_list.extend(return_label_list(type))
        list = []
        list.extend(list_to_display_on_pie_for_assignee(col, assignee_or_domain, type))
        pos = list[0]
        width = 0.1
        color_list = ['b', 'g', 'r', 'y', 'm']
        for i, j, k in zip(list, color_list, range(0, len(list))):
            ax.bar(pos + width * k, i, width, alpha=0.5, color=j, label=assignee_or_domain)

        # Set the y axis label
        ax.set_ylabel('Count')

        # Set the chart's title
        ax.set_title(type)

        # Set the position of the x ticks
        ax.set_xticks([pos + 1.5 * width])

        # Set the labels for the x ticks
        list2 = [assignee_or_domain]
        ax.set_xticklabels(list2)
        # Setting the x-axis and y-axis limits
        plt.xlim(pos - width, pos + width * 3)

        k = 0
        for i in list:
            k += i
        plt.ylim([0, k])

        # Adding the legend and showing the plot
        ax.legend(label_list, loc='upper left')
        ax.grid()
    def bar_chart_for_specified_type(self,text):
        canvas = Canvas(self, width=8, height=6)
        self.gridLayout.addWidget(canvas, 1, 0)
        ax = canvas.figure.add_subplot(111)
        label_list = []
        label_list.extend(return_label_list(text))
        list = []
        list.extend(list_to_display_on_pie(text))
        pos = list[0]
        width = 0.1
        color_list = ['b', 'g', 'r', 'y', 'm']
        for i, j, k in zip(list, color_list, range(0, len(list))):
            ax.bar(pos + width * k, i, width, alpha=0.5, color=j)

        # Set the y axis label
        ax.set_ylabel('Count')

        # Set the chart's title
        ax.set_title(text)

        # Set the position of the x ticks
        ax.set_xticks([pos + 1.5 * width])

        # Setting the x-axis and y-axis limits
        plt.xlim(pos - width, pos + width * 3)

        k = 0
        for i in list:
            k += i
        plt.ylim([0, k])

        # Adding the legend and showing the plot
        ax.legend(label_list, loc='upper left')
        ax.grid()


    def pie_chart_for_specified_type(self, text):
        canvas = Canvas(self, width=8, height=4)
        self.gridLayout.addWidget(canvas,1,0)
        ax = canvas.figure.add_subplot(111)
        label_list = []
        label_list.extend(return_label_list(text))
        pie_chart_list = []
        pie_chart_list.extend(list_to_display_on_pie(text))
        wedges, texts, autotexts =ax.pie(pie_chart_list, explode=None, colors=['b', 'g', 'r', 'y', 'm'], autopct='% 1d %%')
        ax.legend(wedges, label_list,
                  title=text,
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()