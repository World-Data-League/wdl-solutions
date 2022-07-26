# World Data League 2022

## 🎯 Challenge
Predict Waste Production for its Reduction 🌏🗑♻

## 👥 Authors
* Natascia Caria
* Claudia Cozzolino
* Alfredo Petrella

## ✨ Introduction
The City of Austin is engaged in a very challenging goal: to cut garbage production so that by 2040 there will be a 90% reduction in the amount of trash sent to landfills. In fact, their idea is to focus not only on recycling, but on the fact that what is trash to one person today could be another person's treasure tomorrow. As the population continues to grow, the goal becomes more and more difficult. That is why we want to help Austin find trends in garbage production, see if its management can be optimized by forecasting that same production from their precious historical data.

## 🔢 Data
We mainly worked with the Austin waste collection dataset (originally provided). In addition we also exploited:

* [Meteostat](https://meteostat.net/), which provides a Python library to simple access to open weather and climate data using Pandas.

* Austin Open Street Map file for topological insights (freely available [here](https://download.bbbike.org/osm/bbbike/Austin/Austin.osm.pbf))

Although the time series relating to waste collection in Austin are very rich, it would be very useful to include among the features the number of public bins or door racks assigned to each collection route. This, or a high-resolution estimate of population density, would allow to analyze collection route efficiency with greater precision.

## 🧮 Methods and Techniques
Our main approach has been to look for patterns and trends from data analysis, trying to weave together different data resources. We invested a lot of effort in exploring data analysis by seeking validation of our hypotheses with graphical visualization.
With the aim of predicting the garbage load, we attempted to model the time series of interest with different AutoRegressive Integrated Moving Average (ARIMA) models, also trying with different granularities, training sizes and collection type aggregations. The best performing models have then been integrated adding exogenous weather variables and refined to improve their prediction performance.

## 💡 Main Insights
Exploring the available datasets, none of our firstly supposed correlations resulted to be significant: both weather conditions and urban topology features seem not to be associated with waste production. However, quite precise garbage load forecasting was revealed to be possible even with a simple ARIMA model, suggesting the presence of informative patterns in the collection time series.
In addition, analyzing the mean collection frequency and load for each route, evidence of non-optimal collection schedules are visible (higher frequency and lower weight). 

## 🛠️ Product
### Definition
Waste load forecaster 
### Users
Specialized personnel managing collection schedules and trucks
### Activities
* Predict next month daily waste loads
* Help optimize collection schedule postponing/anticipating garbage collection according to forecasted loads.

### Output
Total or single stream/route specific waste load per day for the next month.

## 🌍 Social Impact Measurement
### Outcome
Predict next month daily waste loads, helping optimize collection schedule and consequently maintain an efficient collection service while reducing its impact on the environment.
### Impact Metrics
Number of days the collection can be postponed
Number of collections the could be skipped

### Impact Measurement
At the current stage of work, we are not yet able to quantitatively assess the impact of our product. 
