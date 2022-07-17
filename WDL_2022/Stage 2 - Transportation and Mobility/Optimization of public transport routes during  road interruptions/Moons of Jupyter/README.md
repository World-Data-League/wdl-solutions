# World Data League 2022

## 🎯 Challenge
Optimization of public transport routes during road interruptions by Cascais Municipality

## Team Name
Moons of Jupyter

## 👥 Authors
* Cristian Castro
* Tejas Choudekar
* Ajit Gupta

## ✨ Introduction (250 words max)
Optimization of public transport in cities is without a question a hot topic. The perfomance of the public transport has direct consequences not only in the quality of life of the citizens of each city, but also in the overall CO2 emissions of an entire country. It is a big challenge to focus on. This type of problem has its own name: „Vehicle Routing Problem (VRP)“. The challenge relies within the size of the problem (an entire city). Considering an entire city, this problem becomes a NP-Hard problem. In simple words this means: Very difficult to solve it to optimality (if an optimal solution can actually be found). 

This project centers around this topic. It aims at optimizing bus routes in Caiscais (Portugal), due to street interventions (interruptions in the normal transit). Considering the actual complexity and size of the problem, we decided to grasp this project step by step. Before considering heavy algorithms, heuristics and other methodologies, our approach and methodology based on Divide and Conquer. Our idea is simply going from general to specific, and includes: 1. Analyze the data for the entire city, 2. Assess the frequency of interventions per street and select one street to perform a local bus route optimization, 3. Use a Shortest-Path Exact algorithm (considering rewards and penalties) to provide an efficient and feasible solution. Our hypothesis is that proving that this approach works for one street and one bus route, it can escalate to the entire city.


## 🔢 Data (250 words max)
Caiscais Transit Data included:
- MNIVP Dataset: Dataset with public interventions between 2014 and 2021, with a total of 6617 registers
- EIXODEVIA Dataset: Dataset with the streets of the city in coordinates (Longitude, Latitude)
- MNCAUTOCARRO Dataset: Bus routes in coordinates (Longitude, Latitude)
- GTFS Datasets: Bus routes and stops in coordinates (Longitude, Latitude)
- POI Data: From Google Maps (Manually) POI data was obtained to check for important areas of the city.

We consider that having gps coordinates of the interventions would help to individualise the "hot spots" for interventions and interruptions. And not only feasible solutions for bus route alternatives can be given, but also the problem can be assessed from the causes of the interventions.

## 🧮 Methods and Techniques (250 words max)
Our methodology is based in three parts:

1. Caiscais Transit Data Analysis: This part involves analysing data using standard python libraries for data analysis (including geodata libraries).

2. Analysis of Street Interventions: This part also involves analysing data using standard python libraries for data analysis (including geodata libraries).

3. Route Optimization on a Single Street:
- An Optimization Model for Shortest Path Problem (STP) (https://en.wikipedia.org/wiki/Shortest_path_problem) using Dijsktra's Exact Algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) is implemented in this part. This implementation considers using the neighborhood selected in part (2) as a network, and the bus route as the subject of optimization.
- Dijkstra's algorithm for STP stands as the base case, in which the routes is optimized only considering minimization of the new alternative route. Then this algorithm was modified to include rewards by visiting the closest points to the original bus route. Then this algorithm is again modified to include also penalties for deviating too much for its original route. This is based on an adaptation of the Orienteering Algorithm (https://www.cs.cmu.edu/~avrim/Papers/orienteering-sicomp.pdf)

## 💡 Main Insights (300 words max)
- Simplification is key. Routing problems escalate exponentially and most problems belong to NP-Hard complexity. So start simple and find generalisations that can be applicable.
- Before implementing complex routing algorithms and heuristics, a good comprehension of the metrics (for reward, costs and penalties) to apply for finding new feasible routes are needed.
- Our approach, based on a system of one bus route in a simplified network where only one city is intervened proved to be a good model for the entire problem. It needs to be escalated and planned to grow until the scale of the problem is the desired one.
- More data is always good to tackle public transport routing problems. Nonetheless, there is space for improvement. With 6516 reported interventions, it was not possible to analize root causes and to study this issue on a finer resolution. Although these data is great for this approach, further improvement would include to have gps coordinates for each event. In this way not only feasible solutions for alternative bus routes can be found, but also identified geospatial patterns in interventions. This can open new areas and objectives of study.

## 🛠️ Product
### Definition
A methodology that provides an approach to tackle the entire problem.

### Users
Further consulting teams, that need to escalate our findings.

### Activities
* States the feasibility of new routes not only based on shortest distances, but also convenience for the passengers (rewards and penalties for the routes).
* Suggests the course of action and methodology to escalate the solution, in order to include not only bigger areas but more bus routes.
* Provides a clear understanding of the complexity of the problem, and delivers efficient solutions that solve the problem as good as possible.

### Output
Alternative bus route given a cut or interruption in the studied street.

## 🌍 Social Impact Measurement
### Outcome
By using rewards and penalties, our methodology seeks to reduce the social discomfort by public transport re-routing when interruptions occur. Our solutions plus good information and planning, make this possible. The algorithm provided is very sensitive to these metrics (rewards and penalties to the new bus routes), which can be adapted to capture social discomfort by the municipality.

### Impact Metrics
* Deviation of bus route length less than 5% of its original route length when a street is interrupted.
* Deviation of bus route stops less than 5% of its original route stops when a street is interrupted.

### Impact Measurement
The alternatives bus routes comply with the constraints, as our approach is very sensitive to the definition of these metrics. 

Example:
* Our methodology has as constraints:
- Deviation of bus route length less than 5% of its original route length when a street is interrupted.
- Deviation of bus route stops less than 5% of its original route stops when a street is interrupted.