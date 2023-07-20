# World Data League 2023



## 🎯 Challenge
*Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data*


## Team Name
* CEOS - Champions Engineer their Own Science *


## 👥 Authors
* Ana Maria Sousa
* Duarte Rodrigues
* Mariana Sousa
* Mariana Xavier
* Ricardo Brioso


## ✨ Introduction
* Imagine a Lisbon that is not just a beautiful and historic city, but also a sustainable and vibrant place to live, work, and drive. A city where the streets are not stuffed with cars, but instead filled with people walking, biking, and enjoying the fresh air.

Right now, Lisbon has an astounding 1.3 million cars, which more than doubles its average population. The result? A chaotic mess of traffic causes unreliable public transportation and harmful levels of pollution, including toxic gases, such as nitrogen dioxide, which are currently exceeding the European legislation limits. But there is hope.

Our team's proposition is to understand the anthropodynamics of mobility, or in simpler terms, the patterns that govern our daily lives and affect the traffic of people, independently of the means of transportation. By analyzing where people are located throughout the day and how they move around the city, we can estimate where they will be depending on key factors, that generally affect our lives. If we can modulate these conditions, we can then realize how the city is affected and have a notion if the traffic gets affected positively or if another traffic congestion may be caused.

Imagine a future where emptier streets mean cleaner air, safer roads, and a happier and healthier community. We can make it happen. Let's work together to create a more livable Lisbon, for us and future generations. *


## 🔢 Data
* Getting back to a term introduced before, the anthropodynamics of mobility can only be explained and analyzed, if indeed we have the history of where people are concentrated throughout the city. Lucky for us, the surmountable data given by the WDL was the perfect kickstart to build this model about Lisbon. The denomination follows the “Lisbon_challenge_data_dictionary” given in the challenge brief.

Dataset1 gave us the number of people in each city zone based on grid squares, and we were able to validate its usability by animating the city and observing that the areas got highlighted during rush hours and dimmed otherwise.

Dataset7 from Waze was also helpful, however, it lacked information both spatially and temporally, as there are plenty of hours without information and the roadmap is vacant, with existing data only on a few paths. Having complete data would allow us to get the rush hour times more effectively, as the data is connected mostly to vehicles. The direction of travel would also be good, to understand how people spread when entering and exiting Lisbon.

Dataset8 provided information that could affect and explain traffic jams by correlating the conditioning with the people present. However, while engineering the data considering time and place, it became too prolonged to be used, failing to be part of the final model.

Finally, a dataset found on LisboaAberta website, regarding meteorological and environmental information, was a great find. It helped us quantify rain, a factor that generally influences traffic.  *


## 🧮 Methods and Techniques
* The first step of the project was to perform EDA on various datasets. Dataset1 gives the number of people inside each zone at a certain time, we can visualize their movement and identify critical rush hours per zone. Moreover, we can also understand which parts of the city always get congested and how frequent it is in a month. Dataset7 appeared to be too disaggregated, but when the data were concatenated and averaged per hour according to weekdays, a pattern emerged. The dataset provided a generalized view of the city’s state, including the level of congestion and speed or delay. Similarly, the meteorological dataset also provided the rain values, that were assumed to affect the entire region.

By combining all the descriptors computed from these datasets, we were able to get a general feel of the city’s state, that supports the past individual records per square. Hence, the goal was to understand the patterns of each weekday and hour to predict the number of people in each grid square in the future. To achieve it, we implemented the most common regressor models such as Random Forest, Gradient Boosting, and Extreme Gradient Boosting with a grid search for validation of the best hyperparameters.

In summary, the objective was to understand the movement of people in the city and predict their behavior in the future. The machine learning models helped us to create a better understanding of the patterns in each grid square and provided valuable insights and outcomes. *


## 💡 Main Insights
* With such a huge amount of data, it was impossible not to stumble upon a few interesting facts and curiosities. For example, when evaluating the rush hours, we constantly get the same regions reactivating, almost like a pumping heart of people moving from these parishes, specifically Campo de Ourique and Campolide. Actually, these regions are known to be highly residential, usually from older aged groups, as this was a common place to acquire houses in the middle of the last century.

Regarding the data from waze, is interesting to see that what defines rush hours is not exactly having super congested streets, but rather exhibiting a high search and demand over almost the entirety of the roadmap. People search a high diversity of destinations during those hours (6:30 to 10:30 and 16h30 to 20h). Another curious fact is that the city seems almost to behave in unison when it comes to traffic jams. During parts of the day, we can identify that, although there are not as many searches, almost all the ones that are being made result in a high level of congestion at the same time (not necessarily during rush hour). Of course, this also provokes the city to more slowly, increasing the delay of transportation. *


## 🛠️ Product

### Definition
An assistant to predict the anthropodynamics in mobility, based on conditions and descriptors of the city.


### Users
The user would be city planners and mobility experts, as they would be able to understand how people move and what spaces get affected, when a new condition/descriptor is imposed (for example, excessive rain with risk of floods) in Lisbon.
It could also be used by data scientists and engineers to generate new data to support studies on how to optimize the city's traffic flow.


### Activities
* Predicts the number of people in a region of Lisbon, given a set of conditions/descriptors;
* Flexible to be upgraded to multiple types inputs, such as meteorological, traffic, construction work, special events (like football games, concerts, etc);


### Output
The product outputs, for the intended zone (grid square), the estimated number of people/terminals inside, according to the input conditions.


### Scalability
Our solution can be scaled on multiple areas always leading to a more complete, flexible and accurate solution. The process to upgrade our software would be to understand what conditions could be affecting a certain square during our training data, for example matching the construction work periods to the time and specific square. Once this is added as descriptor of the city zone in the model, we can use it to generate a new output and understand how that zone would react in the future to new constructions or to a mix of conditions, like construction and heavy rain. Another aspect could be, instead of evaluating square by square, doing it parish by parish. This means that for our solution, imagination and creativity are the limits.


## 🌍 Social Impact Measurement

### Outcome
Our solution aims to assist city planners in understanding the direct impacts of their proposed changes in Lisbon, to the flow of people. In the future, they would be able to develop the optimal plan and set of variables, ensuring that traffic jams are prevented, flow is maintained, delays are minimized, and there is a quantifiable damage control in place, in terms of traffic disruptions caused by the new plan.


### Impact Metrics
* Number of grid squares above 80% the threshold of congestion;
* Daily maximum on the grid below the threshold of congestioned;
* The absolute difference of people on the squares corresponding to highways, between rush hours and off-peak times, to be close to zero.


### Impact Measurement

* *Based on mobility estimation article*: In case one of the model conditions added is the affect of a new bus lane, the car traffic on that route can reduce around 12%, diminuuishing mostly the transportation for students on individual cars
* *Based on similar traffic situation in cities with same population*: Cities with the same population numbers as Lisbon have 3 to 4 peak hours daily, meaning that our solution could lessen the peak time in an average of 2 hours (one in the morning and one in the afternoon). 