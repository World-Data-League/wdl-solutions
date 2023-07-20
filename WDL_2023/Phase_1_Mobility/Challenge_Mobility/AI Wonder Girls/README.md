# World Data League 2023


## Executive Summary Template
This executive summary is one of the mandatory deliverables when you submit your solution. Its structure follows the WDL evaluation criteria and it has dedicated sections where you should add information. Make sure your executive summary covers all the sections since it will be an integral part of the Insights Report and your evaluation. Make sure your content is relevant and straight to the point.
**There is no need to reach the maximum number of words.**


Instructions:


1. 🧱 Create a separate copy of this template and do not change the predefined structure
2. 👥 Fill in the Authors section with the names of allteam members
3. ✏️ Write your executive summary - make sure you write for a non-technical audience. 
4. 📄 Fill in all the text sections
5. 🗑️ Remove this section (‘Executive Summary Template’) and any instructions inside other sections
6. ⬆️ Upload the .md file to the submission platform.


## 🎯 Challenge
Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data


## Team Name
AI Wonder Girls


## 👥 Authors
Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.
* Ernitia Paramasari
* Pankaja Shankar
* Divya Kamat
* Emma Roscow


## ✨ Introduction (250 words max)
Provide a contextualization of the problem, together with an estimation of its size using real numbers and references. In this section you should demonstrate your understanding of the problem.
*Write here*
In recent years, Lisbon has seen more of its population move to the surrounding metropolitan area and commute into the city, primarily by car. In 2018, 370,000 cars entered the city of 500,000 residents every day [1], causing reduced safety and quality of life for residents, an overloaded road network, and high carbon emissions. In response, Lisbon City Council wishes to promote soft mobility options and reduce commuter reliance on private car use, to improve residents' daily lives and meet its aims to reduce greenhouse gases by 40% [1] by 2030. To support the city in meeting these goals, we provide insight into the routes that people take into the city during morning weekday rush hours. Our innovation is twofold: first, we focus on where people terminate their journeys during morning rush hours: that is, where they head to. We identify the top destinations, where 120,000 people arrive every morning, and identify shortcomings in current public transport and cycling infrastructure that serves these routes. Secondly, we develop a graph neural network that learns the dynamic connections between city grids, as a prototype tool for visualising, predicting and simulating how people travel. This tool allows city planners to anticipate and predict the effect that interventions on commuters' routes might have on the flow of people in the city during rush hours. We estimate that, by improving soft mobility infrastructure, carbon emissions could be reduced by XXX.
[1] Move Lisboa: Strategic Vision for Mobility 2030


## 🔢 Data (250 words max)
Explain what data you used (both provided by WDL and external) and improvements you suggest to those datasets. Explain how those improvements would lead to a better solution.
*Write here*

*Graph neural network data*
Our primary data source was dataset 1 (mobile data in grids), which we used to build a graph neural network. We reduced this dataset to:
* the morning rush hour (7am - 10am) on weekdays and non-roaming devices, to focus on the routes taken by commuters into the city, to identify how to reduce the total number of cars in the city
* grids with at least 500 poeple entering and/or exiting the grid per hour during morning rush hours, to focus on mobility via common commuter routes
* entries and exits, to reveal mobility patterns

The resulting model is a prototype which has room for future improvement. Specifically, we suggest:
* including data from the axes, to gather more information on mobility which would lead to more accurate predictions
* interpolating over the time series, to get high temporal resolution about the flow of people for a more sensitive analysis of flow
* mapping device data to roads rather than grids, to better model movements between them
* adding additional data which previous research efforts have found beneficial such as weather and commercial/residential/other use of land [1]

*Visualisation*
To visualise movement through the city, we also used datasets 3, 4 and 5 which contain grid locations and shapefiles.

*Soft mobility analysis*
We augmented the provided datasets with open-access data on public transport and cycling infrastructure in the city, from Lisboa Aberta [2] and OpenStreetMap [3].

*Carbon emissions analysis*
To estimate the potential savings in carbon emissions from reducing congestion, we used the data on traffic jams from dataset 8.

[1] Zhu et al., 2020. AST-GCN: Attribute-Augmented Spatiotemporal Graph Convolutional Network for Traffic Forecasting. IEEE Transactions on Intelligent Transportation Systems
[2] https://lisboaaberta.cm-lisboa.pt/index.php/pt/
[3] https://www.openstreetmap.org/


## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.
*Write here*

*EDA*
We began by visualising the data provided to us, and identified that the highest peak in incoming traffic to Lisbon (via the 11 axes) comes during the morning weekday rush hour. We therefore identified that our solution should focus on understanding mobility patterns during this period to have maximum impact on private vehicle traffic in the city.

*Feature engineering*
We reduced the dataset as described above, and divided the data into a training set (1st Sep - 31st Oct), a validation set for improving the model (1st - 15th Nov), and an unseen test set (16th - 30th Nov). The grids were used as nodes for the graph neural network, their entries and exits per timestamp the node features, and the distance as edge features.

*Model training*
We used the datasets provided to train a prototype of a temporal graph convolutional network to predict movement around the gridded locations of Lisbon from mobile devices.
Model used for training is temporal graph convolutional network (T-GCN) model, which is in combination with the graph convolutional network (GCN) and gated recurrent unit (GRU). Specifically, the GCN is used to learn complex topological structures to capture spatial dependence and the gated recurrent unit is used to learn dynamic changes of traffic data to capture temporal dependence. 
Model is trained for 20 epochs. 

*Model simulations*
By manipulating mobility data, we used the TGCN based graphic neural network to infer the result of hypothetical changes to mobility patterns.

*Analysis of commuter destinations*
The grids with the highest difference between entries and exits during morning rush hours were isolated as destination grids (specifically, the top 5th percentile), and we used the spatial relationships between destination grids and soft mobility infrastructure to analyse weaknesses.

*Carbon emissions analysis*
[Description of carbon emissions analysis here]



## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.
*Write here*
There are a small number of grids in the city which serve as destinations for a large number (around 120,000) of people during morning rush hours, and are typically located far away from existing public transport infrastructure (train and metro stations, tram stops, and river transport stops): on average, the nearest of these is 2 km away from the grid centre. Lisbon is already committed to providing more buses and trams [1]: to provide soft mobility options for commuters heading to these destinations, either the public transport provision needs to be increased to serve these destinations, or additional mobility options such as shared bike schemes need to be provided to facilitate travel from these public transport facilities to the destination grids. The destination grids are currently better served by buses (there are, on average, 3 bus stops within 1 km of a destination grid centre), but this provision could be increased to encourage bus travel as a viable commuting option. Lisbon also has a docked bike sharing system which is useful for connecting with major transport hubs such as train stations, but these are also located too far away from destination grids to be convenient for commuters (1.2 km away from the destination grid centres, on average).
[Add insights from the graph model results: what are the busiest routes? What difference could it make if use of some axis was increased or decreased?]

[1] https://cities-today.com/how-lisbon-is-reshaping-its-mobility-landscape/


## 🛠️ Product
In this section you should define the product that can be created by using the model developed. Make sure that the product solves the problem in a holistic way, takes into account the constraints of the topic entities (specifically mention these constraints).
### Definition
Define in **one sentence** what product(s) could be built out of the code you produced.
Example: A dashboard that assists in traffic control
Our model serves as a prototype simulator of the flow of people into and around the city during morning rush hours, based on real or simulated data as needed. [Add in some metric of accuracy for performance on test data, if it's good enough?]


### Users
Describe who would be the users of your product and for what purpose would they use it.
Example: Traffic controllers use the dashboard during their work to better plan where to dispatch resources
Lisbon City Council (for example Lisbon's Department of Transportation) can use this to predict the effect that various interventions might have on the flow of people during morning rush hours: for example, if traffic along an axis were reduced by encouraging train usage into the city, or reducing capacity on some roads by pedestrianising or making way for cycle paths. City planners typically need to weight up various possible interventions to ensure return on investment and engage stakeholders, so simulating the effects of their plans can be a powerful tool for selecting the right approach to meet their goals.


### Activities
Describe what features your product has.
Example:
* Predicts the most likely locations for traffic accidents
* Suggests the fastest route from dispatch centres

Our model does three things:
1. It describes the flow of mobile devices through the city's main grids during morning rush hours, providing visual insights into commuters' most popular routes and destinations.
2. It predicts the movements depending on entries to the city via the main axes based on learned connections between the grids.
3. It can predict the resulting movements following interventions which would change the patterns of entry via the axes, allowing evaluation of possible projects to promote sustainable mobility over private car use among commuters from the metropolitan area.
We also envision future refinements which would allow prediction of traffic jams and resulting carbon emissions from the predicted movement around the city, given more time to add features to the product, to better aid users in optimising traffic flow and minimising greenhouse gas emissions.


### Output
Describe what the product outputs to the users and how it does that. You can add mockups and/or visualisations.
Example: Location of the accident on a map and suggest the fastest route from the dispatch centre.
The output is a model which allows users to simulate and predict effects or changes to the flow of people during morning rush hours. This will alow them to identify the best interventions to promote sustainable mobility. We believe that by providing more integrated soft mobility options to serve the most common destinations, commuters can be persuaded not to use the 11 axes as their point of entry to the city, and our tool can help city planners predict how transport users will move around the city in response. Ultimately, by making better use of public space, the city can be made more liveable and carbon emissions can be reduced.


### Scalability
Discuss the scalability and the ease of implementation of your solution in the scope of the topic entity. Feel free to mention any road blocks you see and how they could be solved.
The model is flexible enough that it can be extended to various other datasets: from other cities, other times of day beyond rush hours, vehicle data rather than mobile data, other times of year, more recent data, or longer periods of time. Re-training the model is simple and scalable, although with very large amounts of data it may require high-spec hardware.


## 🌍 Social Impact Measurement
This section will help to guide you on how to measure the impact of your product. Make sure that measurement is thoroughly quantitative, even if you need to estimate some of the numbers.
### Outcome
If the outputs are your immediate results, describe your long-term results. What do you want your product to achieve? What ''good'' are you creating?
Example: To decrease response time from dispatchers so that people in urgent need receive help faster.
Our analysis and model will improve the experience for:
- residents of Lisbon, who will face less congestion and pollution in their city
- city planners, who can show that their planning is data-driven and assess possible interventions more easily
- commuters, who will have more options to reach their destinations including healthy and sustainble mobility
- tourists, who will benefit from a more enjoyable city and plan their visit better
- the planet, thanks to promotion of more sustainable and environmentally friendly transit


### Impact Metrics
From the outcome, define **2 to 4 metrics** that measure, whether you are achieving that outcome or not.
Example:
* Average Dispatch Time
* Average Distance from Accident Location and Dispatch Center
Reduced number and average length of traffic jams, thanks to fewer private vehicles and better flow of people around the city during rush hours.


### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.
Example:
* *Based on model predictions*: Our model estimates a decrease of 6 minutes of the average dispatch time and a decrease of the average distance of 200 metres
* *Based on proxy products*: Similar studies in other cities show that the dispatch time can be decreased by as much as 13 minutes, depending on the traffic intensity of that city.
Estimated carbon emissions from traffic jams in Lisbon per day is 15.4 kilo tonnes of CO2. Reducing 10% of traffic jam would theoretically save approximately 1.5 kilo tonnes of CO2.
