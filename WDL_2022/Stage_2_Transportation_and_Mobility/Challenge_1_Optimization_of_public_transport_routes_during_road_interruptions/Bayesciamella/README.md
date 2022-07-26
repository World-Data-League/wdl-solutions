# World Data League 2022

## 🎯 Challenge
*Optimization of public transport routes during road interruptions*

## 👥 Authors
* Natascia Caria
* Claudia Cozzolino
* Alfredo Petrella

## ✨ Introduction (250 words max)
In order to improve the effectiveness and the reliability of public transport, the municipality of Cascais is committed to a challenging objective: to try to improve the service of public transport when usual routes are interrupted by interventions. Road works can be of different types, such as water, electricity, gas, or other maintenance. And these works can cause roads to be blocked for hours, days, or even weeks. As a result, the passengers face constant delays or cancellations of trips, and they start lacking confidence in the service. Awareness of trends and an effective rerouting solution are essential to enhance reliability in the public transport system. Thus, we want to help the municipality of Cascais to identify locations and periods where maintenance is most often carried out and provide a solution for reorganizing the road network to cope with changes in the road system.

## 🔢 Data (250 words max)
As the data provided were many and highly articulated, we mainly used the data provided by WDL:
* [GTFS Public Transport Network of Cascais](https://dadosabertos.cascais.pt/dataset/gtfs-mobicascais)
* [Interventions in public roads](https://dadosabertos.cascais.pt/dataset/obras-de-intervencao-na-via-publica)
* [Bus Routes](https://dadosabertos.cascais.pt/dataset/carreira-de-autocarro)
* [Road Network](https://dadosabertos.cascais.pt/dataset/eixo-de-via)

One of the problems encountered was that the road intervention data did not have the coordinates associated with the intervention site. For those occurring at bus stops it was possible to match the geolocation, but for the others we had to use the Google Maps API service, with the credits provided by WDL.

A useful but unavailable piece of data could have been a dataset containing records with the actual arrival timestamps of the buses at the stops. This would have made it possible to understand which stops are most affected by road interventions in terms of delay with respect to the expected arrival time.

With this data on hand, it would also have been interesting to study the effect that weather conditions have on traffic. Thus suggesting different rerouting according to the weather. In the passengers' shoes, we would never want a stop to be moved too far away, forcing to walk further in the rain.

## 🧮 Methods and Techniques (250 words max)
We approached the problem one step at a time, starting with the simplest cases and gradually adding degrees of complexity which the model can handle.
We considered a generic trip and, at first, an interruption involving a single stop.
Taking into account the fact that fewer changes, generate more credibility for a usual passenger, we force the bus to travel the routes set by its schedule up to the one before the road interruption. At that point, using Dijkstra's algorithm, we search for the minimum path, outside the usual bus trip, allowing to reach the node subsequently available.
However, it may happen that this alternative path does not exist! In this case, by means of the Google Maps API services, we search for the shortest driving mode route, narrowing the search field to the 5 stops closest to the broken one.
We have also considered the case of forcing the crossing of a node outside the usual route. In this way we guarantee that the stop is not completely skipped, but replaced, thus reducing the maximum distances between consecutive stops.
Finally, we tested the model with a case with two road breaks. In general, the model should work in the event of a generic number of outages.

## 💡 Main Insights (300 words max)
Looking at the distribution of the interventions on the Cascais map it is evident that the area near the coast, in particular in the south west, is the most subject to interventions. The most frequent type of work is that of maintenance of the water supply. The parish with higher overall number of interventions is U.F. Cascais e Estoril and the stops within Rua Joaquim Ereira, in the same parish, are the ones more affected by works on road. In general, looking at the time series per parish, we see a slightly increasing trend over time, highlighting the urgency of finding an effective solution to the problem.

## 🛠️ Product
### Definition
A platform which optimizes public transportation in presence of traffic interruptions on the route, promotes physical activity through gamification and gathers users' sentiment information about the implemented solution.

### Users
On one hand, bus drivers use the dashboard to choose alternative paths avoiding traffic interruptions while granting an optimal stops' coverage; on the other hand, public transportation users (passengers) are informed on temporary service modifications and motivated to reach the nearest alternative stop through gamification.

### Activities
* Suggests the optimal alternative route(s) to the bus drivers to avoid interruptions while granting an high quality service.
* Suggests the optimal walking path to the new nearest stop to the passengers.
* Motivates the passengers to follow the dashboard advices, thanks to the presence of a fitness leaderboard and to motivational sentences about the health benefits of physical activity.
* Improves users' sentiment and sympathy, making them more tolerant with respect to the inconvenients.

### Output
Our product outputs the best alternative route handling, in real time, possible route interruptions due to various anomalous events. We have represented the bus route on a direct graph, whose nodes represent all city bus stops and edges are associated to the currently followed paths. When an interruption occurs, nodes which are close to the given road maintenance coordinates and their adjacent edges are dropped, and the graph is locally enriched with possible alternative paths between the closest stops. At this point we used the Dijkstras’s algorithm to find the best path between the line stops remained disconnected. In doing this, the algorithm is allowed to consider the closest alternative stops depending on the distance returned by the Google Maps Directions API. A similar approach, quite simple a priori, can handle multiple bus routes, resulting in an improvable tool with a measurable impact.

## 🌍 Social Impact Measurement
### Outcome
Improving our product up to a full service state can help improving users' awareness about the organizational difficulties deriving from the service, fidelize and obtain active contributions from the users themselves (e.g., implementing GPS tracking to predict anomalous traffic and oprimize the alternative paths computation. Moreover, a score board can be implemented to encourage contributions and promote chosing the habit of reaching alternative stops on foot or by bike, sponsoring a healty lifestile.

### Impact Metrics
* Variation of the total length of the path
* Variation of the maximum distance of two consecutive stops
* Change in the number of passengers using the public transport service

### Impact Measurement
In general, we found little literature on the topic of gamification applied to public transport, which suggests a new research direction!
Gamified design has been used in the health field and can dramatically transform people’s health and physical activity levels. One example from the UK is the Beat the Street initiative. In Reading, it has encouraged thousands of residents to walk and cycle for health benefits.[1] Similar techniques are exploited to design an on demand public transportation service, or also implementing Augmented reality indications and checkpoints to be superimposed on the mobile camera output, relying on the potential of this new and catchy technology with well known results.[2]
[1](https://theconversation.com/how-gamification-can-make-transport-systems-and-choices-work-better-for-us-57663)
[2](https://ieeexplore.ieee.org/abstract/document/8286940)