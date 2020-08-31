import csv

def writing_username_and_pwd(file,username,password):
    new_User = (username + "," + password + "\n")
    with open(file, 'a') as f:
        f.write(new_User)

def reading_and_checking_credentials(file,username,password):
    with open(file) as g:
        reader1 = csv.reader(g, delimiter=",")
        data_as_a_list_of_rows = list(reader1)
        row_count = len(data_as_a_list_of_rows)
        print(row_count)
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        for i in range(row_count):
            if username == data[i][0] and password == data[i][1]:
                login = True
                print("success")
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