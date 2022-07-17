# World Data League 2022

## 🎯 Challenge
*Air Quality Prediction in Busy Streets*

## 👥 Authors
* TinWan Ng
* Fernando Chavez

## ✨ Introduction
"Stadhouderskadet is a busy inner-city road with a lot of car traffic"[1] which could trigger the pollution up. Also, it was one of the most polluted parts in Amsterdam back in 2018 [2]. Because of the environmental issues, a project called the Green Mile was started to turn Stadhouderskade into a more green and safe place for people to spend time[3].  

To achieve this objective, it is essential that factors contributing to the air pollution are found. In addition, we would build a ML model as the bais of an air quality mobile app, which serves as both a self-serve analytics tool, and a warning system for the public.


## 🔢 Data
We used the air quality data provided by World Data League and weather data from the [meteostat](https://meteostat.net/en/place/nl/amsterdam) website.

Both of the datasets provided us good insights into the analysis and correlation. It could have been better if traffic data, noise and power plants data throught the years was publicly available. On https://data.amsterdam.nl/, we have only managed to find a traffic prediction data, and a noise map without the exact data. Though they are useful for gaining insights into the situation, they are not sufficient for hypothsis proving. For instance, a calculation of coreelatio matrix is not possible.


## 🧮 Methods and Techniques
**Data Cleaning:**
- We used a 3 point rolling mean to fill null values for some of the weather data values. Rolling mean was could provide a more accurate estimation compared to mean or median imputations.
- To facilitate machine learning development, skewness for the data was normalised with Scipy module.

**Data Analysis:**
- We considered the need for an open-source, easy-to-use tool. We, therefore, developed a Google Data Studio Dashboard which can also allow users to gain insights about pollutants emission in Stadhouderskade. With this dasboard they could easily filter their desired timeframes within one click. 

**Modelling:**  
Because of the lack of data, we only extracted datatime components and weather data as features. This will inevitably affect the accuracy of the model negatively.
1. Auto ARIMA: Auto ARIMA is a powerful model which automates the optimization of (p, d, q) order and return the best parameters. The AR part utilizes past values for predictions, while the MA part utilizes past residuals for shocks resistance. However, it did not perform well for data with seasonality and a SARIMA model would have performed better. The mean absolute percentage error is 108% and the root mean squared error is 1.87.

2. XGBoost:  As for the XGBoost model, it is not optimiseed due to time constraints. Nevertheless, its predictions have around 0.3 lower root mean squared error, yet 10% higher mean absolute percentage error.

Though mathematically-wise they both have a better performing metric, XGBoost is superior in graph presentation. While Auto ARIMA's predictions are a straight line, XGBoost's manages to predict limited seasonality. Unfortunately, both models' predictions left high residuals.


## 💡 Main Insights  
1. All air pollutants show a decreasing trend from 2014 to 2022, ranging from 11% to 81%. Compounds (Xylene - 81%, Toluene - 71%) have decreased the most. Specifically:
- Benzene - 34.5%
- NO2 - 37.8%
- PM10 - 11.5%
- PM25 - 24%

2. However, Toulene is the only pollutant which still have its average emission above the safe level in 2022. The main source of Toulene is traffic, hence a positive relationship between may be proved if data is present.
 
3. During the months of May to August (Summer), the pollutant value decreases and air quality index increases. However, during the month of December, the pollution levels skyrocket.
 
4. Pollution levels for NO2 are lower in the early mornings when compared to the entire day where they are consistent. For other pollutants, there is no such pattern observed. Morning is when peak hours vehicles commute and power plants operate. Given that NO2 originates from the burning of fossil fules such as vehicles and power plants, we suspect that they are main source of this increase.

5. Wind speed and the pollutants FN and NO2 have a weak negative correlation (-0.4). It reflects the dissipation of pollutants by wind - if wind speed goes up, part of the FN and NO2 pollutants are blown away.


## 🛠️ Product
### Definition
A mobile app that shows visualizations of the pollutant values over time and informs about the prediction (1 week ahead) of the air quality including a warning system.

### Users
1. Members of the Green Mile Project could utilize the self-service dashboard to extract alarming trends and pursuade for a change for Stadhouderskadet. For example, for how long is certain pollutants beyonf the safe level? And what effects will it have on the human body? The app will have answers to these questions.
2. The public could see the prediction of the pollutants amount predictions up to 1 week ahead of time. This allows them to plan for outdoor activities on days with better air quality.

### Activities
* Weekly predictions of the air quality
* Filters/ Sliders within the dashboard allowing users to visualize the values for every pollutant over a timeframe of years, months and changes over one day.  
* Warning system: 
1. it sends users notifications 1 week before the day having predicted moderate/severe air pollution level via smartphone/ emails notifications.  
2. as well as instant warning when the level is beyond safe for 5 consecutive hours.
* Weekly reminder of the effects of moderate level air pollution have on human bodies  
* User surveys on whether the warning has helped them in deciding the time of going outdoor

### Output
In the mobile app dashboard section, two types of visualizations are displayed.  
1. Past data analysis: the user can interact with the graphs and choose the pollutants or the timeframe they would like to see.  
2. Air quality forecast for the next week and its comparison with this week's.  


## 🌍 Social Impact Measurement
### Outcome
The product should be publicly available so that everyone can see and interact with the measured pollutant values over the years, what might be causing them, and prediction of the pollutant values over time. By making this product publicly available, the community would get a bigger notion and could also take part in the change.  

Specifically, the Green Mile Project can utilize the app for more convenient analysis, in turn focus on the implementation of designing and revitalizing Stadhouderskadet. 

### Impact Metrics
* Average warnings per week  
* Average user ratings of the app  
* Average response rate of the survey per month
* Average MAPE(mean absolute persentage error) of the predictions over the week

### Impact Measurement
* *Based on C7H8 model predictions*: average MAPE is 108%
* *Based on C7H8 model predictions*: average instant warnings per week is 29  


[1]https://www.nhnieuws.nl/nieuws/184883/milieudefensie-stadshouderskade-meest-vervuilde-plek-van-amsterdam
[2]https://www.parool.nl/amsterdam/ggd-lucht-amsterdam-nog-te-vies-maar-het-gaat-beter~b1818ac7/?referrer=https%3A%2F%2Fwww.google.com%2F
[3]https://www.greenmileamsterdam.com/