import csv

def writing_username_and_pwd(file,username,password):
    new_User = (username + "," + password + "\n")
    with open(file, 'a') as f:
        f.write(new_User)

def duplicates_checking(file,username):
    with open(file) as g:
        reader1 = csv.reader(g, delimiter=",")
        data_as_a_list_of_rows = list(reader1)
        row_count = len(data_as_a_list_of_rows)
        print(row_count)
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        user_credentials = [row for row in csv.reader(f)]
        for i in range(row_count):
            if username == user_credentials[i][0]:
                return True
        return False
def get_col_of_specified_feild(file,text):
    with open(file) as g:
        reader1 = csv.reader(g, delimiter=",")
        data_as_a_list_of_rows = list(reader1)
        row_count = len(data_as_a_list_of_rows)
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        user_credentials = [row for row in csv.reader(f)]
        if len(user_credentials)!=0:
            max_col=len(user_credentials[0])
        for i in range(row_count):
            for j in range(max_col):
                if text == user_credentials[i][j]:
                    return j
        return -1

def list_of_specified_col(file,col):
    list1=[]
    with open(file) as g:
        reader1 = csv.reader(g, delimiter=",")
        data_as_a_list_of_rows = list(reader1)
        row_count = len(data_as_a_list_of_rows)
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        user_credentials = [row for row in csv.reader(f)]
        for i in range(1,row_count):
            list1.append(user_credentials[i][col])
        return list1

def return_password_for_user(file,username):
    with open(file) as g:
        reader1 = csv.reader(g, delimiter=",")
        data_as_a_list_of_rows = list(reader1)
        row_count = len(data_as_a_list_of_rows)
        print(row_count)
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        user_credentials = [row for row in csv.reader(f)]
        for i in range(row_count):
            if username == user_credentials[i][0]:
                return user_credentials[i][1]
        return ""