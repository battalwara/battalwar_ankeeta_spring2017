
# coding: utf-8

# # Questions 3
# - Use 'cricket_matches.csv'
# - For each team, check matches they won for either innings 1 or innings 2 for home matches.
# - Calculate average score for these teams during the siad matches and write it to a CSV

# In[20]:

import os
import pandas as pd


# In[22]:

#Using relative path for reading the CSV file
#Using only those columns that are needed
cwd = os.getcwd()
data = pd.read_csv(cwd+"//"+"Data//cricket_matches.csv", usecols=[6,7,8,12,13,17,18])
data.head()


# In[23]:

#Sorting data by Home
sortedData = data.sort_values(['home'], ascending=True)

#Checking for teams that won in either games of innings 1 or innings 2
sortedInnings1Data = sortedData[(sortedData['home'] == sortedData['winner']) & (sortedData['winner'] == sortedData['innings1'])]
sortedInnings2Data = sortedData[(sortedData['home'] == sortedData['winner']) & (sortedData['winner'] == sortedData['innings2'])]


# In[24]:

#Creating 2 new data frames to hold the data for innings 1 and 2
data_innings1 = pd.DataFrame({'home': sortedInnings1Data['home'], 'Runs': sortedInnings1Data['innings1_runs']})
data_innings2 = pd.DataFrame({'home': sortedInnings2Data['home'], 'Runs': sortedInnings2Data['innings2_runs']})

#Concatenating both data frames to get all teams which won in either innings 1 or 2
final_data = data_innings1.append(data_innings2, ignore_index=True)


# In[25]:

#Calculating average of runs for each team which hosts the game (=home)
averageRuns = final_data['Runs'].groupby(final_data['home']).mean()
finalScore = pd.DataFrame({'Home' : averageRuns.index, 'Score' : averageRuns})
finalScore.head()


# In[26]:

#Writing the output to a CSV file in the folder- Outputs
os.chdir(cwd+"//"+"Outputs")
current=os.getcwd()
averageRuns.to_csv('Q3_Output.csv', index=False , encoding='utf-8')

