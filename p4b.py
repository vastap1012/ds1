################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
################################################################
Base='C:/dsr/'
sInputFileName='Good-or-Bad.csv'
sOutputFileName='Good-or-Bad-02.csv'
################################################################
Base='C:/dsr/'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
################################################################
### Import Warehouse
################################################################
sFileName=Base + sInputFileName
print('Loading :',sFileName)
RawData=pd.read_csv(sFileName,header=0)

print('################################')  
print('## Raw Data Values')  
print('################################')  
print(RawData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
print('################################')
################################################################
RawData.to_csv(sFileName, index = False)
################################################################
TestData=RawData.dropna(axis=1, how='any')
################################################################
print('################################')  
print('## Test Data Values')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
TestData.to_csv(sFileName, index = False)
################################################################
print('################################')
print('### Done!! #####################')
print('################################')
print('By prithvi vasta')
################################################################