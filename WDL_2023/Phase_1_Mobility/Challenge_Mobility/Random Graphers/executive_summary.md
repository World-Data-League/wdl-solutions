# World Data League 2023

## 🎯 Challenge

Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data


## Team Name

Random Graphers


## 👥 Authors

* José Almeida
* Juliana Machado
* Marta Colaço
* Rui Santos


## ✨ Introduction

Mobility in the center of Lisbon has been changing over the years due increasing outflows to suburbs and increasing tourism in the city center. 
According to the Lisbon city hall, the number of people living in the city center has decreased by approximately 300,000 habitants in the past 4 decades ([as shown here](https://www.lisboa.pt/fileadmin/cidade_temas/mobilidade/documentos/Lisbon_Mobility_Strategic_Vision_MOVE_2030_EN.pdf)). The migration movement to the suburbs has lead to a car usage increase, mainly due to home-work-home or home-school-home commuting, given the lack of offer and overcrowded public transportation that there is between the key suburban areas (Sintra, Amadora, Oeiras, Cascais, Loures, etc) to the city center.
To become an accessible and sustainable city, and to implement a multi dynamic transportation ecosystem that serves all stakeholders (Lisbon residents, tourists, students and workers in general) it is crucial to define new ways of traveling to and within Lisbon. 
To support this exercise, our group developed a data model to predict the key flows currently in place within the Lisbon city based on data shared by the LxDataLab Lisbon.


## 🔢 Data
To build our model, we used the following data sets:
* Provided by LxDataLab Lisbon
    * Dispositivos móveis quadrículas
    * Dispositivos móveis grelhas e eixos
* External to WDL sources
    * Road network data from the Lisbon City Hall in GeoJSON format [available here](https://dados.cm-lisboa.pt/dataset/rede-viaria-escala-1-20000)


## 🧮 Methods and Techniques

While road traffic rules are simple, traffic itself can be highly nonlinear – hence, it is important to use methods capable of handling these nonlinearities and their intrinsic temporospatial nature. In that sense, we decided that an attention-gated temporal graph convolutional neural networks, otherwise known as [A3T-GCN](https://doi.org/10.3390/ijgi10070485), could be our best approach.
We encoded our data as a graph where each node is connected to neighboring roads, according to the “Rede Viária” GeoJSON and the provided data on mobile device grid cells. 
For a set of 5 points (15 minute intervals), we used the features of each node (the number of terminals as a proxy for the number of people, and whether the node has a road, the time of the day, between 0 and 1, and whether it is a weekend, to predicted the number of people for the next set of timepoints. 
The reason why we used A3T-GCN for this is that graph convolutional neural networks are excellent at dealing with spatial relationships, whereas the temporal aspect of A3T-GCN enables it to model temporal relationships through the use of a gated recurrent unit (a staple of complex temporal modeling). Finally, attention gating allows the model to learn which timepoints are the most important for prediction. We trained this using gradient descent with an Adam optimizer and obtained a model which requires relatively little information – a road network, the number of people in a node and whether that node co-occurs with a train or metro station – to predict these complex temporospatial movements of people through cities.


## 💡 Main Insights

If you were to ask a Lisbon citizen what are the main flows within the city center during rush hour, 8 out of 10 people would answer places like Marquês de Pombal, Saldanha or Oriente. We won’t know for sure, because we haven’t asked any citizens that, yet! What we’ve done, however, enabled us to support common sense with data. Indeed, places like Saldanha, Marquês de Pombal, Oriente, etc. are among the places within City center with the highest traffic flow during rush hours. 
One of the insights it was clear to see from the beginning was the habits of the Lisbon citizens throughout the day and throughout the week - early in the morning and close to the end of the afternoon, as well as during weekdays, are the moments in time with highest level of traffic, mostly related with work/school commute. The databases shared had a few outliers, probably due unusual traffic within Lisbon, which might impact the analysis performed when not excluded.
Another conclusion that doesn’t surprise us is the amount of mobile data registered through the day in the airport region! Of course being in the center of lisbon might mix the insights on the city center flow, but that’s a topic for another challenge!
Last, but not the least, if you ever find yourself in a “no” day and feel like having a zen moment (almost alone) we suggest you try to hide somewhere in the Monsanto park. Based on the data we were able to analyze, you’re likely to be safe from car traffic and breathe clean air.
These insights might be obvious for a Lisbon citizen, but when powered by data models, it enabled us to develop a model capable of predicting endpoints (people) flow in grids based on the near past, as explained in the previous section.


## 🛠️ Product

From our model, we suggest the creation of the following tools:
* **Digital dashboard to assist individual commute planning** - for example, display on key roads that are used to access Lisbon (e.g. IC19, A5, A17, A16) digital panels showing traffic affluence in different roads and potential alternatives where terminal permanence is reduced. Timings to reach a certain point of the road might be presented as well (as is currently done in A2 for bridge access). This can be especially helpful when public transport strikes happen.
* **Investment in additional buses with alternative routes / less stations**  – while these sorts of investments can be expensive, they allow for a better experience for those living in and visiting Lisbon. Additionally, simpler alternatives are also possible, like creating a traffic app specific for bus drivers to suggest alternative routes based on traffic
* **Gamification on driving apps** – partner with Waze / uber and other drive apps (or develop a new one specific for Lisbon mobility!) to give points to users that choose to travel in less crowded roads / follow alternative roads, specially during rush hours.


### Users

* Carris / bus drivers could benefit from having a specific app that proposes more efficient routes throughout the day, according to traffic, strikes, climate conditions, etc.
* Carris (bus) and Lisbon City Hall might benefit from a dashboard predicting affluence to the city center during rush hours on strike days to increase the number of bus and implement alternative routes for those days
* Uber / taxi drivers and individuals in general might benefit from digital dashboards / panels on the roads showing road congestion to evaluate alternative routes, if possible.

### Activities

Our model is capable of predicting terminal occupancy in the near future for relatively small areas, creating an unique opportunity of detecting necessary traffic changes and rerouting for public transportation and individual users of the public road networks.

### Output

Our model can create density maps for different areas of the city, making its output legible and easily interpretable.


### Scalability

While the model is based on deep neural networks, it is easily trainable and deployable – training takes under a minute on a consumer-grade GPU and only a few minutes on CPU. The incorporation of additional data – such as landmark location and neighboring areas – can make this model more informative at little cost.


## 🌍 Social Impact Measurement

By contributing towards early traffic rerouting, we can prevent accidents in heavily congested streets. Ambulances will also have an easier traveling through emptier streets, shortening the amount of time necessary to provide support for those in need. Additionally, the amount of human-hours saved on a more efficient commute can also have a positive impact on life quality.


### Impact Metrics

* Absolute difference in predicted and real terminal occupancy;
* Average travel time for buses;
* Average travel time for individual users.


### Impact Measurement

* Our model can be used as an early warning system – being able to notify the city hall of a potential increase in terminal permanence implies that traffic rerouting can be done earlier, leading to fewer accidents; additionally, traffic control police can be more quickly dispatched;
* Similarly to other products like Google Maps or Waze, we are interested in planning the optimal route between two points. However, some cases where Waze leads to traffic in residential areas [have been reported](https://www.streetlightdata.com/waze-traffic-effect-4-steps-for-neighborhoods-cities-to-fight-back/
). We estimate that our model could be used to refine these predictions and prevent additional traffic.