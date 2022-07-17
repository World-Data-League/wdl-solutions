# World Data League 2022

## 🎯 Challenge
*Predicting a safety score for women in Costa Rica*

## Team Name
Bayesciamella

## 👥 Authors

* Claudia Cozzolino
* Alfredo Petrella
* Natascia Caria

## ✨ Introduction (250 words max)

Violence against women in cities, specifically in public spaces, has become an increasingly worrying public issue. Sexual harassment and other forms of violence against women and girls in public spaces are present in every country, in rural areas as well as cities, and even in online spaces.
According to 2019 #MeToo Study (RESEARCH ON SEXUAL HARASSMENT AND ASSAULT) worldwide, nearly 2 women out of 3 have been subjected to street harassment. Assuming this rate also holds for Costa Rica, approximately one million women have been, at least once, victims of this abuse. However, only in 2020 this country declared street sexual harassment as a crime. Making cities and public spaces safe for all women and girls is then a matter of citizens’ security and a duty of all of us.

## 🔢 Data (250 words max)

We mainly used the data provided by Urbanalytica, in particular:
* Crime records for Costa Rica from 2010 to 2022
* Street Harassement reported in 2021 in Costa Rica
* Demographic, crime-rate data and Social Development Index 2017 at the district level
* Google ratings and reviews of parks in Costa Rica and of transit stations in San Jose

As external resources, we got data from [National Institute of Stastistics and Census](https://www.inec.cr/):
* Population projected according to province, canton, district and sex in the period 2011-2025

In addition, as external resources, we exploited Open Street Map to get:
* Information on lighted streets
* Urban network properties (graph density)

The main problem in manipulating the data provided for the challenge was the lack of keys to match information from different data sources.
Mainly the problem was the lack of uniformity in writing the names of provinces, cantons, districts, which are reported in a different format among the various datasets.

In addition, having more time-dependent data would have been useful. Socio-economic data, albeit at district level, are only provided for the year 2017. This could have helped in the quarterly or yearly prediction of the women safety index.


## 🧮 Methods and Techniques (250 words max)

To accomplish the request of predicting the women's security score on a quarterly/annual basis, a Random Forest model was implemented on multiple time series at the district level. In practice, instead of training a different model for each district in Costa Rica (almost 500!), a single Random Forest was trained by concatenating the time series of the districts and using lag and differences in crimes as features.

To uncover the impact of external factors on criminality, regression models (Linear and again Random Forest) are employed.
The models have been fed with socio-economic indexes, data on street lighting, perception of danger from reviews, and the structure of the urban network (graph density). After training the models to predict the crime rate for each district, SHAP features importance techniques are exploited to draw the final conclusions. The advantage of using linear regression is that we can define the security index as a simple linear combination of external factors. However, since the linearity assumptions for the model are not met, the estimations are not reliable. On the other hand, by combining the Random Forest model with SHAPley Additive exPlanations, we obtain a more accurate and at the same time still interpretable prediction.


## 💡 Main Insights (300 words max)

Looking at the crime time series' trends, we firstly observed a drastic decrease in reported crimes since October 2020, probably due to COVID-19 pandemic restriction measures. This makes us believe that the data available for street harassments, covering the year 2021, are not really representative of the problem in Costa Rica.

Our regression models confirmed the association between criminality and population factors already proved by other works.
A relevant finding is the positive association of crime rate with the perception of danger, extracted from reviews.
On the other hand, street lighting revealed to be not significant, probably as a consequence of the limited lighting data reported.
Another meaningful insight regards the graph density impact: the level of interconnection which characterizes each district in positively correlated with the safety index: in other words, an higher probability of finding isolated streets determines an higher crimes rate.


## 🛠️ Product
### Definition

A "what-if" tool to simulate the effects of urban interventions on women's security index for each district in Costa Rica.

### Users

Policy makers can use the "what-if" tool to test and quantify how different urban planning solutions impact on women security.

### Activities

* Prediction of the increase in security as an effect of urban changes at district level
* Cost-effectiveness analysis as decision support in an urban planning phase to understand which interventions should be preferred

### Output

Policy makers can use the tool to test the effectiveness of different intervention solutions to make public environments safer: "What if we increase the number of street lamps in Carmen district in the province and canton of San José?"

## 🌍 Social Impact Measurement
### Outcome

The root cause of criminality lies significantly in socio-economic factors, such as uneven sex ratio, educational level, women employment rate or political representation. However, these variables cannot be easily manipulated. That is why we propose a simple solution to mitigate gender violence by modifying urban design for a more inclusive and safe environment.


### Impact Metrics

* Number of crimes per 10k inhabitants
* Percentage of negative reviews expressing fear of danger
* Percentage of roads with adequate lighting

### Impact Measurement

* Several works in literature find evidence that urban planning and design improve the liveability of cities and towns.
For instance, in [1](Chalfin, A., Hansen, B., Lerner, J. et al. Reducing Crime Through Environmental Design: Evidence from a Randomized Experiment of Street Lighting in New York City), with a randomized experiment in NYC, evidence is given of a 35% reduction in outdoor, nighttime index crimes.
According to the available data, more than 57% of the crimes recorded in Costa Rica occurred at night. Although we cannot say whether outdoors or not, even if these were only 30% of the total, this would result in a reduction in the crime index of 10%.
