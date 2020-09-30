from PyQt5.QtWidgets import QMessageBox

def display_create(title_ret,des_ret,build_ret,assignee_ret,domain):
    display_msg = ""
    count = 0
    print("in display")
    print(title_ret[0], "1", title_ret[1])
    print(des_ret[0], "1", des_ret[1])
    print(build_ret[0], "1", build_ret[1])
    print(assignee_ret[0], "1", assignee_ret[1])
    print("calling")
    if(title_ret[1] == False):
        count += 1
        if(len(display_msg) > 0):
            display_msg +="\n" + title_ret[0]
        else:
            display_msg += title_ret[0]
    if (des_ret[1] == False):
        if (len(display_msg) > 0):
            display_msg += "\n" + des_ret[0]
        else:
            display_msg += des_ret[0]

    if (build_ret[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + build_ret[0]
        else:
            display_msg += build_ret[0]

    if (assignee_ret[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + assignee_ret[0]
        else:
            display_msg += assignee_ret[0]

    if (domain[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + domain[0]
        else:
            display_msg += domain[0]
    if(count > 0):
        Msg = QMessageBox()
        Msg.setWindowTitle("Information")
        Msg.setText(display_msg)
        x = Msg.exec_()
        return False
    else:
        return True

def  display(title_ret,des_ret,build_ret,assignee_ret,si_state,cr_state,git,domain,reason,buildid):
    print("in display")
    #print(title_ret[0],"1",title_ret[1])
    #print(des_ret[0],"1",des_ret[1])
    #print(build_ret[0],"1",build_ret[1])
    #print(assignee_ret[0],"1",assignee_ret[1])
    #print(git[0],"1",git[1])
    #print(reason[0],"1",reason[1])
    display_msg = ""
    count = 0

    if (title_ret[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + title_ret[0]
        else:
            display_msg += title_ret[0]
    if (des_ret[1] == False):
        if (len(display_msg) > 0):
            display_msg += "\n" + des_ret[0]
        else:
            display_msg += des_ret[0]

    if (build_ret[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + build_ret[0]
        else:
            display_msg += build_ret[0]

    if (assignee_ret[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + assignee_ret[0]
        else:
            display_msg += assignee_ret[0]

    if (si_state[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + si_state[0]
        else:
            display_msg += si_state[0]

    if (cr_state[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + cr_state[0]
        else:
            display_msg += cr_state[0]

    if (git[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + git[0]
        else:
            display_msg += git[0]

    if (reason[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + reason[0]
        else:
            display_msg += reason[0]

    if (buildid[1] == False):
        count += 1
        if (len(display_msg) > 0):
            display_msg += "\n" + buildid[0]
        else:
            display_msg += buildid[0]
    if (count > 0):
        Msg = QMessageBox()
        Msg.setWindowTitle("Information")
        Msg.setText(display_msg)
        x = Msg.exec_()
        return False
    else:
        return True
