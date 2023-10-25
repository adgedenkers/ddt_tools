'''
Name: test_sp2.py
Description: Test script for sp2.py
Author: Adge Denkers / github.com/adgedenkers/
Created: 2023-10-25
Updated: 2023-10-25
(C) 2023 denkers.co 
'''

import unittest
from sp2 import SharePoint
import pandas as pd
import os

class TestSharePoint(unittest.TestCase):

    def setUp(self):
        self.sp = SharePoint("TestSite")

    def test_get_token(self):
        token = self.sp.get_token()
        self.assertIsNotNone(token)

    def test_set_token(self):
        self.sp.set_token("test_token")
        self.assertEqual(self.sp.get_token(), "test_token")

    def test_get_file(self):
        # Mocking the SharePoint library and file for testing
        library = "TestLibrary"
        file = "TestFile.xlsx"
        self.sp.get_file(library, file)
        # Add your own assertions based on your specific requirements

    def test_get_file_as_dataframe(self):
        library = "TestLibrary"
        file = "TestFile.csv"
        df = self.sp.get_file_as_dataframe(library, file)
        self.assertIsInstance(df, pd.DataFrame)

    def test_create_list_from_dataframe(self):
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob'],
            'Age': [30, 40]
        })
        list_name = "TestList"
        self.sp.create_list_from_dataframe(df, list_name)
        # Add your own assertions based on your specific requirements

if __name__ == "__main__":
    unittest.main()
