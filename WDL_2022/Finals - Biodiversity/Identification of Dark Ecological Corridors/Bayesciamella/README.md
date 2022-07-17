# World Data League 2022

## 🎯 Challenge
*Identification of Dark Ecological Corridors*

## Team Name
Bayesciamella

## 👥 Authors
* Alfredo Petrella
* Claudia Cozzolino
* Natascia Caria

## ✨ Introduction (250 words max)
Artificial light at night (ALAN) has been nowadays recognized as one of major human burden on environment. Recent estimates have shown a 24% increase in light pollution in the UK between 1993 and 2000: it is a real environmental emergency that puts global biodiversity at risk, altering the circadian rhythms and habits of many animals.
Bats, as strictly insectivorous nocturnal animals,revealed to be one of the most vulnerable species for this phenomenon. Light pollution expecially reduces their foraging opportunities as well as their reproductive and social behaviors.
Ecological interventions should be implemented worldwide to curb this effect. To this purpose, the city of Bristol, one of the largest city in South West England, has declared climate and ecological emergencies and is taking concrete actions to meet to reduce human burden on nature. To assess the impact of lighting on bats and insects, the Bats and Lighting Research Project was initiated in 2007. The local council has planned to create dark ecological corridors where bats can thrive and move. Street lighting will be controlled by a Central Management System (CMS) which should be smartly programmed taking into account bats needs as well as public security.


## 🔢 Data (250 words max)
We exploited the data provided by the Bristol Regional Environmental Records Centre and the Bristol City Council:

* Streetlights in Bristol (2022)
* Data on bat populations in Bristol (1923 - 2021)
* Data on populations of Moths (1968 - 2021)
* Records of green alley species found in Bristol (2015-2016)

These data allowed investigation of where it would be best to define dark corridors and then switch off the lights to reduce ALAN.
However, we also needed data to understand where it would be best to avoid turning off lights to ensure safety on the streets.
For this reason, we also considered the following external datasets:

* Bristol's amenities, public, and transport services from Open Street Map [https://download.geofabrik.de/europe/great-britain/england/bristol-latest.osm.pbf](https://download.geofabrik.de/europe/great-britain/england/bristol-latest.osm.pbf)
* Traffic accidents from Open Data Bristol [https://opendata.bristol.gov.uk/](https://opendata.bristol.gov.uk/)
* Criminality rate at ward level from Open Data Bristol [https://opendata.bristol.gov.uk/](https://opendata.bristol.gov.uk/)

Open street map data were used as an indicator of the level of frequentation of a given area.
Accident and crime data are used as an indication of the need for additional security measures.

Unfortunately, the available data lack some valuable information that could help improve the accuracy of the study. For example, we have no data indicating whether the places where the bats were observed were roosting, feeding, or breeding areas.
Moreover, the bat and moth datasets have an abundance column, which should indicate how many of them have been spotted. However, in most cases, the numerical quantity is not present, thus only enabling us to roughly estimate the minimum number of bats spotted.


## 🧮 Methods and Techniques (250 words max)
To contribute to the Bats and Lighting Research Project, we started with a simple solution to the problem, gradually increasing its complexity, through the following steps.

1. Looking at the geographic distribution of bats and moths' reports over time, we noticed that locations change significantly over time. Thus, our first step was to apply X-means to extract clusters that would locate the areas preferred by bats and moths. The advantage of this algorithm, compared to the better-known K-means, is that it does not require the number of clusters to be specified.

2. At this point, we tessellated Bristol’s surface with a grid of squares of one-kilometer long sides. Dijkstra’s algorithm has been implemented to determine the Least-Cost path between specific centroids, to identify potential dark corridors. The cost function we defined accounts for the number of bats, moths, street lights, and penalties for switching lights off.

3. Markov chain processes on graphs have been implemented to mimic bats’ behavior. In fact, the state vector after a fixed number of iterations provides a map describing the most likely directions a bat would take based on a reward function, symmetrically obtained from the cost function described above. 

4. Finally, an Agent-Based Model has been designed to try to achieve an overall optimal street lighting configuration. ABM naturally adapts to ecological problems, providing a tool to simulate ecological dynamics in natural systems with entities interacting with each other and with ecosystems.


## 💡 Main Insights (300 words max)
Looking at the spatio-temporal distribution of the bat records, we noticed that few fixed poind persist as years go by, while the vast majority of data points is spread in a non-informative way, at least at first sight.
Looking at the spatio-temporal distribution of the bat records, we noticed that few fixed points persist as years go by, while the vast majority of data points is spread in a non-informative way, at least at first sight.
Nevertheless, considering seasonality trends in the presence of bats, for example with monthly granularity, it is clearly revealed that bats are well hidden during their lethargy, while during summer it is possible to spot three clusters in the city center which, given the period (June-July), could be associated to the so called nurseries, where females are giving birth and are roosting with their offspring.
In addition, considering the distribution of amenities and other nodes obtained from OpenStreetMaps, it is evident that the central area of the city of Bristol is the most urbanized. This same area also has the highest numbers of crimes and traffic accidents records. This suggests that we should be very careful in reducing street lighting there so as not to seriously impact safety in such an exposed setting.

## 🛠️Product
### Definition
A tool that finds optimal dark corridor positions in Bristol.

### Users
The product is strictly addressed to Bristol council members. In a second phase, after the outcome has been validated by experts in the field and by the same members, the product could also be integrated to work automatically with the Central Management System. 

### Activities
The main features of the developed product are the following:
* predicts the locations most likely to be visited by bats in their flights;
* suggests optimal areas in which to reduce public lighting in favor of bat needs without putting public safety at risk;
* provides graphical visualization of the output on Bristol map.

### Output
Best locations where public lighting should be reduced to create dark corridors in Bristol. The solution encompasses bats and moths distrubutions as well as presence of urban and natural elements.


## 🌍 Social Impact Measurement
### Outcome
Achieve trade-off between urban life presence and preservation of bats species, without any risk for humans.

### Impact Metrics
* Number of clusters of bats connected to clusters of moths or other bats (to maximize).
* Percentage of lights to turn off in areas most likely to be visited by bats as a measure of species preservation (to minimize).
* Percentage of lights to turn off in urban area as a measure of public security (to minimize).

### Impact Measurement
In the metrics proposed above, the first two are highly dependent on observed conditions and difficult to predict without real data. On the other hand, for the third one, numerous studies can be found in the literature regarding the importance of street lighting in reducing car accidents and improve overall streets security. For example, the NZTA Economic Evaluation Manual (EEM) quotes a 35% reduction in crashes as the effect of upgrading or improving lighting where lighting is poor.
Lastly, in the previous challange we proved how urban lighting is essential to reduce crime and guarantee a safer and more equal society.
