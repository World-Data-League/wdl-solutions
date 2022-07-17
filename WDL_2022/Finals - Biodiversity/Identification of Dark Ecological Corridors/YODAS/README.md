# World Data League 2022

## 🎯 Challenge
***Finals:*** Identification of Dark Ecological Corridors

## Team Name
YODAS

## 👥 Authors
* Cristiana Carpinteiro
* Diogo Polónia
* João Matos
* João Pereira
* Patrícia Rocha

## ✨ Introduction
Artificial Light at Night (ALAN) is a global phenomenon that poses a major threat to biodiversity. Being nocturnal animals, bats are likely to be strongly affected by ALAN in mainly two ways [1]:

1. If the light levels are too high along their routes, it can constrain their movement and restrict their use of commuting, foraging, or roosting areas.
2. When moths or other insects are attracted to the light, it creates a vacuum of insects in the dark areas, thus influencing the availability and abundance of prey to light-avoiding species.

The amount of light pollution increased by 24% in England between 1993 and 2000 [2]. Not all species respond equally to lighting, but light-averse ones include UK’s rarest bat species [3]. In 2020, Bristol was the first city in the UK to announce an ecological emergency in response to the decline in wildlife. One of their goals is understanding the current ecological network and how to improve it.

With this in mind, the Bristol City Council challenged us to create an optimization algorithm that connects all habitats through dark corridors, thus mitigating the impacts of ALAN on bat activity and movements.

## 🔢 Data

Datasets provided by the WDL organization (which can be downloaded [here](https://wdl-data.fra1.digitaloceanspaces.com/bristol/2022_05_30_bristol_datasets.zip)):

* ***Streetlights*** contains information on the location and type of streetlights in Bristol (2022).
* ***Bat records*** contains data on bat populations in Bristol (1923-2021). Includes information such as the location of sightings, the name of the bat species and the abundance. However, bat records within the last 10 years or bat records that identify roosts were obscured to 1km in resolution for security purposes.
* ***Moth records*** contains data on *Noctua pronuba* (Large Yellow Underwing moth) populations in Bristol (1968-2021).
* ***Wildlife corridors*** contains data on current wildlife corridors in Bristol.
* ***Green alley species*** contains records of plant species in Bristol (2015-2016).

Datasets from Open Data Bristol:

* ***[Watercourses](https://opendata.bristol.gov.uk/explore/dataset/surface-water-sampling-points/table/?location=11,51.46179,-2.60261&basemap=jawg.streets)*** contains the location of watercourses in Bristol.
* ***[Bus stops](https://opendata.bristol.gov.uk/explore/dataset/bus-stops/map/?location=11,51.43732,-2.73251&basemap=jawg.streets)*** contains the location of bus stops in Bristol.
* ***[Traffic count](https://opendata.bristol.gov.uk/explore/dataset/fact-traffic-counts/table/?disjunctive.countdevicedescription&disjunctive.link&sort=rollupdatetime)*** contains the hourly traffic flow data from SCOOT traffic counters in Bristol.
* ***[Population density](https://opendata.bristol.gov.uk/explore/dataset/population-estimates-time-series-ward/table/?disjunctive.ward_2016_name&sort=ward_2016_code)*** contains population estimates by ward in Bristol (2002-2020).

There were other datasets (e.g., records of older buildings and trees or disused tunnels where bats usually roost) that we ended up not using because they either did not have enough data for Bristol or lacked spatial information (coordinates, grid reference).

***Possible improvements:***

Since we were asked to take into consideration the safety of pedestrians and/or road users, more human-oriented data (commercial/residential areas, streets, nightlife places, buildings' contruction year) would be welcome.

Regarding the biological data, since the species of bats in Bristol are generally small and the moth species, *Noctua pronuba*, is a large moth, there may not exist a clear and linear relationship of predator-prey. 

## 🧮 Methods and Techniques
#### ***1. Prepare and Explore the Data***

We started by splitting the city of Bristol into a hexagonal grid. Each hexagon was associated with a curated set of animal and human-oriented features. Some visualizations can be seen below. Given the bat records, we also formed clusters depicting high bat activity spots that we want to connect through dark corridors.

#### ***2. Create Scores***

We then created 3 different scores: animal "discomfort", human "discomfort" and cluster scores. Each score is a linear combination of all respective features weighted by their importance. Although the first two scores are static, since the number and location of bat sightings vary throughout the year, we also calculated a cluster score for each season and year, as predicted in a 10-year frame, discussed below.

#### ***3. Predator-Prey Analysis***

Biological populations are dynamic and cyclically evolve as trophic relationships take place. The ***Lotka–Volterra*** equations, also known as the predator–prey equations, are a pair of first-order nonlinear differential equations, frequently used to describe the dynamics of biological systems in which two species interact, one as a predator and the other as prey [4]. With this premise, we:
* Fit all our bats and moths sightings data to the model, with a downhill simplex algorithm.
* Apply this model to each cluster, in which we consider the learned parameters, as well as the total bats and moths per cluster as boundary conditions, to produce predictions throughout the next 10 years.
* The cluster score is updated for each cluster, with the predicted data.

#### ***4. Dark Corridors Optimization***

In this section, 3 steps are followed:
* Dijkstra's Algorithm [5] computes the least costly paths between all nodes (bat clusters). The cost minimizes the discomfort for both humans and animals, while prioritizing clusters with more importance.
* Minimum Spanning Tree Algorithm [6] finds the best way to connect all the intended nodes, amongst all possible paths.
* The zones of the dark corridors are crossed with the light positions to shut down all lights inside them.

#### ***5. Central Management System***
We produced a Python package with a dashboard, availabe to download with pip. Instructions on how to use are [here](https://github.com/joao-afonso-pereira/YodasLib):
```
pip install git+https://github.com/joao-afonso-pereira/YodasLib.git
```

We also built an app, which can be used for other cities or animals, that you can access [here](https://drive.google.com/drive/folders/1Tlgi7uc7n5IB7NKZArXi6nPkIJvfcZLv?usp=sharing).

## 💡 Main Insights

***Feature Extraction:*** After some research on bat's activity and movement, we chose a set of ***animal-oriented features*** including the number of prey sightings within a specific radius or the proximity to relevant places (watercourses, trees, habitats). To ensure people's safety, same logic was applied and we chose a set of ***human-oriented features***. An example of such features can be seen below:

![](https://i.imgur.com/lLUs2Io.png)

***Seasonal Clustering:*** Regarding the bat records, we decided to explore seasonal variations and noticed that the ***number and location of sightings vary throughout the year***. Most sightings happen during Summer, which is when they become most active (breeding and feeding). During Winter, bats usually hibernate sheltered inside their roosts.

![](https://i.imgur.com/Er9VnKt.png)

As a result of these seasonal variations, we decided to calculate different clusters and their respective scores for each season:

![](https://i.imgur.com/1UsZkWX.png)

***Predator-Prey Analysis:*** We also used the ***Lotka-Volterra equations*** to describe the dynamics between the two populations that interact via predation and predicted their evolution in each cluster for the next 10 years. The phase portraits for each cluster can be seen below. If the curves are closed, it means that the system is periodic and the cycle will continue *ad infinitum* with the growth and decline of both populations:

![](https://i.imgur.com/G5jQ74h.png)

***Seasonal Lighting System:*** As a consequence of the seasonal variations, ideally, there should be different dark corridors in each season to accomodate the changes of high bat activity places throughout the year.

![](https://i.imgur.com/7JnjaET.gif)

***Yearly Lighting System:*** On the other hand, according to our predictions, the yearly lighting system does not change that much, validating our solution on the long term.

![](https://i.imgur.com/A1K95Zi.gif)


## 🛠️ Product
### Definition
A Central Management System that can assist a user in finding dark ecological corridors connecting places of high bat activity.

### Users
Bristol City Council and/or any entity responsible for taking measures against the decline in wildlife.

### Activities
Our solution:
* Creates animal and human-oriented scores.
* Finds high bat activity places in each season.
* Predicts the evolution of populations in these places.
* Suggests **dark ecological corridors** to connect such places, that can be valid for 1 year-long, each season, and for predictions in the next 10 years.
* Suits new species, different cities, different features, weights and scores, and future restrictions.

### Output
Our product outputs an updated .csv file of Bristol streetlights recommending which lights to turn off and a plot of the new lighting system at night.

## 🌍 Social Impact Measurement
### Outcome
Mitigate the impact of ALAN on bat activity and movement.

### Impact Metrics
We assess the impact of our solution with 3 main metrics:
* Increased Bat Activity, per year (considering that horseshoe bats have a reduction in activity by a factor of 4 [7]).
* Saved CO2, from shut down lights, every year (with the premise that 100W lights run an average of 3940h per year [8], and that, in the UK, in 2020, 76.7% of the energy derived from unsustainable sources [9]).
* Financial Saving in electricity, from shut down lights, every year (taking into account that each light costs £6.25 per season [10]).

### Impact Measurement
We estimate that, per year, we can:
* Increase bat activity, overall, by 10%
* Save about 185 tons of emitted CO2
* Save about £25,000 in electricity from shut down lights

## 👓 References
[1] Voigt, Christian C., et al. *Guidelines for consideration of bats in lighting projects*. Unep/Eurobats, 2018.

[2] https://www.batcon.org/article/hiding-from-the-lights/

[3] https://www.bats.org.uk/about-bats/threats-to-bats/lighting

[4] https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations

[5] https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

[6] https://en.wikipedia.org/wiki/Minimum_spanning_tree

[7] Pauwels, J, et al., *Adapting street lighting to limit light pollution’s impacts on bats*, Global Ecology and Conservation, 2021

[8] *U.S Energy Information Administration*, EIA, accessed in June 14, 2022

[9] *UK Energy in Brief, 2021*, Department for Business, Energy & Industrial Strategy

[10] *Street lighting facts*, Shropshire Council, accessed in June 14, 2022