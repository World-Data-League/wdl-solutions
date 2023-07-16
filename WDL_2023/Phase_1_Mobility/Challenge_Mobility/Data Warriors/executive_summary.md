# World Data League 2023

## 🎯 Challenge

Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data

## Team Name

Data Warriors

## 👥 Authors

* Clara Pedroso

* Gonçalo Ferreira

* João Anacleto

* Madalena Diniz

## ✨ Introduction

The City of Lisbon is a big metropolis with a population of over 500,000 people, and its traffic and mobility patterns are constantly changing and it has been increasing. In recent years, the city has experienced a significant increase in tourism, with over 7 million visitors in 2019 alone. This influx of people has led to challenges in transportation and mobility planning, making it crucial to have a clear understanding of the main mobility flows in the city.

To address this problem, researchers have turned to mobile device data as a source of information. By analysing data collected from mobile devices, researchers can gain valuable insights into the movement patterns of individuals in the city, including where they are coming from, where they are going, and the modes of transportation they are using.

This study aims to determine the main mobility flows in the City of Lisbon based on mobile device data. By analysing this data, the researchers hope to provide insights into the mobility patterns of individuals in the city, which can be used to inform transportation and mobility planning efforts. This study will contribute to a better understanding of the mobility challenges faced by the city and help policymakers develop more effective solutions to improve the transportation system for residents and visitors alike.

## 🔢 Data

To develop our solution, we used some of the datasets that were given to us and some external data provided by the Lisboa Aberta, MeteoBlue and Portugal’s Shapefiles and GIS data websites.

From the datasets that were given to us, the most important ones were the datasets from WAZE with information regarding traffic restrictions and the overall traffic flows in Lisbon. With them, we were able to not only see but also comprehend the traffic throughout Lisbon and why it was happening.

This information together with the external data (weather conditions and “Freguesias”), allowed us to dive into a deeper understanding of what was the root problem of the traffic and in which areas it was occurring.

Even though we got some good conclusions, there are always ways to improve and build up from these conclusions. For example, if the traffic restrictions dataset also contained all kinds of accidents it could help explain some things that we visualised, and maybe it could even alert the city’s council to problematic roads or paths. 

In conclusion, we found the datasets to be comprehensive based on our findings. However, in addition to the improvements we have already suggested, we propose to incorporate weather conditions (our external data), disruptive situations (events, strike or others)  and highlight troublesome roads, for example, as these could be highly relevant to the subject matter.

## 🧮 Methods and Techniques (250 words max)

We decided to choose the more meaningful variables that impact the target one (“level”) using correlations etc. Besides that we transformed the target variable in a dummy one.

Finally we used random forest to predict if there would be traffic or not.

## 💡 Main Insights (300 words max)

After some research we discovered interesting statistics such as Lisbon has 0.44 cars per capita, higher than cities like Barcelona (0.39), Berlin (0.29), or Stockholm (0.24). Athens, the capital of Greece, has the highest number of cars per inhabitant, with 0.77.

## 🛠️ Product

### Definition

A mobile app that assists decision making on whether you should go by car or not, based on many factors.

### Users

Lisbon citizens, both from Lisbon (“Concelho”) and the outskirts, can use the mobile app to decide if they should use the car to commute or not when going to or travelling in Lisbon.

### Activities

* Evaluates if it is worth it going by car or not.

* Suggests the best hour to leave the location.

* Predicts if the traffic is high, or medium/low according to the location of the person.

### Output

According to the place where the person is, the day he/she is travelling and the hour, the app will give an output: you can leave by car or you cannot leave by car.

The idea is sending a notification with that conclusion as shown in the mock-ups in this folder:

https://drive.google.com/drive/folders/1G6GBlpU1iLVaVMGHXwWmTO5UO9R6w567?usp=share_link


### Scalability

In this phase, this would have a very fast and easy implementation. The model is already working and the output is a dummy variable. It already takes some factors into account such as precipitation, temperature, day of the week, hour of the day, Lisbon zone, the existence of traffic jam and its impact on traffic.

For further work, we recommend using more variables such as big events that happened (football matches, concerts, etc), or people flows. Also, to predict the traffic only the “level” variable was used, but it would be interesting to consider the “delay” or the “speed”, for example.

Besides this, we combine public transportation information

## 🌍 Social Impact Measurement

### Outcome

By predicting the traffic in each Lisbon zone and time slot, the model could help citizens deciding to use the car in a more efficient way. They would only use it as a last resource in a traffic hour, thus contributing to less congestion, less travel times and lower Carbon Dioxide emissions. The long-term objective is to promote sustainable transportation in Lisbon which can be achieved by less cars acquisition and usage. 

Besides this, in a future scenario, it could also help city planners and policymakers to make more informed decisions about transportation infrastructure and policies, such as promoting public transportation, encouraging biking, or implementing road pricing strategies.

In addition to the environmental benefits, the model can also have a positive impact on quality of life for residents of Lisbon. By reducing traffic congestion, the model can help to reduce commute times and improve access to transportation, which can lead to more efficient use of time and increased productivity. Furthermore, it can reduce the number of accidents since most of them are related to traffic jams.

The ultimate goal is to create a more sustainable and liveable city, with cleaner air, less traffic congestion, and healthier citizens.


### Impact Metrics

* Reduction percentage of Carbon Dioxide emissions

* Reduction percentage of travel times

* Increase percentage of public transportation usage

* Average decrease in the number of traffic accidents

### Impact Measurement

Although the model currently implemented does not provide precise figures, there are three illustrative examples that demonstrate its potential impact:

1.Fort Collins, Colorado implemented an advanced traffic management system, which reduced travel times by 36%.

2.In Japan, a personalized travel planning system equipped commuters with GPS-enabled cell phones and internet access to help them choose more environmentally friendly routes and modes of transportation. This resulted in a 20% reduction in carbon dioxide emissions during daily commutes, according to survey data.

3.A traffic management system was introduced in Espanola, New Mexico in 2006, which connected the operations of eight signalized intersections to a traffic operations centre. The project resulted in a 27.5% reduction in total crashes compared to previous years, and a reduction in vehicle delay of 87.5%.

