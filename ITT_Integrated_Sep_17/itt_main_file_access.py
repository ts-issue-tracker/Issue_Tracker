import xlrd
from itt_resource_names import *
import pandas as pd
import numpy as np
from Itt_fileopen import *
"""
# Reading the csv file
df_new = pd.read_csv('cr_list_entry.csv')

# saving xlsx file
GFG = pd.ExcelWriter('cr_list_entry.xlsx')
df_new.to_excel(GFG, index=False)

GFG.save()
# Give the location of the file
#file_location = "cr_list_entry.xlsx"
file_location="cr_list_entry.xlsx"

wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)
row = 0
col = 0
result_list = []
"""

file ='cr_list.csv'
#sheet = []
#max_col = 0
"""
with open(file) as f:
    global max_col
    reader = csv.reader(f, delimiter=",")
    sheet = list(reader)
    print(len(sheet))
    #data = [row for row in csv.reader(f)]
    if len(sheet) != 0:
        max_col = len(sheet[0])
"""
sheet = []
max_col = 0
def sheet_update():
    global sheet
    global max_col

    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        sheet = list(reader)
        print(len(sheet))
        # data = [row for row in csv.reader(f)]
        if len(sheet) != 0:
            max_col = len(sheet[0])
    f.close()

def return_col_of_specified_col_name(col_name):
    #global max_col
    global sheet
    global max_col

    print(sheet)
    print("max_col",max_col)
    for i in range(len(sheet)):#sheet.nrows):
        for j in range(max_col):#sheet.ncols):
            #if sheet.cell_value(i,j)==col_name:
            print("j",j)
            if col_name == sheet[i][j]:
                print(j)
                return j
    return -1

def return_list(counting_list,label_list,col):
    global sheet
    global max_col

    for i, j in zip(label_list, range(0,len(label_list) )):
        for k in range(len(sheet)):#sheet.nrows):
            print(k,col)
            #if sheet.cell_value(k,col)==i:
            if sheet[k][col] == i:
                counting_list[j]+=1

    return  counting_list

def list_to_display_on_pie(col_name):
    global sheet
    global max_col

    print("colname",col_name)
    col = return_col_of_specified_col_name(col_name)
    print(col)
    label_list = []
    label_list.extend(return_label_list(col_name))
    list2 = []
    for i in range(0, len(label_list)):
        list2.append(0)
    return return_list(list2, label_list, col)

def list_to_display_on_pie_for_assignee(assignee_col,assignee_name,col_name):
    global sheet
    global max_col

    print(assignee_name,assignee_col,col_name)
    assignee_filter_list=[]
    list2 = []
    col = return_col_of_specified_col_name(col_name)
    print(col)
    for k in range(len(sheet)):#sheet.nrows):
        #if sheet.cell_value(k, assignee_col) == assignee_name:
        if sheet[k][assignee_col] == assignee_name:
            assignee_filter_list.append(sheet[k][col])#sheet.cell_value(k, col))
    if len(assignee_filter_list)!=0:
        list=[]
        list.extend(return_label_list(col_name))
        print(list)
        for i in range(0,len(list)):
            list2.append(0)
        for i,k in zip(list,range(0,len(list))):
            for j in assignee_filter_list:
                if i==j:
                    list2[k]+=1
    print(list2)
    return list2

def return_label_list(col_name):
    state_list=[]
    domain_list=[]
    issue_list=[]
    assignee_list=[]
    names=resource_names()
    state_list.extend(names.get_cr_state_names())
    domain_list.extend(names.get_domain_names())
    issue_list.extend(names.get_issue_type_names())
    assignee_list.extend(names.get_assignee_names())
    get_label_list_of_specified_col_name = {
        "State": state_list,
        "Domain": domain_list,
        "Issue Type": issue_list,
        "Assignee": assignee_list
    }
    return get_label_list_of_specified_col_name.get(col_name)