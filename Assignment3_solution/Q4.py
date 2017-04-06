
# coding: utf-8

# # Question 4
# - Use 'movies_awards.csv'
# - Split each record into wins and nominations based on the different categories of awards (Oscar, Golden Globe, Primetime, BAFTA)
# - Also, calculate total nominations and total wons and append them together
# - Write output to CSV in the format specified

# In[2]:

import os
import pandas as pd
import datetime
import numpy as np
import re


# In[21]:

#Using relative path for reading the CSV file
#Using only those columns that are needed
cwd = os.getcwd()
data = pd.read_csv(cwd+"//"+"Data//movies_awards.csv", usecols=[5,15])


# In[22]:

#Replacing & with .
data['Awards']=data['Awards'].str.replace(r'&','.')

#Replacing another with ''
data['Awards']=data['Awards'].str.replace(r'Another','')
#data=data.drop(data.columns[[0,1,2,3,4,6,7,8,9,10,11,12,13,14,16,17,18]],axis=3) 


# In[24]:

finalData=pd.DataFrame(columns=['Title','Awards','Awards_won','Awards_nominated','Prime_awards_Nominated','Oscar_awards_Nominated','Gloden_Globe_Nominated','BAFTA_Awards_Nominated','Prime_awards_Won','Oscar_awards_Won','Gloden_Globe_Won','BAFTA_Awards_Won'])

#Using for loop with if statements to get wins and nominations for every category 
for index, row in data.iterrows():
    
    #These variables will hold the total number of wins and nominations
    wins=0
    nominations=0
    
    #These variables will hold awards nominated for and awards won for Oscar, Golden globe, Primetime and BAFTA
    Oscar_nominations=0
    Oscar_won=0
    Golden_Globe_won=0
    Golden_Globe_nominations=0
    Primetime_nominations=0
    Primetime_won=0
    BAFTA_nominations=0
    BAFTA_won=0
    
    #Eliminating NaN values and splitting the data by .
    if type(row['Awards'])!=float:
        row['Awards']=row['Awards'].split('.')   
        for i in range(len(row['Awards'])-1):                     
            if 'win' in row['Awards'][i]:
                wins+=int(row['Awards'][i].split()[0])
            if 'nomination' in row['Awards'][i]:
                nominations+=int(row['Awards'][i].split()[0])
            if 'Oscar' in row['Awards'][i]:
                if 'Nominated' in row['Awards'][i]:
                    Oscar_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Oscar_nominations
                if 'Won' in row['Awards'][i]:
                    Oscar_won+=int(row['Awards'][i].split()[1])
                    wins+=Oscar_won
            if 'Golden Globe' in row['Awards'][i]:
                if 'Nominated' in row['Awards'][i]:
                    Golden_Globe_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Golden_Globe_nominations
                if 'Won' in row['Awards'][i]:          
                    Golden_Globe_won+=int(row['Awards'][i].split()[1])
                    wins+=Golden_Globe_won  
            if 'Primetime Emmy' in row['Awards'][i]:
                if 'Nominated' in row['Awards'][i]:
                    Primetime_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Primetime_nominations
                if 'Won' in row['Awards'][i]:
                    Primetime_won+=int(row['Awards'][i].split()[1])
                    wins+=Primetime_won
            if 'BAFTA' in row['Awards'][i]:
                if 'Nominated' in row['Awards'][i]:
                    BAFTA_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=BAFTA_nominations
                if 'Won' in row['Awards'][i]:
                    BAFTA_won+=int(row['Awards'][i].split()[1])
                    wins+=BAFTA_won
        finalData=finalData.append(pd.Series([row['Title'],row['Awards'],wins,nominations,Primetime_nominations,Oscar_nominations,Golden_Globe_nominations,BAFTA_nominations,Primetime_won,Oscar_won,Golden_Globe_won,BAFTA_won],index=['Title','Awards','Awards_won','Awards_nominated','Prime_awards_Nominated','Oscar_awards_Nominated','Gloden_Globe_Nominate','BAFTA_Awards_Nominated','Prime_awards_Won','Oscar_awards_Won','Gloden_Globe_Won','BAFTA_Awards_Won']),ignore_index=True)
finalData.head()


# In[25]:

#Writing the output to a CSV file in the folder- Outputs
os.chdir(cwd+"//"+"Outputs")
current=os.getcwd()
finalData.to_csv('Q4_Output.csv', index=False , encoding='utf-8')

