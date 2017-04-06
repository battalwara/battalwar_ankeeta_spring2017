
# coding: utf-8

# # Question 1 Part 1
# - Use 'vehicle_collisions.csv'
# - For every month of year 2016, find out accidents in just the borough Manhattan as well as in NYC
# - Calculate percentage of accidents in manhattan to total accidents in NYC
# - Write it to a CSV file with 4 columns: Month, Manhattan, NYC, Percentage

# In[4]:

import os
import pandas as pd


# In[5]:

#Using relative path for reading the CSV file
#Using only those columns that are needed
cwd = os.getcwd()
data = pd.read_csv(cwd+"//"+"Data//vehicle_collisions.csv", parse_dates=['DATE'], usecols=[0,1,3])
data.head()


# In[30]:

#Filtering out the data only for the year of 2016
data_2016 = data[data.DATE.dt.year == 2016]

# Offsetting the warning that python gnerates
pd.options.mode.chained_assignment = None

# Extract month for each date in the dataframe containing 2016 data
data_2016['Month'] = data_2016['DATE'].dt.strftime('%b')


# In[25]:

#Grouping the data by the months in which the accidents occured
NYCdata = data_2016['UNIQUE KEY'].groupby(data_2016['Month']).count()

#Sorting result according to the months
NYCdata.index = pd.CategoricalIndex(NYCdata.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
NYCdata = NYCdata.sort_index()


# In[26]:

#Now, grouping data by months and counting accidents only in Manhattan
ManhattanData = data_2016['UNIQUE KEY'][data_2016['BOROUGH'] == "MANHATTAN"].groupby(data_2016['Month']).count()

#Sorting result according to the months
ManhattanData.index = pd.CategoricalIndex(ManhattanData.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
ManhattanData = ManhattanData.sort_index()


# In[28]:

# Creating a new data frame with both NYC and Manhattan data
Columns = ["Month","Manhattan", "NYC", "Percentage"]
dataFrame = pd.DataFrame({'Month' :NYCdata.index, 'Manhattan' :ManhattanData, 'NYC' :NYCdata, 'Percentage' :ManhattanData/NYCdata})
finalResult[Columns].head()


# In[29]:

#Writing the output to a CSV file in the folder- Outputs
os.chdir(cwd+"//"+"Outputs")
current=os.getcwd()
finalResult.to_csv('Q1_Part_1_Output.csv', index=False , encoding='utf-8')

