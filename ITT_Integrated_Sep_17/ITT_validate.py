import re
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from itt_utils import *

def bt_title_validate(title):
    mymsg = ""
    ck = False
    ret = []
    print(type(ret))
    numbers = re.findall('\d+', title)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (len(title) == 0):
        print("vt1")
        ck = False
        mymsg += "Title is Empty"
        print(mymsg)
        ret = [mymsg,ck]
        print("ret ,", ret)
        return ret

    if (len(numbers) > 0):
        print("vt2")
        ck = False
        if (mymsg != ""):
            mymsg += ","
        mymsg += "Invalid title only alphabets are allowed"
        print(mymsg)
        ret = [mymsg, ck]
        print("ret ,", ret)
        return ret

    if (regex.search(title) != None):
        print("vt3")
        ck = False
        if (mymsg != ""):
            mymsg += ","
        mymsg += "Invalid title only alphabets are allowed"
        print(mymsg)
        ret = [mymsg, ck]
        print("ret ,", ret)
        return ret

    if (len(title) > 80):
        print("vt4")
        ck = False
        if (mymsg != ""):
            mymsg += ","
        mymsg += "Invalid title max only 80 characters are allowed"
        print(mymsg)
        ret = [mymsg, ck]
        print("ret ,", ret)
        return ret

    else:
        print("vt5")

        if (mymsg != ""):
            mymsg += ","
        mymsg += "Valid title"
        print(mymsg)
        ret = [mymsg, True]
        print("ret ,", ret)
        return ret

def bt_des_validate(des):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    ck = False
    mymsg = ""
    if (len(des) == 0):
        print("d1")
        mymsg += "Description is Empty"
        print(mymsg)
        ret = [mymsg, ck]
        print("ret ,", ret)
        return ret

    if (regex.search(des) != None):
        print("d2")
        if (mymsg != ""):
            mymsg += ","
        mymsg += "Invalid Description only alphanumeric are allowed"
        print(mymsg)
        ret = [mymsg, ck]
        print("ret ,", ret)
        return ret
    else:
        print("d3")
        if (mymsg != ""):
            mymsg += ","
        mymsg += "Valid Description only alphanumeric are allowed"
        print(mymsg)
        ret = [mymsg, True]
        print("ret ,", ret)
        return ret


def bt_assignee_validate(assignee):
    mymsg = ""
    ck = False
    print(assignee)
    assignee = str(assignee)
    numbers = re.findall('\d+',assignee)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    print("len:",len(assignee))
    if(len(assignee) == 0):
        print("a1")
        if (mymsg != ""):
            mymsg += ","
        mymsg += "Valid assignee"
        ret = [mymsg, True]
        print("ret ,", ret)
        return ret

    if (len(numbers) > 0):
        print("a2")
        if (mymsg != ""):
            mymsg += ","
        mymsg += "Invalid assignee only alphabets are allowed"
        print(mymsg)
        ret = [mymsg, ck]
        print("ret ,", ret)
        return ret

    if (regex.search(assignee) != None):
        print("a3")
        if (mymsg != ""):
            mymsg += ","
        mymsg += "Invalid assignee only alphabets are allowed"
        print(mymsg)
        ret = [mymsg, ck]
        print("ret ,", ret)
        return ret

    else:
        print("a4")
        file = "Credentials.csv"
        ass_list = [value_chk.empty.value]
        util = utils()
        print(util.user_name_validtion(ass_list, file, assignee))

        if (ass_list[0] == value_chk.valid.value):
            print("a5")
            if (mymsg != ""):
                mymsg += ","
            mymsg += "Valid assignee"
            print(mymsg)
            ret = [mymsg, True]
            print("ret ,", ret)
            return ret
        else:
            if (mymsg != ""):
                mymsg += ","
            mymsg += "Assignee not registered"
            print(mymsg)
            ret = [mymsg, False]
            print("ret ,", ret)


def bt_build_validate(buildid):
    print(buildid)
    ck = False
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    mymsg = ""
    if(regex.search(buildid) != None):
        if (mymsg != ""):
            print("b1")
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

def title_validate(title):
    numbers = re.findall('\d+', title)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(len(title) == 0):
            print("t1")
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("Please enter the title")
            x = msg.exec_()

    if(len(numbers) > 0):
        print("t2")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Title is not valid, Enter only alphabets")
        x = msg.exec_()

    if (regex.search(title) != None):
        print("t3")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Title is not valid, Enter only alphabets")
        x = msg.exec_()

    if(len(title) > 80):
        print("t4")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Please enter the title less than 80 characters")
        x = msg.exec_()

def des_validate(des):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(len(des) == 0):
        print("d1")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Description is empty")
        x = msg.exec_()

    if (regex.search(des) != None):
        print("d2")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Description is not valid, Enter only alphabets characters")
        x = msg.exec_()

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
        msg.setWindowTitle("Information")
        msg.setText("No Cr exist Please create a new Cr")
        x = msg.exec_()
        return False
    else:
        return ck

def build_validate(buildid):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if (regex.search(buildid) != None):
        print("d2")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Build I'd is not valid, Enter only alphanumeric characters")
        x = msg.exec_()
        return False

    if(len(buildid) == 0):
        print("b2")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Please enter Build I'd")
        x = msg.exec_()
        return False
    else:
        print("b3")
        return True

def assignee_validate(assignee):
    file = "Credentials.csv"
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    numbers = re.findall('\d+', assignee)
    ck = False

    ass_list = [value_chk.empty.value]
    util = utils()
    print(util.user_name_validtion(ass_list,file,assignee))

    if (len(numbers) > 0):
        print("t2")
        ck = True
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("assignee is not valid, Enter only alphabets")
        x = msg.exec_()

    if (regex.search(assignee) != None):
        print("t3")
        ck = True
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Title is not valid, Enter only alphabets")
        x = msg.exec_()

    if((ass_list[0] != value_chk.valid.value and ck == False) and len(assignee)!=0):
        print("3")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Assignee not registered")
        x = msg.exec_()