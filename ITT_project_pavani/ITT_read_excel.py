import csv

def read_new_no():
    print("reading excel")
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader1 = csv.reader(j, delimiter=",")
        data1 = list(reader1)
        row_count1 = len(data1)
        new_cr = int(data1[row_count1-1][0]) + 1
        return str(new_cr)

def read_last_cr():
    print("last cr")
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader2 = csv.reader(j, delimiter=",")
        data2 = list(reader2)
        current_row = len(data2)
        current_cr_num = int(data2[current_row-1][0])
        return str(current_cr_num)

def read_last_title():
    print("last title")
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader3 = csv.reader(j, delimiter=",")
        data3 = list(reader3)
        current_row = len(data3)
        current_title = data3[current_row-1][1]
        print(current_title)
        return str(current_title)

def read_last_assignee():
    print("last title")
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader4 = csv.reader(j, delimiter=",")
        data4 = list(reader4)
        current_row = len(data4)
        current_assignee = data4[current_row-1][3]
        return str(current_assignee)

def read_last_crstate():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_crstate = data5[current_row - 1][4]
        return str(current_crstate)

def read_last_des():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_des = data5[current_row - 1][2]
        return str(current_des)

def read_last_issuetype():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_issue = data5[current_row - 1][7]
        return str(current_issue)

def read_last_si_label():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_si_label = data5[current_row - 1][5]
        return str(current_si_label)

def read_last_domain():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_domain = data5[current_row - 1][6]
        return str(current_domain)

def read_git_id():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_git= data5[current_row - 1][8]
        return str(current_git)

def read_build():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_build= data5[current_row - 1][9]
        return str(current_build)

def read_create_time():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_createon= data5[current_row - 1][10]
        return str(current_createon)

def read_lastmodi_time():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_laston= data5[current_row - 1][11]
        return str(current_laston)








