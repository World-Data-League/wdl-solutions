# World Data League 2022


## 🎯 Challenge
*Identification of Dark Ecological Corridors by Bristol City Council*

## 👥 Authors
* Juan Diego Arango
* Melissa Montes Martin
* Santiago Cardona Urrea
* Irune Lansorena Sanchez
* David Gamba


## ✨ Introduction (250 words max)
One of the main characteristics of any modern population center is the presence of artificial lighting at night. The use of artificial light has made people more active and cities safer. Sadly, the use of lights at night has been detrimental to biodiversity. Animal species adapted for nightlife are harmed by the presence of a constant barrage of light. A concrete example of this is the Horseshoe bat. In areas with a high presence of light at night, Horseshoe bats have reduced their hunt for food, and lost access to the foraging area. It has been recorded that in areas with high lighting, their buzzes (trace of their hunt in an area) have reduced as much as 60%[1] indicating that they have reduced their hunting in those areas. This is backed by studies that show they avoid areas with levels of light as low as 50 lux [2], which corresponds to the light found in an average family home [3]. The extent of this problem is such that it has been suggested that the decline of the Horseshoe bat in Switzerland was caused in part by artificial lights at night. Those lights pushed the Horseshoe bats out from the foraging area that was then dominated by a competitive species, the Common pipistrelle[4]. Our objective is then to create a dark ecological network. Which is essentially a network of low light areas and corridors that will help bats be more active and roam freely towards food and roosting places in Bristol.

## 🔢 Data (250 words max)

We have used the following datasets:
1. The set of sightings of bats and moths in the area of Bristol. Provided by WDL. A point of improvement would be a better definition of the number of individuals seen in each sighting. The tagging is ambiguous, and it led us to ignore the number of individuals seen and just take into account their presence at a point. Also, if the date had a better resolution, we could have improved on the inference of behavioral patterns. 
2. Satellite information provided by the _NASA Visible Infrared Imaging Radiometer Suite_. It quantifies the amount of light reflected from Earth. A point of improvement for the data could be to have simpler units in its measurements. We had to make some approximations to obtain a conversion factor to compare to traditional measures used in assessing light impact. 3. Information about POIs in Bristol obtained from OSM such as hospitals. It gave us the necessary information about the locations of buildings we cannot turn off the lights and whose height makes them obstacles for bat transit.
4. Geolocalized information of lights, rivers, forests, and dark corridors was provided by WDL. This information was adequate. It gave an accurate description of the features and locations of the natural areas surrounding Bristol.
5.Number of crimes per district. This was found at Bristol Open Data.

## 🧮 Methods and Techniques (250 words max)
In the next section we offer a summary of the techniques we use for the development of the project and how are they used:
* We have noisy information on the reported locations of bats and moths in Bristol, and we estimate activity areas where the bats agglomerate using HBDSCAN[5].
**HDBCAN Bats**

![Bats_Cluster_HDBSCAN.png](https://storage.googleapis.com/geoneas-bucket/bat-s4/Images/Bats_Cluster_HDBSCAN.png)

* We assign to each grid cell a weight. The function describes how "desirable" a hexagon is. This way,we create a weighted graph. Multiple functions were prepared each giving different weight to the needs of humans and the needs of Bats. The part function that reflects human interests gives a high score if a hexagon is lighted and safe, and in the case of the part of the function that reflects the needs of bats it gives high score in the presence of darks and a nature habitat.
* We translate the hexagon grid into a graph. The nodes are hexagons where bats locate, and the edges indicate adjacent Hexagons. 

![Minimum_paths_graph.png](https://storage.googleapis.com/geoneas-bucket/bat-s4/Images/Minimum_paths_graph.png)

* We perform minimum path cost optimization through Dijkstra's algorithm[8] to find paths between all pairs of activity zones of bats. These are the potential corridors of the dark ecological network
* Since we ended with many corridors, we simplify the dark ecological network using the Minimum spanning tree algorithm[7]. This leaves only the least costly corridors that connect all the networks. The simplification makes the graph's  analysis more manageable. 
![Minimum_spaning_tree.png](https://storage.googleapis.com/geoneas-bucket/bat-s4/Images/Minimum_spaning_tree.png)

*Then, we used to define the shortest path for the bats to move.

![Optimize_paths_cost_function_0.5.png](https://storage.googleapis.com/geoneas-bucket/bat-s4/Images/Optimize_paths_cost_function_0.5.png)



## 💡 Main Insights (300 words max)
As we developed the project, some details appeared which influenced the course of the final product. These insights relate to the different species of bats found in the data, the evolution of the population of bats in time, the types of modifications we could perform on the city, the types of obstacles for bats in the city, and the final shape of the solution.

First, there are multiple bat species in Bristol, and one cannot take any species of bat as a stand-in for the species that is the focus of this work, Horseshoe Bats. The reason for this is that there are spots in Bristol that are large in their presence of bats, but none are identified as Horseshoe bats. This gives no evidence that different bats go to the same places.

Regarding the population of Horseshoe bats,  we saw that the population of bats has been declining in the last 15 years. These observations suggested that this particular species of bats has been dwindling recently.

Another insight was that not all places can have their lights modified. This led us to look for places where light would be hard or inconvenient to modify (hospitals, stadiums). This became a restriction on the possible path for the bats to move through. Another set of restrictions became high buildings. They are barriers to the bats movement [9].

On the side of the solution to the problem, our main insight was that the Horseshoe bats do not need to go all places. Bats will go to where the other bats are or where food sources are. Then, we decided, early in the development of the project, to focus on the points where Horseshoe bats are located and try to create paths between those points under the restrictions mentioned above. 

## 🛠️ Product
### Definition
Tool for the generation and evaluation of dark ecological networks for the transit of light sensitive fauna.

### Users
Public officials that have the control over light in the city and can enforce the modifications shown by the product.

### Activities
Describe what features your product has.
* Estimates potential activity zones of the fauna based on their reports and reports of food or other factors correlated with the species presence
* Finds corridors between the potential areas and optimizes the corridors to give a least costly configuration
* The cost function takes into account benefits for bats as well as cost for humans; it is also fully parameterizable and could be further improved with more domain expert knowledge
* The methods are general enough to be applied to other areas and other species of night dwelling creatures
* Provides suggestions for the amount of light that needs to be reduced to make those paths viable for animal transit. It also determines the specific lights that require dimming.

### Output
For a given parameter configuration (such as changing the cost function) it generates a map of the proposed dark ecological network areas and corridors.
Location of possible bats routes and amount of light that it needs to have for it to be viable. 

![Optimize_paths_cost_function_1.png](https://storage.googleapis.com/geoneas-bucket/bat-s4/Images/Optimize_paths_cost_function_1.png)





## 🌍 Social Impact Measurement
### Outcome
We hope that with our product the Horseshoe Bats will be able to move through larger parts of Bristol. Then, they will be able to reach points, where they can hunt, that were previously unreachable because of the excess light. Ideally, this will help the bat population increase.  


### Impact Metrics
From the outcome, define **2 to 4 metrics** that measure if you are achieving that outcome or not.
* Amount of buzzes made by Horseshoe bats at night. This measurement can indicates of activity
* Amount of Horseshoe Bats seen in Bristol and its surroundings.  
* Amount of Horseshoe bat droppings. This can indicate their presence in part of the city. It will help them know if they are expanding their area of reach.

### Impact Measurement
As a metric to measure the impact of our proposed solution, we considered three scenarios for the construction of dark corridors for the commute and unburned by light. In the first one, we considered most of the weight to human needs, which refers to the presence of light (cost function 0);in the second, we equally weighted the need for light for humans and the need of bats for darkness and space to move (cost function 0.5); and in the third, most of the weight was given to the bat preference for darkness and space to move around (cost function 1). In the principal cases, the ones where the needs of humans and bats are balanced and the ones where the needs of humans were given preference, an increase of area for dark corridors was seen. In the balanced case, the increase was 10.7% and in the case, for only humans, the increase was 79.03%. When the preference for bats behavior is analyzed a decrease of 30.24% of the area is observed because the locations where bats are comfortable is less than the current; however, cost functions were defined considering literature reviews and data analysis and we could pass some information. This tool needs to be calibrated with biology experts in order to define cost functions and obtain relevant results. Finally, this shows that our implementation gives a path for the improvement of conditions for the Horseshoe bat.

Another metric of impact that we consider was money saved. Money savings for the decrease in lightning were calculated considering a cost of 80 euros for turning off a streetlight completely. With the number of streetlights and the costs of light to obtain a comfortable threshold for bat commute the savings were measured. The cost function that prioritizes bats commute (alpha = 0) saves 60K euros in the summer followed by the cost function that prioritizes human impact (alpha = 1) with 57 euros in the summer. Finally, the balanced cost function (alpha = 0.5) saves 40 K euros in the summer. This is an approximation considering multiple sources, the Bristol government could refine these measures with detailed data of cost and street lights specifications. We considered the saving in two scenarios:
In the scenario where we consider the needs of men and bats equally, the total savings are 39,802 euros. 
In the scenario where we only consider the needs of bats, the savings were 66,148 euros.

### Limitations and future work

The solution has limitations related to the bats and moths granularity. Observations are static and does not have timestamp preventing seasonality calculations. In the future, data gathering must be improved considering installation of GPS and sensors to detect bats and moths. Furthermore, lights saving estimations could be improved when the monitoring systems is working, this allow decisionmakers to take choice in real time and to calculate precise indicators about impact on human beings and fauna. Crimes should be monitorized considering georeferenced data to determinate if dark ecological corridors are influencing this incidents. On the other hand, biology experts and bat specialists are crucual to define resistancefunction while decision makers could help in the impact function. To involve those experts in the decision give flexibility to the solution and space to improve it.

### References 

[1]Kuijper, D.P.J., Schut, J., van Dullemen, D., Toorman, H., Goossens, N., Ouwehand, J. &
Limpens, H.J.G.A. (2008) Experimental evidence of light disturbance along the
commuting routes of pond bats (Myotis dasycneme). Lutra, 51, 37-49.  
[2] Stone E.L., Jones G. & Harris S. (2012) Conserving energy at a cost to biodiversity? Impacts of LED lighting on bats. Global Change Biology, 18, 2458-2465.
[3]Pears, Alan (June 1998). "Chapter 7: Appliance technologies and scope for emission reduction".
[4]Arlettaz, R., Godat, S., and Meyer, H (2000) Competition for food by expanding pipistrelle
bat populations (Pipistrellus pipistrellus) might contribute to the decline of lesser
horseshoe bats (Rhinolophus hipposideros). Biological Conservation, 93, 55-60.
[5]McInnes, Leland & Healy, John & Astels, Steve. (2017). hdbscan: Hierarchical density based clustering. The Journal of Open Source Software. 2. 10.21105/joss.00205. 
[6]https://eng.uber.com/h3/
[7] Numpy and Scipy Documentation — Numpy and Scipy documentation. Retrieved 2021-12-10. A minimum spanning tree is a graph consisting of the subset of edges which together connect all connected nodes, while minimizing the total sum of weights on the edges.
[8]Dijkstra, E. W. (1959). "A note on two problems in connection with graphs". Numerische Mathematik. 1: 269–271
[9] Foraging and commuting habitats of the greater horseshoe bat, revealed by high-resolution GPS- tracking
