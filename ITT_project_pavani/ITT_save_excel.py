from csv import DictWriter
import csv
from ITT_read_excel import *
import os
from ITT_save_update import *

def append_dict_as_row(file_name, dict_of_elem, field_names):
    with open(file_name, 'a+', newline='') as write_obj:
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        dict_writer.writerow(dict_of_elem)
        write_obj.close()

def save_in_excel(combo_dict):
        print("in write excel file")
        mylist = [ ]
        global field_names
        field_names =['CR', 'Title', 'Description','Assignee','State','Software Image',
                         'Domain','Issue Type','GIT/Gerrit link',
                       'Build ID','Create On','Last Modified On','History']

        file = 'cr_list_entry.csv'
        combo_dict = dict(combo_dict)
        #mylist = list(combo_dict.values())
        mylist = ["Created by " + combo_dict['Assignee']]
        combo_dict.update({'History':mylist})
        print(combo_dict)
        append_dict_as_row(file, combo_dict, field_names)

def save_update_info(combo_dict1,cr,index,history_dict):
    print("update file")
    print(history_dict)
    field_names = ['CR', 'Title', 'Description', 'Assignee', 'State', 'Software Image',
                   'Domain', 'Issue Type', 'GIT/Gerrit link',
                   'Build ID', 'Create On', 'Last Modified On', 'History']
    #coll_data = []
    combo_dict1 = dict(combo_dict1)
    print("old")
    olddata = collect_olddata(cr,index)
    print("old",olddata)
    #newdata = list(combo_dict1.values())
    newdata = collect_newdata(history_dict)
    olddata.extend(newdata)
    combo_dict1.update({'History': olddata})
    print(combo_dict1)
    print("saving")
    save_data(combo_dict1,index)
    print("complete")

def collect_newdata(history_dict):
    history_dict = dict(history_dict)
    if 'assignee' in history_dict.keys():
        print("assignee")

def collect_olddata(crnum,index):
    olddata = [ ]
    with open('cr_list_entry.csv') as g:
        reader1 = csv.reader(g, delimiter=",")
        data1 = list(reader1)
        row_count1 = len(data1)
    with open('cr_list_entry.csv') as f:
        reader = csv.reader(f, delimiter=",")
        data = [row for row in csv.reader(f)]
        for i in range(row_count1):
            if i == index and data[i][0] == crnum:
                #cr = data[i][0]
                #title = data[i][1]
                #des = data[i][2]
                #assignee = data[i][3]
                #state = data[i][4]
                #si = data[i][5]
                #domain = data[i][6]
                #issue_type = data[i][7]
                #git = data[i][8]
                #bid = data[i][9]
                #con = data[i][10]
                #lon = data[i][11]
                history = data[i][12]
                print(type(history))

                olddata = [history]
                print(type(olddata))
                f.close()
                print("closed")
                return olddata