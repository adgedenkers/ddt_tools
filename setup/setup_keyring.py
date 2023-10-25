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
        u         = keyring.get_password(self.namespace, "SQL_USER")
        p         = keyring.get_password(self.namespace, "SQL_PASS")
        driver    = keyring.get_password(self.namespace, "SQL_DRIVER")
        a_srv     = keyring.get_password(self.namespace, "SERVER_A")
        b_srv     = keyring.get_password(self.namespace, "SERVER_B")
        c_srv     = keyring.get_password(self.namespace, "SERVER_C")
        
        self.conn_1 = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(u, p, a_srv, "Database1", driver)
        self.conn_2 = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(u, p, c_srv, "Database2", driver)
        
        keyring.set_password(self.namespace, "SQL_PMDBS", self.conn_1)
        keyring.set_password(self.namespace, "SQL_PWRAS", self.conn_2)



        # Setting up the SharePoint Keyring Values
        keyring.set_password(self.namespace, "root_url",     "https://example.sharepoint.com")
        keyring.set_password(self.namespace, "resource",     "00000003-0000-0000-0000-000000000000/example.sharepoint.com@abcd1234-efab-56cde-789f-a12b34c45d56e78")
        keyring.set_password(self.namespace, "tenant",       "abcd1234-efab-56cde-789f-a12b34c45d56e78")
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

def setup_keyring(self):
    parser = argparse.ArgumentParser(description="set the Namespace variable")
    parser.add_argument('namespace', type=str, help="Provide the Namespace for the keyring passwords")
    args = parser.parse_args()
    setup_instance = setup(args.namespace)


if __name__ == "__main__":
    setup_keyring()