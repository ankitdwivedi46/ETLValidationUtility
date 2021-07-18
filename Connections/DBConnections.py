import pyodbc
import pandas as pd

'''
Creator : Ankit Dwivedi
Date : 18-07-2021
Use : Class which defines Connections to different DataBases
'''

class DBConnections:

    '''
    Creator : Ankit Dwivedi
    Date : 18-07-2021
    Use : Constructor which initializes Username, Password, Server, Driver, DB
    '''

    def __init__(self):
        self.__driver = "ODBC Driver 17 for SQL Server"
        self.__server = "localhost"
        self.__username = ""
        self.__password = ""
        self.__database = "Demo"

    '''
    Creator : Ankit Dwivedi
    Date : 18-07-2021
    Use : Function which connects to SQL Server and returns Connection Object
    '''

    def connect_to_sql_server(self):
        conn = pyodbc.connect('DRIVER={' + self.__driver + '};'
                              'Server=' + self.__server + ';'
                              'Database=' + self.__database + ';'
                              'Username=' + self.__username + ';'
                              'Password=' + self.__password + ';'
                              'Trusted_Connection=yes')
        return conn




