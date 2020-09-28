from PyQt5.QtWidgets import QMessageBox

def display_create(title_ret,des_ret,build_ret,assignee_ret):
    print("in display")
    print(title_ret[0], "1", title_ret[1])
    print(des_ret[0], "1", des_ret[1])
    print(build_ret[0], "1", build_ret[1])
    print(assignee_ret[0], "1", assignee_ret[1])
    if (title_ret[1] and des_ret[1] and build_ret[1] and assignee_ret[1]):
        print("true")
        return True

    else:
        print("any one false")
        msg = ""
        msg += title_ret[0] + ", " + des_ret[0] + ", " + build_ret[0] + ", " + assignee_ret[0]
        print(msg)
        Msg = QMessageBox()
        Msg.setWindowTitle("Information")
        Msg.setText(msg)
        x = Msg.exec_()
        return False

def  display(title_ret,des_ret,build_ret,assignee_ret,si_state,cr_state,git,domain,reason,buildid):
    print("in display")
    print(title_ret[0],"1",title_ret[1])
    print(des_ret[0],"1",des_ret[1])
    print(build_ret[0],"1",build_ret[1])
    print(assignee_ret[0],"1",assignee_ret[1])
    print(git[0],"1",git[1])
    print(reason[0],"1",reason[1])
    if(title_ret[1] and des_ret[1] and build_ret[1] and assignee_ret[1] and si_state[1] and cr_state[1] and git[1] and domain[1]
            and reason[1] and buildid[1]):
        print("true")
        return True
    else:
        print("any one false")
        msg = "" 
        msg += title_ret[0]+", " + des_ret[0]+ ", " + build_ret[0]+ ", " + assignee_ret[0] + ", " + si_state[0] + ", " +cr_state[0] + ", "\
               + git[0] + ", " + domain[0] + ", " + reason[0] + ", " + buildid[0]
        print(msg)
        Msg = QMessageBox()
        Msg.setWindowTitle("Information")
        Msg.setText(msg)
        x = Msg.exec_()
        return False