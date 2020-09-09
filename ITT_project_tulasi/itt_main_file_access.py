import xlrd
# Give the location of the file
file_location = "main.xlsx"

wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)
row = 0
col = 0
result_list = []

def return_col_of_specified_col_name(col_name):
    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            if sheet.cell_value(i,j)==col_name:
                return j
    return -1

def return_list(counting_list,label_list,col):
    for i, j in zip(label_list, range(0,len(label_list) )):
        for k in range(sheet.nrows):
            if sheet.cell_value(k,col)==i:
                counting_list[j]+=1
    return  counting_list
def list_to_display_on_pie(col_name):
    col = return_col_of_specified_col_name(col_name)
    print(col)
    label_list = []
    label_list.extend(return_label_list(col_name))
    list2 = []
    for i in range(0, len(label_list)):
        list2.append(0)
    return return_list(list2, label_list, col)
def list_to_display_on_pie_for_assignee(assignee_col,assignee_name,col_name):
    assignee_filter_list=[]
    col = return_col_of_specified_col_name(col_name)
    print(col)
    for k in range(sheet.nrows):
        if sheet.cell_value(k, assignee_col) == assignee_name:
            assignee_filter_list.append(sheet.cell_value(k, col))
    if len(assignee_filter_list)!=0:
        list=[]
        list.extend(return_label_list(col_name))
        print(list)
        list2=[]
        for i in range(0,len(list)):
            list2.append(0)
        for i,k in zip(list,range(0,len(list))):
            for j in assignee_filter_list:
                if i==j:
                    list2[k]+=1
    print(list2)
    return list2

def return_label_list(col_name):
    state_list = ["Open", "Analysis", "In Progress", "Reopen", "Closed"]
    domain_list = ["Audio", "Video", "Camera"]
    issue_list = ["Bug", "Internal", "Blacklisting"]
    assignee_list = ["Tulasi", "Santhoshi", "Pavani", "Suma", "Suresh"]

    get_label_list_of_specified_col_name = {
        "State": state_list,
        "Domain": domain_list,
        "IssueType": issue_list,
        "Assignee": assignee_list
    }
    return get_label_list_of_specified_col_name.get(col_name)