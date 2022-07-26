# World Data League 2022

## 🎯 Challenge
Predicting a Safety Score for Women in Costa Rica

## Team Name
YODAS - Your Omnipotent DAta Scientists

## 👥 Authors
* Cristiana Carpinteiro
* Diogo Polónia
* João Matos
* João Pereira
* Patrícia Rocha

## ✨ Introduction
The world is becoming more and more aware of gender violence regarding aggression or sexual harassment in public, especially against women. However, street harassment can be very hard to define and control. In fact, 70% of Costa Rican women have faced some form of sexual harassment in public spaces, but street sexual harassment only generates around 7,000 complaints in Costa Rican courts annually ([Tico Times 2020](https://ticotimes.net/2020/06/09/legislation-against-street-sexual-harassment-advances-in-costa-rican-congress#:~:text=Street%20sexual%20harassment%20generates%20some,from%20the%20country's%20judicial%20system.))!

The low number of complaints might be rooted in the fear that women feel regarding their aggressors or because they consider that the system cannot do anything for them. To mitigate this, in 2020, Costa Rica put into effect a law that criminalizes street sexual harassment and punishes it with jail terms and fines.

However, with only 43 counts of offenses against the sexual harassment law reported in 2021, there is an obviously long way to go to protect women. Thus, it is urgent to find new ways to ensure women's right to enjoy public spaces without being harassed or threatened.

With this in mind, YODAS set out to build a Proof-of-Concept for SafeMaps, a navigation software for route planning for traveling by foot, bike, and public transportation capable of not only identifying the safest routes in terms of street sexual harassment but also becoming a reporting tool for such crimes.

## 🔢 Data

To build our solution, we used the following [resources provided by the WDL organization](https://wdl-data.fra1.digitaloceanspaces.com/urbanalytica/urbanalytica_datasets.zip):

* ***ArcGIS Zoning Data (San Jose)*** contains environment and urban planning information such as land-use zones, housing complexes, healthcare and security facilities, green areas, roads, etc.
* ***District Data*** contains demographic data at the district level.
* ***Costa Rica Crime Data*** contains crime records from 2010 to 2022.
* ***Costa Rica Street Harassment*** contains street harassment reports in 2021.

We also conducted a [survey](https://docs.google.com/forms/d/e/1FAIpQLSfPoSufr1mILJoAV1PgB-hptOqmeUqSbPoeng5W74ZVtelFqw/viewform) to gather information on people's perception of safety. [153 answers](https://docs.google.com/spreadsheets/d/1JJmQjiB_IQ5fa7IyTIql9qfbNz1HikzAqF7drj5WShQ/edit?usp=sharing) were obtained amid Portuguese young adults.


**Possible Improvements:**

*Granularity*: the provided datasets on demographic and crime data have extremely low granularity (district level), which makes machine learning techniques inadequate. With only 11 districts in San Jose's canton, it's not possible to accurately score those districts in terms of danger, using machine learning. If crimes and harassment incidents would be recorded by street address, for example, scoring would become more reliable.

*Additional data*: it would also be interesting to have data on the flow of people (e.g., national and foreign flow count with origin in A and destination in B) to normalize the crime data. Further demographic data would also be welcome.


## 🧮 Methods and Techniques

***1. Prepare and Explore the Data***
We started by splitting the canton of San Jose into a grid and studied the geographical distribution of demographic and urban planning factors that influence the feeling of safety. In the end, each square of the grid was associated with a curated set of features.

***2. Create a Danger Score***
To create a danger score, we needed to understand the impact of each feature on the population. To do so, we used two different strategies:
* First, we calculated the *Pearson's correlation coefficient* between each feature and the historical crime data. However, we realize this approach is flawed since we are dealing with different levels of granularity, and we only have 11 data points in the crime dataset (corresponding to the 11 districts).
* Secondly, to ensure the score reflects the population's perception of safety, we sent a survey questioning people which factors they would intuitively say to have more impact on their safety. We received over 150 answers!

Our final score is a linear combination of all features weighted by their importance. This score will be used to suggest the safest path between two points.

***3. Crime Forecast***
SafeMaps is able to obtain accurate forecasts of the number of crimes in future quarters per district, allowing the update and visualization of the temporal evolution of the safety score. Also, it allows the security forces to manage their distribution in the territory over time.

***4. Route Optimization for SafeMaps***
SafeMaps uses *Dijkstra's Shortest Path* algorithm to find zone-based paths between two points that minimize the traveled distance as well as the overall danger score. The rationale behind the algorithm was to create a cost matrix depicting the costs between adjacent zones: distance and score.


## 💡 Main Insights
After some research on safety factors in cities, we chose a set of **urban planning features** among the data provided by the organization.

The **proximity to an area with roads**, for instance, can be correlated to several **safety** indicators, e.g., permeability, which is defined as the ease of movement between two places, is a safety indicator. A high permeability means there are alternative routes to reach from point A to point B and allows us to choose the safest one. Permeability can be calculated based on the number of **road intersections**. Also, main roads are more likely to be crowded or have enough lighting for clear visibility. Such features are depicted in the figures below:

![roads](https://i.imgur.com/rRIGbkL.png)
![road_intersections](https://i.imgur.com/UHhQ5We.png)


**Demography features**, like electoral participation, education, and healthcare quality of the resident population were also taken into account in the creation of the score. In the plots below, we show the weights given to each feature (normalized from -1 to +1) according to the (1) **correlation with crimes** in each zone and to (2) **people's perception on city safety**, collected in the survey we conducted.


![weights1](https://i.imgur.com/vSPLh0C.png)

![weights2](https://i.imgur.com/Q5sOiyF.png)

Public perception on demographic factors is **more aligned** with crime-correlated trends than urban plan factors, which often have opposite trends for each approach.

Finally, the **danger scores for women in San José** are exhibited below. Values are normalized between 0 and 100. Zones' scores will be a key input to SafeMaps.
![score](https://i.imgur.com/4JWo30U.jpg)


## 🛠️ Product
### Definition

A **navigation app** which allows users to find foot, bike or public transportation routes, according to **street sexual harassment safety index** (and distance), as well as to **report** and **track** street crimes.

### Users
Any citizen who is **concerned about their safety while travelling the streets** of a given city. Most relevant segments are:
1. Women (for sexual harassment purposes)
2. Tourists (who don't know the streets)

Furthermore, SafeMaps' safety dashboard can be used by public istitutions and law enforcement entities to better **understand** and **act upon** crime factors and trends for better policies.

### Activities
Our Solution:
1. **Scores San Jose's zones according to a danger index**, related to the probability of suffering from street sexual harassment;
2. **Predicts crime-related incidents by quarter** (to serve as law enforcement tool or update danger scores);
3. **Computes shortest, safest, and "danger threshold" paths between different zones**, allowing the user to choose the route they feel most confrotable with;
4. Allows the **reporting of sexual harassment incidents** and updates danger scores automatically.

### Output
SafeMaps is a user-friendly navigation tool that suggests the **fastest, safest or any balanced route** from a start point to an end point, specified by the user:

![image alt](https://i.imgur.com/JgwV19N.jpeg)

Users can define any **safety threshold** to make sure the recommended paths have a safety score above the score that is more confortable for the user. Besides, SafeMaps will warn the user if the safest path is of low safety or if it is impracticable:

![image alt](https://i.imgur.com/UYngedZ.png)

In parallel, users are able to **report incidents** and SafeMaps will automatically update danger/safety scores per zone.

Public institutions and law enfocement agencies can use SafeMaps **zone dashboard** to get deeper insights into the factors that contribute to higher danger and probability of harassment, as well as, how it these values are expected to change in the near future.

![image alt](https://i.imgur.com/0uibeSg.png)
![image alt](https://i.imgur.com/IG66akU.png)
SafeMaps is an hollistic platform that can provide extra security for any citizen and also offer insightfull data for authorities.



## 🌍 Social Impact Measurement
### Outcome
* To decrease the number of street crimes, including sexual harassment;
* To make it easier and more confortable for people to report sexual harassment inciddents;
* To increase women's safety and confidence when walking, biking or travelling by public transportation;
* To increase harassment and crime-fighting effectiveness

### Impact Metrics
* Number of sexual harassment reports 
* Number of other street crimes reports
* Average safety score vs. distance travelled ratio of users choice of path
* Safety score 

### Impact Measurement
* *Based on model and survey predictions*: Our routing model, together with our survey, estimates an **increase in people's safety of 9.09%** by having the option to choose for safer paths.

## 💬 Final Remarks
### Fairness & Explainability
The weights of each factor contributing to the danger score are based both on correlation with crime records and people's safety perception. To mitigate a possible societal bias, we give more attention to urbanistic features (70%), rather than to demographic ones (30%).

Sensitive features such as related to ethinicity are not included. 

To ensure explainability, we opt to use a Pearson correlation of both urbanistic and demographic features with crime reports to create the safety index.   

### Discussion of SafeMaps' Real-Use
When implementing and using the SafeMaps, it would be important to consider the phenomenon of **feedback loop**. Would "less safe zones" become even less safe because people would avoid them more? Or would they become "safer" because people would start avoiding them and less crimes would take place? The way the safety score is updated, as new crime reports take place, must be conducted in a very careful way to mitigate these questions.