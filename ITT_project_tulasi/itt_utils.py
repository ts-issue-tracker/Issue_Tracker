from validations import *
from PyQt5.QtWidgets import *
from validations import itt_validations as valid
import itt_credentials_file_access as file_access
import enum

class utils:
    def __init__(self):
        pass

    def empty_fields_message(self, list,lb_list):
        final_msg = ""
        count = 1
        for i in range(0,len(list)):
            if list[i] == value_chk.empty.value:
                count += 1
                final_msg += lb_list[i]
                final_msg += ","
        if len(final_msg) != 0:
            final_msg = final_msg[:-1]
        if count != 1:
            if count == 2:
                final_msg += " is Empty\n"
            else:
                final_msg += " are Empty\n"
        return final_msg

    def invalid_fields_message(self, list, lb_list,username):
        final_msg = ""
        count = 1
        for i in range(0, len(list)):
            if list[i] == value_chk.invalid.value or list[i]==value_chk.incorrect.value:
                count += 1
                final_msg += lb_list[i]
                if i==0 and list[i]==3:
                    final_msg=""
                    if not len(list)>2:
                        final_msg+="{} Didn\"t Registered yet,please register".format(username)
                        return final_msg
                    if  len(list)>2:
                        final_msg+="{} Username already available,please use any other".format(username)
                        return final_msg
                final_msg += ","
        if len(final_msg) != 0:
            final_msg = final_msg[:-1]
        if count != 1:
            if count == 2:
                final_msg += " is Invalid\n"
            else:
                final_msg += " are Invalid\n"
        return final_msg

    def user_name_validtion(self, list, credentials_file, username):
        msg_to_return = ""
        result = valid.username_check(username)
        if valid.SUCCESS == result:
            if username != "":
                is_duplicate = file_access.duplicates_checking(credentials_file, username)
                if not is_duplicate:
                    list[0]=value_chk.incorrect.value
                    msg_to_return+="Didnt Registered yet,please register"
                    return msg_to_return
            list[0] = value_chk.valid.value
        elif valid.EXCEED_LIMIT_ERR == result:
            msg_to_return += 'Information', "Max 15 characters are allowed\n"
            list[0] = value_chk.invalid.value
        elif valid.INVALID_INPUT_ERR == result:
            msg_to_return += "Invalid Username,Only alphabets are allowed\n"
            list[0] = value_chk.invalid.value
        return msg_to_return

    def user_name_validtion_register(self, list, credentials_file, username):
        msg_to_return = ""
        result = valid.username_check(username)
        if valid.SUCCESS == result:
            if username != "":
                is_duplicate = file_access.duplicates_checking(credentials_file, username)
                if is_duplicate:
                    list[0]=value_chk.incorrect.value
                    msg_to_return+="Username is already available,please use another"
                    return msg_to_return
            list[0] = value_chk.valid.value
        elif valid.EXCEED_LIMIT_ERR == result:
            msg_to_return += 'Information', "Max 15 characters are allowed\n"
            list[0] = value_chk.invalid.value
        elif valid.INVALID_INPUT_ERR == result:
            msg_to_return += "Invalid Username,Only alphabets are allowed\n"
            list[0] = value_chk.invalid.value
        return msg_to_return

    def password_validation(self, list, password):
        msg_to_return = ""
        result = valid.password_check(password)
        if valid.SUCCESS == result:
            if password=="":
                list[1]=value_chk.empty.value
            else:
                list[1] = value_chk.valid.value
        elif valid.EXCEED_LIMIT_ERR == result:
            msg_to_return += "Max 15 characters are allowed\n"
            list[1] = value_chk.invalid.value
        elif valid.INVALID_INPUT_ERR == result:
            msg_to_return += "Invalid Password,Only alphanumerics are allowed\n"
            list[1] = value_chk.invalid.value
        return msg_to_return
    def confirm_password_validation(self, list, confirm_password):
        msg_to_return = ""
        result = valid.password_check(confirm_password)
        if valid.SUCCESS == result:
            if confirm_password == "":
                list[2] = value_chk.empty.value
            else:
                list[2] = value_chk.valid.value
        elif valid.EXCEED_LIMIT_ERR == result:
            msg_to_return += "Max 15 characters are allowed\n"
            list[2] = value_chk.invalid.value
        elif valid.INVALID_INPUT_ERR == result:
            msg_to_return += "Invalid Confirm Password,Only alphanumerics are allowed\n"
            list[2] = value_chk.invalid.value
        return msg_to_return
    def email_validation(self,list,email_id):
        msg_to_return = ""
        result = valid.email_id_check(email_id)
        if result == valid.SUCCESS:
            if email_id=="":
                list[3]=value_chk.empty.value
            else:
                list[3]=value_chk.valid.value
        else:
            msg_to_return += "Invalid Email ID"
            list[3]=value_chk.invalid.value
        return msg_to_return

# creating enumerations using class
class value_chk(enum.Enum):
    invalid = 1
    empty = 2
    incorrect = 3
    valid=4