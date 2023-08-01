################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
################################################################
sInputFileName='Good-or-Bad.csv'
sOutputFileName='Good-or-Bad-03.csv'
Company='01-Vermeulen' 
Base='C:/dsr/'
################################################################
print('################################')
print('Working Base :',Base, ' using ')
print('################################')

################################################################
################################################################
sFileDir=Base + '/' + Company
if not os.path.exists(sFileDir): os.makedirs(sFileDir) 
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
sFileName=sFileDir + '/' + sInputFileName
RawData.to_csv(sFileName, index = False)
################################################################
TestData=RawData.dropna(thresh=2)
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
sFileName=sFileDir + '/' + sOutputFileName
TestData.to_csv(sFileName, index = False)
################################################################
print('################################')
print('### Done!! #####################')
print('################################')
print('By Prithvi Vasta')
################################################################
