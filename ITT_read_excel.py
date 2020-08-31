import csv

def read_new_no():
    print("reading excel")
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as g:
        reader1 = csv.reader(g, delimiter=",")
        data1 = list(reader1)
        row_count1 = len(data1)
        new_cr = int(data1[row_count1-1][0]) + 1
        return str(new_cr)

def read_last_cr():
    print("last cr")
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as f:
        reader2 = csv.reader(f, delimiter=",")
        data2 = list(reader2)
        current_row = len(data2)
        current_cr_num = int(data2[current_row-1][0])
        return str(current_cr_num)

def read_last_title():
    print("last title")
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as h:
        reader3 = csv.reader(h, delimiter=",")
        data3 = list(reader3)
        current_row = len(data3)
        current_title = data3[current_row-1][1]
        print(current_title)
        return str(current_title)

def read_last_assignee():
    print("last title")
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as i:
        reader4 = csv.reader(i, delimiter=",")
        data4 = list(reader4)
        current_row = len(data4)
        current_assignee = data4[current_row-1][3]
        print(current_assignee)
        return str(current_assignee)

def read_last_crstate():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_crstate = data5[current_row - 1][4]
        print(current_crstate)
        return str(current_crstate)

def read_last_des():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_des = data5[current_row - 1][2]
        print(current_des)
        return str(current_des)

def read_last_si():
    with open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_si= data5[current_row - 1][5]
        print(current_si)
        return str(current_si)




