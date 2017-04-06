
# coding: utf-8

# # Question 2 Part 1
# - Use 'employee_compensation.csv'
# - Calculate mean of total compensation for every department in each organization
# - From this, get highest to lowest paid department and save it to a CSV file.

# In[1]:

import os
import pandas as pd


# In[11]:

#Using relative path for reading the CSV file
#Using only those columns that are needed
cwd = os.getcwd()
data = pd.read_csv(cwd+"//"+"Data//employee_compensation.csv", usecols=[3,5,21])
data.head()


# In[19]:

#Calculating mean of total compensation for every department
#Grouping by the Organization group and Department and then getting the mean value
compensation = data.groupby(['Organization Group','Department']).mean()

#To create flat index
compensation = compensation.reset_index()

compensationFinal = compensation.sort_values(['Organization Group','Total Compensation'],ascending = [True, False])
compensationFinal.head()


# In[18]:

#Writing the output to a CSV file in the folder- Outputs
os.chdir(cwd+"//"+"Outputs")
current=os.getcwd()
compensationFinal.to_csv('Q2_Part_1_Output.csv', index=False , encoding='utf-8')

