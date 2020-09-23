from csv import DictWriter
import csv
from ITT_read_excel import *
import os
from ITT_save_update import *
import shutil

def append_dict_as_row(file_name, dict_of_elem, field_names):
    with open(file_name, 'a+', newline='') as write_obj:
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        dict_writer.writerow(dict_of_elem)
        write_obj.close()
    shutil.copyfile(file_name,'cr_list.csv')

def save_in_excel(combo_dict,path):
        print("in write excel file")
        mylist = [ ]
        global field_names

        field_names =['CR', 'Title', 'Description','Assignee','State','Software Image',
                         'Domain','Issue Type','GIT commit id/Gerrit link',
                       'Build ID','Create On','Last Modified On','History']

        file = 'cr_list_entry.csv'
        combo_dict = dict(combo_dict)
        #mylist = list(combo_dict.values())
        if(len(path) > 0):
         mylist = ["Created by " + combo_dict['Assignee'] + " and log file location is " + path + " on " + combo_dict['Create On']]
        else:
            mylist = [
                "Created by " + combo_dict['Assignee'] + " on " + combo_dict['Create On']]
        combo_dict.update({'History':mylist})
        print(combo_dict)
        append_dict_as_row(file, combo_dict, field_names)

def save_update_info(combo_dict1,cr,index,history_dict,path):
    print("update file")
    print(history_dict)
    field_names = ['CR', 'Title', 'Description', 'Assignee', 'State', 'Software Image',
                   'Domain', 'Issue Type', 'GIT commit id/Gerrit link',
                   'Build ID', 'Create On', 'Last Modified On', 'History']
    #coll_data = []
    combo_dict1 = dict(combo_dict1)
    olddata = collect_olddata(cr,index)
    print("old",history_dict)
    print("old",olddata)
    #newdata = list(combo_dict1.values())
    newdata = collect_newdata(history_dict,combo_dict1,path)
    print("newdata",newdata)
    olddata.extend(newdata)
    combo_dict1.update({'History': olddata})
    print("new",combo_dict1)
    print("saving")
    save_data(combo_dict1,index)
    print("complete")

def collect_newdata(history_dict,combo_dict,path):
    main_list = [ ]
    last_date = ["on",history_dict['last date']]
    history_dict = dict(history_dict)
    if 'assignee' in history_dict.keys():
        assignee = history_dict['assignee']
        assignee_list = ["Changed assignee to " + history_dict['assignee']]
        main_list.extend(assignee_list)
        print(assignee,main_list)
    else:
        assignee = combo_dict['Assignee']
    name = [assignee]
    print(name,type(name))
    if(len(path) > 0):
        path_add = ["Attached log file " + path]
        main_list.extend(path_add)
        print("path",main_list)

    if 'title' in history_dict.keys():
        title_list = [" modified title to"+history_dict['title']]
        main_list.extend(title_list)
        print("title", main_list)

    if 'git/gerrit' in history_dict.keys():
        git_list = [" added git/gerrit id: "+history_dict['git/gerrit']]
        main_list.extend(git_list)
        print("git/gerrit", main_list)

    if 'cr state' in history_dict.keys():
        cr_list = [" changed CR state to " + history_dict['cr state'] + " and SI state is changed to " + combo_dict['Software Image']]
        main_list.extend(cr_list)
        print("cr state", main_list)

    if 'domain' in history_dict.keys():
        domain_list = ["changed domain to " + history_dict['domain']]
        main_list.extend(domain_list)
        print("domain", main_list)

    if 'buildid' in history_dict.keys():
        build_list = [" changed build id to" + history_dict['buildid'] ]
        main_list.extend(build_list)
        print("buildid", main_list)

    if 'description' in history_dict.keys():
        des_list = [" changed description to "+ history_dict['description']]
        main_list.extend(des_list)
        print("description", main_list)

    if 'issue type' in history_dict.keys():
        print("issue")
        print(history_dict['issue type'])
        issue_list = [" changed issue type to " + history_dict['issue type'] + " because "+ history_dict['issue Reason']]
        main_list.extend(issue_list)
        print("issue type", main_list)

    if 'si state' in history_dict.keys():
        si_list = [" changed si state to " + history_dict['si state'] + " and CR state is changed to " + combo_dict['State']]
        main_list.extend(si_list)
        print("si state", main_list)

    name.extend(main_list)
    name.extend(last_date)
    print(name)
    return name

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
