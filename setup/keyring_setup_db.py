'''
File: c:\python\ddt_main_keyring_setup.py
Version: 1.0
Project: 'ddt_tools'
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
import hashlib
import keyring

class setup():

    def __init__(self, NAMESPACE) -> None:
        keyring.set_password(NAMESPACE, "SALT", hashlib.md5(NAMESPACE.encode('utf-8')).hexdigest())
        keyring.set_password(NAMESPACE, "SQL_USER", 'DDTAutomations')
        keyring.set_password(NAMESPACE, "SQL_PASS", 'TA2XVMLQ6^xDSm4cYbVTA$Qjx9CdVxZj')
        keyring.set_password(NAMESPACE, "SQL_DRIVER", 'SQL Server Native Client 11.0')
        keyring.set_password(NAMESPACE, "SERVER_A", 'OITORLSQL1A.r03.med.va.gov')
        keyring.set_password(NAMESPACE, "SERVER_B", 'OITORLSQL1B.r03.med.va.gov')
        keyring.set_password(NAMESPACE, "SERVER_C", 'OITORLSQL1C.va.gov')
        keyring.set_password(NAMESPACE, "KeyTest", True)
        
        # Setting Additional Database Variables in the Keyring
        u         = keyring.get_password("DDT-AUTO", "SQL_USER")
        p         = keyring.get_password("DDT-AUTO", "SQL_PASS")
        driver    = keyring.get_password("DDT-AUTO", "SQL_DRIVER")
        a_srv     = keyring.get_password("DDT-AUTO", "SERVER_A")
        b_srv     = keyring.get_password("DDT-AUTO", "SERVER_B")
        c_srv     = keyring.get_password("DDT-AUTO", "SERVER_C")
        
        self.pmdb = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(u, p, a_srv, "PMDAccess", driver)
        self.pwra = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(u, p, a_srv, "PowerHCM",  driver)
        self.pwrb = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(u, p, b_srv, "PowerHCM",  driver)
        self.delr = "mssql+pyodbc://{}:{}@{}/{}?driver={}&Trusted_Connection=no".format(u, p, b_srv, "delrio",  driver)
        
        keyring.set_password(NAMESPACE, "SQL_PMDBS", self.pmdb)
        keyring.set_password(NAMESPACE, "SQL_PWRAS", self.pwra)
        keyring.set_password(NAMESPACE, "SQL_PWRBS", self.pwrb)
        keyring.set_password(NAMESPACE, "SQL_DELRS", self.delr)

        print("DDT Keyring Setup for this user, on this machine.")

if __name__ == "__main__":
    setup("DDT-AUTO")



