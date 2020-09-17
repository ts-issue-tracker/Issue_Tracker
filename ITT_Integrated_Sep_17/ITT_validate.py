import re
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

def title_validate(title):
    numbers = re.findall('\d+', title)
    symbols = re.findall(r"[~`!@#$%^&*(){}[]_-+':;<>?=|\\/\"]", title)

    if(len(title) == 0):
            print("t1")
            msg = QMessageBox()
            msg.setWindowTitle("Invalid")
            msg.setText("Please enter the title")
            x = msg.exec_()
            return False

    if(len(numbers) > 0 or len(symbols)>0):
        print("t2")
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Title is not valid")
        x = msg.exec_()
        return False

    if(len(title) > 80):
        print("t3")
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Please enter the title less than 80 characters")
        x = msg.exec_()
        return False

    else:
        print("t4")
        return True

def des_validate(des):
    numbers = re.findall('\d+', des)
    symbols = re.findall(r"[~`!@#$%^&*(){}[]_-+':;<>=?|\\/\"]", des)

    if(len(des) == 0):
        print("d1")
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Description should not be empty")
        x = msg.exec_()
        return False

    if (len(numbers) > 0 or len(symbols) > 0):
        print("d2")
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Description is not valid")
        x = msg.exec_()
        return False
    else:
        print("d3")
        return True

def domain_validate(domain):
    if domain == "Select":
        print("d01")
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Please Select tech area/domain")
        x = msg.exec_()
        return False
    else:
        print("do2")
        return True

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

def build_validate(buildid):
    print(buildid)
    symbols = re.findall(r"[~`!@#$%^&*(){}[]_-=+':;<>?|\\/\"]", buildid)
    print(symbols)
    if(len(symbols) > 0):
        print("b1")
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Build Id is not valid")
        x = msg.exec_()
        return False
    if(len(buildid) == 0):
        print("b2")
        msg = QMessageBox()
        msg.setWindowTitle("Invalid")
        msg.setText("Please enter Build id")
        x = msg.exec_()
        return False
    else:
        print("b3")
        return True

def assignee_validate(assignee):
    ck = False
    if(len(assignee == 0)):
        return True