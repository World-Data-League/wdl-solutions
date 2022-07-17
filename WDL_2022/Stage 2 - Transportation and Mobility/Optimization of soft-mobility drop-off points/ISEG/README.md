# World Data League 2022

## 🎯 Challenge
**Optimization of Soft-Mobility Drop-off Points**

## Team Name
ISEG

## 👥 Authors
* Alessandro Consiglio
* Emil Henrikson Ene
* March Behse
* Navid Saffari

## ✨ Introduction (250 words max)
*A state-of-the-art city has to adapt to changes in society and the demand from the population. Sustainable and modern mobility can benefit from existing transport methods by producing a super-efficient system of connections. The city of Porto has decided to introduce E-scooters in order to promote ICT projects and to boost soft-mobility within the context of the city of Porto and its metropolitan area. The idea sounds great, but are these parking spots allocated efficiently?.
The aim of this project is to understand how parking spots have been arranged and find a way to improve their deployment. The project has been carried out in Porto, but we hope the results may be applied to the general case as well*

## 🔢 Data (250 words max)
*We have used the datasets about soft-mobility and one external dataset to get useful insights:
1) E-scooter parks: it includes all the scooter parkings information necessary for the analysis, including geospatial data, it's very detailed, the only problem is that the variables have been written in Portuguese. 
2) GTFS metro and bus: It includes all the metro and bus information about the stations. It's a very big datasets with different txt. files, it took time to understand the variables and translate them in something concrete.
3) Porto taxi trajectories: https://figshare.com/articles/dataset/Porto_taxi_trajectories/12302165, it has been fundamental to get the most important places and "hotspots" in Porto based on the taxi pick-up locations. It has been used as a metrics to evaluate which are the hotspots and if these spots need to be boosted with more the E-scooter parking zones *

## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.
*We started with an exploration of the location of the E-scooters parking spots and the Metro- and Bus stations. In order to do that we created a map based on the geospatial data (latitude/longitude), it gave us a general uderstanding of where the parking spots were originally located and if they are close to points of interest. We have considered two types of points of interest. The first type is metro stations, by measuring the number of stops at each metro station we can find their relative importance, therefore we want to keep parking spots that are within 340 meters of the most important metro stations. The second point of interest is hotspots, an area is considered a hotspot if there has been more than 1000 taxi pick-ups at that area. For this point of interest we also want to keep the E-scooter parking spots that are within 340 meters of the hotspot. For reassinging underitilzed parking zones we decided to move an underutilized parking spot from it's original position to a hotspot if that hotspot does not have a bus stop within 100 meters.*

## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.
*We have discovered that the E-scooters drop-off points are mainly deployed in the city centre close to the main areas of interest, but there are other parts of the city that are important as well but are not served at all by the E-scooter service. We have also found a "busyness" measure for the different metro stops of Porto, which shows on you on a map which stations have more or fewer departures per day.*

## 🛠️ Product
### Definition
**A set of E-scooter drop-off points to relocate efficiently**
*Our product will be one list of the underutilized parking spots, meaning parking spots that currently are not optimally located, and another list of suggested locations for new parking spots to relocate to. With these two lists we also attach an interactive map, showing the distribution of poorly positioned- and optimally poistioned parking spots in Porto.

### Users
*Municipality of Porto together with operational management and experts of Porto Digital*

### Activities
* Point out E-scooter parking spots that are underutilized, poortly positioned.
* Suggestions for new optimal parking spots.
* Gives an idea of the most visited places in Porto, the "hotspots".
* Gives a map for evaluating the optimality of a parking spot of the city based on the distance to metro stations and popular taxi pick-up spots.

### Output
List of less useful drop-off points in different parts of the city, ready to be relocated in critical points.

## 🌍 Social Impact Measurement
### Outcome
We trust that proper reallocation of scooter parking spaces will lead to less car use. The aim is to create a car-free city, even though studies show that even electric scooters are polluting the environment.
### Impact Metrics
* Top 25% used metro stations in Porto
* Average distance between a "hot-spot" and a drop-off point

### Impact Measurement
Based on our model and some similar studies in the municipality of Paris, we can say that the allocation of the E-scooters was not made with a view to improving the lives of citizens but to encourage visits to tourist sites. An optimization of the allocation of the E-scooters drop-off points can give a big boost in the urban mobility organizations since 72% of the population shifted to soft-mobility services.