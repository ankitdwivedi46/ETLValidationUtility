from Connections.DBConnections import DBConnections
from Common.CommonFunctions import CommonFunctions
from termcolor import colored
import  pandas as pd

class UniqueCheck:

    def __init__(self,source_uniq_query,target_uniq_query):
        self.__sourceuniqquery = source_uniq_query
        self.__targetuniqquery = target_uniq_query

    def unique_validation(self):
        dbconn = DBConnections()
        cfunc = CommonFunctions()
        conn = dbconn.connect_to_sql_server()
        s_uniq_data = pd.read_sql_query(self.__sourceuniqquery,conn)
        t_uniq_data = pd.read_sql_query(self.__targetuniqquery, conn)
        s_uniq = len(s_uniq_data)
        t_uniq = len(t_uniq_data)
        if(cfunc.validate_source_target_metrics(s_uniq,t_uniq)):
            print(colored("Unique Validation Passed","green",attrs=['bold']))
        else:
            print(colored("Unique Validation Failed","red",attrs=['bold']))
            print(colored("Source Unique Count : "+str(s_uniq),"red",attrs=['bold']))
            print(colored("Source Unique Data : " + str(s_uniq_data), "red", attrs=['bold']))
            print(colored("Target Unique Count : "+str(t_uniq),"red",attrs=['bold']))
            print(colored("Target Unique Data : " + str(t_uniq_data), "red", attrs=['bold']))



