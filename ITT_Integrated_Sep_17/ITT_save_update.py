import csv
from csv import DictWriter
import os

def save_data(combo_dict,index):
    print("in save excel")
    field_names = ['CR', 'Title', 'Description', 'Assignee', 'State', 'Software Image',
                       'Domain', 'Issue Type', 'GIT/Gerrit link',
                       'Build ID', 'Create On', 'Last Modified On', 'History']

    with open("otemp.csv", "w",newline="") as f_out:
        with open('cr_list_entry.csv') as g:
            reader1 = csv.reader(g, delimiter=",")
            data1 = list(reader1)
            row_count1 = len(data1)
        with open('cr_list_entry.csv') as f:
            reader = csv.reader(f, delimiter=",")
            data = [row for row in csv.reader(f)]
            for i in range(row_count1):
                if (i == index):
                    dict_writer = DictWriter(f_out, fieldnames=field_names)
                    dict_writer.writerow(combo_dict)
                    print("myindex")
                else:
                    mydict = dict(zip(field_names, data[i]))
                    dict_writer = DictWriter(f_out, fieldnames=field_names)
                    dict_writer.writerow(mydict)
                    print("other")
    f.close()
    g.close()
    f_out.close()

    print("removing")
    os.remove("cr_list_entry.csv")
    print("renaming")
    os.rename("otemp.csv", "cr_list_entry.csv")
    print("complete")
