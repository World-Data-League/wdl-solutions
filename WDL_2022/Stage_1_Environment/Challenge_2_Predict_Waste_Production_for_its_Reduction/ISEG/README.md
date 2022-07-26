# World Data League 2022

## 🎯 Challenge
Predict Waste Production for its Reduction

## 👥 Authors
* Emil Henricsson Ene
* Marc Behse
* Alessandro Consiglio
* Navid Saffari

## ✨ Introduction (250 words max)
Rapid urbanization is a fact. Cities all across the globe are growing rapidly, and with them waste and pollutions increase as well. In 2016, cities generated a total 
of 2.01 billion tons of solid waste.
For this challenge we try to find trends in waste production for identifying patterns and insights that might help optimize waste processing and, ultimately, reduce 
waste production overall.
The project has been carried out using Austin, Texas, as the subject of study, but we hope the results may be applied to the general case as well.


## 🔢 Data (250 words max)
We have used three datasets:
1. Waste-data https://data.austintexas.gov/Utilities-and-City-Services/Waste-Collection-Diversion-Report-daily-/mbnu-4wq9
  Records waste-loads in pounds by date and time. Data is categorized by type of waste, where it is dropped off and the number of the route.
  This is quite nice data but unfortuanntley many missing values. More available data generally means better models and better predictions, so it could be improved in
  that way.

2. Population data https://www.austintexas.gov/sites/default/files/files/Planning/Demographics/population_history_pub.pdf
  Total poluation per year and annual growth rate. 
  Needs to be updated for recent years, we googled to find values for most recent years.
  
3. Austin weather data https://www.kaggle.com/grubenm/austin-weather 
  Daily weather data for Austin, cointains multiple measures. We used daily temperatures per month to find average monthly temperatures.
  Only contains values for 2013-12 to 27-07. Needs to be updated with more recent values to train models on longer time periods.

## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.
1. Exploratory/Descriptive analysis:
  This is where we explored the data to understand what we were working with. In this stage we transformed the data, for example from the date and time into summarized 
  monthly observations. We also performed statistcal tests to find indicators of how 'well-behaved' data was. We also plotted the data over time to find patterns such 
  as 'Seasonality' and other underlying patterns that are difficult to see otherwise.

2. Algorithms for forecasts:
  This is where we built the actual models. For the Vector Autoregressive(VAR) model, we built it to make predictions of future waste production based on information 
  from previous waste- and temperature data. The model did not make accurate predictions when given a test set, however it did make predictions that aligned with 
  the patterns of the actual data. For the ARIMA (Auto Regressive Integrated Moving Average) we built the model using an auto_arima function that automatically 
  calculated the best parameters for the ARIMA (p,d,q) (P,D,Q) model, in our specific case we decided to use a seasonality P=12. Also a Naive Seasonal method have
  been used to compare the quality of the two models since the serie seems affected by seasonality. Finally, we also used a Prophet model based on an additive model to
  make a out of sample predictions since the data showed yearly seasonality.
  

## 💡 Main Insights (300 words max)
Main insights from these anlyzes are to take advantage of the strong seasonality of the data shown in several models and decompositions presented. If the operational 
management can anticipate and plan for heavy- and easy waste production resources can be used more efficiently and waste processing can happen smoothly.

## 🛠️ Product
### Definition
A schedule to reorganize the collection of the garbage during differents peiods of the year.

### Users
Municipality of Austin together with operational management of waste processing company.

### Activities
Predicts when waste production will be heavy.

### Output
Calendar showing what times of the year you can expect heavy- and low waste production.

## 🌍 Social Impact Measurement
### Outcome
We hope that this product will increase efficiency in waste management. Both in resources used (employees, garbage trucks needed, etc) and in effective waste 
processing. So that processing can happen correctly, meaning that landfills and recycling stations don't get too overloaded to the point that they fail to handel the 
waste properly.

### Impact Metrics
* Monthly garbage production per capita.
* Number of trucks in operations.
* Average accumulation of garbage in different load sites.

### Impact Measurement
Based on proxy products: Waste management plans are essential in the projection towards a circular economy and a good waste management plan can reduce improper waste handling by up to 20%.
