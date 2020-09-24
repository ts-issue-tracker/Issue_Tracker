#from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame, QGridLayout, QComboBox, QLabel, QLineEdit
import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from itt_mail_sending import *
from itt_main_file_access import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
from itt_utils import *
from PyQt5.QtGui import *
from itt_resource_names import *

from PyQt5.QtGui import QPalette,QImage,QPageSize,QBrush
from PyQt5.QtCore import QSize

class Statistics_Window(QWidget):
    def __init__(self):
        super().__init__()

        title = "Display Statistics"

        self.filtertype = ""
        self.list_to_send = []
        self.list_of_labels_to_send = []
        self.list=[value_chk.empty.value,value_chk.empty.value,value_chk.empty.value]
        self.label=["Mail ID","Password","Recipient Mail ID"]
        self.setWindowTitle(title)
        self.setMinimumWidth(1000)
        self.setMinimumHeight(800)

        oImage = QImage("image2.jpg")
        sImage = oImage.scaled(QSize(1000, 1000))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.frame = QFrame(self)
        self.frame.setFixedSize(1000, 700)
        #self.frame.setFrameShape(QFrame.StyledPanel)

        #self.setGeometry(330, 35, 700, 1000)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)

        self.frame_one = QFrame(self)
        #self.frame_one.setFrameShape(QFrame.StyledPanel)
        self.frame_one.setFixedSize(950, 60)

        self.gridLayout_one = QGridLayout(self.frame_one)
        self.gridLayout.addWidget(self.frame_one,0,0)

        self.frame_two = QFrame(self)
        #self.frame_two.setFrameShape(QFrame.StyledPanel)
        self.frame_two.setFixedSize(850, 60)

        self.frame_canvas=QFrame(self)
        #self.frame_canvas.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_canvas = QGridLayout(self.frame_canvas)
        self.frame_canvas.setFixedSize(950, 350)
        self.gridLayout.addWidget(self.frame_canvas, 1, 0)

        self.gridLayout_two = QGridLayout(self.frame_two)
        self.gridLayout.addWidget(self.frame_two, 2, 0)

        self.frame_three = QFrame(self)
        #self.frame_three.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_three = QGridLayout(self.frame_three)
        self.frame_three.setFixedSize(400, 200)
        self.gridLayout.addWidget(self.frame_three, 3, 0)
        self.names=resource_names()

        self.MyUI()

    def MyUI(self):
        self.TypeCombo = QComboBox(self)
        self.TypeCombo.setFont(QFont('Arial', 10))
        self.TypeCombo.addItem('State')
        self.TypeCombo.addItem('Domain')
        self.TypeCombo.addItem('Issue Type')
        self.TypeCombo.activated[str].connect(self.readType)
        self.TypeCombo.setFixedWidth(120)

        typeLabel = QLabel("&Type:")
        typeLabel.setFont(QFont('Arial', 10))
        typeLabel.setFixedWidth(50)
        typeLabel.setBuddy(self.TypeCombo)

        self.names.get_assignee_names()

        self.AssigneeCombo = QComboBox(self)
        self.AssigneeCombo.setFont(QFont('Arial', 10))
        for i in self.names.get_assignee_names():
            self.AssigneeCombo.addItem(i)
        self.AssigneeCombo.activated[str].connect(self.readAssignee)
        self.AssigneeCombo.setFixedWidth(120)

        AssigneeLabel = QLabel("&Assignee:")
        AssigneeLabel.setFixedWidth(80)
        AssigneeLabel.setFont(QFont('Arial', 10))
        AssigneeLabel.setBuddy(self.AssigneeCombo)

        self.DomianCombo = QComboBox(self)
        self.DomianCombo.setFont(QFont('Arial', 10))
        for i in self.names.get_domain_names():
            self.DomianCombo.addItem(i)
        self.DomianCombo.activated[str].connect(self.readDomain)
        self.DomianCombo.setFixedWidth(120)

        DomainLabel = QLabel("&Domain:")
        DomainLabel.setFixedWidth(100)
        DomainLabel.setFont(QFont('Arial', 10))
        DomainLabel.setBuddy(self.DomianCombo)

        self.ChartTypeCombo = QComboBox(self)
        self.ChartTypeCombo.setFont(QFont('Arial', 10))
        self.ChartTypeCombo.addItem('Pie Chart')
        self.ChartTypeCombo.addItem('Bar Chart')
        self.ChartTypeCombo.activated[str].connect(self.readChartType)
        self.ChartTypeCombo.setFixedWidth(120)

        ChartTypeLabel = QLabel("&ChartType:")
        ChartTypeLabel.setFixedWidth(100)
        ChartTypeLabel.setFont(QFont('Arial', 10))
        ChartTypeLabel.setBuddy(self.ChartTypeCombo)

        email_lb1 = QLabel("Mail ID")
        email_lb1.setFont(QFont('Arial', 10))

        self.mail_txt = QLineEdit()
        self.mail_txt.setFont(QFont('Arial', 10))
        self.mail_txt.setFixedWidth(200)
        self.mail_txt.editingFinished.connect(lambda: self.email_validation(email_lb1.text(),0))
        #self.mail_txt.setFixedWidth(250)

        email_pwd = QLabel("Password")
        email_pwd.setFont(QFont('Arial', 10))

        self.pwd_txt = QLineEdit()
        self.pwd_txt.setFont(QFont('Arial', 10))
        self.pwd_txt.editingFinished.connect(self.password_validation)
        #self.pwd_txt.setFixedWidth(250)
        self.pwd_txt.setEchoMode(QLineEdit.Password)
        self.pwd_txt.setFixedWidth(200)

        rx_email_lb = QLabel("Recipient Mail ID")
        rx_email_lb.setFixedWidth(165)
        rx_email_lb.setFont(QFont('Arial', 10))

        self.rx_email_txt = QLineEdit()
        self.rx_email_txt.setFont(QFont('Arial', 10))
        self.rx_email_txt.editingFinished.connect(lambda: self.email_validation(rx_email_lb.text(),2))
        self.rx_email_txt.setFixedWidth(200)

        send_mail_btn = QPushButton()
        send_mail_btn.setText("Send Mail")
        send_mail_btn.setFont(QFont('Arial', 10))
        send_mail_btn.clicked.connect(self.send_mail_btn_click)
        send_mail_btn.setFixedWidth(100)

        exit_btn = QPushButton()
        exit_btn.setText("Exit")
        exit_btn.setFont(QFont('Arial', 10))
        exit_btn.clicked.connect(self.exit_btn_click)
        exit_btn.setFixedWidth(100)

        self.msg_txt = QTextEdit()
        self.msg_txt.setFont(QFont('Arial', 10))
        self.msg_txt.setFixedWidth(250)
        self.msg_txt.setFixedHeight(self.frame_canvas.height()-20)
        self.msg_txt.setReadOnly(True)

        self.gridLayout_canvas.addWidget(self.msg_txt,1,0)

        self.gridLayout_one.addWidget(typeLabel, 0, 0)
        self.gridLayout_one.addWidget(self.TypeCombo,0,1)

        self.gridLayout_one.addWidget(AssigneeLabel,0,2)
        self.gridLayout_one.addWidget(self.AssigneeCombo,0,3)

        self.gridLayout_one.addWidget(DomainLabel, 0, 4)
        self.gridLayout_one.addWidget(self.DomianCombo, 0, 5)

        self.gridLayout_one.addWidget(ChartTypeLabel, 0, 6)
        self.gridLayout_one.addWidget(self.ChartTypeCombo, 0, 7)

        self.gridLayout_three.addWidget(email_lb1,0,0)
        self.gridLayout_three.addWidget(self.mail_txt, 0, 1)

        self.gridLayout_three.addWidget(email_pwd, 1, 0)
        self.gridLayout_three.addWidget(self.pwd_txt, 1, 1)

        self.gridLayout_three.addWidget(rx_email_lb, 2, 0)
        self.gridLayout_three.addWidget(self.rx_email_txt, 2, 1)
        self.gridLayout_three.addWidget(send_mail_btn, 3, 0)
        self.gridLayout_three.addWidget(exit_btn, 3, 2)

        self.pie_chart_for_specified_type(self.TypeCombo.currentText())

        self.util = utils()
        self.msg=""

    def exit_btn_click(self):
        from itt_main_ui import main_window
        self.w = main_window()
        self.w.show()
        self.hide()

    def email_validation(self,mail_label,index):
        if mail_label.__contains__("Recipient"):
            mail=self.rx_email_txt.text()
        else:
            mail=self.mail_txt.text()
        msg_to_display = ""
        msg_to_display += self.email_validation_with_msg(self.list, mail,mail_label,index)
        if len(msg_to_display) != 0:
            QMessageBox.about(self, 'Information', msg_to_display)

    def email_validation_with_msg(self,list,mail_id,mail_label,index):
        msg_to_return = ""
        result = valid.email_id_check(mail_id)
        if result == valid.SUCCESS:
            if mail_id == "":
                list[index] = value_chk.empty.value
            else:
                list[index] = value_chk.valid.value
        else:
            msg_to_return += "Invalid {}".format(mail_label)
            list[index] = value_chk.invalid.value
        return msg_to_return
    def init_msg(self):
        self.filtertype=""
        self.filtertype+="FILTER:"
        self.list_of_labels_to_send=[]
        self.list_to_send=[]
    def get_filter_msg(self):
        msg=""
        return_msg=""
        for i,j in zip(self.list_of_labels_to_send,self.list_to_send):
            msg+=i+": "+str(j)+"\n"
        return_msg+=self.filtertype+msg
        return  return_msg
    def password_validation(self):
        msg_to_display = ""
        if self.pwd_txt.text()=="":
            self.list[1]=value_chk.empty.value
        else:
            self.list[1] = value_chk.valid.value
        #msg_to_display+=self.util.password_validation\
        #   (self.list,self.pwd_txt.text())
        if len(msg_to_display)!=0:
            QMessageBox.about(self, 'Information', msg_to_display)


    def send_mail_btn_click(self):
        mail_deliver_msg=""
        msg_to_send="Hey,..Please find the statistics details mentioned below :)\n\n\n"
        subject="Issue Tracking Tool: Selected Statistics Information"
        msg_to_send+=self.get_filter_msg()
        mail_id=self.mail_txt.text()
        pwd=self.pwd_txt.text()
        rx_mail_id=self.rx_email_txt.text()
        print(mail_id+pwd+rx_mail_id)
        msg=self.util.empty_fields_message(self.list,self.label)
        msg+=self.util.display_statastics_invalid_fields_message(self.list,self.label)
        if msg!="":
            QMessageBox.about(self, 'Information', msg)
        print(self.list)
        print(msg_to_send)
        print(msg)
        if len(msg_to_send)!=0 and len(msg)==0 :
            if self.list[0]==value_chk.valid.value and self.list[1]==value_chk.valid.value \
                    and self.list[2]==value_chk.valid.value:
                mail_deliver_msg+=sending_mail(mail_id,pwd,rx_mail_id,msg_to_send,subject)
                QMessageBox.about(self, 'Information', mail_deliver_msg)

    def resizeEvent(self, event):
        self.centerOnScreen(self.frame)

    def centerOnScreen(self, frame):
        frame.move((self.width() - self.frame.width()) / 2, (self.height() - self.frame.height()) / 2)

    def readType(self, text):
        sheet_update()
        self.init_msg()
        self.msg_format_for_display("Type",text)
        if self.ChartTypeCombo.currentText()=="Pie Chart":
            self.pie_chart_for_specified_type(text)
        else:
            self.bar_chart_for_specified_type(text)
        self.msg_txt.setText(self.get_filter_msg())
    def msg_format_for_display(self,type,text):
        self.filtertype+=" \""+type+"\"\nSELECTED: \""+text+"\"\n\n"

    def readChartType(self, text):
        pass

    def readDomain(self, text):
        sheet_update()
        type = self.TypeCombo.currentText()
        domain = self.DomianCombo.currentText()
        self.init_msg()
        self.msg_format_for_display("Domain & Type",domain+" & "+type)
        if self.ChartTypeCombo.currentText()=="Pie Chart":
            self.readDomain_for_pie_chart(type,domain,text)
        else:
            self.readDomain_for_bar_chart(type,domain,text)
        self.msg_txt.setText(self.get_filter_msg())

    def readAssignee(self, text):
        sheet_update()
        type = self.TypeCombo.currentText()
        assignee = self.AssigneeCombo.currentText()
        self.init_msg()
        self.msg_format_for_display("Assignee & Type", assignee + " & " + type)
        if self.ChartTypeCombo.currentText()=="Pie Chart":
            self.readAssignee_for_pie_chart(type,assignee,text)
        else:
            self.readAssignee_for_bar_chart(type,assignee,text)
        self.msg_txt.setText(self.get_filter_msg())

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
        self.gridLayout_canvas.addWidget(self.canvas, 1, 1)
        ax = self.canvas.figure.add_subplot(111)
        col = return_col_of_specified_col_name(assignee_or_domain)
        label_list = []
        label_list.extend(return_label_list(type))
        self.list_of_labels_to_send.extend(label_list)
        list = []
        list.extend(list_to_display_on_pie_for_assignee(col, assignee_or_domain, type))
        self.list_to_send.extend(list)
        wedges, texts, autotexts = ax.pie(list, explode=None, colors=['b', 'g', 'r', 'y', 'm'],
                                          autopct=lambda p: '{:1d}%'.format(round(p)) if p > 0 else ''
                                          )
        ax.legend(wedges, label_list,
                  title=type,
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

    def read_assignee_or_domain_for_bar_char(self,type,assignee_or_domain,text):
        canvas = Canvas(self, width=8, height=6)
        self.gridLayout_canvas.addWidget(canvas, 1, 1)
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
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

        # Adding the legend and showing the plot
        ax.legend(label_list, loc='upper left')
        ax.grid()
    def bar_chart_for_specified_type(self,text):
        canvas = Canvas(self, width=8, height=6)
        self.gridLayout_canvas.addWidget(canvas, 1, 1)
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
            ax.bar(pos + width * k, i, width, alpha=1, color=j)

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
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

        # Adding the legend and showing the plot
        ax.legend(label_list, loc='upper left')
        ax.grid()


    def pie_chart_for_specified_type(self, text):
        sheet_update()
        self.init_msg()
        self.msg_format_for_display("Type", text)
        canvas = Canvas(self, width=8, height=4)
        self.gridLayout_canvas.addWidget(canvas,1,1)
        ax = canvas.figure.add_subplot(111)
        label_list = []
        label_list.extend(return_label_list(text))
        self.list_of_labels_to_send.extend(label_list)
        pie_chart_list = []
        pie_chart_list.extend(list_to_display_on_pie(text))
        self.list_to_send.extend(pie_chart_list)
        wedges, texts, autotexts =ax.pie(pie_chart_list, explode=None, colors=['b', 'g', 'r', 'y', 'm'],
                                         autopct=lambda p: '{:1d}%'.format(round(p)) if p > 0 else '')
        ax.legend(wedges, label_list,
                  title=text,
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
        self.msg_txt.setText(self.get_filter_msg())

class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Statistics_Window()
    window.show()
    sys.exit(App.exec())