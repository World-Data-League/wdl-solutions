# World Data League 2022

## 🎯 Challenge

Identification of Dark Ecological Corridors

## 👥 Authors
* Akshay Punjabi
* Enrico Coluccia
* Pablo Izquierdo Ayala
* Chiara Rucco

## ✨ Introduction

Cities are built for humans but we also coexist with many other species that are (more often than not) forgotten. Creating safe environments for these species is a matter of responsibility and should be and point to be taken into account when making decisions that will undoubtedly impact the lives and customs of these living beings.

One example is that of bats in Bristol. Many bat colonies have been spotted within the city of Bristol. Creating safe dark corridors for these little mammals can be a way of improving their life conditions and assimilating them into a more symbiotic relationship with humans.

We developed a tool to generate these safe corridors with a set of constraints. This tool can be used to simulate many scenarios and aid the decision-makers into taking accurate decisions that benefit us all.

## 🔢 Data

The datasets we utilised are the ones provided by WDL. Our main source is the bats dataset. This dataset contains the coordinates of bat populations within the city of Bristol. 

Using the location of bats as the basis, we can then enrich the model with practically any dataset that contains coordinate points within Bristol. 

For instance, we were provided a dataset containing the location of light sources within Bristol. We can then use this information to then compute the number of light sources between bat colonies, the amount of light per km, etc and all of these parameters can then be optimised. 

Another example would be the green areas dataset. We have the location of green areas within Bristol. We can then use this information to create constraints within our solution to, for example, create pathways that contain at least 1 green area.

We can also use external datasets, such as noise levels within Bristol. As long as there is a spacial reference to the location of the noise, the data can be mapped into the cost function and used accordingly.	


## 🧮 Methods and Techniques

Our solution is quite simple and has the benefit of being completely scalable and reusable. One can adapt it to specific questions at hand and simulate many different scenarios.

This solution is based on a graph that we initially create based on the positions of the bats. We can also cluster the initial positions of the bats to obtain a simplified version of the graph.

We then create the edges of the graph by simply connecting all of the nodes. The important part is the cost function. We give a cost to each edge in the graph. This function is completely customizable and is the key point of our solution. For instance, we can use the number of lights between nodes, the number of green areas, the distance between nodes or a combination of all of them as cost functions and create different scenarios that we can then analyse.

As a last step, we compute what is defined as the Minimum Spanning Tree (MST). This MST is the minimal representation of the graph. We use this as our optimization algorithm to remove edges that have a high cost in the graph and prioritise lower cost ones. For instance, if we want to create pathways with the least amount of light, we can set our cost function to the number of light sources between bat areas and by computing the MST we would obtain a graph that shows the current dark corridors between bat populations. Our solution is presented in the form of a graph.

(When computing distances between points, we use the haversine distance to take into account the curvature of the Earth. This might be negligible for Bristol, but we wanted to keep it consistent towards other problem sets where distances may be way bigger.)

Additionally, we also perform some in depth analysis on the dataset just to understand the distribution of certain variables, such as number of bats or amount of food, over time.

## 💡 Main Insights

The most exciting part about our solution is that it is completely open and flexible. One can add or remove nodes to represent different scenarios (i.e adding nodes to represent places we want bats to go through or removing them to represent places we want to avoid).

The weight function is also completely customizable. It can be as complex as a combination of several metrics or as simple as the distance between nodes. This can then be adapted to the problem at hand to create accurate simulations of the environment.

Finally, one can even remove certain areas within Bristol where we do not want bats or bat corridors and keep them out of the equation.


## 🛠️ Product
### Definition

We provide a graph-based approach that can be used to model multiple real world scenarios. We then use this approach to effectively identify possible Dark Ecological Corridors within the city of Bristol.

### Users

Our product is a ready-to-use tool for Bristol politicians and decision-makers but it can be easily customised on other cities and use-cases (e.g. on other kind of animals). It can even be used by scientists to track some possible paths taken by the bats and try to understand the reasoning behind their migrations.

### Activities

This tool can be used in a myriad of scenarios to simulate different distributions of bats or of resources. This simulations are shown in the form of a graph containing the generated corridors. One can then use this information to accurately impact the area by, for instance, switching lights off, creating feeding stations for bats or even reducing traffic in certain areas.

### Output

Optimal graph with corridors within the city of Bristol based on a set of ad-hoc conditions to simulate different scenarios.

## 🌍 Social Impact Measurement
### Outcome

Improving the ecosystem of bats by creating safe and optimal pathways within the city of Bristol. 
Reducing luminic contamination by switching off certain lights based on the dark corridors created for the bats. 
Creating bat free areas within Bristol

### Impact Metrics

Our model is agnostic to the problem, so the impact metrics are dependent on the constraints used to create the graph. One could for example compute the amount of power saved by turning a specific amount of lights off or the average distance bats need to travel to the nearest source of nourishment as KPI’s.
### Impact Measurement

A way of measuring impact over time would be analysing the behaviour of said KPI’s over time. For example, one could look for a decrease in the number of lights or a decrease in the average distance that bats must travel to the nearest source of food.

Alternatively, one could create hypothetical scenarios using our graph model and then calculate the impact they could have.



