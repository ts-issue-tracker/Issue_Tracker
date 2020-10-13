import pandas as pd
import csv
INVALID_TYPE_GIVEN = -1
OPEN_DATA_FILE = 1
OPEN_CREDENTIAL_FILE = 2
CLOSE_DATA_FILE = 3
CLOSE_CREDENTIAL_FILE = 4

def openfile(filetype):
    global wb
    global wb1
    global f1
    global f2
    if filetype == OPEN_DATA_FILE:

        with open('cr_list_entry.csv') as f1:#cr_list.csv') as f1:
            reader1 = csv.reader(f1, delimiter=',')
            if not f1.closed:
                print("cr_list file is open")
            sheet = list(reader1)

        return sheet

    elif filetype == OPEN_CREDENTIAL_FILE:

        with open('Credentials.csv') as f2:
            reader2 = csv.reader(f2, delimiter=',')
            namesheet = list(reader2)
        return namesheet

    if filetype == CLOSE_DATA_FILE:
        if not f1.closed:
            print("cr_list is open so closing it")
            f1.close()

    if filetype == CLOSE_CREDENTIAL_FILE:
        if not f2.closed:
            print("usercredential is open so closing it")
            f2.close()


    return INVALID_TYPE_GIVEN

