import numpy as np
from Connections.DBConnections import DBConnections
from Common.CommonFunctions import CommonFunctions
from termcolor import colored
import  pandas as pd

class DataCheck:

    def __init__(self,source_data_query,target_data_query):
        self.__sourcedataquery = source_data_query
        self.__targetdataquery = target_data_query

    def data_validation(self):
        dbconn = DBConnections()
        cfunc = CommonFunctions()
        conn = dbconn.connect_to_sql_server()
        s_data = pd.read_sql_query(self.__sourcedataquery,conn)
        t_data = pd.read_sql_query(self.__targetdataquery, conn)
        data = pd.concat([s_data,t_data],sort=True)
        data = data.replace(np.nan,'',regex=True)
        data = data.reset_index(drop=True)
        data_gpby = data.groupby(list(data.columns))
        match = [x[0] for x in data_gpby.groups.values() if len(x)>1]
        mismatch = [x[0] for x in data_gpby.groups.values() if len(x)==1]
        matched_data = data.reindex(match)
        mismatched_data = data.reindex(mismatch)
        if (cfunc.validate_source_target_metrics(len(mismatched_data),0)):
            print(colored("Data Validation Passed", "green", attrs=['bold']))
        else:
            print(colored("Data Validation Failed", "red", attrs=['bold']))
            print(colored("Mismatch Data : ", "red", attrs=['bold']))
            print(mismatched_data)







