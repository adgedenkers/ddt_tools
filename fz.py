'''
File: fz.py
Version: 1.0
Project: ddt_tools
Created Date: 2023-10-26
Author: Adge Denkers
Email: adriaan.denkers@va.gov1
-----
Last Modified: 2023-10-27
Modified By: Adge Denkers
Email: adriaan.denkers@va.gov
-----
Copyright (c) 2023 U.S. Department of Veterans Affairs
-----
NOTICE:
This code/script is the explicit property of the United States Government
which may be used only for official Governemnt business by authorized
personnel. Unauthorized access or use of this code/script may subject 
violators to criminal, civil, and/or administrative action.
'''

# import libraries
import datetime
import keyring
import pandas as pd
import pyodbc

# import individual modules
from datetime import datetime, date, time, timedelta
from sqlalchemy import text

class tools:

    # initialize the tools object
    def __init__(self):
        self.namespace = 'DDT-AUTO'
        #self.my_username = 
        self.today = date.today()
        self.odbc_pwras = keyring.get_password(self.namespace, 'SQL_ODBC_PWRAS')
        self.odbc_pwrbs = keyring.get_password(self.namespace, 'SQL_ODBC_PWRBS')
        self.odbc_pmdbs = keyring.get_password(self.namespace, 'SQL_ODBC_PMDBS')
        self.pwras = keyring.get_password(self.namespace, 'SQL_PWRAS')
        self.pwrbs = keyring.get_password(self.namespace, 'SQL_PWRBS')
        self.pmdbs = keyring.get_password(self.namespace, 'SQL_PMDBS')

        pass
    # -------------------------------------------------------
    # the fz functions and classes
    # -------------------------------------------------------
    def clean_dataframe(self, df):
        # create a new dataframe to store the cleaned data
        cleaned_df = pd.DataFrame()

        # # loop through each row and column
        # for col in df.columns:
        #     # cleaned df column = (if float, convert to int, then convert everything to string except nulls)
        #     cleaned_df[col] = df[col].apply(lambda x: str(int(x)) if isinstance(x, float) and x.is_integer() else (str(x)).strip() if pd.notnull(x) else x)

        # return cleaned_df

    def exec_sql(connection_string, sql_statement, **params):
        """
        Execute a SQL Statement on a SQLAlchemy database connection engine
        
        Parameters:
        engine (sqlalchemy.engine.base.Engine): the database connection engine
        sql_statement (str): The SQL statement/command to execute
        **params: Parameters to pass to the SQL Statement

        Returns:
        sqlalchemy.engine.result.ResultProxy: The result of the SQL execution
        """
        # prep the sql statement
        sql = text(sql_statement)

        conn = pyodbc.connect(connection_string)
        
        cursor = conn.cursor()
        try:
            result = cursor.execute(sql)
        except:
            result = -1

        return result