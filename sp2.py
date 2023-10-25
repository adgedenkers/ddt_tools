'''
Name: sp.py
Description: Script to interact with SharePoint Online via REST API
Author: Adge Denkers / github.com/adgedenkers/
Created: (date the file was originally created)
Updated: (date the file was last updated)
(C) 2023 denkers.co 
'''

import io
import os
import requests
import pandas as pd
import keyring
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

class SharePoint:
    def __init__(self, site):
        self.site = site
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f"Bearer {self.get_token()}",
            'Content-Type': 'application/octet-stream'
        })

    def get_token(self):
        """
        Retrieve the SharePoint token from the keyring.
        """
        try:
            return keyring.get_password("SharePoint", "token")
        except Exception as e:
            logging.error(f"Failed to retrieve token: {e}")
            raise

    def set_token(self, token):
        """
        Store the SharePoint token in the keyring.
        """
        try:
            keyring.set_password("SharePoint", "token", token)
        except Exception as e:
            logging.error(f"Failed to set token: {e}")
            raise

    def get_file(self, library, file):
        """
        Get a file from a SharePoint library.
        """
        req_url = f"https://dvagov.sharepoint.com/sites/{self.site}/_api/web/GetFileByServerRelativeUrl('/sites/{self.site}/{library}/{file}')/$value"
        try:
            response = self.session.get(req_url, timeout=10)
            response.raise_for_status()
            
            f = io.BytesIO(response.content)
            df = pd.DataFrame()
            # Your DataFrame logic here
        except requests.RequestException as e:
            logging.error(f"Failed to get data: {e}")
            raise

    def get_file_as_dataframe(self, library, file):
        """
        Get an Excel or CSV file from a SharePoint library and return it as a Pandas DataFrame.
        """
        req_url = f"https://dvagov.sharepoint.com/sites/{self.site}/_api/web/GetFileByServerRelativeUrl('/sites/{self.site}/{library}/{file}')/$value"
        try:
            response = self.session.get(req_url, timeout=10)
            response.raise_for_status()
            
            file_extension = os.path.splitext(file)[1]
            
            if file_extension == '.csv':
                df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
            elif file_extension == '.xlsx':
                df = pd.read_excel(io.BytesIO(response.content), engine='openpyxl')
            else:
                logging.error("Unsupported file type")
                return None
            
            return df
        except requests.RequestException as e:
            logging.error(f"Failed to get data: {e}")
            raise

# Store the token in the keyring (do this once)
# Uncomment the next two lines to set the token
# token = "your_token_here"
# SharePoint().set_token(token)

# Usage
# Uncomment the next two lines to use the class
# sp = SharePoint('your_site_here')
# df = sp.get_file_as_dataframe('your_library_here', 'your_file.xlsx')
