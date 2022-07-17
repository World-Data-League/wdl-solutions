# World Data League 2022

## 🎯 Challenge

Optimization of soft-mobility drop-off points

## 👥 Authors

Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.
Luís Ventura
Pedro Leal
Aníbal Silva

## ✨ Introduction (250 words max)

According with censos 2021, Porto is approximately home to 230 thousand habitants, where 30 thousand are aged between 0-24 and 121 thousand between 25-64 years old. Since there are many people that work in Porto from close towns, we can safely assume that the usage of Porto's street is overwhelmed. Also, it is one of the most touristic cities in the world, ranked at 32th with 2.5 million annual visitors acccording with [this source](https://thesavvybackpacker.com/most-visited-cities-in-europe/).

Taking this factors into account, one of major problem regarding mobility in Porto is traffic. Clearly, the implementation of bus and metro stations are not enough. One reason for this is that the closest station to a given location can still be far away and by that token, a given person still might prefer to use his private vehicle. One of the possible problems to overcome this issue is to implement soft-mobility vehicles drop-off sites around the city, the question lies in what are the optimal places to insert them.

## 🔢 Data (250 words max)

Explain what data you used (both provided by WDL and external) and improvements you suggest to those datasets. Explain how those improvements would lead to a better solution.

We have used the original Bus and Metro GTFS datasets, as well as the E-scooter ride and park datasets. As a complement, we have also included [*Census* data](http://mapas.ine.pt/download/filesGPG/2021/municipios/BGRI2021_1312.zip) from the Portuguese National Institute of Statistics and amenity data from [*Open Street Map*](https://www.openstreetmap.org/#map=5/51.330/10.453).

Assuming that the e-scooters are a complement to the current public transportation network, we decided to analyze what were the busiest bus and metro stops and use this as *hotspots* (i.e, points which likely require a scooter park) in our model. We first attempted to use passenger *Ticket Validation* data (metro and bus) from the third challenge. This, however, proved to be inefective due to Covid.

Therefore, as a measure of passenger volume, we instead used the average number of bus/metro rides during a day through a given stop. This should be a *proxy* for volume, as the transportation company (STCP) likely assigns vehicle frequency proportional to the number of passengers in a given route. However, this proxy fails if there are inefficiencies in the system - e.g, there are stops for which the few passing buses are packed and stops for which the frequent buses are half-empty.

## 🧮 Methods and Techniques (250 words max)

In our view, our scooters should be integrated with the current transportation network, but closely linked to the amenities that young people are likely to use. Therefore, we extracted amenity data from *Open Street Map* and use this to compute an **amenity importance score**. This goal is that sites with a larger score would be assigned a larger number of e-scooter parks.

*Amenity score*

We select a subset of amenities which are likely to be overused by the target population - universities, schools, fast-food restaurants, ... - and assign an importance weight to each. We then compute the distance in Km from the point of interest (POI) to the amenity and generate a score using:

$Score_{Amenity}^{POI}(Weight, Distance) = Weight \times f(Distance)$

For the *amenity score* of Model 1 - call this standard amenity score - we have used $f(Distance) = \theta(Threshold- Distance)/(reg + Distance)^2$, where *reg* is a regularization term and *Threshold* guarantees that only amenities sufficiently close to a POI are considered.

For the *amenity score* of Model 2, the points of interest are the stops. Therefore, we want to penalize amenities that are too close to these - because we want the scooter parks to be close to a bus stop which *itself* is **not at walking distance** of an important amenity. To that effect, we use $f(Distance) = \theta(Threshold- Distance)Burr(c,k)$, where $Burr$ is the [Burr distribution](https://en.wikipedia.org/wiki/Burr_distribution).

*Modeling*

We propose two preliminary models:

Model 1 - Use weighted K-Means in a user-defined grid:
1. Split Porto in a grid of points. For each grid of points, compute the associated population using the *Census* data.
2. Compute an amenity score for each point in this grid. In this particular case, we include bus/metro stops as amenities.
3. Use weighted k-Means - with the number of clusters equal to the number of parks - to design a rough distribution of parks, to be adjusted later as *per* the constraints of the problem (dispersion of parks, geographical considerations, ...)


Model 2 - Use weighted K-Means on the bus/metro stops:
1. Determine the level of usage of bus/metro stops.
2. Compute a *modified* amenity score of each bus/metro stops.
3. Apply a weighted clustering algorithm to the stops - with the number of clusters equal to the number of parks - where the weights are a combination of
    * Positive (reward) weights: Average number of rides, amenity score;
    * Negative (penalty) weights: Density of bus stops - if there is a large density of stops, it is possible that the transportation network is well-connected and there is less need for the scooters.


## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.

0. Why it is not possible to use validation data as user volume metric (see Fig 1 of *Visualisations* in the submission notebook).

1. Generated an amenties map for the city of Porto (see Fig 2). This allows us to understand where the young users of the transportation network are likely to go. However, Open Street Maps is likely missing venues. Later, we used this to compute an amenity score.

2. Determined the ride volume per bus/metro stop and represented it in the map of Porto. This allows us to understand which areas of Porto are currently being well targeted by public transport and which are not. The center of Porto comes out as the busiest (see Fig 4 in *Visualisations* in the notebook). We also figured out that the metro dataset has missing ride data for the yellow line (line D).

3. With regards to the e-scooters:
    1. Generated an heatmap for scooter rides, which allows us to understand where the users are riding the scooters;
    2. Computed how many scooters have been decomissioned since the program started. This is relevant for policy makers because, for scooters to be an alternative to traditional transportation, they have to be reliable;
    3. Computed the distribution of ride lengths to check our hypothesis. There are plenty of long rides, so certainly some people are using them as a replacement of bus/tram, which would refute our hypothesis. However, we are unsure if using a constant average ride velocity for all trip lengths is reasonable - our expectation is, as the rides become longer (in time), users take more breaks such that their average speed goes down and with it, the traveled distance (see Fig 5);
    5. Checked the start and end times for the rides (See Fig 6);
4. We found that using weighted KMeans clustering to define the position of the scooter parks is not sufficient as the parks are too spread across Porto. A different clustering approach is likely required.

# 🛠️ Product
### Definition
A e-scooter distribution model that accounts for public transportation user patterns and their likely points of interest.

Define in **one sentence** what product(s) could be built out of the code you produced.
This model would allow policy makers to understand what happens when the number of parks is adjusted. For example, could it be minimized while retaining a large total amenity score? A smaller number of scooter parks is easier to maintain, requiring less resources in distributing the scooters, thereby reducing the carbon footprint. 

### Users
Policy makers at the city-hall level understanding if more scooter parks are needed to address mobility issues and managing partners of the e-scooter maintenance company, which can add their own restrictions to the current set of weights.


### Activities
* Analyse changing dynamics in the transportation network and assess what can be improved by adding/removing scooters from certain city locations.



### Output
Visualization of the current scooter parks and integration with the transportation network.



## 🌍 Social Impact Measurement
### Outcome
Create a system that leads to a more integrated transportation network for the user, using mostly public transport. This creates conditions for users to dismiss the need of a personal vehicle, thereby reducing congestion and carbon gas emissions. 


### Impact Metrics
* Amenity score
* Number of scooter rides per time of time, checking if it its coordinated with bus/metro schedules
* Reduction of carbon footprint
 

### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.

Example:
* *Based on model predictions*: Our model estimates a decrease of 6 minutes of the average dispatch time and a decrease of the average distance of 200 meters
* *Based on proxy products*: Similar studies in other cities show that the dispatch time can be decreased by as much as 13 minutes, depending on the traffic intensity of that city.