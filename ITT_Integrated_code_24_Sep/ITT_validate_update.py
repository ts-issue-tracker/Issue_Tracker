import re
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from itt_utils import *

def domain_validate(domain):
    if(domain == "Select"):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Please select any Domain/Techarea")
        x = msg.exec_()
        return False
    else:
        return True

def title_validate_update(title):
    numbers = re.findall('\d+', title)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (len(title) == 0):
        print("t1")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Please enter the title")
        x = msg.exec_()
        return False

    if (len(numbers) > 0):
        print("t2")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Title is not valid, Enter only alphabets")
        x = msg.exec_()
        return False

    if (regex.search(title) != None):
        print("t3")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Title is not valid, Enter only alphabets")
        x = msg.exec_()
        return False

    if (len(title) > 80):
        print("t4")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Please enter the title less than 80 characters")
        x = msg.exec_()
        return False
    else:
        True

def des_validate_update(des):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(len(des) == 0):
        print("d1")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Description is empty")
        x = msg.exec_()
        return False

    if (regex.search(des) != None):
        print("d2")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Description is not valid, Enter only alphabets characters")
        x = msg.exec_()
        return False

    else:
        return True

def assignee_validate_update(assignee):
    file = "Credentials.csv"
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    numbers = re.findall('\d+', assignee)
    ck = False

    ass_list = [value_chk.empty.value]
    util = utils()
    print(util.user_name_validtion(ass_list, file, assignee))

    if (len(numbers) > 0):
        print("t2")
        ck = True
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("assignee is not valid, Enter only alphabets")
        x = msg.exec_()
        return False

    if (regex.search(assignee) != None):
        print("t3")
        ck = True
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Title is not valid, Enter only alphabets")
        x = msg.exec_()
        return False

    if ((ass_list[0] != value_chk.valid.value and ck == False) and len(assignee) != 0):
        print("3")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Assignee not registered")
        x = msg.exec_()
        return False
    else:
        return True

def build_validate_update(buildid,newid):
    regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')

    if (regex.search(buildid) != None and regex.search(buildid) != None ):
        print("d2")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Build I'd is not valid, Enter only alphanumeric characters")
        x = msg.exec_()
        return False

    if(len(buildid) == 0 and len(buildid) == 0):
        print("b2")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Please enter Build I'd")
        x = msg.exec_()
        return False

    if(buildid == newid):
        print("b4")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Build id should not same as the one given when the CR is created.")
        x = msg.exec_()
        return False

    else:
        print("b3")
        return True

def git_validate_update(git):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(len(git) == 0):
        print("g1")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Build id should not same as the one given when the CR is created.")
        x = msg.exec_()
        return False

    else:
        print("g2")
        return True

def issue_reason_validate_update(reason):
    regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
    if (regex.search(reason) != None):
        print("t3")
        ck = True
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("reason in valid")
        x = msg.exec_()
        return False
    else:
        return True

def bt_build_validate_new(buildid,new):
        print(buildid)
        ck = False
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        mymsg = ""
        if(buildid == new):
            print("b0")
            if (mymsg != ""):
                mymsg += ","
            mymsg += "Build id should not be same Please change"
            print(mymsg)
            ret = [mymsg, ck]
            print("ret ,", ret)
            return ret
        if (regex.search(buildid) != None):
            print("b1")
            if (mymsg != ""):
                mymsg += ","
            mymsg += "Invalid build I'd only alphanumeric are allowed"
            print(mymsg)
            ret = [mymsg, ck]
            print("ret ,", ret)
            return ret

        if (len(buildid) == 0):
            print("b2")
            mymsg += "Build I'd is Empty"
            print(mymsg)
            ret = [mymsg, ck]
            print("ret ,", ret)
            return ret
        else:
            print("b3")
            mymsg += "Valid build I'd"
            print(mymsg)
            ret = [mymsg, True]
            print("ret ,", ret)
            return ret