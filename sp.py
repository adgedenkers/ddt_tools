'''
File: sp.py
Version: 2.1
Project: ddt_tools
Created Date: 2023-10-24
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

import io
import keyring
import pandas as pd
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SP:
    def __init__(self, site_name:str) -> None:
        """
        Initializes the SP object with credentials and site information.

        Args:
            site_name (str): The name of the site.
        """
        self.site       = site_name
        self.namespace  = "DDT-SP"
        self.root_url   = keyring.get_password(self.namespace, "root_url")
        self.tenant     = keyring.get_password(self.namespace, "tenant")
        self.resource   = keyring.get_password(self.namespace, "resource")
        self.grant_type = keyring.get_password(self.namespace, "grant_type")
        self.client     = keyring.get_password(self.site, "client")
        self.secret     = keyring.get_password(self.site, "client_secret")

    def get_token(self) -> str:
        """
        Retrieves the access token.

        Returns:
            str: The access token.
        """
        payload = {
            'grant_type':       self.grant_type,
            'client_id':        self.client,
            'client_secret':    self.secret,
            'resource':         self.resource
        }
        url = f'https://accounts.accesscontrol.windows.net/{self.tenant}/tokens/OAuth/2'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            token_data = response.json()
            return token_data['access_token']
        except requests.RequestException as e:
            logging.error(f"Failed to retrieve token: {e}")
            return None

    def loadFileToDF(self, library: str, file: str, start_line: int = 0) -> pd.DataFrame:
        """
        Loads a file to a DataFrame.

        Args:
            library (str): SharePoint Document Library URL part.
            file (str): Name of the file to load.
            start_line (int, optional): Line number to start reading from. Defaults to 0.

        Returns:
            pd.DataFrame: The loaded DataFrame.
        """
        file_type = file.split(".")[1]
        site      = self.site

        req_headers = {
            'Connection':'keep-alive',
            'Authorization':'Bearer {}'.format(self.getToken()),
            'Content-Type':'application/octet-stream'
        }

        req_url = "https://dvagov.sharepoint.com/sites/{s}/_api/web/GetFileByServerRelativeUrl('/sites/{s}/{l}/{f}')/$value".format(l=library, f=file, s=site)
        response = requests.get(req_url, headers=req_headers)
        f = io.BytesIO(response.content)
        
        df = pd.DataFrame()

        if file_type == 'xlsx':
            df = pd.read_excel(f, skiprows=start_line, engine='openpyxl')
        if file_type == 'csv':
            df = pd.read_csv(f, skiprows=start_line)
        return df

    def saveFileInLibrary(self, library, file_name, file_path):
        """safeFileInLibrary

        Args:
            library (str): SharePoint Document Library URL part.
            file_name (str): Name of the file to save.
            file_path (str): Path of the file to save.
        """
        site = self.site
        req_headers = {
            'Connection':'keep-alive',
            'Authorization':'Bearer {}'.format(self.getToken()),
            'Content-Type':'application/octet-stream'
        }
        req_url = "https://dvagov.sharepoint.com/sites/{s}/_api/web/lists/getbytitle('{l}')/rootfolder/files/add(url='{fn}', overwrite=true)".format(l=library, fn=file_name, s=site)

        with open(file_path, 'rb') as file:
            response = requests.put(req_url, headers=req_headers, data=file)
            
            
    def getListItemIdFromItemTitle(self, listname: str, itemtitle: str) -> int:
        """
        Retrieves the list item ID from the item title.

        Args:
            listname (str): The name of the list.
            itemtitle (str): The title of the item.

        Returns:
            int: The ID of the list item.
        """
        site = self.site
        
        req_headers = { 
            'Connection':'keep-alive',   
            'Authorization':'Bearer {}'.format(self.getToken()),
            'Accept':'application/json;odata=verbose'
        }

        req_url = 'https://dvagov.sharepoint.com/sites/{site}/_api/web/lists/GetByTitle({listname})/items?$filter=Title eq \'{itemtitle}\'&$select=ID'

        response = requests.get(req_url, headers=req_headers)
        
        if response.status_code == 200:
            data = response.json()
            item_id = data['d']['results'][0]['ID']
            return item_id
        else:
            print("Failed to retrieve the item ID")
            print("Status code:", response.status_code)
            print("Response text:", response.text)

    def getRequestHeader(self):
        # set the request header json data
        req_headers = {
            'Connection':'keep-alive',
            'Authorization':'Bearer {}'.format(self.getToken()),
            'Content-Type':'application/octet-stream'
        }
        # return the json object
        return req_headers



    # SP API Request Example #
    def exampleFunction(self):
        
        req_headers = self.getRequestHeader()
        req_url = 'https://dvagov.sharepoint.com/sites/{self.site}/_api/web/lists/GetByTitle({listname})/items?$filter=Title eq \'{itemtitle}\'&$select=ID'
        response = requests.get(req_url, headers=req_headers)
        
        if response.status_code == 200:
            data = response.json()
            item_id = data['d']['results'][0]['ID']
            return item_id
        else:
            print("Failed to retrieve the item ID")
            print("Status code:", response.status_code)
            print("Response text:", response.text)


# Usage
#cust_site = SP("/sites/oitautomations/customers")