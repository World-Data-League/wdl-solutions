# World Data League 2022


## 🎯 Challenge

*Predict Waste Production for its Reduction*

## 👥 Authors

* Magdalena Brach
* Anant Pingle
* Karim Anwar

## ✨ Introduction (250 words max)

*According to the official website of the city of Austin there exist many challenges related to waste collection. Since February 2022, Austin Resource Recovery (ARR) suspended large brush and bulk collection due to staffing shortages. In 2021 only, ARR collected 63,030 tons of recycling, 53,455 tons of compost and 138,955 tons of trash through curbside collections from 209,981 single-family homes and multifamily properties with four units or fewer. ARR's goal is to reach zero waste by 2040, which means reducing the amount of trash sent to landfills by 90 percent. These examples are only the tip of the iceberg. Our analysis goal is to find patterns in waste collection and predict the upcoming waste loads which would allow to better plan collections in the future. We want to help municipality in identifying the main areas regarding waste collection in order to focus their efforts of increasing the awareness of personal waste management in these parts of the city.*

## 🔢 Data (250 words max)

*We used the Austin Resource Recovery waste collection and diversity dataset which was provided as the main data set by the WDL. While the main dataset was enough for us to predict the amount of waste in a short horizon in the future, we think it did not have enough information for us to predict other trends. For example, including which areas of the city the trash was collected from would help us in understanding which areas the municipality should we focus on (either by providing more bins or by sending bigger trucks to collect this garbage). Including the capacity of trucks, count of personnel on duty can help us analyse if resources are efficiently allocated to different locations. Including the weather data for each of the day can help us understand if the weather plays a role in the garbage collection. For example, we can understand if a different way of collecting garbage is needed during rainy/windy days. We could have also used the Census Data of the city of Austin to explore if number of people in a given district of the city has a significant impact on the waste collected. Due to time constraint we couldn't explore all the datasets we wanted to include.*

## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.

*We have decided to use Prophet library for modeling because it allows fast, automated forecasting that can be easily tuned. It is not the most advanced procedure for forecasting time series, but we wanted to use something relatively simple and easy to explain. Moreover, Prophet is robust to missing data and shifts in the trend, and typically handles outliers well. This allows us to save some time on dealing with outliers and sporadic missing values that we would take care of if we had more time disponible. 

We used cross-validation for tuning hyperparameters of the models. For that we created a grid with the values that allow to explore different models with quite ‘conservative’ parameters. We are aware that more extensive hyperparameters optimization would be desired. However, due to time constraint we limited our search to the one mentioned above. *

## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.

We discovered that our 'best' models for RECYCLING - SINGLE STREAM, BRUSH, SWEEPING AND TIRES didn't include public holidays, so probably the holiday didn't have a huge impact on waste collection of these load types.
RECYCLING - SINGLE STREAM: linear increasing trend since 2003 which mean that the residents are going towards recycling (especially that is one of the top load types)
SWEEPING: linear deacreasing trend, which means that less and less trash is collected directly from the streets. These could mean that residents are littering less
BRUSH: the trend was raising quickly until 2010 and then stabilised for the next years, the lowest values are for winter time
TIRES: more change point in the trend that is increaing slowly until year 2012, then decreasing until 2017 and the raising quite quickly in the following years, this can be related to recently increasing number of cars in the city
BULK: linear increasing trend since late 2004, could be explained with the increase of the population size in the city and their needs.
RECLED METAL: From the years 2004 to 2006 there were high values with a sharp decrease in 2007 then stabilisation in the following years. There in weak yearly seasonality with the highest value in January.
MIXED LITTER: Decreasing trend from 2004 until 2009 then it stabilizes until 2013 then with another sharp increase in the following years. No clear pattern in yearly seasonality.
GARBAGE COLLECTIONS: The trend is relatively stable. Relatively weak yearly seasonality with the smallest value in Feburary and September.
ORGANICS: This load_type started to be collected in 2018 and has an increasing trend, with a peak in March and lowest values in August.
LITTER: A lot of change points in the trends with a peak for 2012. Yearly seasonality with the highest values for March.
DEAD ANIMAL: Decreasig trend with a charpness in 2007 with a rapid decrease until 2012, then followed with a more steady decrease in the trend. For the yearly seasnality the highest values are in November and the lowest are in Februray.



## 🛠️ Product
### Definition
A dashboard that assists in waste management and planning

### Users
Austin municipality waste management team use the dashboard during their work to better plan the waste collection.

### Activities
* Predicts the waste by load type
* Gives an overview of the historical data and trends

### Output

Forecast of the waste load in the next 30 days and it's share by load type.
Impact metrics monitoring regarding zero wasteby 2040 goal.

## 🌍 Social Impact Measurement
### Outcome
To optimize waste collection across the different load types and respond quickly to the changes. To educate residents to move towards more efficient and eco-friendly waste collection.

### Impact Metrics
* Average Daily/Weekly/Monthly Waste Weight by Load Type
* Percentage of reusable/recycled material (Diversion Rate)
* Segregation rate

### Impact Measurement
We will focus according to each route that designates different areas in Austin to find using our forecast which type of garbage collection has to be focused on to achieve their goal for their next fiscal (year/month) in each area.
We estimate taht Austin can increase their city waste diversion rate by 10pp. in the next 5 years, this conclusion is based on the on the results observed on the twin city of Austin which is Phoenix.
Due to the expansion of its community and educational outreach on the five pillars--reduce, reuse, recycle, reconsider and reimagine--the city contributed in increasing awareness of the importance of waste diversion and management.