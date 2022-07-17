# World Data League 2022

## 🎯 Challenge
Air Quality Prediction in Busy Streets by UNStudio

## 👥 Authors
* Akshay Punjabi
* Enrico Coluccia
* Pablo Izquierdo Ayala
* Chiara Rucco

## ✨ Introduction (250 words max)

Air pollution is a big issue and proposes a big challenge in our modern world. Not only is a high level of pollution directly linked with climate change, but it is also well documented the negative impact a prolonged exposure to high levels of pollution will have on our health. 
The European Environment Agency (EEA) describes it as a major cause of premature death and disease, and the largest environmental health risk in Europe (cite https://www.eea.europa.eu/themes/air/health-impacts-of-air-pollution) This is also backed by recent articles, some claiming that long term exposure is even linked to heightened autoimmune disease risk (cite
https://www.bmj.com/company/newsroom/long-term-exposure-to-air-pollution-linked-to-heightened-autoimmune-disease-risk/ ).

Within air pollution, some components entail a higher risk than others. For instance, the PM25 (one of the features of the dataset that was provided by WDL) describes the amount of particles that are present in the air that are 2.5micrometers or smaller. These particles will inevitably be inhaled by people and cause the most substantial health impact.

With this in mind we decided to approach this challenge with the goal of creating social conscience. One can create many measures to tackle this problem, but in the end it is way more efficient to inform and convince people that change is needed or they will suffer from its absence.

To do this we provide a complete and descriptive data analysis of the air pollution in Stadhouderskade that can be used and repurposed to educate people about this issue. We also provide a predictive model that can be utilized to predict the trend and the future impact of reducing the pollution today.




## 🔢 Data (250 words max)

Data for this challenge was a problem. We ended up focusing exclusively on the dataset provided by WDL, as the OpenWeather limit was too restrictive. 

Two improvements that would help and bring more insights to the dataset provided would be adding O3 as a pollutant (it is included in the CAQI index and is as important as PM10, PM2.5 or NO2) and adding more sensors throughout the road to understand the pollution distribution among it.

Data availability was the main issue for this challenge. We had many ideas on alternative datasets we could have used, but these datasets were either outdated or of private access (paid access). Given the upset of not being able to access 2 years of data in OpenWeather, providing some additional datasets (traffic, noise, etc) would have been ideal and a huge improvement to the solution.


## 🧮 Methods and Techniques (250 words max)

Our whole analysis is done in Python. We used some popular Python libraries (numpy, pandas, matplotlib, plotlib, sklearn, xgboost, stata). 

Regarding methods and algorithms:
-	We performed a seasonal decomposition of the time series to understand trends and seasonality. 
-	We analyzed the stationarity by performing a Dickey-Fuller test. -	We computed the Common Air Quality Index and analyzed both the trends and the daily and weekly distributions.
-	We performed a thorough feature engineering process that included computing Mutual Information, Permutation Importance, PCA and SHAP
-	We pivoted the initial dataset and added different range lags to convert the timeseries to improve the predictive performance of our models
-	Used several Machine Learning models and compared their performance (RMSE Loss, Models: xgboost, catboost)
-	Given the nature of the problem, we focused on explainability, so we analyze the features that have the biggest impact on the model

Aside from this, we also did a literature review to understand the problem. This included papers on the impact of pollution in health, causes and solutions.

## 💡 Main Insights (300 words max)

We discovered several interesting facts:

Even though pollution is a big problem worldwide, the overall trend in this specific street (even before the COVID pandemic) shows a gradual decline. This is really interesting, as one would assume exactly the opposite. The reason behind this can be attributed to several factors, such as local measures (increase in public transportation options, making public transportation more affordable), technological reasons (electric cars and more efficient urban planning) or ecological reasons (The Netherlands is the country with the highest number of bikes per capita in the world and that already speaks for the “eco-friendly” nature of their folk. This also implies that the government has invested a big amount of money in infrastructure surrounding cycling and Amsterdam is considered one of the most bike-friendly cities in the world).
There is clear seasonality in the data, with an increase in pollution over the winter months and a decrease over summer. This again can be attributed to the climatic conditions, as with nice weather people are more inclined to take public transportation and bicycles.
Rush hour coincides with the highest daily pollution values. This is not a surprise, as with a higher amount of traffic there should be more pollution. This is highly impacted by a poor structural street design. Stadhouderskade is one of the main arteries of the city, but it is a 2 way street with one line in each direction. Having such an important and crowded street this narrow makes it completely inefficient, presumably creating big traffic jams every morning.
New Years is the most polluted time of the year
Most days have a really low pollution level within healthy levels


## 🛠️ Product
### Definition

Traffic control policies, articles, feature importance and aggregate data, mid-long term impact of anti-pollution policies.

### Users

Main value of our product is the analysis. This could be used to:

Create efficient traffic control policies, i.e rerouting traffic in certain times of the day.
Create additional anti pollution policies, like limiting the usage of certain fireworks in New Years to reduce the pollution levels
Underestimated, but one could use our analysis to create articles or media campaigns to generate social conscience on the pollution problem (it is easier to change things if you convince people first)
Create KPIs based on the features our models deemed more important
Create aggregate data, like lags or some of the feature engineered samples shown to increase the quality of a prediction

Our models can also provide a prediction regarding future air quality and this can be used to see the mid and long term impact of some of the measures applied.

### Activities

Describes and gives context to the current pollution state of the street
Predicts the future pollution trend for this upcoming year
Generates social conscience by linking the current state to the causes and consequences that air pollution has in our health and daily life

### Output

The necessity of healthy air has always been of great importance. As air is vital for all living beings on earth, it is our responsibility to keep the air clean. The rapid urbanization and industrialization have led the world into a new era of air pollution and seen as a modern-day curse. Because of the impact air quality has on people’s everyday life, how to predict air quality precisely, has become an urgent and essential problem. The work demonstrates the benefits of machine learning for short and long-term predictions of air pollutants, and foresee sudden spikes of high pollution level.

The product is able to output precise visualization about the air pollution trends. In a final product idea these visualizations can be gathered in a real time dashboard. Furthermore, the product outputs the pollution future predictions.

## 🌍 Social Impact Measurement
### Outcome

Our notebook is focused on long-term impact. We can always create models, policies, etc, but in the end, the biggest impact comes from making people understand the consequences certain factors have and will have in their lives. To achieve this we focused on building a complete and comprehensive analysis of the pollution state in that specific street. Our goal is that this product could be used to make people realize that even with the amount of environmentally friendly policies Amsterdam and the Netherlands have put in place, it is still not enough. Creating social conscience leads to change.

We also provide a long-term predictive model. This can be used to create actionable deadlines, where the government proposes to reduce the pollution levels by a specific date and on by a specific percentage . Our model can then be easily retrained to predict the impact of said measures

### Impact Metrics

Average Daily CAQI
Hourly CAQI


### Impact Measurement

The literature agrees that urban air quality prediction is a challenge that needs a multivariate temporal-spatial approach. The air pollutants occur in a space profoundly influenced by the weather with frequent changes in temperature, rain, among other weather conditions. Meteorological information is thus highly crucial to include among other dependent variables that have been studied, such as traffic and geolocation information. Problem solutions often take advantage of time series tendencies due to air quality is in constant change and is reliant on its historical trace. However, the literature search found no exploration of the impact of events. Events and urban human mobility data are believed to influence air pollution. Unfortunately, because of both technical details and limited time, this was not pursued in this study either. Based on the model prediction we can orientate different policies (e.g. traffic restrictions, eco-incentives ..) against the air pollution.  In many real-life events, the ability to foresee general sudden changes in air pollution is helpful if there is a need to take preventative measures. 

Based on the visualizations tools we can create a dashboard to monitor the impact of the aforementioned policies on the selected KPIs.
Its purpose is to visualize the concentration of air pollutants over time in multiple geographical areas, as well as to show the correlations between measurements of different areas, which may be indications for major sources of pollution.