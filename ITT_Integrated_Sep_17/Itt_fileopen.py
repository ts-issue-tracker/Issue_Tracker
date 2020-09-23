import pandas as pd
import xlrd
import csv
INVALID_TYPE_GIVEN = -1

def openfile(filetype):
    global wb
    global wb1
    global f1
    global f2
    if filetype == 1:

        with open('cr_list_entry.csv') as f1:#cr_list.csv') as f1:
            reader1 = csv.reader(f1, delimiter=',')
            if not f1.closed:
                print("cr_list file is open")
            sheet = list(reader1)
        """
        df_new = pd.read_csv('cr_list_entry.csv')

        # saving xlsx file
        GFG = pd.ExcelWriter('cr_list_entry1.xlsx')
        df_new.to_excel(GFG, index=False)

        datafilename = 'cr_list_entry1.xlsx'
        GFG.save()
        file_location = datafilename
        wb = xlrd.open_workbook(file_location)
        sheet = wb.sheet_by_index(0)
        return sheet
        """

        return sheet

    elif filetype == 2:

        with open('Credentials.csv') as f2:
            reader2 = csv.reader(f2, delimiter=',')
            namesheet = list(reader2)
        return namesheet
        """
        print("in credentials")
        df_new1 = pd.read_csv('Credentials.csv')

        # saving xlsx file
        GFG1 = pd.ExcelWriter('Credentials1.xlsx')
        df_new1.to_excel(GFG1, index=False)

        namesfilename = 'Credentials1.xlsx'
        GFG1.save()
        file_location = (namesfilename)
        wb1 = xlrd.open_workbook(file_location)
        namesheet = wb1.sheet_by_index(0)
        return namesheet
        """

    if filetype == 3:
        if not f1.closed:
            print("cr_list is open so closing it")
            f1.close()

    if filetype == 4:
        if not f2.closed:
            print("usercredential is open so closing it")
            f2.close()
        """
        fileobj = open('cr_list.csv',"r")#'cr_list_entry1.xlsx', "wb+")
        if not fileobj.closed:
            print("data file is already opened")
            fileobj.close()
            #del wb
    #if filetype == 4:
        fileobj1 = open('userCredentials.csv', "r")
        if not fileobj1.closed:
            print("Credentials file is already opened")
            #del wb1
            fileobj1.close()
        """

    #    wb.Close(True)
    #    wb1.Close(True)
    #    wb.__exit__()

    return INVALID_TYPE_GIVEN

# Give the location of the file
#file_location = "cr_list_entry.xlsx"