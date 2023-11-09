'''
File: setup/setup_keyring.py
Version: 1.0
Project: ddt_tools
Created Date: 2023-08-01
Author: Adge Denkers
Email: adriaan.denkers@va.gov
-----
Last Modified: 2023-08-01
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
import argparse
import hashlib
import keyring

class setup():

    def __init__(self, NAMESPACE) -> None:
        self.namespace = NAMESPACE

        keyring.set_password(self.namespace, "SQL_USER", 'SQLUsername')
        keyring.set_password(self.namespace, "SQL_PASS", 'SQLPassword')
        keyring.set_password(self.namespace, "SQL_DRIVER", 'SQL Server Native Client 11.0')
        keyring.set_password(self.namespace, "SERVER_A", 'server_a.example.com')
        keyring.set_password(self.namespace, "SERVER_B", 'server_a.example.com')
        keyring.set_password(self.namespace, "SERVER_C", 'server_a.example.com')
        keyring.set_password(self.namespace, "KeyTest", True)
        
        # Setting Additional Database Variables in the Keyring
        self.u         = keyring.get_password(self.namespace, "SQL_USER")
        self.p         = keyring.get_password(self.namespace, "SQL_PASS")
        self.driver    = keyring.get_password(self.namespace, "SQL_DRIVER")
        self.a_srv     = keyring.get_password(self.namespace, "SERVER_A")
        self.b_srv     = keyring.get_password(self.namespace, "SERVER_B")
        self.c_srv     = keyring.get_password(self.namespace, "SERVER_C")

        self.setup_connections()
    
    def setup_connections(self):

        # Setup SQLAlchemy Connection Engines
        self.conn_1 = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(self.u, self.p, self.a_srv, "PMDAccess", self.driver)
        self.conn_2 = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(self.u, self.p, self.a_srv, "PowerHCM", self.driver)
        self.conn_3 = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(self.u, self.p, self.b_srv, "PowerHCM", self.driver)
        
        keyring.set_password(self.namespace, "SQL_PMDBS", self.conn_1)
        keyring.set_password(self.namespace, "SQL_PWRAS", self.conn_2)
        keyring.set_password(self.namespace, "SQL_PWRBS", self.conn_2)

        # Setup Simple PyODBC Connection Strings
        self.odbc_pmdbs = f'DRIVER={self.driver};SERVER={self.a_srv};DATABASE=PMDAccess;UID={self.u};PWD={self.p};'
        self.odbc_pwras = f'DRIVER={self.driver};SERVER={self.a_srv};DATABASE=PowerHCM;UID={self.u};PWD={self.p};'
        self.odbc_pwrbs = f'DRIVER={self.driver};SERVER={self.b_srv};DATABASE=PowerHCM;UID={self.u};PWD={self.p};'

        keyring.set_password(self.namespace, "SQL_ODBC_PMDBS", self.odbc_pmdbs)
        keyring.set_password(self.namespace, "SQL_ODBC_PWRAS", self.odbc_pmdbs)
        keyring.set_password(self.namespace, "SQL_ODBC_PWRBS", self.odbc_pmdbs)


        # Setup SharePoint Data

        # Setting up the SharePoint Keyring Values
        keyring.set_password(self.namespace, "root_url",     "https://dvagov.sharepoint.com/sites/")
        keyring.set_password(self.namespace, "resource",     "00000003-0000-0ff1-ce00-000000000000/dvagov.sharepoint.com@e95f1b23-abaf-45ee-821d-b7ab251ab3bf")
        keyring.set_password(self.namespace, "tenant",       "e95f1b23-abaf-45ee-821d-b7ab251ab3bf")
        keyring.set_password(self.namespace, "grant_type",   "client_credentials")

        # Add an entry formatted like below, providing the client and client_secret required to use the
        # SharePoint REST API

        # add site sites/Budget
        site = "Budget"
        keyring.set_password(site, "client",        "abcdef123-567a-89bc-def0-1234ab567890")
        keyring.set_password(site, "client_secret", "GQITXua1u072h7/eQ/HwMgk3e43072h7/eQ/kgYBmc=")

        # add site sites/Finance
        site = "Finance"
        keyring.set_password(site, "client",        "abcdef123-9876-54ab-321b-56ab789cd01")
        keyring.set_password(site, "client_secret", "zZze072h7/eQ/H72h7/eQ/kgY43ucKD+mpoIsb/Yo=")



        print("DDT Keyring Setup for this user, on this machine.")


if __name__ == "__main__":
    setup_keyring()