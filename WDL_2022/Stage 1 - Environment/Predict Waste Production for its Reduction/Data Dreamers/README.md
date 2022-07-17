# World Data League 2022

## 🎯 Challenge
*Predict Waste Production for its Reduction*

## 👥 Authors
* Sourabh Hujare
* Nikhil Kulkarni
* Roney Mathew
* Luckshan Sivakumar

## ✨ Introduction (250 words max)

* Austin is the capital city of Texas state with a population of approx 960k. More than 50% of this population is employed earning at least $ 40k annually.  These numbers give us a good enough idea about the spending potential of the Austinites. A good enough spending potential would directly justify the corresponding waste generation.*

* The Waste collection data provided by the Austin authorities show that between 2005 to 2020 around 3 Million Tons of solid waste was generated and the yearly trends show that solid waste will only increase with time. The rate of increase could be as high as 200 US Tons/year, ignoring any drastic events that might occur (eg. pandemics etc.).*

* With this rate of increase, it makes sense to have a fairly reliable method of calculating the expected waste generated and keep the collection, separation & dumping facilities up to speed with it. At the same time it would also be valuable to identify some insights from the historical data of waste generation to find the major causes of waste and eventually draw solutions from them to reduce the waste generated. *



## 🔢 Data (250 words max)

* The main dataset that was used was the one provided by the city of Austin with daily reports of waste collection. It contains logs of the amount and type of waste collected on various routes and dumped at different dumpsites. The dataset provides great preliminary insights into the waste collection trends.
The dataset would be very much enriched if the location data of the routes were included in it or an additional supplement dataset with more detailed guides to the routes was available. In such a scenario, a location based optimization could be examined.
We used events/festivals data and income data from online websites referenced in Notebook. *

## 🧮 Methods and Techniques (250 words max)

* We used the open-source forecasting package called “Prophet”. Prophet uses a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. Mathematically, Prophet uses curve fitting to calculate the forecasts. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.
We obtained forecasting results with a MAPE (Mean Average Percentage Error) metric around 5%, which indicates a good performance of the model. The results show an increasing trend of waste generation as was expected and it also shows yearly seasonality that makes sense. *

## 💡 Main Insights (300 words max)
 
* 1) Our model identifies that some events contribute to increasing solid waste generation in Austin, specially the SXSW event.
2) From our explorative analysis we see that the number of trips made by waste collection trucks has the potential to be reduced drastically.
3) Waste collection of type ‘Yard Trimmings' peaks in March. This might be because the leftover budget of Waste collection authorities for every financial year is used for “Yard Trimming” purposes.
4) We see that the real median income of households has a direct effect on solid waste generation. *
 

## 🛠️ Product
### Definition

** Product 1 : An application that assists in waste collection by planning collection trips along different routes based on the forecasts generated for each route and Load type. The forecasts could also assist in budget planning for waste collection and disposal**

** Product 2 : A public dashboard which shows a solid waste generation forecast for upcoming big events to increase public awareness and to assist waste collection.**

Product 1 will be referred to as an Application and Product 2 will be referred to as a Dashboard from now on.

### Users

Waste collection facilities would be primary users of the application. Waste collection authorities can use the application to plan waste collection trips in Austin. They can use the dashboard additionally to plan their staffing, budget & collections during special events.

Government authorities can use the dashboard to plan the awareness activities for big events happening in Austin.

Public can use the dashboard to become more aware of the waste generated in famous events.

### Activities

* The application suggests when to dispatch a collection truck on a specific route and for a specific load type based on the threshold values reached using our forecasting models.

* After each waste collection trip, the load weight collected can be input into the application for that specific trip so as to dynamically improve the schedules for the rest of the year and thus this product can also be used as a data logger. Thus its a “2 in 1” - a data logger and a smart scheduler that learns from new data and adapts quickly to changing trends.

* The application makes route planning/scheduling efficient by changing it from a one-time yearly manual activity to dynamic automated activity.

* Dashboard shows prediction of the amount and type of waste that different upcoming Events generate.

### Output

The application product outputs a schedule of allocating trucks to specific routes for collecting a specific type of waste. 

The Dashboard product outputs the prediction of load weight and load type for different events happening in Austin in the form of bar/pie charts.

## 🌍 Social Impact Measurement
### Outcome

To increase efficiency of waste collection by dispatching trucks only when needed and thus decreasing the number of unnecessary trips that contribute to increasing air pollution and costs.

To prepare the local authorities and make the public aware of the huge wastes that occur during events.

The dashboard can encourage new solutions from new waste management organizations who identify potential business opportunities from data. 

### Impact Metrics

* Number of collection trips in a year.
* Costs saved through better planning of trips.
* Average capacity utilization of trucks.
* Number of trucks added to the fleet per year.
* The Energy and Carbon Footprint of Waste Collection Fleet
* Amount of waste generated in events.
* Number of new waste separation and recycling facilities.

### Impact Measurement

* Based on our Exploratory analysis : There is potential to reduce approx 6000 trips in a year for garbage collection and recycling single stream. Similar reductions are possible in the number of trips for all the other Load Types. (Refer to the visualizations section in the Notebook)
* Similar optimization studies have shown huge potential of savings for the civic authorities in addition to the qualitative impacts of less traffic disruption, less vehicle driver fatigue and less pollution.