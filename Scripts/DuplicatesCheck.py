from Connections.DBConnections import DBConnections
from Common.CommonFunctions import CommonFunctions
from termcolor import colored
import  pandas as pd

class DuplicatesCheck:

    def __init__(self,source_dup_query,target_dup_query):
        self.__sourcedupquery = source_dup_query
        self.__targetdupquery = target_dup_query

    def duplicate_validation(self):
        dbconn = DBConnections()
        cfunc = CommonFunctions()
        conn = dbconn.connect_to_sql_server()
        s_dup_data = pd.read_sql_query(self.__sourcedupquery,conn)
        t_dup_data = pd.read_sql_query(self.__targetdupquery, conn)
        s_dup = len(s_dup_data)
        t_dup = len(t_dup_data)
        if(cfunc.validate_source_target_metrics(s_dup,t_dup)):
            print(colored("Duplicates Validation Passed","green",attrs=['bold']))
        else:
            print(colored("Duplicates Validation Failed","red",attrs=['bold']))
            print(colored("Source Dup Count : "+str(s_dup),"red",attrs=['bold']))
            print(colored("Source Dup Data : " + str(s_dup_data), "red", attrs=['bold']))
            print(colored("Target Dup Count : "+str(t_dup),"red",attrs=['bold']))
            print(colored("Target Dup Data : " + str(t_dup_data), "red", attrs=['bold']))



