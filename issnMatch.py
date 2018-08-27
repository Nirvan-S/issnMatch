"""
Author: Nirvan Sengupta
Date: August 27th, 2018
Filename: issnMatch.py
Description: 
Script to find matching ISSNs in SSCI and SCIE metrics files from a list of ISSNs provided by client. 
Returns JIFs for 200 ISSNs when they are found. 
"""

import pandas as pd

### Read Client's Data ###


### Read SSCI and SCIE data ###
inputDir = "C:\\Users\\u6048427\\OneDrive - Clarivate Analytics\\General\\"

print("Reading SCIE JCR Metrics file")
scie = pd.read_excel( io = inputDir + 'JCR_SCIE_2017.xlsx')
scie = scie[['ISSN','IMPACT_FACTOR']]

print("Reading SSCI JCR Metrics file")
ssci = pd.read_excel( io = inputDir + 'JCR_SSCI_2017.xlsx')
ssci = ssci[['ISSN','IMPACT_FACTOR']]