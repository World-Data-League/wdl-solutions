# World Data League 2022

## 🎯 Challenge
Air Quality Prediction in Busy Streets

## 👥 Authors
Catarina Bento
Cátia Correia
José Luís Mourão
Lúcia Moreira
Pedro Fernandes

## ✨ Introduction (250 words max)

The challenge tackled by our team concerns the air quality of Stadhouderskade, a street in Amsterdam considered one of the most
polluted in the city. Main sources of pollution are road traffic (Stadhouderskade faces heavy traffic congestion, since it's located
in the city centre) and industry. For that reason, people report feeling the effects of the bad air quality when spending large amounts of time in Stadhouderskade (such as coughing), affecting more the elderly and young children.
As such, people are expectedly not attracted to the thought of spending more time than the strict necessary.  (Reference 1)
Death rates attributed to air quality pollution have decreased in the Netherlands between 1990 and 2014 (approximately 45%), but plateaued in 2014 (References 2 & 3), which brings a renewed need to protect the quality of the air, not only in Stadhouderskade, but as a whole.

References:
(1) https://www.iqair.com/netherlands/north-holland/amsterdam
(2) https://ourworldindata.org/grapher/share-deaths-air-pollution?tab=chart&region=Europe&country=~NLD
(3) https://ourworldindata.org/grapher/air-pollution-deaths-country?tab=chart&country=~NLD

## 🔢 Data (250 words max)

The primary data used to analyze the problem was provided by WDL in a .csv file, containing the measures of 8 different pollutants in Stadhouderskade between 2014/01/01 and 2022/02/16.
The dataset consisted of an unique ID for each measurement of the 8 pollutants in an hour.
During the initial phase of our assessment of the problem, we read papers published about this issue and a key assumption that all had in common is that air quality is intrinsically
linked to the weather. For example, a strong wind will direct the pollutant particles to another place; the rain washes away the pollutants to the earth.
We also restricted our predictions to the most studied pollutants: PM2.5, PM10 and NO2.
Regarding the temporal data, we engineered this variable to create new variables like season, period of day and weekend.

## 🧮 Methods and Techniques (250 words max)

We conducted exploratory analysis to get initial insights: boxplots, pivot tables.
We also analyzed the time series, looking for stationarity (all hypothesis tests showed that our time series were stationary), trends, seasonality (the data presented has strong seasonality by hour of the day and months, for example).
As for prediction, we applied models like SARIMA, Holt-Winters and LightGBM. LightGBM was the best performing model, for both hourly and daily predictions.

## 💡 Main Insights (300 words max)

We found out that air pollution seems to be less pronounced during the hotter seasons (summer and spring), which validates the fact that weather has a strong influence in the overall levels of pollution.
Regarding the weather parameters (rain, temperature, pressure and wind), we see that the pollutants have the same general behavior when we explore correlation between the values of pollution and the weather conditions.
We also found that the levels of pollution have a strong seasonality throughout the day, week and months.


## 🛠️ Product
### Definition

Dashboard that classifies the predictions obtained by the models in air pollution bands defined by official studies and measurements.

### Users

Policy makers can use the dashboard to take decisions in order to curb air pollution.
For example, traffic limitation, incentives to the public to use more green modes of transportation as well as the improvement of the infrastructures (equipments)
for those modes of transportation, creation of public activities (partnering with local businesses) on Stadhouderskade on days with lower levels of air pollution 
so that Stadhouderskade is presented as a good lifestyle place where people can spend more time.
The dashboard can also be used to assess the impact of measures taken by comparison with the historical data provided.

### Activities

Predicts the air quality level for a given hour of the day/mean air quality level of the day for each pollutant.

### Output

The dashboard would take the form of a greenlight with more colours (one for each band of air pollution level), based on the values predicted.
The reference for the values for NO2, PM2.5 and PM10 can be found here: https://qualar.apambiente.pt/node/metodo-calculo-indices
We include some examples of the dashboard in the jupyter notebook.


## 🌍 Social Impact Measurement

We expect that our product leads to a lifestyle change regarding Stadhouderskade through the implementation of data-driven decisions by the policy makers.
Instead of just a street to pass through, we intend that it can be transformed in a more vibrant, healthy public space
where people won't have to worry about any side effects regarding the air pollution. 
Along with a "revival" of the way people face Stadhouderskade, this can lead to a more sustainable mindset, as well as have a good economic impact on the businesses housed on the street itself.

### Impact Metrics

Comparison air pollution levels before and after deployment of the dashboard and decisions taken based on the information provided:

•	Number of days with acceptable/unacceptable levels.
•	Percentage of air pollution decrease after deployment of our product.


### Impact Measurement

As our intention is to create a more public friendly street (through the use of our final product, the dashboard),
we refer to Vision Zero, a project created in New York City, and the changes made by Mayor Bloomberg. With a focus on
reducing traffic-related incidents and creating pedestrian safe zones in some of New York's most congested
blocks, they were able to see the following changes:

•	Decrease of traffic-related accidents.
•	Stimulus to the local economy.
•	Increase of green zones (trees and plants), which help fight air pollution.
•	Creation of cultural hotspots that attract the population to those areas.