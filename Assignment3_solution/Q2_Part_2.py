
# coding: utf-8

# # Question 2 Part 2
# - Use 'employee_compensation.csv'
# - Use only calendar year data. Find average (mean) salary for every employee.
# - Now, find employees whose overtime salary is greater than 5% of their total salaries
# - For every Job Family, calculate percentage of total benefits wrt total compensation.
# - Write it to a CSV file with added column 'Percent Total Benefit'

# In[2]:

import os
import pandas as pd


# In[22]:

#Using relative path for reading the CSV file
#Using only those columns that are needed
cwd = os.getcwd()
data = pd.read_csv(cwd+"//"+"Data//employee_compensation.csv", usecols=[0,1,9,11,12,13,14,15,16,17,18,19,20,21])


# In[23]:

#Filtering the data by Calendar year
calendarData = data[(data['Year Type']=='Calendar')]

#Grouping and finding the mean
averageSalary = calendarData.groupby(['Year','Job Family','Job','Employee Identifier']).mean()

#To create flat index
averageSalary = averageSalary.reset_index()

# To find people whose overtime is greater than 5% of their salaries 
overtime = averageSalary[(averageSalary['Overtime'] > (.05 * averageSalary['Salaries']))]


# In[26]:

#Grouping by Job Family and finding the mean
averageJobFamily = averageSalary[['Job Family', 'Total Benefits', 'Total Compensation']]
averageJobFamily = averageJobFamily.groupby(['Job Family']).mean()


# In[30]:

#Calculating percentage of total benefits for each Job Family and writing it to a new column
averageJobFamily['Percent Total Benefit'] = 100*(averageByJobFamily['Total Benefits'] / averageByJobFamily['Total Compensation'])


# In[29]:

#Sorting to get the top 5
finalAverage= averageJobFamily.sort_values(['Percent Total Benefit'], ascending=[False])
finalAverage.head()


# In[32]:

#Writing the output to a CSV file
finalAverage.reset_index()
os.chdir(cwd+"//"+"Outputs")
current=os.getcwd()
finalAverage.to_csv('Q2_Part_2_Output.csv', index=False , encoding='utf-8')

