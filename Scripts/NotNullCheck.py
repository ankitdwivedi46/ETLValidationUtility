from Connections.DBConnections import DBConnections
from Common.CommonFunctions import CommonFunctions
from termcolor import colored
import  pandas as pd

class NotNullCheck:

    def __init__(self,source_notnull_query,target_notnull_query):
        self.__sourcenotnullquery = source_notnull_query
        self.__targetnotnullquery = target_notnull_query

    def notnull_validation(self):
        dbconn = DBConnections()
        cfunc = CommonFunctions()
        conn = dbconn.connect_to_sql_server()
        s_notnull_data = pd.read_sql_query(self.__sourcenotnullquery,conn)
        t_notnull_data = pd.read_sql_query(self.__targetnotnullquery, conn)
        s_notnull = len(s_notnull_data)
        t_notnull = len(t_notnull_data)
        if(cfunc.validate_source_target_metrics(s_notnull,t_notnull)):
            print(colored("Not Null Validation Passed","green",attrs=['bold']))
        else:
            print(colored("Not Null Validation Failed","red",attrs=['bold']))
            print(colored("Source Not Null Count : "+str(s_notnull),"red",attrs=['bold']))
            print(colored("Source Not Null Data : " + str(s_notnull_data), "red", attrs=['bold']))
            print(colored("Target Not Null Count : "+str(t_notnull),"red",attrs=['bold']))
            print(colored("Target Not Null Data : " + str(t_notnull_data), "red", attrs=['bold']))



