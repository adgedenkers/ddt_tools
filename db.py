'''
File: db.py
Version: 1.6
Project: ddt_tools
Created Date: 2023-08-01
Author: Adge Denkers
Email: adriaan.denkers@va.gov
-----
Last Modified: 2023-10-25
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

import keyring
import pandas as pd
import pyodbc
import sqlalchemy

from sqlalchemy import create_engine, text, true

def connection(alias):
    conn_str = keyring.get_password("DDT-AUTO", alias)
    return create_engine(conn_str)
