# World Data League 2022

## 🎯 Challenge
Optimization of Soft-Mobility Drop-off Points

## Team Name
YODAS

## 👥 Authors
* Cristiana Carpinteiro
* Diogo Valente Polónia
* João Afonso
* João Matos
* Patrícia Rocha

## ✨ Introduction
In most cities, public transportation is not that good and it is difficult to fix. Building infrastructures for public transport, like digging subway tunnels, is costly. Buses have rigid routes and schedules, often compromised by high traffic. Cars with empty seats create emissions, congestion, and massive inefficiency.

Porto is the second-largest city in Portugal and has been a tourism hotspot over the past years. However, it is also the stage for a grueling traffic situation, likely caused by late urban development. Portugal only became a democracy in 1974, which fostered economic growth. On top of that, in the 1980s and 1990s, there were few guidelines in urban planning, combining the abundance of money with a lack of care for urbanism.

Fast forward to today, Porto is ranked 158<sup>th</sup> in the world in the 2021 Traffic Index, with a congestion level of 23%. That means a 30-minute trip will take 7 minutes longer when compared to free-flow conditions. After one year, people have wasted an estimated amount of 52 hours stuck in highly pollutant traffic.

Although there have been improvements in the past couple of years - the congestion level dropped 8%p since 2019 -, there is still an urge to reduce road traffic and CO<sub>2</sub> emissions, thus improving the quality of life for its citizens.

## 🔢 Data

To build our solution, we used the following data:
* *[TIP Rodov and TIP Ferrov](https://wdl-data.fra1.digitaloceanspaces.com/porto/InterMunicipality.zip)* Entry and exit validation data (TIP) on road and rail public transport. These datasets were provided by WDL on the challenge 'Predicting the Flow of People for Public Transportation Improvements'.
* *[E-Scooter Transport Data and E-Scooter Location Data](https://wdl-data.fra1.digitaloceanspaces.com/porto/Soft-Mobility.zip)* List of E-Scooter parks and trips in Porto. Also provided by WDL.
* *[GTFS for Bus and Metro Stations](https://wdl-data.fra1.digitaloceanspaces.com/porto/Soft-Mobility.zip)* Public transport schedule data in General Transit Feed Specification (GTFS) format. Each file describes a particular aspect of transit information: stops, routes, frequencies, etc. We used this dataset to create features such as the proximity to stops, route diversity, and frequency.
* *[Bike Lanes](https://opendata.porto.digital/dataset/int-igvp-igvp-ciclovias)* This dataset contains all bike lanes in the city of Porto and was obtained from Open Data.

We also manually collected information on points of interest - tourist attractions, colleges, and public schools:
* *[Top 10 attractions](https://www.timeout.com/porto/attractions/portos-top-10-attractions)*
* *[University of Porto](https://www.up.pt/)*
* *[Public Schools](https://www.cm-porto.pt/sistema-educativo/rede-escolar-do-porto)*

## 🧮 Methods and Techniques
***1. Prepare and Explore the Data***
We started by splitting Porto into a simple grid and studying the geographical distribution of factors that influence the usage of soft mobility by mapping them to each square of the grid. Some of the visualizations can be seen below.

***2. Identify Most Influencing Factors on the No. of Scooter Trips***
We used these factors of influence as features to train an auxiliary model that classifies each zone into 'low number of (soft-mobility) trips' or 'high number of trips'. We only used zones that currently have a single drop-off zone to avoid bias. By analyzing the feature importance, we assigned a weight to each feature based on how useful they are at predicting the target variable. This way, we could identify which zones with one drop-off zone have a higher number of trips than others and why.

We then calculated a score for each zone as a linear combination of each feature and its respective weight: zones with the highest the score are the ones where a dropoff zone will generate more trip starts.

***3. Drop-Off Placement Optimization***
Based on this information, a *PuLP* linear optimization model was built to maximize the total score of the city (sum of scores of zones with drop-offs). To make sure the drop-offs are spread across the city, the model was restricted by a minimum number of drop-offs per parish and a maximum number of drop-offs in a certain radius based on the most travelled distances by scooter.

## 💡 Main Insights
* ***Points of Interest (POI)*** We considered essentially three types of POI according to who we assume to be the main target of soft-mobility solutions. The University of Porto consists of 14 colleges spread across three university campuses: Polo I - Downtown, Polo II - Asprela, and Polo III - Campo Alegre. We can also see that most tourist attractions are located downtown, overlapping one of the campuses. Regarding public schools, these are spread out across the city.
![Points of Interest](https://i.imgur.com/Rql3JXR.png)
* ***Bike Lanes*** We thought it would be interesting to consider the proximity to bike lanes as a factor of influence. We only estimated the proximity to existing bike lanes (green paths). In the future, it would be interesting to incorporate the ones that are being planned (grey paths).
![Bike Lanes](https://i.imgur.com/Qg46vDd.png)
* ***Number of Bus and Metro Trips*** We visualized the number of vehicles that pull into a bus stop (upper figure) or metro station (lower figure) each day. We can see which bus routes have a higher frequency and which areas of the city they serve.
![Number of Trips](https://i.imgur.com/LMpJaRx.png)
* ***Entry/Exit Validations*** We also visualized the number of entry/exit validations per hour per bus stop (upper figure) or metro station (lower figure) to have a better understanding of the real flow of people in public transport.
![Validations](https://i.imgur.com/FFsGknJ.png)

These visualizations provided us with some insights into the geographical distribution of factors that influence the usage of soft-mobility. E.g., we noticed some areas simultaneously hold points of interest and are near other traditional public transport, thus being great candidates for drop-off points.

## 🛠️ Product
### Definition
A data-driven decision support system for optimization of soft-mobility drop-off zones in order to maximize the usage of these solutions by the population.

### Users
Porto's management departments for transportation and mobility, when deciding the drop-off zones for the e-scooters.

### Activities
Our solution:
* Predicts scores combining factors that influence the usage of soft-mobility solutions.
* Suggests optimal drop-off points maximizing the usage of the e-scooters.

### Output
A data-driven dashboard that consists of two tabs:

First, the dashboard allows the user to choose a weight for each feature. These weights can be either provided by our classification model or defined by the user based on domain expertise and/or the municipality’s goals. After setting the weights, each zone is assigned a score reflecting the likelihood of that specific location successfully maximizing the usage by the population.

![Dashboard1](https://i.imgur.com/p4mq2oY.png)

Then, an optimization model suggests optimal drop-off points that will maximize these scores, given the problem constraints, which can also be manipulated by the user. You can watch the full demo ***[here](https://www.youtube.com/watch?v=TTKaWskbGfQ)***.

![Dashboard2](https://i.imgur.com/m8w5pEC.png)

If the cost of moving around the drop-off zones is acceptable for the municipality, we strongly advise that this process is repeated from time to time, with the most recent data on soft-mobility trips, since we believe that the model will capture seasonal trends. For instance, during the Winter, the distance to the nearest tourist attraction might have less impact on the score than during the peak season as there is less flow of tourists.

In conclusion, we offer an interactive, flexible, and dynamic solution that helps maximize the usage of the e-scooters throughout the whole year.

## 🌍 Social Impact Measurement

### Outcome
* Increase the usage of soft-mobility solutions by the population.
* Increase the accessability of scooters for the users.
* Reduce road traffic and CO<sub>2</sub> emissions.
* Improve the quality of life of the municipality's citizens.

### Impact Metrics
* Total number of scooter trips.
* Trips started/ended from/in each drop-off.
* Total decrease in car trips in the city. 

### Impact Measurement
* ***Based on model predictions***: Our model estimates an increase on scooter trips by 2,53% (over 10 000 more uses).