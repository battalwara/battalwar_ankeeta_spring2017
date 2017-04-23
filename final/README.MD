# Final Submission: Pattern 1
## Data for Analysis
- I've used the Airbnb data available online for the cities Boston and Seattle
- Each folder contains the following files:
  1. listings.csv: It contains complete detailed information on every listing ID.
  2. reviews.csv: It includes unique ID for each reviewer and detailed comments.
  3. calendar.csv: It contains information on a particular date, listig ID and the price and availability for that day
- I chose this dataset to study the usage, popularity of the Airbnb app in two major cities
- Analysing this information has also provided some statistics on the number of visitors and prices in these two major U.S. cities.

## Packages used:
- Numpy and Pandas
- matplotlib and seaborn for plotting
- nltk.tokenize

## Types of graphs plotted: 
Line graph, Bar graph, Scatter plot, Box plot

## Analysis 1: Using Boston data
Analysis of the 'calendar.csv' file for Boston Airbnb data for the following information:

### 1. Availability of the listings over days
  <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-1/Output1.jpg" width=700>
  
#### Conclusion:
The above graph shows us the trend of busiest days in Boston between September 2016- September 2017 based on the % availability of listings. Availability has increased drastically from Sepetember to December 2016, maybe because many hosts joined Airbnb with its increasing popularity. 

### 2. Price variations of listings across the year for data available
  <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-1/Output2.jpg" width=700>

#### Conclusion: 
The above graph shows the trend for average price of listings over the month-year data available. We can infer that as the Airbnb app got popular, the average prices have remained about the same close to 150 dollars , as compared to around 200 dollars in September 2016.

## Analysis 2: Using Boston data
Analysis of the 'listings.csv' file for Boston Airbnb data for the following information:

### 1. Increase in the poularity of Airbnb, based on addition of new hosts.
  <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-2/Output1.jpg" width=700>
  
#### Conclusion:
The number of new hosts has increased drastically over the years of 2014-2016, with maximum users joining Airbnb in mid 2014. 

### 2. Number of apartments listed at the different prices.
  <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-2/Output2.jpg" width=700>

#### Conclusion:
- There are more than 2500 listings at price range of 0-200 dollars while the number of apartments listed above 500 dollars is very less.
- This strongly supports the idea of Airbnb which is focused on providing affordable housing for travelers.

### 3. Number of reviews based on the listing price.
  <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-2/Output3.jpg" width=700>

#### Conclusion:
- Above graph shows a scatter plot mapping the number of reviews for the listings vs their price
- We can see that affordable and economic apartment listings hav more number of reviews as compared to high-end expensive apartment listings.

### 4. Variations in Price based on Apartment Type
  <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-2/Output4.jpg" width=700>
  
#### Conclusion:
- Above Box plot shows variation in prices based on the type of apartment.
- Box plot is more informative as it gives us the median/mean value, as well as the upper and lower whiskers (Scores outside the middle 50% values)
- Here, comparing on median values, we can see that fancy apartment tyes such as boats and villas are most expensive while dorms, townhouses and B&Bs are cheapest.

## Analysis 3: Comparison of both cities based on Calendar data
Comparison and analysis of the 'calendar.csv' file for Boston and Seattle Airbnb data for the following information:

### Comparison of Price of listing based on month-of-year
   <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-3/Output.jpg" width=800>
   
#### Conclusion:
- Based on the plot, most expensive time of the year in Boston is November and December
- In seattle, prices are quite constant across the year with little variation
- Comparatively, prices in Boston are much higher as compared to Seattle. Thus, we can conclude that Boston is more expensive than seattle

## Analysis 4: Comparison of both cities based on reviews
Comparison and analysis of the 'reviews.csv' file for Boston and Seattle Airbnb data for the following information:

### Number of visitors visiting the two cities during different times of the year
   <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-4/Output.jpg" width=800>
   
#### Conclusion:
- In Boston, we can see number of visitors is maximum in the months of july-september
- The same trend is seen in Seattle.
- On an average, number of visitors in Seattle is higher than number of visitors in Boston, based on Airbnb data. This can be seen in the period of Sep. 2014- Dec. 2015


## Analysis 5: Comparison of both cities based on Listings data
Comparison and analysis of the 'listings.csv' file for both Boston and Seattle Airbnb data for the following information:

### 1. Variations in Price based on Neighborhoods in Boston and Seattle
  <img src= "https://github.com/battalwara/battalwar_ankeeta_spring2017/blob/master/final/analysis/analysis-5/Output1.jpg" width=800>
  
#### Conclusion:
- Above Box plots shows variation in prices based on the neighborhoods for Boston and seattle.
- Box plot is more informative as it gives us the median/mean value, as well as the upper and lower whiskers (Scores outside the middle 50% values)
- Here, comparing on median values, we can see that:
    1. In Boston, most expensive areas are Harvard Square, Downtown Crossing, Financial Distict and the cheapest places to rent Airbnbs are Hyde Park and Mattapan
    2. In Seattle, most expensive areas are Fairmount park, Industrial District and the cheapest places to rent Airbnbs are in Holly Park and Olympic Hills.
    
### 2. Using NLTK package to find most common words used in listings for both cities.
