'''
Name: sp.py
Description: Script to interact with SharePoint Online via REST API
Author: Adge Denkers / github.com/adgedenkers/
Created: 2023-08-13
Updated: 2023-10-25
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

    def create_list_from_dataframe(self, df, list_name):
        """
        Create a SharePoint list from a Pandas DataFrame.
        """
        # Create the list
        create_list_url = f"https://dvagov.sharepoint.com/sites/{self.site}/_api/web/lists"
        list_payload = {
            '__metadata': {'type': 'SP.List'},
            'BaseTemplate': 100,
            'Title': list_name
        }
        try:
            response = self.session.post(create_list_url, json=list_payload)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Failed to create list: {e}")
            raise

        # Add columns to the list based on DataFrame dtypes
        for col, dtype in df.dtypes.items():
            add_field_url = f"https://dvagov.sharepoint.com/sites/{self.site}/_api/web/lists/getbytitle('{list_name}')/fields"
            field_type = 'SP.FieldText'  # Default to text field
            if dtype == 'int64':
                field_type = 'SP.FieldNumber'
            elif dtype == 'float64':
                field_type = 'SP.FieldNumber'
            # Add more dtype to SharePoint field type mappings as needed

            field_payload = {
                '__metadata': {'type': field_type},
                'Title': col,
                'FieldTypeKind': 2  # Corresponds to SP.FieldText
            }
            try:
                response = self.session.post(add_field_url, json=field_payload)
                response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"Failed to add field {col}: {e}")
                raise

        # Populate the list with data from the DataFrame
        for _, row in df.iterrows():
            add_item_url = f"https://dvagov.sharepoint.com/sites/{self.site}/_api/web/lists/getbytitle('{list_name}')/items"
            item_payload = {'__metadata': {'type': 'SP.Data.TestListItem'}}
            for col in df.columns:
                item_payload[col] = row[col]
            try:
                response = self.session.post(add_item_url, json=item_payload)
                response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"Failed to add item: {e}")
                raise

    def save_file_to_library(self, library, file_path):
        """
        Save a file to a SharePoint library.
        """
        file_name = os.path.basename(file_path)
        req_url = f"https://dvagov.sharepoint.com/sites/{self.site}/_api/web/GetFolderByServerRelativeUrl('/sites/{self.site}/{library}')/Files/add(url='{file_name}', overwrite=true)"
        
        with open(file_path, 'rb') as f:
            file_content = f.read()
        
        try:
            response = self.session.post(req_url, data=file_content)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Failed to save file: {e}")
            raise

    def search_list_and_return_df(self, list_name, query):
        """
        Search a SharePoint list and return data in a Pandas DataFrame.
        """
        req_url = f"https://dvagov.sharepoint.com/sites/{self.site}/_api/web/lists/getbytitle('{list_name}')/items?{query}"
        
        try:
            response = self.session.get(req_url)
            response.raise_for_status()
            data = response.json()['value']
            df = pd.DataFrame(data)
            return df
        except requests.RequestException as e:
            logging.error(f"Failed to search list: {e}")
            raise

# Store the token in the keyring
token = "your_token_here"
sp = SharePoint('your_site_here')
sp.set_token(token)

# Usage
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [30, 40]})
sp.create_list_from_dataframe(df, 'NewList')

# Save a file to a library
sp.save_file_to_library('Documents', 'C:/path/to/your/file.txt')

# Search a list and return data in a DataFrame
query = "$filter=Title eq 'Alice'"
result_df = sp.search_list_and_return_df('NewList', query)
