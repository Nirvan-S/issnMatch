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
print('Reading target ISSN data')
clientData = pd.read_excel('ACL OAA Data Reach Database.xlsx')

#Get Target ISSNs#
targetISSNs = clientData[['ISSN']]

### Read SSCI and SCIE data ###
inputDir = "C:\\Users\\u6048427\\OneDrive - Clarivate Analytics\\General\\"

print("Reading SCIE JCR Metrics file")
# scie = pd.read_excel( io = inputDir + 'JCR_SCIE_2017.xlsx')
# scie = scie[['ISSN','IMPACT_FACTOR']]
scie = pd.read_csv('scie_IF.csv')
print("Reading SSCI JCR Metrics file")
# ssci = pd.read_excel( io = inputDir + 'JCR_SSCI_2017.xlsx')
# ssci = ssci[['ISSN','IMPACT_FACTOR']]
ssci = pd.read_csv('ssci_IF.csv')
allJournals = pd.concat([ssci, scie])

### Get mapping of ISSN to IF for journals in client data ###
testMerge = pd.merge(targetISSNs, allJournals, on = 'ISSN', how = 'inner')
JIFs = testMerge.groupby(['ISSN']).apply(lambda df: df.iloc[0,:])
JIFs.reset_index(drop = True, inplace = True)

### Merge ISSNs on to clientData ###
testFinal = pd.merge(clientData, JIFs, on = 'ISSN', how = 'left')

testFinal.to_csv('w_JCR_IF.csv', index = False)

### Clean Merge ###
# targetCounts = targetISSNs.ISSN.value_counts().sort_index()
# mergeCounts  = testMerge.ISSN.value_counts().sort_index()
# ISSNs = targetISSNs.ISSN.value_counts().sort_index().index

# problemISSNs = ISSNs[targetCounts < mergeCounts].unique()

# #Grab nonproblem records
# nonProbMerge = testMerge[~testMerge.ISSN.isin(problemISSNs)]
# #Grab problem records
# probMerge    = testMerge[testMerge.ISSN.isin(problemISSNs)]
# #remove duplicates

# probMerge.groupby(['ISSN']).apply( lambda df: df.iloc[:int(len(df)/2)])

# gb = probMerge.groupby(['ISSN'])
# for issn, df in gb:
#     print(df.iloc[:int(len(df)/2)],)
#Stack the two sets

#Write to file