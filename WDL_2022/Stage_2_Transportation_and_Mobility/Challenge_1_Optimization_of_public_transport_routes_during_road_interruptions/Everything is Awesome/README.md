# World Data League 2022

## 🎯 Challenge
*Optimization of public transport routes during road interruptions*

## 👥 Authors
* Elena Viganò
* Emil Pedersen
* Filip Claesson
* Julian Jensen 
* Robert Nyquist

## ✨ Introduction (250 words max)
Optimizing public transport is critical to maintain users trust and use of the system. In the words of Tupac Shakur:

```The most expensive thing in the world is trust. It can take years to earn and just a matter of seconds to lose.```

Our approach is to estimate the delays, using advanced network analysis, looking at the new routes during interruptions. \
Secondarily, we evalute the delay time and experienced discomfort by the residents, based on behavioural studies and as a function of number of replacement busses. \
Thirdly, we build a tool that develops new effective paths for a chosen bus route affected by a chosen disturbance. 

By using our data tools, Cascais would be able to effectively plan and excecute road maintenance, while perserving effectiveness and trust in the public transport system.

## 🔢 Data (250 words max)
* Road network from open streetmap
* List of planned roadblocks in Cascais
* Existing bus routes and time tables for Cascais

## 🧮 Methods and Techniques (250 words max)
We mapped the roads and routes to graphs. We matched the disruption data to the bus routes. \
In this way, we were able to find the routes that are affected by the disruption and that eventually will have roads closed for traffic. \
We choose a disturbance on a route and, by using standard pathfinding and graph algorithms, we recalculate the new shortest routes. \
We also estimate the loss of connectedness for bus routes, using new and different paths. \

Taking these factors into accounts into effect we found the average increase in wait time assuming same or different amount of busses. \
Through established research ( [1](https://ojp-content.s3.us-east-2.amazonaws.com/NHI/Old/BaseImages/2014/04/d.pdf) ), ( [2](https://transp-or.epfl.ch/heart/2020/abstracts/HEART_2020_paper_147.pdf) ), ( [3](https://eprints.whiterose.ac.uk/2062/1/) ), we translated this wait time to accumulated commuter dissatisfaction.


## 💡 Main Insights (300 words max)
- Caiscais should develop a good info system (as good info decrease experienced dissatisfaction by 20%)
- By taking all routes affected into account, we can find new routes for the busses, estimate new accumulated annoyance, and use it to tell how extra busses should best be allocated to the affected routes.
- Through the pathing tool developed, Cascais planners can find the most effective route for a chosen bus route affected by a chosen disturbance. 

## 🛠️ Product
Planning tool for the city of cascais to plan reroutes and additional capacity, to maintain trust in the public transport system

### Definition
Our product is data backed recommendations for the city of Cascais. We provide a model to identify possible reroutes, delays and concrete suggestions on what kind of measures the city should take to make the wait time more reasonable for Cascais public transport users in case of road disruptions.

### Users
Cascais city planners, and bus companies.

### Activities
1. The tool is able to reroute and calculate delay information.
2. The tool allows to estimate discomfort as a function of additional capacity, and precence/absence of accurate information
3. The tool allows planners to reroute a chosen route and a chosen disturbance. 

### Output
A report based on the insights analysis: See our presentation.

## 🌍 Social Impact Measurement
### Outcome
* Prediction of possible delay times for commuters due to change in bus routes caused by disruptions.
* Predition of commuter dissatisfaction.
* Possibility to take action and improve commuter mobile apps for the city of Cascais with the introduction of real time information around the roads affected by the disruption and the realistic waiting times.
* Reduction of commuters annoyance.

### Impact Metrics
- Wait time for users for public transport of Cascais (measured by taking into consideration increased time needed by the bus to follow a new route given that the primary one is closed)
- Accumulated commuter dissatisfaction

### Impact Measurement
* Based our model interpretation: We predict that disturbancies will increase wait time and commuter dissatisfaction
* Based on similar previous studies [1](https://ojp-content.s3.us-east-2.amazonaws.com/NHI/Old/BaseImages/2014/04/d.pdf): We think that improving the mobile app associated with public transport in Cascais to update commuters in real time with the correct estimation of the possible delay, riders won't perceive their wait time to be longer than their measured wait time. This would contribute to decreasing the dissatisfaction of the commuters. 
* In a 1 block cases study at the end of our anlysis, we show how optimally allocated busses can make a huge difference. Ie. when addind 300% extra busses if allocated wrongly users could still experience a **factor 3** increae in annoyance. By allocated it correctly annoyance can be reduced to **below 1** (better than normal due to the increae in busses).