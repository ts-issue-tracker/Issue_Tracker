import csv

def save_in_excel(combo_List):
        print("in write excel file")
        size = len(combo_List)
        file = open('C:\\Users\\lenovo\\PycharmProjects\\pythonProject3\\cr_list_entry.csv','a+',newline='')
        with file:
            print("writing")
            write = csv.writer(file)
            write.writerow(combo_List)
            print("complete")




