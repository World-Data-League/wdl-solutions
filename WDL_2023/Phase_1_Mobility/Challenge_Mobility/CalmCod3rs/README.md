# World Data League 2023


## 🎯 Challenge

Determining The Main Mobility Flows in the City
of Lisbon Based on Mobile Device Data


## 👥 Authors

* Ana Luiza Kaori Akiyama
* Luiz Gustavo Moniz
* Guilherme Caixeta

## ✨ Introduction (250 words max)

In the last decades, the Lisbon Metropolitan Area (AML) has gone through important urban, social, and economic dynamics. Among those dynamics, two are of particular relevance: first, the demographic outward flow of Lisbon residents to AML’s neighboring municipalities, and, secondly,the proliferation of car ownership and its widespread use. [1]

AML’s demographic reorganization has led to an excessive demand on the Lisbon road network, with consequences in terms of traffic and parking, as well as safety and quality of life of those who live and use the city. The growing inadequacy of the public transport system to the new reality of people’s mobility has also contributed to that. [1]

In 2017, the private car accounted for about 46% of journeys, compared to only 22% of public transport. The goal of the Municipal strategic planning (MOVE Lisboa) is to reduce the use of private cars to no more than 34% of trips in the city of Lisbon by 2030. [1]

CalmCod3rs team aims to help the Municipal strategic planning MOVE Lisboa, the city's vision for mobility by 2030.  To this end, we developed a ML based web app project that aims to provide tools to understand peak hours patterns and incentivizing commuters to travel off-peak.



## 🔢 Data (250 words max)

1- CML – DISPOSITIVOS MOVEIS_GRELHA :
Information on the number of active mobile phones per square of 200m/200m every 15 minutes - Squares of the city of Lisbon

2- CML_DISPOSITIVOS MOVEIS_EIXOS :
Number of mobile phones entering and leaving the city every 15 minutes on the 11 main road axes in the city of Lisbon

3- WAZE_JAMS:
Traffic level data recorded through the WAZE platform

4- DISPOSITIVOS MOVEIS_TROÇOS DE VIA_TROÇOS DE VIA:
Mapping of road sections used to calculate city entrances and exits



## 🧮 Methods and Techniques (250 words max)

In the exploratory data analysis we use hvplot library to present interactive visualizations on html,and most of the geospatial dataset was manipulated using geopandas. All of the animated chronological maps were created using plotly express.

To analyze how people move between grids, we use the OpenCV library that uses Wasserstein distance or EMD (earth mover’s distance)  as a metric to compare the similarity between images. The computation of the Wasserstein distance gives, as a by-product, the optimal flow which, in our case, coarsely corresponds to the main directions followed by people. [2]

To analyze and create a predictive model we choose NeuralProphet, a successor to Facebook Prophet, which set an industry standard for explainable, scalable, and user-friendly forecasting frameworks.
NeuralProphet is a hybrid forecasting framework based on PyTorch and trained with standard deep learning methods.

LISA statistics is used for the detection of spatially extended clusters, as well as for the diagnosis of local instability. 

The LISA map displays four results: the first is the representation of the values with a High-High (AA) grouping, composed of spatial units (grids) with high values surrounded by spatial units that also have high values; the second represents spatial units with a Low-High (BA) grouping, where any spatial unit with low value is surrounded by high value spatial units. The third represents spatial units with a Low-Low (BB) grouping, where any spatial unit with low value is ​​surrounded by space units that also have low values. Finally, the fourth represents the High-Low (AB) cluster, in which any spatial unit with a low value of the variable of interest is surrounded by spatial units of high value [3].





## 💡 Main Insights (300 words max)

First, it was studied the outliers in the dataset that represents the number of active mobile phones per square of 200m/200m every 15 minutes. Although there were many uncommon observations, some of them can be explained by some specific city event. In those cases, we didn’t remove the observation. 


The average number of distinct terminals in the grids during weekends are higher than weekdays during the dawn, however during the work hours the weekdays are more than 30% higher. On average, the work hours on Mondays have the highest peaks.


On the Lisa Cluster map and the heatmap of ‘Time x Freguesia’ it is possible to notice the Avenidas Novas, Arroios, São Domingos de Benfica, Santo António and Parque das Nações neighborhoods contain respectively the highest people’s density. On the other hand, the neighborhoods of Benfica, Olivais, Marvila, Belém and Ajuda contain the lowest people 's density.


Both on weekends and weekdays, the highways with the most incoming and outgoing traffic are respectively: IC19, IC2 (Sacavém), IC16.


On the Traffic Jam Analysis during a typical working day, it is possible to realize that the traffic jam occurrences correspond with the same areas of high terminal’s density.


On the heatmap of the number of different foreign SIM Cards terminals, it was possible to see a higher density on the main touristic areas (hotels, restaurants, attractions) and an isolated point in the north which corresponds to the airport.


In order to determine the main mobility flows, it was used the Wasserstein distance metric which indicated the “where-from-where-to” information. Consequently, it is possible to verify where the flow of people that create the high density regions on the map comes from.
It is clear that the flows are directed towards and from the central area of Lisbon, and are mainly determined by commuters.





## 🛠️ Product
### Definition


An Analytics Web App called “Peak Analytics” for the government to manage risks and plan interventions based on the past events and forecasts provided by the tool.

In this Web App, it is possible to simulate scenarios that can help authorities to make decisions:

1- Measure the risk of a planned event

If there is a planned event that can cause traffic, it is possible to use “Peak Analytics” in order to understand the impact of this event on the city's main flows movement.

2- Optimize intervention Plan:

If there is a planned event that can cause traffic, “Peak Analytics can help define areas to increase the number of buses during these off-peak hours.

3- Which periods of the day are recommended to incentivizing commuters to travel off-peak in public transport.

4- Improvements in Lisbon public transportation.
Determining The Main Mobility Flows in the City of Lisbon and reallocating buses to the rush areas at the right time.


### Users

Governments can use the “Peak Analytics” to analyze past events, see forecasts, manage risks and plan interventions.

Service providers can use the “Peak Analytics” to determine points of high demand for transportation services.


### Activities

* Analyze how past events (e.g. constructions, manifestations, etc.) interfered with traffic
* People density forecast
* Risk management for future events
* Plan interventions (e.g increase the number of buses, free public transport during off-peak hours)



### Output

Generates insights that may help government to improve decision making process of interventions like incentivizing commuters to travel off-peak in public transport and cities’ events organization (constructions, manifestations, music concerts, football games etc)


### Scalability

This product depends on data quality and quantity. In order to implement real time analysis it is necessary to use a database that is capable of handling a high amount of data, which may increase the costs.


## 🌍 Social Impact Measurement
### Outcome

The idea of this product is to improve the usage and the population level of satisfaction for the public transportation by bus in the Metropolitan Area of Lisbon. This will also result in the decrease of car usage, representing the decrease of carbon dioxide emission.

In addition, increase population satisfaction with government decisions.


### Impact Metrics

The main metric we are going to use to evaluate the impact of our solution is the decrease of peak hours flows.

Other possible metrics to be evaluated are:

* Improve Availability of public transportation on areas of Main Mobility Flows in the City
* The growth of the usage for public transportation by bus
* Decrease traffic during planned cities events


### Impact Measurement


Recent evidence suggests that millennials (individuals born following Generation X and between the early 1980s and early 2000s) are characterized by different automobility characteristics, including being less likely to have a valid driver’s license, less likely to drive, and being more likely to take public transit than their older counterparts [4].

This reinforces the importance of creating a good experience for the user to increase satisfaction and loyalty in public transport. 

There is a similar study:  Singapore’s INSINC program. This aims to shift demand from peak to off-peak shoulder times in Singapore’s public transport system.

The scheme manages peak-hour congestion by offering incentives for commuters to travel in off-peak periods. These incentives include random (raffle-like) rewards, social influence and personalized offers.

A six-month research pilot, launched in January 2012, achieved a 7.49% shift from peak to off-peak hours for all commuter trips.


The factors most associated with satisfaction are on-board cleanliness and comfort, courteous and helpful behavior from operators, safety, as well as punctuality and frequency of service
[5].

Peak hours can be the most uncomfortable hours in public transport, not only for users but also for bus drivers. A survey [6] shows that higher stress levels of bus drivers were recorded during extreme weather 12 conditions, peak hours and among inexperienced drivers. 

Taking this into account, the stress level of bus drivers with smaller peaks of flow could also decrease.


REFERENCES:

[1] Lisbon Mobility Strategic Vision MOVE 2030

[2] C. Balzotti, A. Bragagnini, M. Briani, E. Cristiani, Understanding human mobility flows from aggregated mobile phone data, IFAC- PapersOnLine 51 (9) (2018) 25-30 (2018).

[ 3 ] ANSELIN, L. Local indicators of spatial association – LISA. Geographical Analysis,

[4]   https://www.sciencedirect.com/science/article/abs/pii/S2214367X17300625

[5] 
https://www.tandfonline.com/doi/abs/10.1080/01441647.2017.1298683

[6] 
https://repository.tudelft.nl/islandora/object/uuid%3A6d4df8a3-4bd5-479b-a96c-968591ce13fa/datastream/OBJ/download

