from csv import DictWriter
import csv
from ITT_read_excel import *


def append_dict_as_row(file,combo_dict,names):
    print(combo_dict)
    with open(file, 'a+', newline='') as write_obj:
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

def save_update_info(combo_dict,index):
    pass