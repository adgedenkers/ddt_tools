# Demo Guide for `sp2.py`

## Introduction

This guide provides a comprehensive walkthrough of the `sp2.py` script, which is designed to interact with SharePoint Online via REST API calls. The script includes various functionalities such as file and list operations.

## Class Overview

### SharePoint Class

This class is the main class for interacting with SharePoint Online. It handles authentication and provides methods for various SharePoint operations.

#### Methods

1. **`__init__`**: Initializes the SharePoint object and sets the site name.
2. **`get_token`**: Retrieves the authentication token.
3. **`set_token`**: Sets the authentication token.
4. **`get_file`**: Downloads a file from a SharePoint library.
5. **`get_file_as_dataframe`**: Downloads a file and returns its content as a Pandas DataFrame.
6. **`create_list_from_dataframe`**: Creates a SharePoint list from a Pandas DataFrame.
7. **`save_file_to_library`**: Saves a file to a SharePoint document library.
8. **`search_list`**: Searches a SharePoint list and returns the data in a DataFrame.

---

## Working Examples

### Initialize SharePoint Object

```python
from sp2 import SharePoint

# Initialize SharePoint object
sp = SharePoint("YourSiteName")
```

### Get and Set Token
```python
# Get token
token = sp.get_token()
print(f"Token: {token}")

# Set token
sp.set_token("YourNewToken")
```

### Get File from SharePoint Library
```python
# Download file from SharePoint
sp.get_file("YourLibraryName", "YourFileName.xlsx")
```

### Get File as DataFrame
```python
df = sp.get_file_as_dataframe("YourLibraryName", "YourFileName.csv")
print(df.head())
```

### Create SharePoint List from DataFrame
```python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [30, 40]
})

# Create SharePoint list
sp.create_list_from_dataframe(df, "YourNewListName")
```

### Save File to SharePoint Library
```python
# Save file to SharePoint library
sp.save_file_to_library("YourLibraryName", "YourFileName.xlsx", "YourFilePath")
```

### Search SharePoint List
```python
# Search SharePoint list and get data as DataFrame
search_df = sp.search_list("YourListName", "YourSearchQuery")
print(search_df.head())
```

