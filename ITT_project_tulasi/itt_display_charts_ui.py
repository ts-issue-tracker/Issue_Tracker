#from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame, QGridLayout, QComboBox, QLabel, QLineEdit
import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from itt_mail_sending import *
from itt_main_file_access import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
from itt_utils import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Display Statistics"
        top = 400
        left = 400
        width = 900
        height = 500

        self.filtertype = ""
        self.list_to_send = []
        self.list_of_labels_to_send = []

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.frame = QFrame(self)
        self.frame.setFixedSize(900, 500)
        self.frame.setFrameShape(QFrame.StyledPanel)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)

        self.frame_one = QFrame(self)
        #self.frame_one.setFrameShape(QFrame.StyledPanel)
        self.frame_one.setFixedSize(850, 60)

        self.gridLayout_one = QGridLayout(self.frame_one)
        self.gridLayout.addWidget(self.frame_one,0,0)

        self.frame_two = QFrame(self)
        #self.frame_two.setFrameShape(QFrame.StyledPanel)
        self.frame_two.setFixedSize(850, 60)

        self.gridLayout_two = QGridLayout(self.frame_two)
        self.gridLayout.addWidget(self.frame_two, 2, 0)
        #self.gridLayout_one.setContentsMargins(20, 20, 20, 20)

        self.MyUI()

    def MyUI(self):
        self.TypeCombo = QComboBox(self)
        self.TypeCombo.setFont(QFont('Arial', 10))
        self.TypeCombo.addItem('State')
        self.TypeCombo.addItem('Domain')
        self.TypeCombo.addItem('IssueType')
        self.TypeCombo.activated[str].connect(self.readType)
        self.TypeCombo.setFixedWidth(150)

        typeLabel = QLabel("&Type:")
        typeLabel.setFont(QFont('Arial', 10))
        typeLabel.setFixedWidth(50)
        typeLabel.setBuddy(self.TypeCombo)

        self.AssigneeCombo = QComboBox(self)
        self.AssigneeCombo.setFont(QFont('Arial', 10))
        self.AssigneeCombo.addItem('Tulasi')
        self.AssigneeCombo.addItem('Santhoshi')
        self.AssigneeCombo.addItem('Pavani')
        self.AssigneeCombo.addItem('Sumalatha')
        self.AssigneeCombo.addItem('Suresh')
        self.AssigneeCombo.addItem('Swetha')
        self.AssigneeCombo.activated[str].connect(self.readAssignee)
        self.AssigneeCombo.setFixedWidth(150)

        AssigneeLabel = QLabel("&Assignee && &Type:")
        AssigneeLabel.setFixedWidth(100)
        AssigneeLabel.setFont(QFont('Arial', 10))
        AssigneeLabel.setBuddy(self.AssigneeCombo)

        self.DomianCombo = QComboBox(self)
        self.DomianCombo.setFont(QFont('Arial', 10))
        self.DomianCombo.addItem('Audio')
        self.DomianCombo.addItem('Camera')
        self.DomianCombo.addItem('Video')
        self.DomianCombo.activated[str].connect(self.readDomain)
        self.DomianCombo.setFixedWidth(150)

        DomainLabel = QLabel("&Domain && &Type:")
        DomainLabel.setFixedWidth(100)
        DomainLabel.setFont(QFont('Arial', 10))
        DomainLabel.setBuddy(self.DomianCombo)

        self.ChartTypeCombo = QComboBox(self)
        self.ChartTypeCombo.setFont(QFont('Arial', 10))
        self.ChartTypeCombo.addItem('Pie Chart')
        self.ChartTypeCombo.addItem('Bar Chart')
        self.ChartTypeCombo.activated[str].connect(self.readChartType)
        self.ChartTypeCombo.setFixedWidth(150)
        ChartTypeLabel = QLabel("&ChartType:")
        ChartTypeLabel.setFixedWidth(100)
        ChartTypeLabel.setFont(QFont('Arial', 10))
        ChartTypeLabel.setBuddy(self.ChartTypeCombo)

        email_lb = QLabel("Email ID")
        email_lb.setFont(QFont('Arial', 10))

        self.email_txt = QLineEdit()
        self.email_txt.setFont(QFont('Arial', 10))
        self.email_txt.editingFinished.connect(self.email_validation)
        self.email_txt.resize(130,100)

        send_mail_btn = QPushButton()
        send_mail_btn.setText("Send Mail")
        send_mail_btn.setFont(QFont('Arial', 10))
        send_mail_btn.clicked.connect(self.send_mail_btn_click)

        self.gridLayout_one.addWidget(typeLabel, 0, 0)
        self.gridLayout_one.addWidget(self.TypeCombo,0,1)

        self.gridLayout_one.addWidget(AssigneeLabel,0,2)
        self.gridLayout_one.addWidget(self.AssigneeCombo,0,3)

        self.gridLayout_one.addWidget(DomainLabel, 0, 4)
        self.gridLayout_one.addWidget(self.DomianCombo, 0, 5)

        self.gridLayout_two.addWidget(ChartTypeLabel, 0, 0)
        self.gridLayout_two.addWidget(self.ChartTypeCombo, 0, 1)

        self.gridLayout_two.addWidget(email_lb,0,2)
        self.gridLayout_two.addWidget(self.email_txt,0,3)

        self.gridLayout_two.addWidget(send_mail_btn, 0, 4)

        self.pie_chart_for_specified_type(self.TypeCombo.currentText())

        self.util = utils()

    def email_validation(self):
        self.list=[]
        self.list.append(0)
        msg_to_display = ""
        msg_to_display += self.email_validation_with_msg(self.list, self.email_txt.text())
        if len(msg_to_display) != 0:
            QMessageBox.about(self, 'Information', msg_to_display)

    def email_validation_with_msg(self,list,email_id):
        msg_to_return = ""
        result = valid.email_id_check(email_id)
        if result == valid.SUCCESS:
            if email_id == "":
                list[0] = value_chk.empty.value
            else:
                list[0] = value_chk.valid.value
        else:
            msg_to_return += "Invalid Email ID"
            list[0] = value_chk.invalid.value
        return msg_to_return
    def init_msg(self):
        self.filtertype=""
        self.filtertype+="FILTER:"
        self.list_of_labels_to_send=[]
        self.list_to_send=[]

    def send_mail_btn_click(self):
        msg_to_send="Hey,..Please find the statistics details mentioned below :)\n\n\n"
        msg=""
        for i,j in zip(self.list_of_labels_to_send,self.list_to_send):
            msg+=i+": "+str(j)+"\n"
        msg_to_send+=self.filtertype+msg
        if len(msg_to_send)!=0:
            sending_mail_with_selected_statistics_info(self.email_txt.text(),msg_to_send)
    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self, frame):
        frame.move((self.width() - self.frame.width()) / 2, (self.height() - self.frame.height()) / 2)

    def readType(self, text):
        self.init_msg()
        self.msg_format_for_display("Type",text)
        if self.ChartTypeCombo.currentText()=="Pie Chart":
            self.pie_chart_for_specified_type(text)
        else:
            self.bar_chart_for_specified_type(text)
    def msg_format_for_display(self,type,text):
        self.filtertype+=" \""+type+"\"\nSELECTED: \""+text+"\"\n\n"

    def readChartType(self, text):
        pass

    def readDomain(self, text):
        type = self.TypeCombo.currentText()
        domain = self.DomianCombo.currentText()
        self.init_msg()
        self.msg_format_for_display("Domain & Type",domain+" & "+type)
        if self.ChartTypeCombo.currentText()=="Pie Chart":
            self.readDomain_for_pie_chart(type,domain,text)
        else:
            self.readDomain_for_bar_chart(type,domain,text)

    def readAssignee(self, text):
        type = self.TypeCombo.currentText()
        assignee = self.AssigneeCombo.currentText()
        self.init_msg()
        self.msg_format_for_display("Assignee & Type", assignee + " & " + type)
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
        self.list_of_labels_to_send.extend(label_list)
        list = []
        list.extend(list_to_display_on_pie_for_assignee(col, assignee_or_domain, type))
        self.list_to_send.extend(list)
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
        self.list_of_labels_to_send.extend(label_list)
        list = []
        list.extend(list_to_display_on_pie_for_assignee(col, assignee_or_domain, type))
        self.list_to_send.extend(list)
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
        self.list_of_labels_to_send.extend(label_list)
        list = []
        list.extend(list_to_display_on_pie(text))
        self.list_to_send.extend(list)
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
        self.list_of_labels_to_send.extend(label_list)
        pie_chart_list = []
        pie_chart_list.extend(list_to_display_on_pie(text))
        self.list_to_send.extend(pie_chart_list)
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