
# World Data League 2022

## 🎯 Challenge
Semifinals- Gender Based Violence in Costa Rica 

## Team Name
Pablitos 

## 👥 Authors
* Joana Rocha Camargo 
* Hiba Laziri 
* Beatriz Barretto 
* Marcelo Moreno 

## ✨ Introduction 
Women safety is a major concern in many developing countries. In fact, governments are attempting to implement additional measures to improve the safety of women and girls in their streets. Taking the case of Costa Rica, a major Central American country, the problem of gender violence is critical, since the number of rapes has increased at a rate of 42 cases per year since 2000, and although this is true, many cases still are not reported or not persecuted if reported. In 2014, for example, only 29.7% of crimes committed were reported. Which means there is a significant lack of data to represent gender based crimes. Our goal is to be able to enhance women’s safety by developing an app based in Costa Rica alongside Urbanalytica, which already has projects in action that use the power of data to improve urban life. We reached out to multiple Costa Rican women, and one issue came up repeatedly: a lack of reporting of violence against women, either because victims feel ignored by the government and police, or because they are afraid of being prosecuted if they do so. They have to rely on the mere support of one another and the support of the community to feel safer. Enhancing the reporting of crimes against women will thus be a significant solution to the problem.

## 🔢 Data 
In this project, four databases were used. The data on crimes in Costa Rica was the most important one when building the index, where all the information about crimes were extracted to measure the safety of each district. It contains data on the type of crime committed, type of victim, time of the day the crime happened, and in which district it happened. The second data used, Costa Rica’s Código Penal, served to measure the weight each type of crime would have on the index. The higher the jail time for a certain crime, the bigger weight that crime would have on the index. This was done so that not all crimes were considered the same. Two datasets about Costa Rica’s population, one from the year 2000 to 2011 and the other one from 2011-2025, were used to calculate population size for each district, to take that into account when looking at crime rates. And, finally, the database on street harassment in Costa Rica only went through Exploratory Data Analysis. Because the data was very incomplete, with no indication of what time period the data referred to, it was not possible to include it in the index. If the data were more complete, it would have given valuable information to measure the danger women are in while walking on the streets of San Jose.

## 🧮 Methods and Techniques 
The Index was constructed manually using data on the crimes for each district, taking into account population size. To give more depth to the index, the jail time for each specific crime was taken into account when weighing the crimes, as well as if the crime was against a woman or a minor (having double the weight). The numbers associated with these three factors were multiplied, resulting in a score for each crime. The final index sums all incident scores for each district every quarter or year, and divides by population size in that same quarter or year. As for the models, the first one was composed of a Time Series with Linear Regression in which a different model was fitted for each district after creating a trend, and seasonal component and adding lags of up to 3 months whenever significant. In the XGBoost model every datapoint was fitted all at once by creating dummy variables for the district and canton. Another possible method would’ve been to use k-means clustering to group similar districts and make a model for each group. However, because of the time constraint, this wasn’t tested, but it could have improved model accuracy. After cross-validation, the time series proved to be the better model. The accuracy of the model decreased for 2020 and on, likely because of COVID’s impact on each district regarding crime. The error in the model is small and is specially accurate when calculating the yearly index.

## 💡 Main Insights 
When it comes to the data, we have found that Costa Rica has little information regarding crimes, data on cities, districts and cantones and gender-based violence. It was also found that most of the crimes reported and prosecuted were done to men or were reported by men. We believe the data may be biased, as it is not correctly representing crimes that happen in Costa Rica. During literature review and interviews, it became clear that underreporting was a problem and, especially for women, reporting was known to be ineffective, where crimes ended up not being prosecuted. As seen in the data, throughout the years (2020 and 2021 being exceptions), the number of crimes committed have increased and, similarly, the number of cases reported by women have also increased, although there still remains a very significant gap between genders. Additionally, it was interesting to compare the count of crimes in districts and speculate why this may be the case. If there was an opportunity for further research, we believe it would be important to look for differences between districts that explain this dissimilarity and possibly implement plans to reach a safer Costa Rica, in all districts. For the model, we found that when utilizing the years of 2010 to 2015 to predict 2016 and so on, the model gave very accurate results. Curiously, when predicting 2020, 2021 and on, the accuracy was lower. We suspect that this may be because although the level of crime has decreased overall during COVID and quarantine, how much it decreased depended on the district, changing the trend and modifying the relationship between districts. We believe that in the future, as Costa Rica and the world recuperate from COVID, the predictions will return to the level of accuracy or even higher accuracy then it had before.

## 🛠️ Product
### Definition
A product that could be built with the model produced is an app that provides a specialized estimate of the safety of an area for a specific person at a specific time of day and year and collects data for gender-based violence through reporting and calling hotlines in case they are faced with such violence.

### Users
The users of our product would be Costa Rican citizens and individuals traveling in Costa Rica, especially women. Our app would be used to inform individuals of their safety score in the location they are in or will be going to. Furthermore, it will help individuals prepare themselves with tips and recommendations of what to do, where to go, when to go, etc, all so they are safer and provide help if they are faced with gender-based violence.

### Activities
* Predicts the safety score of an area specifically for the individual taking into account the time of year, day, location, age, gender, race, etc. The data of the incidences would be weighted in such a way that the index is calculated specifically for each user at a particular point in time.
* Has a hotline to call in case they are faced with gender-based violence
* Has tips and recommendations for safety
* Has a map of the cities showing the crime index of each district
* Has an area to report gender based violence or suspicious behavior

### Output
The product outputs the user's personalized safety score by processing the information inputted by the user into the app and utilizing the safety index as well as other variables to predict this value.

## 🌍 Social Impact Measurement
### Outcome
We hope our app will help women feel safer in Costa Rica, decrease gender-based violence, increase the amount of gender-based violence data, create a support system for women that do face this and increase reporting of these circumstances.

### Impact Metrics
* Number of reports to police of gender based violence
* Number of individuals persecuted because of committing gender based violence
* Increase in data about this topic
* Lower safety index including new data points after a year or two 

### Impact Measurement
Based on the market research, we expect the number of reporting for gender-based violence to increase. In fact, as previously mentioned the biggest problem that women are facing in Costa Rica is the lack of reporting of cases which make it hard for the government or any organization to lead actions against it as long as no major data and statistics are available. Our app interface will therefore facilitate the generation of new data to better tackle the problem basing it on actual evidence so that new policies and measures are established in Costa Rica. In 2022, the European Commission has established guidelines to prevent women violence, and one of the important parts of the recently announced report is the implementation of new measures to improve safe reporting and risk assessment procedures.


