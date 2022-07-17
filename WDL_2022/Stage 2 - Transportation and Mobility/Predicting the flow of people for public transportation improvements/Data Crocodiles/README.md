# World Data League 2022

## 🎯 Challenge
Challenge 2 - Predicting the flow of people for public transportation improvements

## Team Name
Data Crocodiles

## 👥 Authors
* Diogo Pessoa
* Fábio Lopes
* Francisco Valente
* Júlio Medeiros

## ✨ Introduction (250 words max) (129/250)

Porto, the second biggest city in Portugal, is currently placed 158th in the world ranking of the 2021 Traffic Index. Some of the reasons for this are that Porto is an old city with inadequate urban planning and, especially, restricted access to the city in terms of highways and bridges. Furthermore, the public transport system is another concern.

Despite the efforts and implementations to reinforce a better public transport infrastructure and optimization of the transportation areas and lanes, the city still lacks to respond to the community's demands.

Based on data concerning the validation of people using public transportation in Porto city, this challenge aims to study how to improve the city's public infrastructure to help reduce traffic and improve urban sustainability and quality of life for its citizens.


## 🔢 Data (250 words max) (115/250)

Our analysis was based mainly on four datasets provided by the WDL organization: 1)the entry and exit validation (TIP) MOD dataset from public transport in Porto Metropolitan Area, as the primary dataset used in this study; 2) TIP Rodov (road public transport) and 3) TIP Ferrov (rail public transport) datasets as auxiliary datasets to the main one; and finally, 4) the GTFS from Porto’s metro and public bus system, with relevant metadata information about the coordinates and routes.

## 🧮 Methods and Techniques (250 words max)

Exploratory data analysis (EDA)
For EDA, we used several visual methods: heatmaps, time-variation plots, and geographical plots. Throughout those approaches, we observed how validations vary depending on hours and weekdays, how transports and validation rates vary over time, and we obtained interactive geographical representations of public transportation and its use by the citizens.

Predictive model
We created ten different models: short and long-term for pre and post covid and for entering and exiting Porto, and two models (enter and exit Porto) trained with Pre-covid data and tested with Post-Covid data. The models were created using decision trees from the Scikit-learn package (https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html). For training the short-term pre-covid models we used data from 1 Jan-12 Mar and for testing 13-15 Mar. For training the long-term post covid models we used data from 1 Jan-15 Feb and for testing 16 Feb-15 Mar. For training the short-term post covid models we use data from 1 Jun-28 Dec and for testing 29-31 Dec. For training the long-term post-covid models we use 1 Jun-30 Sep and for testing 1 Oct-31 Dec. For the last two models we used for training pre-covid data and for testing post covid data. We then evaluated the error of the models using the relative root mean squared error percent and explained the models using Shapley's values (https://shap.readthedocs.io/).

## 💡 Main Insights (300 words max)

We obtained some interesting patterns in exploratory data analysis (EDA). As expected, people from other municipalities go to Porto for work, as there is an increase in the number of validations to Porto in the rush hours of the morning and another increase of validations from Porto in the rush hours of the afternoon/evening. Furthermore, we could also observe that the number of validations inside the Porto municipality keeps pretty constant during working hours. The EDA also showed that the inter and intra-municipality transportation trips are not optimized, especially during peak hours, because the transports rates do not follow the validation rates, as would ideally happen. During peak hours, there is a lack of transports. Lastly, we could also observe that a larger number of validations occurs around the zone PRT1.

In general, the predictive models were able to follow the pattern of the data when trained specifically for the period in question: pre-covid models for pre-covid testing and post-covid models for post-covid testing. However, as expected, when trained on pre-covid data and tested on post-covid data, the models could not accurately predict the number of validations because the distribution had changed due to pandemic restrictions. In the case of the pre-covid period we found an interesting pattern. At the end of February, after carnival, the number of validations was lower than in the weeks before and after. However, the model was able to predict this change, which aroused our curiosity. We then found that by the end of January there had already been a decrease in the number of validations. We could not explain this pattern. It would have been interesting to see if this occurred in the months prior to January 2020 in order to try to explain what happened in the flow of people.


## 🛠️ Product
### Definition

A dashboard that assists in traffic control providing the reasons of the flow in/out of the metropolitan area of Porto. 

### Users

There are two main users targets: 1) the transport services that can use the dashboard about the flow prediction as a tool to optimize their routes in the metropolitan area of Porto; 2) the citizens or  
traffic control entity that can use the dashboard to have access to traffic information in the metropolitan area of Porto.


### Activities

A model that informs, either in the long or short term, about the flow in the Metropolitan Area of Porto, and as a tool of optimization of routes that require traffic reduction.

### Output

Visualization of the comparison between validations rates and transports rates for each zone, as presented in the notebook, in order to optimize the trips: where/when to add new trips and where/when to remove trips.
Prediction and visualization of future flows in the metropolitan area of Porto. 


## 🌍 Social Impact Measurement
### Outcome

The analysis carried out will potentially lead to a better offer of transport services between areas with a greater flow of people. This will allow people to have better means of transport and will lead to greater adherence by citizens and a consequent reduction in the number of private vehicles.

### Impact Metrics

Number of people circulating between the various zones.
Number of people per transport vehicle used.
Number of validations in the Porto metropolitan area. If it increases, it means that more people are joining public transport.

### Impact Measurement

The optimization of the number of vehicles as a response to the need (more vehicles at peak times between areas with more significant traffic) will allow a better transport offer to citizens. With a better offer, people's satisfaction will increase and, consequently, a greater adherence, leading to a decrease in the number of private vehicles (less traffic, less pollution, less noise). In addition, optimizing transport services can lead to a decrease in costs per vehicle.
