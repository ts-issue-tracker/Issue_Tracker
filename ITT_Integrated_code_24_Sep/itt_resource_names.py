from itt_credentials_file_access import *
class resource_names:
    def __init__(self):
        pass
    def get_domain_names(self):
        domain_list=["Audio","Camera","Video"]
        return domain_list
    def get_cr_state_names(self):
        cr_states=["Open","Analysis","Closed","In-progress","Reopen"]
        return cr_states
    def get_issue_type_names(self):
        issue_types=["Bug","Internal","Blacklisting"]
        return issue_types
    def get_assignee_names(self):
        col=get_col_of_specified_feild("Credentials.csv","Username")
        assginee_list=[]
        assginee_list.extend(list_of_specified_col("Credentials.csv",col))
        return assginee_list