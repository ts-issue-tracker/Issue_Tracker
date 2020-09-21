import csv

def read_index_cr():
    with open('cr_list_entry.csv') as f:
        reader1 = csv.reader(f, delimiter=',')
        data1 = list(reader1)
        current_row = len(data1)
        print(current_row)
        return current_row

def read_new_no():
    print("reading excel")
    with open('cr_list_entry.csv') as f:
        reader1 = csv.reader(f, delimiter=',')
        data1 = list(reader1)
        current_row = len(data1)
        print(current_row)
        current_cr_num = int(data1[current_row - 1][0]) + 1
        print(current_cr_num)
        f.close()
        return str(current_cr_num)

def read_last_cr():
    print("last cr")
    with open('cr_list_entry.csv') as j:
        reader2 = csv.reader(j, delimiter=",")
        data2 = list(reader2)
        current_row = len(data2)
        current_cr_num = int(data2[current_row-1][0])
        j.close()
        return str(current_cr_num)

def read_last_title():
    print("last title")
    with open('cr_list_entry.csv') as j:
        reader3 = csv.reader(j, delimiter=",")
        data3 = list(reader3)
        current_row = len(data3)
        current_title = data3[current_row-1][1]
        print(current_title)
        j.close()
        return str(current_title)

def read_last_assignee():
    print("last title")
    with open('cr_list_entry.csv') as j:
        reader4 = csv.reader(j, delimiter=",")
        data4 = list(reader4)
        current_row = len(data4)
        current_assignee = data4[current_row-1][3]
        j.close()
        return str(current_assignee)

def read_last_crstate():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_crstate = data5[current_row - 1][4]
        j.close()
        return str(current_crstate)

def read_last_des():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_des = data5[current_row - 1][2]
        j.close()
        return str(current_des)

def read_last_si_state():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_des = data5[current_row - 1][5]
        j.close()
        return str(current_des)

def read_last_issuetype():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_issue = data5[current_row - 1][7]
        j.close()
        return str(current_issue)

def read_last_domain():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_domain = data5[current_row - 1][6]
        j.close()
        return str(current_domain)

def read_git_id():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_git= data5[current_row - 1][8]
        j.close()
        return str(current_git)

def read_build():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_build= data5[current_row - 1][9]
        j.close()
        return str(current_build)

def read_create_time():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_createon= data5[current_row - 1][10]
        j.close()
        return str(current_createon)

def read_lastmodi_time():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_laston= data5[current_row - 1][11]
        j.close()
        return str(current_laston)

def read_create_date():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_createdate= data5[current_row - 1][10]
        j.close()
        return str(current_createdate)

def read_cr_by_index(index):
            with open('cr_list_entry.csv') as f:
                csv.reader(f, delimiter=",")
                data = [row for row in csv.reader(f)]
                f.close()
                return data[index][0]

def read_create_date_index(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return data[index][10]

def read_asignee_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][3])

def read_domain_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][6])

def read_git_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][8])

def read_build_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][9])

def read_title_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][1])

def read_des_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][2])

def read_si_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][5])

def read_cr_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][4])

def read_issuetype_with_cr(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][7])

def read_late_date_index(index):
    with open('cr_list_entry.csv') as f:
        csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        f.close()
        return str(data[index][11])