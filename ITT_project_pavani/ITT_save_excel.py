from csv import DictWriter
import csv
from ITT_read_excel import *

def append_dict_as_row(file,combo_dict,names):
    with open(file, 'a+', newline='') as write_obj:
            print("with")
            dict_writer = DictWriter(write_obj, fieldnames=names)
            dict_writer.writerow(combo_dict)

def save_in_excel(combo_dict):
        print("in write excel file")

        field_names =['CR', 'Title', 'Description','Asignee','State','Software Image',
                         'Domain','Issue Type','GIT/Gerrit link',
                       'Build ID','Create On','Last Modified On','History']

        file = 'cr_list_entry.csv'
        combo_dict = dict(combo_dict)
        mylist = list(combo_dict.values())
        combo_dict.update({'History':mylist})
        append_dict_as_row(file, combo_dict, field_names)

def save_update_info(combo_dict1,cr,index):
    print("update file")
    file = 'cr_list_entry.csv'
    combo_dict1 = dict(combo_dict1)
    print(combo_dict1,index)
    print("with1")
    with open('cr_list_entry.csv') as g:
            reader1 = csv.reader(g, delimiter=",")
            data1 = list(reader1)
            row_count1 = len(data1)
    print("with2")
    with open(file, 'a+', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            data = [row for row in csv.reader(f)]
            data[2][2] = "Hello"
            for i in range(row_count1):
                if cr == data[i][0]:
                    data[index][0] = combo_dict1['CR']
                    data[index][1] = combo_dict1['Title']
                    data[index][2] = combo_dict1['Description']
                    data[index][3] = combo_dict1['Asignee']
                    data[index][4] = combo_dict1['State']
                    data[index][5] = combo_dict1['Software Image']
                    data[index][6] = combo_dict1['Domain']
                    data[index][7] = combo_dict1['Issue Type']
                    data[index][8] = combo_dict1['GIT/Gerrit link']
                    data[index][9] = combo_dict1['Build ID']
                    data[index][10] = combo_dict1['Create On']
                    data[index][11] = combo_dict1['Last Modified On']
                    data[index][12] = combo_dict1['History']