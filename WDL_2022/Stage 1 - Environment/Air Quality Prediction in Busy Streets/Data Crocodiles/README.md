# Executive Summary

# World Data League 2022

## 🎯 Challenge
Air Quality Prediction in Busy Streets by UNStudio

## 👥 Authors
* Diogo Pessoa
* Fábio Lopes
* Francisco Valente
* Júlio Medeiros

## ✨ Introduction
Nowadays, governments and/or institutions try to combat pollution by implementing policies or suggesting measures that can directly or indirectly reduce pollution. Pollution comes mostly from anthropogenic origin: industry; land, sea, or air traffic; production of energy and its usage; and from agriculture. Furthermore, not only does this pollution has huge impacts on environmental sustainability, but also on human health. More precisely, there is scientific evidence of the association between environmental pollution and lung diseases and/or cancers.

In the last decades, high concentration levels of pollutants were found in the city of Amsterdam, namely in their busiest roads (being Stadhouderskade one of the most significant examples). To fight that tendency, some policies have been already implemented to turn the city of Amsterdam into a greener and more sustainable place:

- Banning polluting scooters (at least since 2018) 
- Implementation of low emission zones (at least since 2019)
- Installation of blue-green roofs (at least since 2018) 

As the city aims to be completely emission-free by 2050, policy-makers are greatly focusing their efforts on these kinds of policies. Actually, Amsterdam is already considered one of the greenest cities in the world. Nevertheless, there are still some policies or measures that can be adopted to reduce the level of pollutants. This is where this challenge comes in. Through the development of explainable models for the different pollutants that are observed at Stadhouderskade, we aim to suggest potential measures that can have a positive impact and improve the city’s overall sustainability.

## 🔢 Data 
We used two datasets. We considered the dataset provided by the WDL 2022 Organization with the observed levels of several pollutants over time, as measured by the sensor placed in Stadhouderskade. We also used external publicly available data provided by Open Weather API about weather information related to Amsterdam. Furthermore, we created a new dataset by combining these two datasets, matching them by the date-time values.

## 🧮 Methods and Techniques


First of all, we searched news and literature to get a better understanding of pollution sources and get a first impression of how it could impact the air quality in Stadhouderskade. Second, we extracted new features from the date-times. Third, we performed an extensive exploratory data analysis (EDA). It included the study of missing data, variation of pollutant levels over time at different time scales, and also the correlation between all the features. This EDA was strongly based on visual analysis for an easier and better understanding. Afterward, we computed some prediction models to forecast pollutant concentrations, considering different timespans: 3 months, 1 month, 1 week. For that, using GridSearchCV available in scikit-learn, we performed 10-fold cross-validation to get the best hyperparameters for each prediction model (Random Forest Regressor). It is worth noting that we performed this search for each pollutant and for each timespan. After obtaining the best models, we used them to forecast. We evaluated the predicted values by comparing them with observed values using plots and using a statistical metric (relative root mean squared error). Finally, we explained the predictions of the forecasting models developed for 1-week predictions using SHAP values (SHapley Additive exPlanations). Results show that the pollutants are highly dependent on the hour of the day and also on the time of year, being the months of the autumn/winter the ones with the highest concentrations. Furthermore, we concluded that the policies adopted in the last years are taking effect on the reduction of pollution.

## 💡 Main Insights 
The first thing that we asked ourselves was the following question: How did the pollutant levels vary before COVID-19 and during COVID-19 lockdowns? Additionally to what was expected (lower levels during COVID-19 lockdowns), it was also found a downtrend from 2017/2018 onwards of the pollutant concentrations. This downtrend could be probably explained by a set of green measures that were implemented in Amsterdam in the past few years. Furthermore, due to the pandemic, many companies switch their operation to fully, or hybrid, remote work. This could also  be another factor that contributed to this decrease, even after the lockdowns.

Focusing the analysis only on the data of the last year (March 2021 - March 2022),  we were able to found daily and monthly/seasonal patterns: 1) higher levels of pollutants during the working days when comparing to weekends; 2) higher levels of pollutants during the autumn/winter months when comparing to the remaining months/seasons. Another observed pattern was related to the highest levels of pollutants during the rush hours of the day (early morning and evening).

## 🛠️ Product
### Definition
A dashboard that informs about the trends in pollution levels and the reasons for those variations.

### Users
The main users of our product are the decision-makers from Amsterdam Municipality. They can use it to get predictions and insights about pollutant concentrations, in order to apply measures and policies to reduce the pollution levels and, consequently, improve air quality in Stadhouderskade.

### Activities
* Predicts trends in Stadhouderskade’s level of several pollutants. 
* Informs about the reasons for those trends (which features have an impact and how their values impact the pollutant concentrations).

### Output
Indication of when the air will achieve higher levels of pollutant particles, inform about the reasons that lead to the increased concentrations in each case, and suggest measures to counteract and prevent those scenarios.

## 🌍 Social Impact Measurement
### Outcome 
To lower the concentration levels of pollutant particles in Stadhouderskade street and, therefore, increase the air quality. Consequently, it will also improve the health conditions and quality of life of Amsterdam’s inhabitants and tourists.

### Impact Metrics 
* Mean concentration of each pollutant over time
* People perception and satisfaction about the lifestyle quality in Stadhouderskade

### Impact Measurement
We estimate that the pollution concentrations will decrease if we limit traffic circulation (especially from vehicles running on fossil fuels) at certain hours of the day, and if we promote afforestation policies to increase the number of trees in the street. Other innovative solutions can also be implemented to this end, such as the implementation of artificial trees (BioUrban).
Therefore, if we use our forecasting models to predict future pollutants’ concentration, we should obtain lower concentration values for the particles in real measurments since our models were developed with data from a time before this measures were implemented.
