from Connections.DBConnections import DBConnections
from Common.CommonFunctions import CommonFunctions
from termcolor import colored
import  pandas as pd

class CountsCheck:

    def __init__(self,source_count_query,target_count_query):
        self.__sourcecountquery = source_count_query
        self.__targetcountquery = target_count_query

    def count_validation(self):
        dbconn = DBConnections()
        cfunc = CommonFunctions()
        conn = dbconn.connect_to_sql_server()
        s_count = pd.read_sql_query(self.__sourcecountquery,conn)[''][0]
        t_count = pd.read_sql_query(self.__targetcountquery, conn)[''][0]
        if(cfunc.validate_source_target_metrics(s_count,t_count)):
            print(colored("Count Validation Passed","green",attrs=['bold']))
        else:
            print(colored("Count Validation Failed","red",attrs=['bold']))
            print(colored("Source Count : "+str(s_count),"red",attrs=['bold']))
            print(colored("Target Count : "+str(t_count),"red",attrs=['bold']))



