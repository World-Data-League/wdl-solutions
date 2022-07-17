# World Data League 2022

## 🎯 Challenge
Optimization of Soft-Mobility Drop-off Points

## Team Name
Shiny Pandas

## 👥 Authors
* Imre Boda
* Zsolt Kegyes-Brassai
* Peter Michaletzky

## ✨ Introduction (250 words max)
1st of June, 2020, most likely close to the end of the first wave of Covid-19 pandemic, Porto launched the E-scooter service. [Electric Scooters in Porto](https://www.porto.pt/en/news/electric-scooters-are-set-to-go-and-ride-through-porto-starting-1st-june)
The idea is to help people to take the last mile faster, so they are more willing to choose public transportation, instead of using their cars in order to avoid having to walk. The problem of abandoned e-scooters on sidewalks, bike lanes, roads, parks is well known everwhere. Penalizing users for not dropping their e-scooters off at the designated parkings is one side of the solution. At the same time the city feels the responsibility for placing these parkings at the most used and accessible locations, given a few constraints: a maximum of 210 parkings in total, never closer than 40 meters, each having a capacity of Nx10 places.
To find best (optimal) parking locations, given the above constraints, we proposed an optimization algorithm, moving the parking locations closer to current e-scooter usage. This is a usage data-driven approach, i.e. local policies of serving bus/metro stations, covering less popular areas for marking purposes, etc. are not considered, even though they could be incorporated in our algorithm.
The user of this optimizer receives a dashboard on which approximative recommended parking location modifications can be observed in a map view. Exact locations are to be determined by an expert, who can into account all the regulations and practicalities, in the are that we recommend.

## 🔢 Data (250 words max)

[E-scooter dataset: Soft-Mobility.zip](https://wdl-data.fra1.digitaloceanspaces.com/porto/Soft-Mobility.zip) - including:

    * E-scooter trip origin-destination data (GPS coordinates of start and end points, e-scooter status messages)
        * Improvement proposal: the E-scooter operator has information about mis-parked e-scooters, this is how they can fine the riders. If this information was explicitly added to the origin-destination data, we would not have to guess using likely inaccurate GPS coordinates.
    * E-scooter parking station information (GPS, capacity, station name)
        * Current dataset does not contain information about the number of e-scooters stored in parkings. We could use this information in order to properly dimension parking capacity.
    * GTFS data of the public transportation network of Porto (bus and metro stations, routes, schedules)

[OpenStreeMap](https://www.openstreetmap.org/#map=15/41.1548/-8.6146&layers=O) - as background for our map-based visualizations

## 🧮 Methods and Techniques (250 words max)

First we analyzed the dataset from various aspects, such as number of e-scooter rides in total and per each parking place (utilization), determining whether e-scooters are placed properly in the parkings or they are abandoned at different locations, typical trip duration and distance; distance between parking locations.
We approached the problem of finding optimal parking locations by minimizing a cost function, which takes into account the distance of parked e-scooters to the nearest designated parking. The lower this value, the higher the probability that people will actually drop-off their e-scooters properly at parkings.
Finally we came up with an algorithm to minimize this cost by keeping some of the existing parking places, discarding unnecessary ones and building new ones where needed. This cost definition proves quite heavy in computation demand, therefore we had to find a way to overcome this challenge: we applied a hexagonal grid system, aggregating e-scooter trips within the boundaries of hexagonal cells into a virtual points, thus implifying geo-distance calculations by a factor of 10^2. (Individual GPS positions aggregated up to hex cells with 25m edge length.)
Our 4-steps algorithm allocates parking locations in a step-wise manner, always dealing with locations (hex cells) contributing with the highest cost by allocating parking locations in them. Step 1 and 2 look at e-scooter traffic in individual hex cells. In Step 3 and 4 we also factor in traffic information from neighbouring cells.
The result is presented on a dashboard where indications are given to the user about where in Porto to keep/build/discard e-scooter parkings.

## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.

To illustrate the extent the problem of abandoned e-scooters, we found that in 75% of the cases, e-scooters are dropped-off within 10 meters from designated parkings. (The raw data does not distinguish proper vs. improper placement, we use this criteria to indicate proper placement.) We assumed that such cases were scooter drops at designated parking places. The remaining 25% of the cases represent the abandoned e-scooters that can disturb city traffic and to be taken care of.
We could see 4 months of data only, mostly from off-tourist season; a longer time coverage could result in more accurate model.
We observed ~80k e-scooter trips, of which 22% showed some irregularity / strange behaviour such as

* distance between start and end less than 25 meters apart
* trip time less than 30 seconds
* trip ending with "trip_cancel" event.
These trips were excluded from our optimization algorithm.
Regarding the existing parking places:
* there were 4 pairs parkings hurting the rule of minimum 40 meters between parkings (one can be kept only)
* we saw 7 parkings with zero valid trips

Our hex grid system covers Porto with ~17k cells, of which 2253 cells contain e-scooter traffic, while we have 210 cells with parkings.
The way we define our cost function (e-scooter trip location hex distance to nearest parking) results in a baseline cost of 42124.
Our optimization method brings this cost down to 30530, a reduction of 27% percent, i.e. less likelihood of abandoned e-scooters.

## 🛠️ Product
### Definition

A map-based dashboard that gives recommendations on which parkings to keep, which parkings to close, and approximately where to build new stations.

### Users

Management of the e-scooter service can periodically review parking location recommendations, for a data-driven decision approach.

### Activities

* Geospatial aggregation of e-scooter traffic data
* Step-wise approach for selecting best parking locations, ensuring minimum distance to where the usage demand comes from
* Review of approximative recommendations on a map-based dashboard

### Output

Our map dashboard places parking positions on the map, using coloured hexagonal grid:

* green: keep the parking station within the area of this hex
* red: discard the existing stations
* blue: build new station somewhere within the boundaries of the hex
* grey: hex with e-scooter traffic, and without parking. Opacity is proportional to the logarithm of traffic.
* Dark dots represent existing stations by their exact GPS coordinates.

[Map dashboard](http://peter.michaletzky.gitlab.io/dataproj_public/leaflet_final_dashboard.html)

## 🌍 Social Impact Measurement
### Outcome

We would like to make the e-scooter parkings to be located closer to actual demand; i.e. they are at the most convenient locations. This reduces the likelihood of encountering abandoned e-scooters on sidewalks, bike lanes, city parks, roads, etc., rightfully disturbing non-e-scooter using citizens.

### Impact Metrics

Aggregated distance to nearest parking place in the case of abandoned e-scooters. The closer we build parkings to the places where people drop-off their e-scooters, the higher the likelikhood they will park their e-scooters properly.

### Impact Measurement

Our optimization algorithm decreased the aggregated distance as defined above by 27%. Without going into details of psychology, we can assume we will see a decrease of abandoned e-scooters at similar extent.