# World Data League 2023



## 🎯 Challenge
*Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data*


## Team Name
Practicum


## 👥 Authors
* Vasilii Zelenin
* Anton Savinkov
* Ivan Sakov


## ✨ Introduction
The city of Lisbon has experienced a significant loss of inhabitants to its metropolitan area over the last few decades. From the early 1980s until 2017, the population of the city decreased from 800,000 to 500,000. As a result, there has been an increase in car usage, leading to an overload of the road network and parking spaces in the city, decreased safety, and quality of life for its inhabitants. This situation is further exacerbated by a decrease in public transportation use, which accounted for only 22% of journeys starting and ending in the city in 2017. The current modal split needs to be reversed to ensure convergence with the goals of the Paris Agreement, particularly carbon neutrality by 2050.

To achieve this objective, the City Council of Lisbon has set out a plan that aims to promote soft mobility modes, make public transportation more affordable and accessible, and develop an integrated, connected, accessible, and multimodal ecosystem. To implement these measures, it is important to have a deeper understanding of the main flows in the inner city, especially during peak hours. The City Council has acquired data on the number of mobile devices entering and leaving the main axes that connect the city to its metropolitan area, as well as data on mobile devices grouped in a 200x200m grid applied to the city's territory.

The challenge is to use this data to gain a better understanding of how people move between grids during rush hours, predict these movements, and identify potential interventions to improve the commuting experience of people in Lisbon and promote sustainable modes of mobility.


## 🔢 Data 
To build our solution, we used the following data:
* Information on the number of active mobile phones per square of 200m/200m every 15 minutes - Squares of the city of Lisbon
* Number of mobile phones entering and leaving the city every 15 minutes on the 11 main road axes in the city of Lisbon
* Coordinates of the centroids and boundaries of the squares, in the city of Lisbon
* Mapping of the 11 entry and exit points in Lisbon

_Improving the reliability of data would be beneficial, as some periods are missing and some values appear to be outliers. Using a hexagonal grid, such as the H3 grid by Uber, would be preferable for geodata instead of squares._


## 🧮 Methods and Techniques
1. **Prepare and Explore the Data** We started by splitting Lisbon city area into a simple grid and studying the geographical distribution of factors that influence the transition and density of mobile users by mapping them to each square of the grid. Some of the visualizations can be seen below.

2. **Identify the busiest areas.** We decided to conduct data analysis by day of the week and time of day to determine the flow of transit areas that vary over time. To do this, we used various techniques, such as visualizing animated graphs and mapping information.

3. **Simplification of data preparation methods using ML** For this, we used a simple, efficient, and reliable clustering model called MiniBatchKMeans. The dataset used was based on the number of mobile users located or intersecting with a grid cell within a 3-hour time period. After training and clustering the data, we obtained and visualized different clusters on the map.


## 💡 Main Insights 



## 🛠️ Product
### Definition
A dashboard that assists in transit analysis.


### Users
Traffic and mobility analysts.


### Activities
* Fast method for clustering.
* High level of accuracy.


### Output
A GeoDataFrame that can be used both as a standalone tool for analysis and as part of more complex datasets (GTFS, Waze, etc.).


### Scalability
Easy way to apply this model to other areas of interests.


## 🌍 Social Impact Measurement

### Outcome
By visualizing transit areas with high and low levels of traffic, we can better understand the social impact and use this information to identify potential areas for improvement and implement targeted solutions.


### Impact Metrics
This model can be used to evaluate the effects on economic impact on businesses in those areas, such as the level of foot traffic and sales. 
It could also involve analyzing the impact on public transportation systems, such as whether the transit areas with high traffic levels are leading to overcrowding and delays, and how that impacts the daily commute and productivity of people who rely on those systems.


### Impact Measurement
--

