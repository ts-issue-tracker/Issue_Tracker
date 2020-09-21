import pandas as pd
import xlrd
INVALID_TYPE_GIVEN = -1

def openfile(filetype):
    global wb
    global wb1
    if filetype == 1:
        df_new = pd.read_csv('cr_list_entry.csv')

        # saving xlsx file
        GFG = pd.ExcelWriter('cr_list_entry.xlsx')
        df_new.to_excel(GFG, index=False)

        datafilename = 'cr_list_entry.xlsx'
        GFG.save()
        file_location = datafilename
        wb = xlrd.open_workbook(file_location)
        sheet = wb.sheet_by_index(0)
        return sheet

    elif filetype == 2:
        print("in credentials")
        df_new1 = pd.read_csv('Credentials.csv')

        # saving xlsx file
        GFG1 = pd.ExcelWriter('Credentials.xlsx')
        df_new1.to_excel(GFG1, index=False)

        namesfilename = 'Credentials.xlsx'
        GFG1.save()
        file_location = (namesfilename)
        wb1 = xlrd.open_workbook(file_location)
        namesheet = wb1.sheet_by_index(0)
        return namesheet

    if filetype == 3:
        del wb

    #    wb.Close(True)
    #    wb1.Close(True)
    #    wb.__exit__()

    return INVALID_TYPE_GIVEN

# Give the location of the file
#file_location = "cr_list_entry.xlsx"