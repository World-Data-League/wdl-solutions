# World Data League 2022

## 🎯 Challenge
**Optimization of public transport routes during road interruptions** by Cascais Municipality

## Team Name: DataBased

## 👥 Authors
* André Luís
* Rui Monteiro
* José Diogo Castro

## ✨ Introduction 
In Cascais, similarly to many cities, road work happens all the time. Road interventions are a nuance for public transportation, but they are necessary and may cause traffic cuts or drifts, which is an inconvenience to the residents and to the city's entire mobility system. These can lead to situations of distrust in the reliability of the public transport network.

The goal of the project is to model, from the point of view of trends, which routes of the transport road network suffer the most cuts/disturbance due to interventions on public roads. We should try to evaluate the effort needed to adapt the services to match the network's needs in the presence of disruptions due to physical obstacles preventing circulation along usual routes. Additionally, we should try to evaluate and quantify levels of the perception of "inconvenience" by network users caused by different disruptions.

The goal of this project is associated with United Nation’s Sustainable Development Goal 11, "Sustainable Cities and Communities", more specifically with its target 11.2: "provide access to safe, affordable, accessible and sustainable transport systems for all" (source: [United Nations Department of Economic and Social Affairs](https://sdgs.un.org/goals/goal11)).

In fact, with the prediction that two-thirds of the world's population will live in an urban center by 2050, cities are looking for new sustainable growth models, which highlights the importance of Sustainable Development Goal 11. Having a good public transport network is essential for a sustainable city.

## 🔢 Data 
Besides the [General Transit Feed Specification (GTFS)](https://dadosabertos.cascais.pt/dataset/gtfs-mobicascais) data about the public transport network of Cascais, we use data about [Bus Routes](https://dadosabertos.cascais.pt/dataset/carreira-de-autocarro), the [Road Network](https://dadosabertos.cascais.pt/dataset/eixo-de-via) and [Interventions in public roads](https://dadosabertos.cascais.pt/dataset/obras-de-intervencao-na-via-publica). This data was provided by the Cascais Municipality.

Regarding improvements, more data could be added to the road interventions dataset, specifically about a road's polygon/coordinates or its Road ID. This would make it easier to get geographical data about each intervened road, thus generating more trustworthy information.

## 🧮 Methods and Techniques 
We started by **Importing** the data and recovering missing information like the geometry data on each road and bus route.

Then, we performed an **Exploratory Data Analysis**, where we analysed each of the 4 used datasets. In order to analyse the Road Network of Cascais, as well as the Bus Routes, we created different maps to visualize the geographical data. To discover intervention trends on public roads, barplots, histograms and bubble maps were used.

Then we proceeded to **Cluster our Geospatial Data**. To cluster the road's midpoints/centroids, we experimented with 2 algorithms: K-means and Self-Organizing Map. After considering both solutions, we decided to further visualize and analyze the 7-cluster solution we got from K-means.

Finally we moved to the **Modelling** stage, where a route optimization model, subject to contraints related with road interruptions, was created. We used the [**Distance Matrix API**](https://developers.google.com/maps/documentation/distance-matrix) from Google to calculate travel distances and times between locations.

Then, we used this data to simulate interruptions based on the knowledge acquired and give suggestions about alternative stops for users, as well as a measure of the incovenience caused, expressed in the time spent walking from the initial to the nearest stop.

## 💡 Main Insights 
The main insights derived from our analysis were:

* The analysis of the public transport network of the Cascais Municipality shows us that the **highest number of routes is concentrated between the *Carcavelos e Parede* and *Cascais e Estoril*** parishes.
* The top-5 most interrupted routes are all in the ***Cascais e Estoril* parish**. Moreover, in the top-10, only 2 routes are not in *Cascais e Estoril*.
* From 2016 to 2020 the number of interventions was **always increasing**,  hitting the all-time high in **2020**.
* There are **more interventions** starting in the **beginning of the year** (January-March), and mainly on **Mondays**.
* The **water supply network** is the major cause for interventions.

## 🛠️ Product

### Definition
**Dashboard with Road Intervention Analysis and Route Optimization**

### Users

The **Cascais council employees** can use the dashboard to analyse the status of past road interventions and make better decisions about future road interventions. In this way, they will be able to reduce as much as possible the negative impact on the population, and notify those more likely to be affected. The **population of Cascais** can get more precise information and be given accurate suggestions about which stops to take in case of an intervention.

### Activities

* Analyse the impact of the current and past interventioned roads.
* Suggest optimized routes when an intervention occurs.

### Output

The mockup below shows a dashboard example. This would display the status of the current and past interventioned roads and suggest optimized routes. Besides, in a notification section, it would be possible to communicate with the public transport users through push notifications on the mobile app and through warnings near the bus stops.

![Dashboard](https://elogii.com/blog/uploads/dashboard.jpg)


## 🌍 Social Impact Measurement
### Outcome

* Give tools to build new optimized bus routes while some roads are beeing interventioned in order to reduce traffic jams and avoid situations of distrust in the reliability of the public transport network.
* Minimize the impact of the most common interventions, such as water or gas leaks.

### Impact Metrics

* Average Bus Route Time.
* Average Distance people have to walk from the original to the suggested stop

### Impact Measurement

Optibus is a company that deals with fixed-route planning and scheduling. Recently, in [Rio Grande do Sul](https://www.optibus.com/empresa-viamao-to-reduce-operating-costs-in-rio-grande-do-sul-brazil-using-optibus/), they applied their software to change schedules, which reduced workflows from weeks to hours. Similarly, our solution intends to reduce incoveniences caused by interventions from hours to minutes.
