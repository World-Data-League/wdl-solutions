# World Data League 2022

## 🎯 Challenge
#### *Predict Waste Production for its Reduction* (UrbanAI)

## 👥 Authors
* Bruno Alho
* Frederico Rodrigues
* Miguel Zina

## ✨ Introduction

*With world's population escalation, one of the major concerns within high density cities is their generation of environmental pollutants. 
Solid-waste management represents one of the greatest costs to municipal budgets, and given that the projected global waste generation continues to rise, understanding the drivers of it's growth can play a crucial role on improving garbage collection and managent. (https://www.nature.com/articles/502615a)*

*Austin (TX) was the fastest growing metro area of the last decade in the U.S., having its population expanded by a third. The capital of Texas is seen as the next big tech hub in the country and is expected to keep its growth. (https://austonia.com/austin-fastest-growing-metro)*

For this challenge our main purpose was to exlpore the patterns of waste production/collection in the city of Austin as well as the key factors that influence it.

## 🔢 Data

To support our research we have used different sources of information spanning four (4) pivotal areas:
1) *Daily Waste Collection Report for Austin* - a dataset shared by the City of Austin official data portal, containing daily reports of waste collection
2) *Google Trends*  Keyword (Climate Change)- This dataset works as a proof of concept where we can incorporate Google search query data from the population of austin into the Models.
3) *Labour & Unemplyment* - sourced by the US Bureau of Labor Force Statistics, containing historical data of Employment for the city of Austin
4) *Issued Construction Permits* - also shared by the City of Austin official data portal, with historical data of issued construction permits both Residential and Commecercial 
5) *Weather History for Austin*

For our analysis, the team decided to set a particular time-frame that didn't include the recent Covid-19 pandemic. 
This decision was based on our findings regarding abrupt differences during lockdown periods ant the fact that our main dataset didn't include the most recent events (last collection events recorded around mid-2021).

It was settled that the time frame to use would be the last decade [2010, 2020[.

Additionally, we wanted to include as many datasets as we could in our forecasting, because even if we as a group are not able to gather the most recent datasets we believe that in Austin, they will not have those limitations so we tried to provide as comprehensive of an approach as possible.


## 🧮 Methods and Techniques

• Variable Selection - We looked for Correlation between variables (Pearson).
• Modelling - we focused on a main model of SARIMA, we understood the TimeSeries Properties (Stationarity and Trend tested by the Augmented Dickey-Fuller Test, ACF and PACF to check for seasonality and the autoregressive and moving average parts of the SARIMA).
Finaly, we tunned with a GridSearch and finally compared the results of the model against the performance of 2 more common models (Linear Regression and Mean Method) and a differentiating model (Facebook's Prophet).
• Evaluation - Focused on two main metrics for the Forecasting - RMSE and MAPE. For a more macro forecast we focused more on MAPE as it is the easiest to understand. However, for the daily forecast with the event of existing days with 0 garbage recovery the MAPE is not a viable metric so the RMSE is the one chosen.

For the Results:
Monthly Forecasting: we suggest SARIMA for the long term analysis as with the addition of the coefficient we can successfully predict the “future” as well as the causes and the impact that each variable (coefficients) has in the evolution of the Time Series.

Daily Forecasting: Although SARIMA is the model that better explains the alterations. We believe that the managers should follow take the forecast of Prophet into consideration as it is the best performing and daily analysis is less about what causes the changes as is about the what measures could we take into place.


## 💡 Main Insights

From our early exploratory analysis, some hypothesis were confirmed by data and other interesting facts were spotted.
- Monday is the day of the week with the greatest collected volume (as expected)
- Weekend's have  considerably less collections and collected volume (as expected)
- Weekdays present the biggest average waste collected, followed by weekends and then holidays (as expected)
- Garbage collection is the main Load Type (total volume)
- TDS Landfill is the main Drop-off site (total volume and number of drops)
- Between 10 a.m and 3 p.m. are the most common hours of collection

From the forecasting:
-On the daily forecast, the weather and weekend/variables have the biggest impact
- On the montlhy forecast, the new issued construction permits and employment rates have a significant impact


## 🛠️ Product
### Definition
Dashboard for collection route control

### Users
Route Planners and Waste Managers would benefit the most of using this dashboard to control and predict how to allocate their resources for the coming days/ weeks.


### Activities
* Predicts the changes in waste production in short and medium term
* Suggests which areas/routes need to be reinforced or diminished

### Output
Location of route to be improved and expected load weight.


## 🌍 Social Impact Measurement
### Outcome
The long-term goal is to maximize the efficiency of each route, assuring that there is no waste left to be collected on the streets.
Additionally it will also be possible to better distribute the dropp-offs among the different sites.

### Impact Metrics
Example:
* Average Collection Time
* Average Distance covered per Collection
* Total Weight per Drop-off Site

### Impact Measurement
The impact of our product will greatly depend on its usage by the route planners and waste managers, therefore we can only assume that with the correct use of our forecasts there is an opportunity to leverage the resources of the city of Austin to maximize the efficiency of collections.
For example, with our long term forecast it is possible to gauge that an increase in the number of issued permits has a coeffcient of -412.
Using the influence of each variable it will be possible to better determine the impact of a change in the route planning and resource usage.

### Future Work
A dashboard is a good starting point to improve waste management. Nevertheless, we think that the city of Austin can go even further with the appliance of IoT with AI. For instance, it could be employed smart waste beans (with IoT sensors) that would collect information about what type of waste is being disposal, not only would this improve waste collection as it would improve waste disposal and its recycling mechanisms.  AI is recognized by its ability to correct recognize and classify a variety of objects, in that sense the waste picking system would benefit to have such system so it could learn it self and improve to adjust to changing materials streams without any manual intervention.
