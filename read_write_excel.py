import csv

combo_List=[1,2,3,4,5]
def save_in_excel(combo_List):
    print("in write excel file")
    size = len(combo_List)
    file = open('C:\\Users\\DELL\\Downloads\\file.csv','a+',newline='')
    with file:
        print("writing")
        write = csv.writer(file)
        write.writerow(combo_List)
        print("complete")


print("reading excel")
def reading():
 with open('C:\\Users\\DELL\\Downloads\\file.csv') as g:
        reader1 = csv.reader(g, delimiter=",")
        data1 = list(reader1)
        row_count1 = len(data1)
        new_cr = int(data1[row_count1-1][0]) + 1
        print(str(new_cr))
save_in_excel(combo_List)
reading()