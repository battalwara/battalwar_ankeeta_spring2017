
# coding: utf-8

# # Question 1 Part 2 
# - Use 'vehicle_collisions.csv'.
# - From 2015 to present, group by borough and calculate number of accidents by each collision scale
# - Write to CSV with columns- Borough, one_vehicle_involved, two_vehicles_involved etc.

# In[2]:

import os
import pandas as pd


# In[10]:

#Using relative path for reading the CSV file
#Using only those columns that are needed
cwd = os.getcwd()
data = pd.read_csv(cwd+"//"+"Data//vehicle_collisions.csv", usecols=[0,3,19,20,21,22,23])


# In[11]:

#Considering all vehicle types
data_vehicle = data[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]

#Removing all null values
data_type = data_vehicle.notnull()

#Assigning values 0 and 1 to NAN values
data_type = data_type.applymap(lambda x:1 if x else 0)


# In[12]:

#Creating a data frame for comparison
data_location = data[['UNIQUE KEY','BOROUGH']]

#Now, combining this df to data_type df
data_type = pd.concat([data_location, data_type], axis=1)

#Grouping by boroughs and calculating the sum of each vehicle type
data_final = data_type.groupby(data_type['BOROUGH']).sum()


# In[14]:

#Creating the data frame to hold the results
columns = ['Borough', 'One_Vehicle_Involved', 'Two_Vehicles_Involved', 'Three_Vehicles_Involved', 'More_Vehicles_Involved']
result = pd.DataFrame({'Borough' : data_final.index, 'One_Vehicle_Involved' : data_final['VEHICLE 1 TYPE']-data_final['VEHICLE 2 TYPE'], 
                           'Two_Vehicles_Involved' : data_final['VEHICLE 2 TYPE']-data_final['VEHICLE 3 TYPE'], 'Three_Vehicles_Involved' : data_final['VEHICLE 3 TYPE']-data_final['VEHICLE 4 TYPE'],
                           'More_Vehicles_Involved' : data_final['VEHICLE 4 TYPE'] })
result.head()


# In[16]:

#Writing the output to a CSV file in the folder- Outputs
os.chdir(cwd+"//"+"Outputs")
current=os.getcwd()
result.to_csv('Q1_Part_2_Output.csv', index=False , encoding='utf-8')


# In[ ]:



