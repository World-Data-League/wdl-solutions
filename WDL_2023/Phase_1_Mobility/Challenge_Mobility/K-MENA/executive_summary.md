# World Data League 2023



## 🎯 Challenge
Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data

Challenge Provider: LxDataLab Lisbon

## Team Name
K-MENA Team


## 👥 Authors
* Sara Sabzikari
* Mine Yasemin 


## ✨ Introduction (250 words max)
Provide a contextualization of the problem, together with an estimation of its size using real numbers and references. In this section you should demonstrate your understanding of the problem.

#### From 1980s-2017, a decreased from 800.000 to 500.000 of inhabitants has been observed from the city of Lisbon to its metropolitan area - this has lead to increased car use in daily commuting between the city and the metropolitan area, overloading of the road network, in conjunction with decrease in public transport. The Lisbon City Council's objectives for the 2023- 2027 period include boosting soft mobility modes, making it easier and more affordable use of public transportation, and promoting the development of an integrated, connected, accessible, multimodal ecosystem. 

#### Our team aims to help the strategic planning towards a city with "Smooth Traffic Flow". To this end, we developed a DL based forecasting model to support the mobility policies for the city of Lisbon by predicting futures trends on mobility flow at particular areas in the city and clustering these areas by impact levels.

#### We have produced a model and product plan that can help users themselves identify inefficient routes and when to consider alternative routes/modes of transport. Stakeholders need reliable insights to inform policy. and people in Lisbon need alternatives, and they need ones that are reliable and easily accessible.


 

## 🔢 Data (250 words max)
Explain what data you used (both provided by WDL and external) and improvements you suggest to those datasets. Explain how those improvements would lead to a better solution.

#### The two main datasets of use were the mobile traffic datasets (1 and 2) locating and quantifying mobile terminals as a proxy for traffic within Lisbons road network. We were provided with some links to public transport coordinates and use, but these didn't seem to match the timeframe of the datasets provided by WDL. If these datasets had matching timeframes, we could create models that would account for traffic levels and the relationships different traffic levels have with public transport usage - this would tell us so much more! 

#### We also used traffic dataset to label each timeframe of mobile phones dataset so that we can make classification. 

#### We also acquired some lists of point of interest (POI) in Lisbon, such as architecture, restaturants, etc. These data can be found online in Google maps. 


## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.
*Write here*

#### Since we have time series data that can be ordered in a sequence, we decided to use LSTM to model it. Our motivation behind the choice of an LSTM-based model is because it can deal with nonstationary of the time series data.  We identify the relationship between variables before building model to know whether or not one time series is useful for forecasting another. In the dataset we used, there are two main features, number of mobile phones entering and exiting the city on the main axes of the city.  We found that the number of entances  is predictive of the future number of exits.  We also use the weekday as an additional feature and transform it as a categorical variable. To improve the model’s performance, we could add other additional information, like working hours, holidays, rain, events, etc.



## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.

#### Observations of mobility:
- Looking at entry and exit data (dataset 2) the busiest days across most roads are Monday-Wednesday and Friday-Saturday, the latter being the busiest (party time?)
- The top 3 busiest roads across the week are 1) IC19, 2) IC2, 3)IC16. The least busiest is A1.  
- The busiest time period during the day for both entry and exit into Lisbon is within 7am and 8am.
- There are clearly tourist hotspots that can be distinguished from total mobile devices - roaming traffic contributes a large amount to total number of mobile devices recorded within many grids.
- Mobile devices in roaming makes a peak at the grids in Parque das Nações in the first days of November. We found out that Web Summit 2022 took place at this area.
- Traffic issues correlate with the total mobile devices.


## 🛠️ Product
In this section you should define the product that can be created by using the model developed. Make sure that the product solves the problem in a holistic way, takes into account the constraints of the topic entities (specifically mention these constraints).
### Definition
Define in **one sentence** what product(s) could be built out of the code you produced.

#### Application for daily use to help people in Lisbon plan more efficient routes.


### Users
Describe who would be the users of your product and for what purpose would they use it.

#### Public sector stakeholders and construction companies can review the visualisation of the busiest parts of Lisbon and use this to inform changes in policy/infrastructure.

#### Commuters and travelling individuals can open the app at any given point and use it to plan their routes in the near future - it will be reliable and tailored specifically to the population and road networks. It could incorporate public transport data, suggesting alternative routes that are likely to evade traffic. 


### Activities
Describe what features your product has.
cidents

#### Features of Product:
* Provides up-to-date insights and predictions on traffic, a source of reliable information to the users.
* It identifies the busiest entry and exit points in Lisbon, encouraging use of alternative routes or different times of travel.


### Output
Describe what the product outputs to the users and how it does that. You can add mockups and/or visualisations.


#### The interactive map that is available in our notebook file and pitch is our method of visualising the traffic levels across Lisbon. We encourage a data contract to be produced between the data provides and Lisbon City Council so that a frequent frequency of data is provided. We would use LSTM to model this data from all roads, including the entry and exit points, to produce outputs that can be visualised through the interactive map for users.

#### For the relevant stakeholders, this is a reliable way to visualise and identify the busiest times in the past, and feed predicted data into the visualisation to see exactly which points in Lisbon have high traffic, and plan road works, public transport routes and other intervations accordingly. We may not have the expertise to suggest tangible interventions, but we can provide the experts with the information they need in order to do so.


### Scalability
Discuss the scalability and the ease of implementation of your solution in the scope of the topic entity. Feel free to mention any road blocks you see and how they could be solved.


## 🌍 Social Impact Measurement
This section will help to guide you on how to measure the impact of your product. Make sure that measurement is thoroughly quantitative, even if you need to estimate some of the numbers.
### Outcome
If the outputs are your immediate results, describe your long-term results. What do you want your product to achieve? What ''good'' are you creating?


#### The product can predict the traffic flow and suggest users SHARED MOBILITY, for example, car sharing or shifting their short distance car trips by greener transport options such as walking or cycling. It can also help mobility providers on important decisions such as how many buses should operate on a route at different times of day.

### Impact Metrics
From the outcome, define **2 to 4 metrics** that measure, whether you are achieving that outcome or not.

#### Our metrics to define whether we are achieving our outcome: 
* Reduced average mobile terminals in the peak grid IDs during 7am and 8am
* Reduced average traffic congestion level in the peak grid IDs during 7am and 8am

### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.

#### Our model estimates the mobility flow (number of entrances and exits) in the near future. Inspired by the features available on Google Maps and findings from articles such as K. S. Ali, and N. M. Abid's 2021 article "The Importance of Google Maps for Traffic in Calculating the Level of Service for the Road and Traffic Delay", this provides stakeholders with up-to-date visualisations of near-past events, and more accurate predictions of future traffic flows, and if used effectively can help more stakeholders make more informed decisions. 