from PyQt5.QtWidgets import QMessageBox

def  display(title_ret,des_ret,build_ret,assignee_ret):
    print("in display")
    print(title_ret[0],"1",title_ret[1])
    print(des_ret[0],"1",des_ret[1])
    print(build_ret[0],"1",build_ret[1])
    print(assignee_ret[0],"1",assignee_ret[1])
    if(title_ret[1] and des_ret[1] and build_ret[1] and assignee_ret[1]):
        return True
    else:
        msg = "" 
        msg += title_ret[0]+", " + des_ret[0]+ ", " + build_ret[0]+ ", " + assignee_ret[0]
        print(msg)
        Msg = QMessageBox()
        Msg.setWindowTitle("Information")
        Msg.setText(msg)
        x = Msg.exec_()
        return False