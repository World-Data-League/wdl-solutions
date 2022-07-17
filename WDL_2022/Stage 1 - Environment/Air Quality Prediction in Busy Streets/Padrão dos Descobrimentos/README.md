
# World Data League 2022

## 🎯 Challenge
Air Quality Prediction in Busy Streets

## 👥 Authors
* Alexandra Serras
* Diogo Baptista
* Marta Seca

## ✨ Introduction

Increasing air quality is of the utmost urgency since air pollution affects communities in low-, middle-, and high-income countries. In 2016, it was estimated that this major environmental health issue [caused 4.2 million premature deaths](https://www.who.int/news-room/fact-sheets/detail/ambient-%28outdoor%29-air-quality-and-health) worldwide per year. This mortality rate is mostly due to exposure to fine particulate matter (PM2.5), which can cause cardiovascular and respiratory diseases, as well as cancers.

In Amsterdam, where the number of bikes is four times the number of cars, dirty air is the third greatest health risk for its citizens. The main culprits are nitrogen dioxide (NO2) and particulate matter (PM10 and PM2.5). Amsterdam’s contaminated air [reduces the average life expectancy](https://www.amsterdam.nl/en/policy/sustainability/clean-air/) of the city by just over a year. In the Netherlands, pollution sensors are divided into two main categories: traffic and background stations, where Stadhouderskade street - one of the busiest streets in Amsterdam - is qualified as the former. Amongst its peers, this street scores as one of the best, however, when compared to background stations, it performs poorly.

This solution aims to analyze and propose an effective way to predict air pollution in this street, so that the municipality can use this information to increase air quality (competing with values from background stations) by turning the street into a place where people enjoy staying, rather than just transiting through.

## 🔢 Data
For this analysis we used air quality measurements from 2014 to 2022 on Stadhouderskade street provided by World Data League (WDL). The dataset contains hourly concentration values (μ/m3) for eight different components displayed in Table 1.

##### Table 1: Components description
| Component ID | Component Name                            |
|--------------|-------------------------------------------|
| FN           | Nitrogen monofluoride                     |
| PM25         | Particles of a diameter of 2.5 μm or less |
| PM10         | Particles of a diameter of 10 μm or less  |
| NO           | Nitric oxide                              |
| NO2          | Nitrogen dioxide                          |
| C7H8         | Cycloheptatriene                          |
| C6H6         | Benzene                                   |
| C8H10        | Ethylbenzene                              |


To see how Stadhouderskade compares to other major locations in Amsterdam, we included [air quality data from 2018 to 2021 for NO, NO2, PM10 and PM25](https://data.rivm.nl/data/luchtmeetnet/) made available by the National Institute of Public Health and the Environment. This dataset also depicts the type of station where the elements are measured (traffic vs background) as well as its location.

To complement our analysis, we also added daily weather data like temperature, precipitation and weed speed from 2019 to 2022 containing provided by [Meteostat](https://meteostat.net/en/)

We used [holidays](https://pypi.org/project/holidays/), a python package, to have Netherlands' main holidays and we also built a dictionary with the seasons of the year.

In order to develop a model that predicts daily concentration values, we had to transform our data from hourly measurements to daily means.

## 🧮 Methods and Techniques

Since the provided data only had the measured hourly concentration for the components mentioned above, we converted the grain to a daily basis and added date features (season, holiday, time of the day) to allow a deeper exploratory analysis and more accurate choice of variables for the predictive model.

The analysis explored stationarity, moving averages (MA) and lagged values of the time series we were provided with.
* Stationarity: we applied the Augmented Dickey-Fuller to confirm the data was stationary;
* Moving averages: from our analysis we concluded we would benefit from having the moving average of two days as an input to the model;
* Lagged values: it looked like we would benefit from having one lagged feature.

We used correlation matrices to verify which component affects which - from this analysis, where we correlated with moving averages, weather, dates and lagged features, we saw that it would be beneficial to use MA of two days as they were the ones with the highest correlation.

For modeling the time series, we dropped duplicates and missing values and applied [XGBoost](https://arxiv.org/abs/1603.02754) for Regression where the parameters of the estimator are optimized by cross-validated grid-search over a parameter grid. We used the estimator to forecast the daily mean for each of the pollutants and developed a system that, considering this predicted value, triggers a warning each time the average concentration for a given component goes beyond the safety threshold.

## 💡 Main Insights

Since the COVID-19 pandemic started around February 2020, we divided part of the exploratory data analysis in two sets: before Covid (from February 2019 to February 2020) and after Covid (from February 2021 to February 2022). An initial analysis of the PM2.5 element showed an outlier (huge concentration of this pollutant) that we found out was related with New Year festivities - and also that before Covid times, this day had a bigger impact than in the current year.

In general, after 2020, concentration values for PM2.5 have decreased, with Winter being the season where we notice the biggest change.

Another well known festivity for the Dutch is the King's day, held on April 27th. However, this day does not seem to have a significant impact on PM2.5 concentration values in Stadehouderskade.

We have also noticed that the summer is typically a season when the concentration of the PM2.5 particle is at its lowest point, this can be attributed to the weather as sunny days encourage people to leave their car in the garage and be more outside. On the other hand, winter seems to be the season that has the most PM2.5 concentration in the air.

Another interesting point is the influence of the wind speed on some components, given the correlation matrix we generated, this feature negatively impacts some pollutants (one of which is the PM2.5), this is due to the fact that the wind speed is blowing the components away from the street.

## 🛠️ Product
### Definition
An air quality forecasting tool to assist the municipality in improving its citizens’ health.

### Users
The users of our dashboard would be Amsterdam's City Council who would monitor the indicators closely for the following day and communicate the population the healthier streets to roam.

### Activities
The predictive model forecasts the mean value for each pollutant for the next day. The alert system verifies if the value is above the recommended threshold - if it is, it triggers a warning.

### Output
Our final product would be the dashboard shown in the Submission Jupyter Notebook (Figure 1). It shows a line plot for each of the components and shows a red or green marker, according to the predicted value. This way, Amsterdam’s city council is able to take action based on the available forecast.  

Additionally, this dashboard and alerts can be used to bring awareness to the need of enacting long term policies to reduce air pollution.


## 🌍 Social Impact Measurement
### Outcome
Our long-term results aim to improve the health of the people that use Stadhouderskade street. This goal can be achieved by decreasing the number of people that are exposed to these air pollutants when its values are above the limit that is considered as healthy.

### Impact Metrics
* Number of pedestrians walking the street during a day considered as unhealthy;
* Number of vehicles on the street during a day considered as unhealthy;
* Percentage of pedestrians on the street wearing breathing masks during a day considered as unhealthy.

### Impact Measurement
Using the model predictions we can ensure that short term pollution reduction policies can be put in place before the critical periods where we have pollution level above the healthy maximum.
It will also help us long term to monitor the effectiveness of long term pollution reduction policies.