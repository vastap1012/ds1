################################################################ 
import networkx as nx 
import matplotlib.pyplot as plt 
import sys 
import os 
import pandas as pd 
################################################################ 
Base='C:/dsr/' 
################################################################ 
print('################################') 
print('Working Base :',Base, ' using ', sys.platform) 
print('################################') 
################################################################ 
sInputFileName='Retrieve_Router_Location.csv' 
sOutputFileName1='Assess-DAG-Company-Country.png' 
sOutputFileName2='Assess-DAG-Company-Country-Place.png' 
Company='01-Vermeulen' 
################################################################ 
### Import Company Data 
################################################################ 
sFileName=Base + sInputFileName 
print('################################') 
print('Loading :',sFileName) 
print('################################') 
CompanyData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1") 
print('Loaded Company :',CompanyData.columns.values) 
print('################################') 
################################################################ 
print(CompanyData) 
print('################################')
print('Rows : ',CompanyData.shape[0]) 
print('################################') 
################################################################ 
G1=nx.DiGraph() 
G2=nx.DiGraph() 
################################################################ 
for i in range(CompanyData.shape[0]): 
 G1.add_node(CompanyData['Country'][i]) 
 sPlaceName= CompanyData['Place_Name'][i] + '-' + CompanyData['Country'][i] 
 G2.add_node(sPlaceName) 
print('################################') 
for n1 in G2.nodes(): 
     for n2 in G2.nodes(): 
         if n1 != n2: 
             print('Link :',n1,' to ', n2) 
             G2.add_edge(n1,n2) 
print('################################') 
print('################################') 
print("Nodes of graph: ") 
print(G2.nodes()) 
print("Edges of graph: ") 
print(G2.edges()) 
print('################################') 
################################################################ 
sFileDir=Base + '/' + Company  
if not os.path.exists(sFileDir):os.makedirs(sFileDir) 
################################################################ 
sFileName=sFileDir + '/' + sOutputFileName2 
print('################################') 
print('Storing :', sFileName) 
print('################################') 
nx.draw(G2,pos=nx.spectral_layout(G2),node_color='r',edge_color='b', with_labels=True,node_size=8000, font_size=12) 
plt.savefig(sFileName) # save as png 
plt.show()
print('By Prithvi Vasta')# display 
################################################################
