import csv
"""
def read_index_cr():
    with open('cr_list_entry.csv') as f:
        reader1 = csv.reader(f, delimiter=',')
        data1 = list(reader1)
        current_row = len(data1)
        print(current_row)
        return current_row
"""

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
        max_col = len(data3[0])
        for i in range(max_col):
            if("Title" == data3[0][i]):
                print("read",i)
                index = i
                break
        print("read",index,data3[current_row-1][index])
        current_title = data3[current_row-1][index]
        print(current_title)
        j.close()
        return str(current_title)

def read_last_assignee():
    print("last assignee")
    with open('cr_list_entry.csv') as j:
        reader4 = csv.reader(j, delimiter=",")
        data4 = list(reader4)
        current_row = len(data4)
        print(data4[0])
        max_col = len(data4[0])
        for i in range(max_col):
            if ("Assignee" == data4[0][i]):
                print("read", i)
                index = i
                break
        print("read assignee", index, data4[current_row - 1][index])
        current_assignee = data4[current_row-1][index]
        j.close()
        return str(current_assignee)

def read_last_crstate():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("State" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read state", index, data5[current_row - 1][index])
        current_crstate = data5[current_row - 1][index]
        j.close()
        return str(current_crstate)

def read_last_des():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Description" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read des", index, data5[current_row - 1][index])
        current_des = data5[current_row - 1][index]
        j.close()
        return str(current_des)

def read_last_si_state():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Software Image" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read si state", index, data5[current_row - 1][index])
        current_si = data5[current_row - 1][index]
        j.close()
        return str(current_si)

def read_last_issuetype():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Issue Type" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read last modified", index, data5[current_row - 1][index])
        current_issue = data5[current_row - 1][index]
        j.close()
        return str(current_issue)

def read_last_domain():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Domain" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read Domain", index, data5[current_row - 1][index])
        current_domain = data5[current_row - 1][index]
        j.close()
        return str(current_domain)

def read_git_id():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("GIT commit id/Gerrit link" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read Domain", index, data5[current_row - 1][index])
        current_git= data5[current_row - 1][index]
        j.close()
        return str(current_git)

def read_build():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Build ID" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read Domain", index, data5[current_row - 1][index])
        current_build= data5[current_row - 1][index]
        j.close()
        return str(current_build)

def read_create_time():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("   Created    on" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read Domain", index, data5[current_row - 1][index])
        current_createon= data5[current_row - 1][index]
        j.close()
        return str(current_createon)

def read_lastmodi_time():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Last Modified" == data5[0][i]):
                print("read", i)
                index = i
                break
        print("read Domain", index, data5[current_row - 1][index])
        current_laston= data5[current_row - 1][index]
        j.close()
        return str(current_laston)
"""
def read_create_date():
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        current_row = len(data5)
        current_createdate= data5[current_row - 1][10]
        j.close()
        return str(current_createdate)
"""

def read_cr_by_index(index):
        with open('cr_list_entry.csv') as j:
            reader5 = csv.reader(j, delimiter=",")
            data5 = list(reader5)
            max_col = len(data5[0])
            for i in range(max_col):
                if ("CR" == data5[0][i]):
                    print("read CR", i)
                    col = i
                    break
            print("read CR", index, data5[index][col])
            j.close()
            return data5[index][col]

def read_create_date_index(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        max_col = len(data5[0])
        for i in range(max_col):
            if ("   Created    on" == data5[0][i]):
                print("read Created on", i)
                col = i
                break
        print("read CR", index, data5[index][i])
        j.close()
        return data5[index][col]

def read_asignee_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Assignee" == data5[0][i]):
                print("read Assignee", i)
                col = i
                break
        print("read assignee", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_domain_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Domain" == data5[0][i]):
                print("read domain", i)
                col = i
                break
        print("read domain", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_git_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("GIT commit id/Gerrit link" == data5[0][i]):
                print("read git", i)
                col = i
                break
        print("read assignee", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_build_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Build ID" == data5[0][i]):
                print("read git", i)
                col = i
                break
        print("read build", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_title_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Title" == data5[0][i]):
                print("read git", i)
                col = i
                break
        print("read build", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_des_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Description" == data5[0][i]):
                print("read git", i)
                col = i
                break
        print("read build", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_si_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Software Image" == data5[0][i]):
                print("read git", i)
                col = i
                break
        print("read build", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_cr_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("State" == data5[0][i]):
                print("read git", i)
                col = i
                break
        print("read build", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_issuetype_with_cr(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Issue Type" == data5[0][i]):
                print("read git", i)
                col = i
                break
        print("read build", index, data5[index][col])
        j.close()
        return str(data5[index][col])

def read_late_date_index(index):
    with open('cr_list_entry.csv') as j:
        reader5 = csv.reader(j, delimiter=",")
        data5 = list(reader5)
        print(data5[0])
        max_col = len(data5[0])
        for i in range(max_col):
            if ("Last Modified" == data5[0][i]):
                print("read git", i)
                col = i
                break
        print("read build", index, data5[index][col])
        j.close()
        return str(data5[index][col])