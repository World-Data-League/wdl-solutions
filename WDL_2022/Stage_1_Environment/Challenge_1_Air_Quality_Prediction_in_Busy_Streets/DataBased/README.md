# World Data League 2022

## 🎯 Challenge
**Air Quality Prediction in Busy Streets** by UNStudio

## 👥 Authors
* André Luís
* Rui Monteiro
* José Diogo Castro

## ✨ Introduction (250 words max)
This challenge aims to transform Stadhouderskade, a busy street in Amsterdam, into a pleasant place for people to stay and enjoy. This street is the most polluted in the city and it is the one with the most traffic and pedestrian accidents.

According to the [World Health Organization](https://www.who.int/health-topics/air-pollution#tab=tab_1), “**air pollution** is contamination of the indoor or outdoor environment by any chemical, physical or biological agent that modifies the natural characteristics of the atmosphere”. Household combustion devices and motor vehicles are common sources of air pollution, which might be two main causes for the bad air quality in Stadhouderskade. 

It is estimated that 9 out of 10 people worldwide live in places where air quality exceeds WHO guideline limits. As a consequence of high levels of air pollution, people might risk getting diseases like respiratory infections, lung cancer and heart disease. The most health-harmful pollutants are PM2.5 particles that penetrate deep into lung passageways.

The goal of this project is associated with United Nation’s **Sustainable Development Goal 11**, "Sustainable Cities and Communities", more specifically with its target 11.6: **"reduce the adverse per capita environmental impact of cities, including by paying special attention to air quality"** (source: [United Nations Department of Economic and Social Affairs](https://sdgs.un.org/goals/goal11)).


## 🔢 Data (250 words max)

Besides the  [ hourly air quality measurements from 2014 to 2022](https://wdl-data.fra1.digitaloceanspaces.com/unstudio/stadhouderskade_air_quality_2014_to_2022.csv)  on Stadhouderskade street, we used daily weather data provided by [Meteostat](https://meteostat.net/en/place/nl/amsterdam?t=2014-01-01/2022-02-15), as well as some geographic data from the [city open data portal](https://data.amsterdam.nl/) to provide context about the location of this street in the city of Amsterdam.

Regarding improvements to the collected data, it would be more precise to have hourly weather data, instead of daily, and this could be collected by the same sensor that measures the air polutants, as done in [previous work](https://data.cascais.pt/pt-pt/node/253) in the field.

The addition of more explanatory variables should be considered as well, such as data about car traffic and noise levels on Stadhouderskade street.


## 🧮 Methods and Techniques (250 words max)

We started by performing an **Exploratory Data Analysis**, where we analysed the descriptive statistics of each variable, as well as their pairwise relations through scatter plots and correlation values.

Then, we proceeded to the **Data Cleaning** stage in order to inspect the presence of outliers and missing values. Using a Moving Average plot, we understood that some components had unusual/extreme values in the series, for whom we established a maximum threshold based on the EDA. The missing values treatment included a Linear Interpolation procedure for missing observations that were, at most, 1 day apart from a known observation, with the remaining missing values being discarded from our analysis.

Regarding **Feature Engineering**, we derived the [Common Air Quality Index (CAQI)](https://www.airqualitynow.eu/download/CITEAIR-Comparing_Urban_Air_Quality_across_Borders.pdf) from our data, which allows us to have an unified view of the air quality at any given moment, having in consideration three of the measured pollutants: Nitrogen Dioxide (NO2), Particulate Matter 2.5 (PM2.5) and Particulate Matter 10 (PM10).

Next, we moved to the **Modelling** stage, where we followed a traditional time series approach, starting by checking for stationarity and autocorrelation using the Dickey-Fuller test, and further applying an ARIMA model to predict each individual pollutant of the CAQI using the measurements from other pollutants, as well as weather related variables.


## 💡 Main Insights (300 words max)

The main insights derived from our analysis were:
- Geographical data related with the location of outdoor activities in the nearby zones of the Stadhouderskade street showed that **there are no running routes in this street**, and that there is **only one sports park in the vicinity of this road**. 
- The measurements of each pollutant present some **extreme observations**, particularly the Airborne particulate matter (PM2.5 and PM10), as well as Benzene (C6H6), Cycloheptatriene (C7H8) and Ethylbenzene (C8H10), which might indicate this street has **regular traffic congestions**, as these pollutants are mainly emitted by vehicles.
- There is an high correlation between Cycloheptatriene (C7H8) and Ethylbenzene (C8H10), since they are emitted, in general, by the same type of polluters. On the other hand, C8H10 has 9900 missing values. Due to these facts, we **dropped the C8H10 pollutant from our analysis**.
- **6 out of 8 components had their highest median concentration in either 2014 or 2015**, the 2 first years on our analysis. These findings seem great: it might mean Stadhouderskade is already on the right track to decrease the high concentrations of some of these components. However, the impact of the COVID-19 pandemic in the decrease of car traffic might be contributing to these lower values.
- While predicting each pollutant that constitutes CAQI, we noticed that the **wind direction variable was not statistically significant to predict any of the pollutants**. Thus, we dropped it from our analysis.

## 🛠️ Product
### Definition

A dashboard that assists in Air Quality Control

### Users

The population of Amsterdam could check this dashboard with the predictions of Air Quality for the next couple of hours.

The Amsterdam's city council could plan (in advance) which measures needed to be applied if the air became too polluted based on CAQI's thresholds.

### Activities

Predicts the CAQI Air Pollution Index based on the three pollutants that compose it, for a given hour and date.

Suggests when the air is too polluted, according to predefined thresholds.

### Output

The mockup below shows a dashboard example. This would display the predictions for the pollutants' concentrations and suggest measures (e.g. if pollution is 'very high', vulnerable people should be highly recommended to avoid passing on the street).

![Dashboard example](https://assets.new.siemens.com/siemens/assets/api/uuid:e3a6c835-9638-4dee-8352-4d72d38a0423/width:1125/quality:high/cyam-dashboard.jpg)

## 🌍 Social Impact Measurement
### Outcome

- Implement **suggestions to the population if the Air Pollution Levels are "high" or "very high"** - for example, suggest that people with respiratory diseases avoid passing the street in certain times of the day.
- Creation of a **"Low Emission Zone"** where only cars registered after 2011 can circulate in Stadhouderskade, in times of the day where Air Pollution Levels are "high" or "very high".
- **Optimize and add public green spaces** in the vicinity of the street. Less parking lots and more green areas, gardens or parks.
- **Outdoor interactive banners** along the street displaying the amount of air pollutants that were emitted over a certain period, where people could filter and visualize these amounts in real time.


### Impact Metrics

- Average number of pedestrians passing on the street.
- Monthly percentage of "high" or "very high" Air Pollution Levels.
- Monthly number of green space users.


### Impact Measurement

- Based on the model predictions presented in the dashboard, people will be more conscious about walking in Stadhouderskade, which can bring benefits in the long term regarding the decrease of respiratory diseases.
- Based on the example of [Krakow (Poland)](https://www.sciencedirect.com/science/article/pii/S2352146517309158), the implementation of car traffic restrictions will increase the satisfaction with the quality of public space by their users (approximately 80% of customers could become satisfied).