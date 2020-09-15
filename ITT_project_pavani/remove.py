import os
def delete_file():
    os.remove("cr_list_entry.csv.csv")
    os.rename("otemp.csv","cr_list_entry.csv")
    print("renamed")