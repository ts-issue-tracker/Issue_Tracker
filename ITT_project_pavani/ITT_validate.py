import re
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QMessageBox

global msg


def title_validate(title):
    numbers = re.findall('\d+', title)
    symbols = re.findall(r"[~!@#$%^&*()_+':;<>?,.|\\/\"]", title)
    if(len(title) == 0):
            msg = QMessageBox()
            msg.setWindowTitle("Invalid")
            msg.setText("Please enter the title")
            x = msg.exec_()
            return False
    if(len(numbers) > 0 or len(symbols)>0):
        print("val if")
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Title is not valid")
        x = msg.exec_()
        return False
    if(len(title) > 80):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Please enter the title less than 80 characters")
        x = msg.exec_()
        return False
    else:
        return True

def des_validate(des):
    if(len(des) == 0):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Description shouldnot be empty")
        x = msg.exec_()
        return False
    else:
        return True

def cr_state_validate(status):
    if status != "Open":
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Change the CR State to open")
        x = msg.exec_()
        return False
    else:
        return True

def domain_validate(domain):
    if domain == "Select":
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Please Select tech area/domain")
        x = msg.exec_()
        return False
    else:
        return True

def build_validation(build):
    str = str(build)
    symbols = re.findall(r"[~!@#$%^&*()_+':;<>?,|\\/\"]", str)
    if str.isupper() or str.isalnum():
        return True
    if len(symbols) > 0:
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Build Id is invalid")
        x = msg.exec_()
        return False
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Build Id is invalid")
        x = msg.exec_()
        return False

def validate_cr_list(crno):
    ck = -1
    with open('cr_list_entry.csv') as g:
        reader1 = csv.reader(g, delimiter=",")
        data1 = list(reader1)
        row_count1 = len(data1)
    with open('cr_list_entry.csv') as f:
        reader = csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        for i in range(row_count1):
            if crno == data[i][0]:
                ck = i
    if ck == -1:
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("No Cr exist Please create a new Cr")
        x = msg.exec_()
        return False
    else:
        return ck