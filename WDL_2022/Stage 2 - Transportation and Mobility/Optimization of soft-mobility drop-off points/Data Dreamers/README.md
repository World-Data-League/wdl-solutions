# World Data League 2022

## 🎯 Challenge
*Optimization of Soft-Mobility Drop-off Points*

## Team Name
Data Dreamers

## 👥 Authors
* Nikhil Kulkarni
* Roney Mathew
* Luckshan Sivakumar
* Sourabh Hujare

## ✨ Introduction (250 words max)

* The city of Porto is the 2nd biggest city in Portugal with an estimated population of just 231,962 people in a municipality with only 41.42 km2.It is also a top tourist destination. However, Porto has a bad traffic situation, ranking 158th in the world in the 2021 Traffic Index. Porto has recently adapted e-scooters into its public transport ecosystems to help reduce traffic issues and pollution due to automobiles but there are issues of randomly abandoned e-scooters and hence drop-off zones were also created.

Increasing the use of e-scooters benefits the traffic situation and the environment and therefore for this purpose we must make drop-off points more efficient and easy to find. Approximately 500 e-scooter trips take place per day in Porto and if more people do it the better for the city.*

## 🔢 Data (250 words max)

* The data sets used were E-Scooter Transport Data, E-Scooter Location Data, both of which were provided by WDL and the external data we used were from OpenStreetMaps for POIs data and Shape file data using Qgis tool.
We wanted to use the bus schedules data as well but since that data did not have location data in it we hesitated to use it. If bus schedules data is enriched with location data, it will help us analyze behavior patterns of people regarding soft mobility usage eg: People might use e-scooters more in an area where the frequency of buses is less, etc. This can give us insights into prioritizing certain bus stop locations.*

## 🧮 Methods and Techniques (250 words max)

* We did extensive feature engineering to come up with important metrics or KPIs (Key Performance Indicators) for the entire drop-off point set and for individual drop-off points as well. The KPIs we defined helped us to validate our optimization model and they also form important features of the product.*
* We used K-means clustering to help us know the locations where clusters were naturally forming and then combining it with external data from openstreetmap.org helped us understand factors causing these clusters.*
* We used mixed integer programming to formulate an optimization problem that picks 210 drop-off points respecting all the constraints. Results show that the drop-off points picked by the model perform better on our KPIs.*

## 💡 Main Insights (300 words max)
 
* 1) After clustering e-scooters drop-off locations and using external data such as bus stop locations, party places, railway station, etc we found that a lot of clusters are formed near bus stops and tourist attractions. (No of clusters at bus-stops > No of clusters at tourist locations)
2) However, the number of e-scooters dropped-off at tourist locations is more than double the number at bus stops. Therefore it is most likely the tourists who drop-off them at these non-drop-off point locations.
3) The metrics we designed show that some drop-off points are rarely used (ex: those in the outskirts of the city) and some are heavily overused (ex: those in the heart of the city).*

## 🛠️ Product
### Definition

**Product 1 : An application that helps in planning drop-off point locations in the city.**

**Product 2:  A dashboard to monitor performance of existing drop-off points.**

Product 1 will be referred to as an Application and Product 2 will be referred to as a Dashboard from now on.

### Users

Municipal authorities and e-scooter companies use the application to better plan the location of drop-off points in the city and their capacities as well. They also use the dashboard on a day-to-day basis to monitor the performance of the drop-off points.

Public users of the Dashboard product are possible if it's published online or if it is displayed on digital screens on the street in order to bring awareness to the issues in the city due to e-scooters and thereby can also encourage people to improve the metrics of drop-off locations.
### Activities

* Application recommends a set of high performing e-scooter drop-off locations with capacities to establish in the city. It also predicts various performance metrics for them.
* Dashboard shows live performance metrics such as efficiency & utility of a drop-off point and overall efficiency of the entire drop-off points network.

### Output

The application product outputs a set of high performing drop-off points on a map with their suggested capacities. It also predicts various metrics such as efficiency and utilization of the new points.

The Dashboard product outputs live key performance indexes of drop-off points in different locations in the form of bar/pie charts.

## 🌍 Social Impact Measurement
### Outcome

To increase the usage of drop-off points so that e-scooters in the city are better managed and thus help people find e-scooters easily when needed, which contributes to less traffic on the roads and less automobile induced pollution in the city.

### Impact Metrics

* Average distance from the actual drop-off locations to their nearest Drop-off points.
* Metrics defined in the notebook, such as : Efficiency and Utility of Drop-off points.
* Average number of times each e-scooter was used per week.
* Average transportation cost of putting abandoned e-scooters back into points by companies.

### Impact Measurement

* *Based on model predictions* : Our model estimates an increase in performance efficiency of 6.8 % for the drop-off points network in the city.
