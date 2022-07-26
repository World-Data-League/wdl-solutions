# World Data League 2022


## 🎯 Challenge

Predicting the flow of people for public transportation improvements

## 👥 Authors

* Ana Luiza Kaori Akiyama
* Luiz Gustavo Moniz
* Guilherme Caixeta

## ✨ Introduction (250 words max)

The city of Porto has one of the worst traffic situations in the world, ranking 158th in the 2021 world Traffic Index [[1](https://www.tomtom.com/en_gb/traffic-index/ranking/?country=PT)]. This situation has a number of reasons, like the geography of the city, the difficulty of urban planning, the lack of a mobility plan for the Metropolitan Area of Porto and a public transportation system that doesn't meet the population demands  [[2](https://www.deco.proteste.pt/familia-consumo/orcamento-familiar/noticias/transportes-publicos-ineficazes-em-6-cidades)]. 
On this last factor, studies have shown that the level of satisfaction for public network transportation is 6 of 10 in the city of Porto [[3](https://www.deco.proteste.pt/familia-consumo/orcamento-familiar/noticias/transportes-publicos-ineficazes-em-6-cidades)]. So we focused our research on that problem, especially on public transportation by bus, which received 6 of 10 on satisfaction level, on the opposite of the subway, which received 8,5 of 10. We built a model based on the bus lines of the Sociedade de Transportes Colectivos do Porto (STCP) where we calculated the entry validation per stop on each of the lines, enabling us to verify the patterns and the numbers of a normal situation on each stop. The analysis showed that the bus lines have similar characteristics and well-defined flow peaks. Peak hours, of course, can be the most uncomfortable hours in public transport. So the idea of the product is to build an app that uses the inbound forecast model to send personalized offers that give incentives for commuters to travel in off-peak periods. The user can also evaluate the bus service, and both the evaluation and the data can be used for the public transportation authorities to manage and implement improvements on this segment, which can help to increase the level and satisfaction of the users and reduce the traffic in the Metropolitan Area. 

## 🔢 Data (250 words max)

InterMunicipality.zip (from Challenge Available Resources)
Bus line Validation (TIP Folder)
Public transport schedule data in GTFS format (GTFS folder)
Porto Zone Map Shapefile (linhandante.com)

The TIP dataset (Validações Rodov) only contains the ‘Stop name’ column (Paragem). Many times, the same stop name can be spelled in different ways. So it would be important to have a column with the ‘Stop code’, which is unique. Besides, it would be easier to join with other datasets.



## 🧮 Methods and Techniques (250 words max)

In the exploratory data analysis we use hvplot library to present interactive visualizations on html,and most of the geospatial dataset was manipulated using geopandas.

In the forecasting model, we use gluonts, an open source Python package for probabilistic time series modeling, focusing on deep learning based models. We directly modeled the distribution of the validations using an autoregressive RNN, specifically DeepAR [[4](https://arxiv.org/abs/1704.04110)]. In a nutshell, DeepAR attempts to model the conditional distribution of the future of a time series given its past. It learns a global model from historical data of all time series in the dataset. During training, the model learns to parametrize a likelihood function of a chosen probability distribution (in our case, we chose a negative binomial distribution given the count-like nature of the data). DeepAR makes probabilistic forecasts in the form of Monte Carlo samples that can be used to compute consistent quantile estimates for all sub-ranges in the prediction horizon. We created 4 main categorical groups: 'entry_zone','exit_zone', 'group_entry_zone', 'group_exit_zone'. As the model learns seasonal behaviors and dependencies on given covariates across time series, minimal manual intervention in providing covariates were needed in order to capture complex, group dependent behavior. 





## 💡 Main Insights (300 words max)

More than 70% of the flow of people on public transportation focuses on two operators:
- STCP (bus): 42.45%
- Metro do Porto (subway): 35.1%
 
Focusing the analysis only on the bus, the **STCP** has the largest share of the flow of people (72%).
 
Filtering only the **STCP** operator, more than 60% of the flow of people is concentrated in the following zones:
- PRT1
- PRT2
- PRT3
- VNG1
 
On all routes without exception, it is possible to observe that there was a drop in the flow at the beginning of covid (from the middle of March onwards). At the beginning of May, the flow began to increase discreetly, but until the end of 2020 it did not return to the same volume as before the covid, maybe because many people started working remotely.
 
There is a large flow during the working days and it decreases on weekends. It is also possible to see the peaks of flow near 8am and 6pm on weekdays, demonstrating the start and end times of work hours.
 
On weekends, the flow also starts at 6am, but the peak takes place a little later, about 12am.
 
With the analysis, it was possible to notice that the bus lines have similar characteristics and well-defined flow peaks. Peak hours, of course, can be the most uncomfortable hours in public transport.
 
Taking into account that factors most associated with satisfaction are on-board cleanliness and comfort, courteous and helpful behavior from operators, safety, as well as punctuality and frequency of service [[5](https://www.deco.proteste.pt/familia-consumo/orcamento-familiar/noticias/transportes-publicos-ineficazes-em-6-cidades)] , it would be interesting to find a way to reduce these peak hours. 
Thus, we propose a solution with gamification offering incentives for commuters to travel in off-peak periods (random (raffle-like) rewards, social influence and personalized offers). 
 
It would also be interesting to track the level of user satisfaction by bus line, time and user characteristics to better plan the improvements in the public transport in order to retain and attract more users. 
 

## 🛠️ Product
### Definition

A collaborative and gamified application for bus users to have a personalized experience, offering incentives for commuters to travel in off-peak periods (random (raffle-like) rewards, social influence and personalized offers). This solution was inspired by Singapore’s INSINC program [[6](https://theconversation.com/how-gamification-can-make-transport-systems-and-choices-work-better-for-us-57663)]. 

Additionally, the app uses the inbound forecast model to send the personalized offers. For example, if there is an event in the next few days, the forecast model will predict a great increase in the flow, so the app can send personalized offers in off-peak hours.

The data generated by this app can be connected to a dashboard to create a risk assessment and improvements in Porto public transportation.


### Users

The main users will be the Public transportation users, more specifically the bus users. The app will provide incentives to travel in off-peak periods, to see forecasts flow, get real-time information and rate services. Government can use the collected data to improve the public transportation service.


### Activities

* Offers incentives for commuters to travel in off-peak periods based on the flow prediction. These incentives include random (raffle-like) rewards, social influence and personalized offers.
* Send flow anomaly alerts to the user
* Send alerts of interruptions or events that may affect the flow
* Offers the real location of a specific bus, so that the user has an idea of ​​where it is and how long it can take
* Possibility for the user to evaluate the services after a trip, receiving points and being able to win free tickets. 


### Output

Incentives to travel in off-peak periods, real-time information and flow forecast. It would also allow the users to evaluate the service, and consequently generates data to be used to improve public transport.

## 🌍 Social Impact Measurement
### Outcome

The idea of this product is to improve the usage and the population level of satisfaction for the public transportation by bus in the Metropolitan Area of Porto. This will also result in the decrease of car usage, representing the decrease of carbon dioxide emission.

In addition, user satisfaction data may be used by transport entities to generate improvements in the service.


### Impact Metrics

The main metric we are going to use to evaluate the impact of our solution is the decrease of peak hours flows.

Other possible metrics to be evaluated are:

* The growth of the usage for public transportation by bus
* The growth of the population level of satisfaction for public transportation by bus
* The decrease of car usage

### Impact Measurement

The Metropolitan Area of Porto conducted a mobility research in the region in 2017 where they calculated that 67,6% of the population travels by car. Only 11,1% use public transportation to travel around the metropolitan area for work, study, and other day-to-day business [[7](https://boost.up.pt/news/imob2017/)] . 

Recent evidence suggests that millennials (individuals born following Generation X and between the early 1980s and early 2000s) are characterized by different automobility characteristics, including being less likely to have a valid driver’s license, less likely to drive, and being more likely to take public transit than their older counterparts [[8](https://www.sciencedirect.com/science/article/abs/pii/S2214367X17300625)].

This reinforces the importance of creating a good experience for the user to increase satisfaction and loyalty in public transport. 

There is a similar study:  Singapore’s INSINC program. This aims to shift demand from peak to off-peak shoulder times in Singapore’s public transport system.
The scheme manages peak-hour congestion by offering incentives for commuters to travel in off-peak periods. These incentives include random (raffle-like) rewards, social influence and personalised offers.
A six-month research pilot, launched in January 2012, achieved a 7.49% shift from peak to off-peak hours for all commuter trips.



The factors most associated with satisfaction are on-board cleanliness and comfort, courteous and helpful behavior from operators, safety, as well as punctuality and frequency of service
[[9](https://www.tandfonline.com/doi/abs/10.1080/01441647.2017.1298683)].

Peak hours can be the most uncomfortable hours in public transport, not only for users but also for bus drivers. A survey [[10](https://repository.tudelft.nl/islandora/object/uuid%3A6d4df8a3-4bd5-479b-a96c-968591ce13fa/datastream/OBJ/download)] shows that higher stress levels of bus drivers were recorded during extreme weather 12 conditions, peak hours and among inexperienced drivers. 

Taking this into account, the stress level of bus drivers with smaller peaks of flow could also decrease.





