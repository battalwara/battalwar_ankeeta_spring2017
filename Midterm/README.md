
Question 1: Enron dataset

Analysis 1

- Using the Enron data set, I've attempted to parse through all the emails in the Enron data set and get the following information:
	- Top 10 email addresses receiving the most emails
	- Top 10 email addresses sending the most emails
- In order to use the directory structure provied in the question, I've first used the directory to fetch the data as directed (Midterm\data\enron\maildir)
- Later, to write to the txt files, kindly change the directory to where you want these files to be stored for viewing and/or retrieval

- The results were as follows:
- Output file for to_emails is stored at \Question_1\to_email_list.txt
- Output file for from_emails is stored at \Question_1\from_email_list.txt
- Output file for results is stored at \Question_1\Q1_A1_OP.txt

Inference

- From the top 10 receivers of mails (to_email_list), we can see that the top most person to receive emails is Richard Shapiro. He was the Senior Vice President and lobbyist for Enron. A lobbyist is the person who takes part in an organized attempt to influence legislators. In simpler terms, he/she pays bribes to the government to mend laws etc. He was convicted for fraud during the trials by the government.
- The second top most person to receive mails was Jeff Dasovich, who was the Government Relations Executive at Enron. We can think that the corporation was actively involved in maintaining relations with the U.S. government, which might have helped in keeping the fraud hidden.
- The top most person to send emails was Kay Mann. On researching, I found out that she was the Assistant General Counsel and thus was one of the top officials of the legal department at Enron. She was not found guilty on any charges. This shows that not all employees were part of the fraud, only the tp officials were, even after having such a strong legal department.


Analysis 2

- In this analysis, I've tried to retrieve all the domain addresses of email IDs to which mails were sent by the employees at Enron Corportion to see which outer bodies di dthey communicate with.
- For this analysis, I've used the 'to_emil_list.txt' file which was output of the last analysis
- NLTK package is used to use the inbuilt function word_tokenize

- The output is saved here: \Question_1\Q1_A2_OP.txt

Inference

- Thus we can see that Enron corporation maintained communications with a lot of organizations outside the company, some of the notable ones being:
	-uk.standardchartered.com : Enron had relations with a few people in the UK to hide money. This may relate to those transactions.
	-duke_energy.com : This was one of the firms that was accused of fraud too as subsidaries to Enron Corp.
	
Analysis 3

- In this analysis, I have calculated the frequency of those words that raise suspicion, contained in the emails of Kenneth Lay, one of the CEO's of Enron.
- I then calculated the frequency of these words to derive some useful information.
- I've used nltk package for the inbuilt methods word_tokenize and FreqDist.
- The output is saved here: \Question_1\Q1_A3_OP.png

Inference

- Thus, we can see that words such as bankruptcy and brankupt were used more than a 1000 times in the mails exchangd with Kenneth Lay.
- This gives us the information that Kenneth Lay knew they were going to get bankrupt and were avoiding it till the final downfall.


Question 2: NYT API data

NYT Data Extraction and Storage

- I've used data from two API's- Article and Archive
- The archive data contains all articles from October-December 2016
- It is saved at \Question_2\ArchivedData\*.json
- The article API is contained in \Question_2\ClintonData\*.json

- The key has been imported from the OS as an environmental variable, for security

Analysis 1

- In this analysis, I've taken all the archive data for 3 months of 2016.
- With this data, I've analyzed which countries amongst those that U.S. does business actively; Inida, Japan, China, France, are most frequently mentioned in the headlines.
- The output is located at: \Question_2\Q2_A1_OP*

Inference

- Thus, we can see that India has been used most frequent in the headlines, followed by France, Japan and then China.

Analysis 2

- Using the data fetched from Article API data, I've analyzed the number of articles for each section.
- In the next step, I've analzed the number of subsections in the sections of these articles.
- The output is located at: \Question_2\Q2_A2_OP*

Analysis 3

- Using the Archive API data, I have calculated the top 10 frequent sections of news headlines for the available year-months.
- This analysis helps us to know which wre the top news section trends for the following three months in the year of 2016: October, November and December
- I've used matplotlib to build a pie chart to show the top 10 sections of articles for October.
- The output is located at: \Question_2\Q2_A2_OP*
In [ ]:
