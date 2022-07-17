# World Data League 2022

## 🎯 Challenge
Optimization of Soft-Mobility Drop-off Points

## 👥 Authors
* Juan Diego Arango
* Melissa Montes Martin
* Santiago Cardona Urrea
* Irune Lansorena Sanchez
* David Gamba


## ✨ Introduction
The traffic of the city of Porto as it stands today has become a problem for its residents. A resident wastes an average of 52 hours a year in traffic [1]. In contrast, a citizen of Madrid, a city with a population more than 10 times bigger, spends only 41 hours in traffic [2]. This situation is only aggravated by the additional pressure put on public transportation by the influx of tourists in the city. Porto received 3.3 million tourists in 2018 and about 13% of all tourists to Portugal [3]. This number of additional people increases the demand for transportation, and this affects the living conditions of the people of Porto.

The next chart clearly shows the increase in tourism for porto (https://www.worlddata.info/)

![Tourism growth](https://storage.googleapis.com/geoneas-bucket/soft-s2/images/resized/tourism_growth.png)

We GeoNEAS have developed a solution to optimize the parking points for e-scooters across Porto and thus increase their use in the context of tourism and entertainment. This solution would alleviate Porto’s transportation problem as the optimization will encourage the use of the scooter as they would be where they are needed. The increase in the consumption of the scooter service will not only eases the pressure on other transportation means by encouraging both natives and the tourist to move across the city in them but also helps the city’s transition to being more sustainable in its means of transportation.

## 🔢 Data


-[Points of Interest(leisure) of Porto]: (https://www.openstreetmap.org/search?query=porto#map=11/41.1496/-8.6108) Download from OSM using the library OSMNX. The points selected had either one of the following three keys: amenity, tourism, or leisure. Additional filtering was done by omitting labels that were considered unimportant for the problem. It was a parameter in the optimization model. They were used to predict e-scooter demand through the city. In the future, different POIs could have weights considering their importance in the city.

-[Porto’s Road Network]: Downloaded from OSM using the library OSMNX. The lines selected had the key: highway. It was a parameter in the optimization model. They were weighted considering their category in the mobility system. It will be important to organize the road network to have an oficial graph from the municipality because OSM is a collaborative tool and it could have some issues related to typology and connectivity.

-[Porto’s Freguesias Population density]: It uses three sources: The population by freguesia in 2011[4], the area of each freguesia [5], and the population shift in Portugal from 2011 to 2021[6]. It was a parameter in the optimization model.

-[Information about scooters’ position and location]: Scooter’s General Transit Feed, E-Scooter Transport Data, and E-Scooter Location Data Specification provided by WDL.

-[Polygon with the contour of Porto]: Obtained from OSM using OSMNX


## 🧮 Methods and Techniques

Our solution has three components. First, we use clustering to identify potential parking spots, in a manner similar to [16]. This is done by using historical trips information and clustering around the position where the past trips ended. The clustering method used was HDDBSCAN.[7]

**Candidate clusters**

![candidate clusters](https://storage.googleapis.com/geoneas-bucket/soft-s2/images/resized/parking_candidates.png)

For the second component, we estimate the demand in different parts of the city following [17]. We use as training data demand around current parking zones and characterize the area that the parking is in.  developed an explanatory model to predict the demand. This model considers factors such as points of interest, proximity to the sea, population density, and availability of riding routes. With this demand model, we predicted demand on a hexagonal grid that covers the city of Porto.

**Demand covering, darker means less demand**

![Demand covering](https://storage.googleapis.com/geoneas-bucket/soft-s2/images/resized/demand_model_result.png)

The last component is optimization based on [9]. Combining both candidate parking points and demand across the city, we developed an optimization model to assign the candidate parking points such that the demand covered is maximized. This model respects the minimum 40m distance between parking and also considers a maximum distance from the parking location to the demand, which corresponds to an acceptable walking distance for users.[9]

**Optimized points in blue**

![Optimization result](https://storage.googleapis.com/geoneas-bucket/soft-s2/images/resized/optimized_allocation.png)

## 💡 Main Insights

The study of the scooters' travel register showed that the scooters are mainly used for leisure. This conclusion was reached because of various observations. First, most points at the end of each scooter journey were the pier, the beach, downtown, or parks. Additionally, it was possible to see the distribution of travels in time throughout the city. The peak of in the number of travels is in the after-work time. This point further justified the hypothesis that scooters are used in leisure activities and not for work transportation. That made our selection of the points of interest and attributes to model demand focus mainly on leisure-related locations to optimize their usage around those locations.

**Plot with the trip ends in blue and the official parkings in orange**

![trip ends](https://storage.googleapis.com/geoneas-bucket/soft-s2/images/resized/trip_ends_vs_parking.png)

![time distribution](https://storage.googleapis.com/geoneas-bucket/soft-s2/images/resized/trip_profile_per_day.png)

From the demand model results we could interpret the coefficients and found that in general more points of interest, proximity to sea, proximity to center and public transport stops are correlated with higher demand, while population density and big highways are correlated with decreasing demand. These findings also support the hypotheses that the parking zones with the most demands tend to be those of touristic or entertainment interest. One possibility to improve this model is to add more variables related to other aspects of the zone. This could allow for a greater insight into current demand.

With the optimization, we obtained an optimized allocation of parking points which covers 97% of the demand with less than 180 parking zones. In contrast, the current scheme uses 210 parking locations to accommodate 85% of the estimated demand. From this we can find that we could cover an estimated 14% more demand in the optimized setting

## 🛠️ Product
### Definition
Decision support system for urban planning: a location-allocation model for drop-off optimization.

### Users
The end-user(s) of the solution are service providers (Bird, Circ, Hive Porto), and government, or regulatory agencies aiming to optimize the use of currently available resources under citizenship demand requirements.

Users will use the product to create insights on the current use of e-scooters, demand analysis, and achieve right and more informative decisions in terms of drop-off relocation/allocation, rebalancing the inventory of scooters. The ultimate goal will be to promote their use and accessibility under Sustainable Tourism Plan 202-2023[13].

### Activities
Main features of our product:

* Understand current soft mobility and drop-off patterns based on historical journey data.
* Predicts scooter demand in an area. This helps to identify some demand gaps and potential new nest/drop off candidates as well to identify which factors should be optimized (density in terms of
* Optimization model able to accommodate current demand needs under the following capacity constraints: min_distance_dropoffs > 40m, max_dropoff_zones=210). The problem has been formalized as a Location-Allocation Problem (LA).
* Suggest reallocation and/or new drop-off points. Also, identification of some e-scooter rebalancing needs.


### Output

After optimization, we can generate a map of the city with all optimum parking points highlighted in blue. The map can be explored in this [kepler.gl link](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/age87ufktjbohr8/results_allocation_2022-04-21.json)
![Optimized parking points](https://storage.googleapis.com/geoneas-bucket/soft-s2/images/resized/optimized_allocation.png)

## 🌍 Social Impact Measurement

### Outcome
Managers of the scooter services and municipality officials will be able to find the optimum location to place the scooters. We believe this will lead to higher use by residents and tourists. The higher usage will reduce the pressure on the city’s transportation, especially on the last-mile journeys. There will also be the added benefit of reducing the CO2 emissions in the city. This will contribute to a  cleaner, more sustainable, and livable city.

### Impact Metrics
* Number of scooter journeys per day and how they increase against the status quo.
* Percentage of scooters that are correctly dropped in a parking zone.
* Visit increase to relevant points of interest(many of those are businesses related to leisure).

### Impact Measurement
In some successful case studies, 34% of local passengers and 48% of visitors took an e-scooter instead of driving their cars or using Uber, Lyft, or a taxi. [11]. If we translate this number to the case of Porto, the number of visitors that use e-scooter under the current capacity to attend demand is around 1.6 million. Under our optimization procedure, the scooter service can attend to 12% more demand. This would result in 180 thousand more people moving on scooters and easing pressure on the transportation system of Porto.

Additionally, Given that a person in a car emits 404 grams of CO2 equivalent emitted per mile. The reduction in emission per transportation mile would constitute  80. 2 tons. [15]

References
[1](TomTom provided statistics of travel time in Portugal: https://www.tomtom.com/en_gb/traffic-index/portugal-country-traffic)

[2](TomTom provided statistics of travel time in Spain: https://www.tomtom.com/en_gb/traffic-index/spain-country-traffic)

[3](Porto Tourism statistics: https://www.investporto.pt/en/sectors/tourism)

[4] (2011 Portugues census): https://web.archive.org/web/20131204165051/http://www.ine.pt/investigadores/Quadros/Q601.zip

[5] (Data set with freguesia size from the Portuguese census): https://web.archive.org/web/20131109154435/http://www.igeo.pt/produtos/cadastro/caop/download/Areas_Freg_Mun_Dist_CAOP20121.zip

[6] (shift in Portugal's population from 2011 to 2021 census): https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=526271534&DESTAQUESmodo=2


[7]Ester, Martin; Kriegel, Hans-Peter; Sander, Jörg; Xu, Xiaowei (1996). Simoudis, Evangelos; Han, Jiawei; Fayyad, Usama M. (eds.). A density-based algorithm for discovering clusters in large spatial databases with noise. Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (KDD-96).

[8] (Uber’ H3 library): https://eng.uber.com/h3/

[9]Pérez-Fernández, O.; García-Palomares, J.C. Parking Places to Moped-Style Scooter Sharing Services Using GIS Location-Allocation Models and GPS Data. ISPRS Int. J. Geo-Inf. 2021, 10, 230. https://doi.org/10.3390/ ijgi10040230

[10]https://www.theinformation.com/articles/inside-birds-scooter-economics

[11]https://www.bcg.com/publications/2019/promise-pitfalls-e-scooter-sharing

[12]https://findingspress.org/article/19537-can-you-park-your-scooter-there-why-scooter-riders-mispark-and-what-to-do-about-it

[13]http://business.turismodeportugal.pt/SiteCollectionDocuments/sustentabilidade/sustainable-tourism-plan-2020-2023-turismo-de-portugal.pdf

[14] https://github.com/gboeing/osmnx

[15]https://youmatter.world/en/sustainable-mobility-electric-scooters-28897/

[16] Sandoval, R; Van Geffen, C; Wilbur, M, Brandon, H; Dubey, A; Barbour, W; Work, DB. Data Driven methods for effective micromobility parking. Transportation research interdisciplinary perspectives. 2021, 10, 100368. https://doi.org/10.1016/j.trip.2021.100368

[17] Mix, R.; Hurtubia, R.; Raveau, S. (2022). Optimal location of bike-sharing stations: A built environment and accessibility approach. Transportation Research Part A. 2022, 160, 126-142. https://doi.org/10.1016/j.tra.2022.03.022
