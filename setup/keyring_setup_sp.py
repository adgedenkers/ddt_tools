'''
File: keyring_setup_sp.py
Version: 1.0
Project: 'ddt_tools'
Created Date: 2023-10-25
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

# set main sharepoint variables
namespace="DDT-SP"
keyring.set_password(namespace, "root_url",     "https://dvagov.sharepoint.com")
keyring.set_password(namespace, "resource",     "00000003-0000-0ff1-ce00-000000000000/dvagov.sharepoint.com@e95f1b23-abaf-45ee-821d-b7ab251ab3bf")
keyring.set_password(namespace, "tenant",       "e95f1b23-abaf-45ee-821d-b7ab251ab3bf")
keyring.set_password(namespace, "grant_type",   "client_credentials")

# set per-site credentials

# add site sites/HCMDynamicDataTeamAutomation
site = "HCMDynamicDataTeamAutomation"
keyring.set_password(site, "client",        "d777099b-9b0b-40dc-ade1-5801eb296719")
keyring.set_password(site, "client_secret", "GQITXua1u072h7/eQ/W3wyjDNw6HhC0dOQJT5kgYBmc=")

# add site oitautomations
site = "oitautomations"
keyring.set_password(site, "client",         "7cbc97f9-9640-45c1-965b-62bb3411fa74")
keyring.set_password(site, "client_secret",  "zZzehsFZv+iQ6Dkp18HHwMgk3e43ucKD+mpoIsob/Yo=")

# add site oitautomations/customers
site = "oitautomations/customers"
keyring.set_password(site, "client",        "4dfe12c6-1acf-4e7b-91bd-d4580dd3df34")
keyring.set_password(site, "client_secret", "QOzTnPR05BAp4rvVgupIXk0mDbXY0vcj8ZOO2FDm9co=")

# add site oitautomations/customers/awards
site = "oitautomations/customers/awards"
keyring.set_password(site, "client",        "0ba42e07-3757-476a-a952-d452c4a69dfa")
keyring.set_password(site, "client_secret", "sLW1BnhVT/K/0wDJ9O6ScutKFN5nmOxkGSy+PgXfYZs=")

# add site oitautomations/customers/ddt
site = "oitautomations/customers/ddt"
keyring.set_password(site, "client",        "051423b6-5150-4156-95f8-900aac251973")
keyring.set_password(site, "client_secret", "MYd5sDlwM+bdEfhCsG7Cy19arxD6GQggvgHwI8KzNaE=")

# add site oitautomations/customers/eperf_reporting
site = "oitautomations/customers/eperf_reporting"
keyring.set_password(site, "client",        "4223b0e2-1a63-4c95-badf-29a95da3f705")
keyring.set_password(site, "client_secret", "Y3uX1UCm0wTHC3OfLa4UdHyCadEzxSRJsCheAiU3msg=")

# add site OITCareersIntake
site = "OITCareersIntake"
keyring.set_password(site, "client",        "d28f7086-4b20-442e-8c12-9bf13e11c7c6")
keyring.set_password(site, "client_secret", "fwSnKbUkGAxbEVBwcwO0fdodL3iSzqXZVaoalUXumio=")

# add site OITHR
site = "OITHR"
keyring.set_password(site, "client",        "d0eff23c-8a80-485f-befd-058252284ee8")
keyring.set_password(site, "client_secret", "PxUTjFE/vYaYJzK3X23PC82DYk6Aq6ruFeU4QeVqjbg=")

# add site OITHR/OPS
site = "OITHR/OPS"
keyring.set_password(site, "client",        "d0eff23c-8a80-485f-befd-058252284ee8")
keyring.set_password(site, "client_secret", "PxUTjFE/vYaYJzK3X23PC82DYk6Aq6ruFeU4QeVqjbg=")

# add site OITHR/AMO
site = "OITHR/AMO"
keyring.set_password(site, "client",        "28aed58b-cf0d-40a3-88de-f95d42c5260c")
keyring.set_password(site, "client_secret", "seDDSBj/wP3upYWlleeiErsLvcO702dnKfpiw04Sxww=")