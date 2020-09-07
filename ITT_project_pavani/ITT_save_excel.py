from csv import DictWriter
import csv

def append_dict_as_row(file,combo_dict,names):
    print(combo_dict)
    with open(file, 'a+', newline='') as write_obj:
            dict_writer = DictWriter(write_obj, fieldnames=names)
            dict_writer.writerow(combo_dict)

def save_in_excel(combo_dict):
        print("in write excel file")
        size = len(combo_dict)
        field_names =['CR', 'Title', 'Description','Asignee','State','Software Image',
                         'Domain','Issue Type','GIT/Gerrit link',
                       'Build ID','Create On','Last Modified On','History']
        #file = open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv','a+',newline='')
        file = 'cr_list_entry.csv'
        append_dict_as_row(file, combo_dict, field_names)