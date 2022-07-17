
# World Data League 2022

## 🎯 Challenge
Predict Waste Production for its Reduction

## 👥 Authors
-   Rui Granja
-   Pedro Ruas
-   Tiago Neves
-   Pedro Miguez

## ✨ Introduction (250 words max)
After researching the topic of urban waste collection, including the [article](https://www.mdpi.com/2313-4321/5/4/25/pdf) referenced in the challenge, we identified a significant problem that needs improvement: the efficiency of garbage collection routes. There is a lack of tools to optimize the routes and adjust the vehicle type for specific scenarios. This led us to try to see what we could leverage out of the Austin-related datasets that would bring us to any interesting insights in this regard. According to the *Daily Waste Collection Report for Austin*, by assuming a maximum capacity for each garbage collection vehicle based on the route's 99th percentile of maximum load weight, we have seen that, on average, these vehicles reach the end of their route at 60.7% capacity. Our goal is thus to present a model that can evaluate which routes are under-performing in terms of truck occupancy in a given calendar quarter, which by its turn, can be used to improve the efficiency of waste collection routes.


## 🔢 Data (250 words max)

We mainly focused on the [*Daily Waste Collection & Diversion Report*](https://data.austintexas.gov/Utilities-and-City-Services/Waste-Collection-Diversion-Report-daily-/mbnu-4wq9) dataset were the most important data for our work was the collection dates, the routes, and the load weights of the collections. However, we consider that the main limitations of this dataset are the absence of data relative to the geographical point of the collections, whether through addresses or coordinates and also the absence of the truck volume associated with each collection, which we hypothesize could improve our models comparing to the load weight that was actually used. Besides, the dataset misses the address of most of the drop-off sites.

We couldn't muster anything of relevance to our use-case out of the [*Garbage Routes*](https://data.austintexas.gov/Locations-and-Maps/Garbage-Routes/azhh-4hg8) and of the [*City of Austin Population History*](https://www.austintexas.gov/sites/default/files/files/Planning/Demographics/population_history_pub.pdf) datasets. Regarding the *Garbage Routes* dataset, the main obstacle was missing information about the specific path for each route. Instead, the dataset only presents the coverage area of each collection route. It would be amazing if we had a path containing a couple of checkpoints, and even better, we had data about the waste gathered at each checkpoint! <!-- (is this possible?)--> The dataset *City of Austin Population History* only includes data up until 2016, so it could be potentially useful if more recent data covering the remaining years until the present moment were available.

## 🧮 Methods and Techniques (250 words max)

* Preprocessing and Exploratory Data Analysis: Pandas

* Modelling: sklearn ('GradientBoostingRegressor', 'median\_absolute\_error')

* Visualizations: matplotlib


## 💡 Main Insights (300 words max)


* On average, the garbage trucks circulated with 39.3% of free space.
* Model 1 can predict the total weight in each quarter for the years > 2016 by route with a median absolute error of 12.1%
* The most important features to predict the total weight of each route in a given calendar quarter are the collections of the latest quarter and the equivalent quarter of the previous year.
* The Model 2 can predict the truck occupancy in each quarter for the years > 2016 by route with a median absolute error of 8.1%
* The most important features to predict the truck occupancy of each route in a given calendar quarter are the collections of the latest quarter and the equivalent quarter of the previous year.
* Different types of routes have very different levels of occupancy: the routes collecting dead animals have the lowest occupancy, whereas the routes collecting bulk garbage have the highest occupancy.

The main insights we have taken away from analyzing and working with the data for this challenge are regarding *garbage truck occupancy* and routes and information about the type and quantity of waste collected over the years. 
On the first point, most of the trucks are completing their routes with only 61% occupancy on average and making many trips for lower load weights in categories such as Bagged Litter, Contaminated Organics/Recycling. Based on the type of waste in these categories, it's understandable that they need to be collected quickly. Still, it's important to note that hopefully, smaller and fewer pollutant trucks are being used in such scenarios. 

As for the second type, we identified that the waste categories with a higher load weight are Garbage Collections and Recycling. It's also relevant to note that starting in 2018, the collection of Organics has been increasing steadily, proving that [Austin's efforts in this direction are proving successful.](https://www.austintexas.gov/composting)

## 🛠️ Product
### Definition
A business intelligence platform with insights on future garbage route performance.

### Users
Garbage route planners can use this tool to know which routes need improvement.
Landfill owners can better plan their layouts through insights on expected waste production.

### Activities
* Identify which routes are sub-optimized.
* Predicts whether a given route is likely to be sub-optimized.
* Predicts how much weight is expected in each route for a given quarter.
* Suggests which routes should receive urgent optimization.
	* Either by reducing the number of trips or changing the route layout.

### Output
An example of a direct outcome of our models would be a simple dynamic dashboard that shows the prediction of Route Performance for the next quarter based on the data currently available. This would allow the route planners to easily identify which routes are most likely to be underperforming and try to understand what can be improved. More information could be added as needed, such as Waste Type associated with each route and estimated Total Weight for the next quarter. 

![image](https://user-images.githubusercontent.com/70525853/159818348-a4d9fa17-981d-4351-b8b0-9f9319d5f1fa.png)

It could also contain more advanced insights; for example, all of the routes for a certain waste type ordered by their estimated occupancy for the next quarter:
![image](https://user-images.githubusercontent.com/70525853/159818975-5322e402-f714-4155-98c7-fe45a14227ad.png)

## 🌍 Social Impact Measurement
### Outcome

Reduction on carbon footprint:
* **From reduction on wasteful trips from garbage collection trucks.**
* Less road congestion.
* Reduction in noise and odor pollution.
* Reduction of the number of trucks needed to cover the city.

In addition, the saving from operating more efficiently can be used for further initiatives, like optimizing landfill management and increasing recycling capacity and awareness. These savings will create extra incentives for efficient operation in other areas, creating a compounding effect that significantly improves our society. 


### Impact Metrics
* Reduce the number of circulating trucks in the city
* Readjust the Size of the fleet required to cover the city
* Lower the carbon footprint
* Increase the air quality in the city

### Impact Measurement

By increasing the average occupancy of a truck by 5%, 10%, or 20%, we will reduce the number of trips required by 5%, 10%, or 20%, respectively, which reduces the carbon footprint by similar amounts.
