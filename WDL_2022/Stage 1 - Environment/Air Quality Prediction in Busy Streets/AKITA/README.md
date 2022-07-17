# World Data League 2022


## 🎯 Challenge
Air Quality Prediction in Busy Streets

## 👥 Authors
Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.
* Hongyu Ao
* Yu Luo
* Xiaoxiao Ma
* Wanghan Yuanliu

## ✨ Introduction (250 words max)
Provide a contextualization of the problem, together with an estimation of its size using real numbers and references.
Air pollution contributes not only Global Warming but also the downturn of human health. In this project, we analyze the air quality detected among the busy streets in the City of Amsterdam to help provide more insights for The Green Mile project. Major pollutants such as PM2.5, PM10, NO2 were detected and leveraged to determine the aire quality of the day. Based on the sources of pollutants, current policies in the City of Amsterdam, as well as our analitical results, we are able to optimize the process of the Clean Air Act proposed by the city. 

## 🔢 Data (250 words max)
We used the provided data of the hourly measurements of different air pollutants at Stadhouderskade. We found out that although 8 pollutants are expected to be detected, there are instances with a 9th pollutant, which is unknown. In our analysis we have dropped the 9th pollutants for more consistent analysis. There are also missing and negative values in the dataset, and we either removed or imputated them to conduct futher analysis. However, having to remove a rather significant amount of data can negatively affect the quality of modeling. We suggest that the data provider make sure the detected components have labels, as well as give explanation for negative values. 

## 🧮 Methods and Techniques (250 words max)
Using cluster methods, hourly detected air values are classified into 7 groups according to their NO2, PM2.5 and PM 10 values. Hours with relatively unsatisfactory or worse air quality are identified. Through explanatory analysis, most of the worst hours happened on the New Year's due to the fireworks. As for the second worst group, there exists a plunge since 2020 which matches the appearance of Covid. In order to understand air quality impact due to the change of transportation and human activities during Covid, time series models are applied on the pre-Covid period (2014-2019) data to predict how the air quality supposed to be if there had been no Covid during 2020-2022.

## 💡 Main Insights (300 words max)
We validated the observed difference that lockdown has resulted in air quality. We determined the cutoff point of pre-lockdown and during lockdown to be March, 2020 because this is when the City of Amsterdam started to shut down public revenues that are likely to be crowded such as restaurants and bars. The results of time series modeling indicate that the predicted air pollution during the time of lockdown is indeed higher than the actual. In other words, the change in the daily behaviors of citizens has caused the decrease. The lockdown period is when the need for transportation minimized. This tells us that transportation contributes significantly to the air pollution in Amsterdam, and by reducing the emission from transportaion, air quality can be improved. 

## 🛠️ Product
### Definition
A analytically-inspired suggestion on optimizing the Air Pollution Measures in the City of Amsterdam. 

### Users
The Green Mile Project and the city government/department of transportation  in general. 

### Suggestion Details
The Clean Air Act of the City of Amsterdam states that by 2030, the city will be emission-free. By comparing the predictions without lockdown to the actual values with lockdown, we identify that a major source of Air Pollution in the city is indeed transportation. Therefore by speeding up the emission-free process, the amount of pollutants detected in air can be most efficiently reduced. Adapting a "Congestion Charge", like in many other cities, but only for non-emission-free vehicles is one of the most effective ways. Furthermore, to significantly speed up the process, we suggest that the city increases the "Congestion Charge" by a small percentage each year until 2030. We also want to make sure that this decline does not spike other sources of pollution by increase the awareness of the significance of air pollution. 

## 🌍 Social Impact Measurement
### Outcome
The suggestions are likely promoting clean energy and emission-free transportation, as well as lighter traffic. 

### Impact Metrics
* Level of pollutants
* The trend of the number of non-emission-free vehicles
* Citizen's support rate on government decisions

### Impact Measurement
As seen in other cities with "Congestion Charge" such as London and Stockholm, the amount of traffic has decrease significantly. In our case, while we focus on gas/diesel operated vehicles, we expect the amount of such vehicles decrease, and therefore lower air pollution in general. 
