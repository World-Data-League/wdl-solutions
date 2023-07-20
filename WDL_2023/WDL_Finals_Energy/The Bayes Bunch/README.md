# World Data League 2023

## 🎯 Challenge 3: Energy communities inclusive of residents vulnerable to energy poverty


## Team Name
The Bayes Bunch

## 👥 Authors
* Mitra Ganeson
* Roisin Holmes
* Samantha Hakes
* Stuart McGibbon
* Zhen-Yen Chan

## ✨ Introduction 
In Europe, energy prices continue to be unstable as environmental needs change and as a reaction to current geopolitical tension. In Belgium, this instability led to an increase in the cost of natural gas from 0.078 € per kWh, to 0.118 € per kWh in the space of one year. [source](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20230426-2#:~:text=Average%20gas%20prices%20also%20increased,the%20second%20half%20of%202022.)

Whilst Belgian inflation as a whole is no longer increasing at the rate of mid 2022, consumers are undoubtedly feeling the impacts of an increased cost of living. 
![](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/44ec70ae646c9cf369ecaba8f68f140fcb97b681/image4.png)

Given that energy costs are a key spend for households, it’s unsurprising that there has been an increased demand for help with regards to energy payments, with many households falling into the population at risk of energy poverty (In Gent alone, there are estimated to be as many as 35,000 people at risk of [energy poverty](https://www.citego.org/bdf_fiche-document-1160_en.html)). 

The impacts of energy poverty on society are far reaching, contributing to a reduced standard of living, and also impacting health and social services.

Alternatives to commercial energy usage are potentially an excellent way to enable households to remain on top of finances and take back control of their energy consumption.
Whilst the costs of installing energy production infrastructure may be too great for an individual to consider, the opportunity to form energy communities and share costs, could alleviate some of the energy bill stresses, whilst contributing to a greener environment. 



## 🔢 Data

In this phase we used the provided WDL Gent datasets on energy consumption, EV charging, decentralised energy installations, rent pricing and solar irradiance. These datasets were at various levels of details and did not always allow for the necessary level of information to be used within our modelling.

We also used several non-WDL sources in our modelling, such as statistics from Statbel on Belgium and Gent population, income etc. We used open street data to enable geospatial joins at the level of the solar irradiance dataset. Another source we utilised was the newly published Belgian Index of Multiple Deprivation (BIMD), which considers several factors when creating an aggregate deprivation index for each Belgian statistical sector.

We ingested and cleaned these datasets, dealing with any null/missing values as appropriate. One area of improvement could be the accuracy of the property type data. We could also spend further time researching the energy consumption and production metrics, to provide enhanced features for modelling.

In future, combining the solar irradiance data with property level census data could enable a further layer of analysis, which we were unable to achieve from the reduced datasets above.


## 🧮 Methods and Techniques
We explored various options for formulating a data problem that can be solved using optimisation. Our top 3 approaches are:
Firstly, we defined criteria to reduce the pool of households to those that are more likely to face energy poverty and those who are near potential energy sources. We ran a k-means algorithm to cluster these participants into energy communities.
We created an inference function where users could adjust the constraints and size of the clusters, and visualised the results on an interactive Streamlit dashboard.
The second approach was spatial optimisation using the pygeoda library. Using queen contiguous weights ensures that the distance within clusters are minimised and clusters are physically next to each other. We also applied max-p regionalisation to impose constraints such as a minimum total income in each cluster.
This can be extended to other indicators to ensure vulnerable populations are equitably distributed across communities. Geoda is also available as a free visualisation software, but unfortunately due to compute limitations we were not able to run this algorithm on the full dataset.
Our third approach utilised reinforcement learning (RL). We created a custom environment specifically for defining energy communities (CommunityEnv), where the actions are features relevant to model users (like energy poverty indicators).

The reward function is defined based on the aims for the communities and the model was trained using DeepQNetwork, learning the best way to create energy communities that maximise the reward.

## 💡 Main Insights
This plot shows the deprivation index per sector for Gent.
![BIMD in Gent](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/44ec70ae646c9cf369ecaba8f68f140fcb97b681/image5.png)


Higher scores indicate lower levels of deprivation which are prevalent in the city centre regions.

For our rules-spatial solution, the number of clusters was fixed at 23 (to match the RL output). The size of the communities were equally distributed at ~1000 addresses. This community size is likely too high for practical purposes. Expert judgement and more granular data (at address level) are needed to distinguish smaller communities. The best available solar sites were mapped to these communities. 
The algorithm found ~13 communities with high density of good solar panel sites. These are the recommended communities/ larger subset from which smaller communities could be formed. The plot below shows the model output, different colours indicate separate clusters. 

![Energy Communities](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/44ec70ae646c9cf369ecaba8f68f140fcb97b681/image3.png)

The reinforcement learning algorithm was constrained to finding the best communities totalling 400 participants. This ability to prioritise is an advantage of the RL model over the MVP solution. The reward over time for the Reinforcement algorithm is shown below:

![Reward](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/44ec70ae646c9cf369ecaba8f68f140fcb97b681/image2.png)

This demonstrates that the agent was able to learn from the data and improve the communities (in the context of our reward system). The derived communities from the RL solution are shown below:

![RL Communities](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/44ec70ae646c9cf369ecaba8f68f140fcb97b681/image1.png)


For evaluation, the two methods were compared using **ranked_mean**:
- Average of the mean rank of selected features per cluster
- Ranking order is selected based on the feature and challenge requirements (e.g, lower BIMD scores are ranked higher as we prioritise less affluent areas)
 
![Comparrison](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/44ec70ae646c9cf369ecaba8f68f140fcb97b681/image6.png)


The MVP solution outperforms the RL algorithm for most clusters (order arbitrary). The RL algorithm can be improved by tuning the reward function (community priorities) with SME input. The MVP also runs faster than RL (1.3 seconds vs 40mins) so we conclude that rules-spatial method is more suitable in a live application.


## 🛠️ Product

### Definition
Ecomapper is an open source Python package and dashboard, to be utilised to optimise energy community location and drive down energy poverty.

### Users
The main types of consumers that we see as key users of Ecomapper are:
Governmental/ council workers (e.g. City of Gent staff)
Charity workers who are focused on helping those at risk of energy poverty.
Individual households who may be in search of information and detail on their potential to start/ join an energy community.

### Activities
Users can visualise areas of Gent which are at particular risk of energy poverty.
Understand which locations would be suitable to propose as energy communities.
Toggle dashboard levers, and optimise the output to fit individual constraints.
Calculate the costs and cost-benefit analysis of forming energy communities, and planning ways to best deal with energy poverty.
Collect valuable insight in order to engage with governing bodies to incentivise a transition to a greener energy system.

### Output 
For technical users, our open source python package allows for technical implementation and iteration on the tool.This is available here (https://github.com/StuartJMc/ecomapper) and can be altered to work in different environments.

For non-technical users, Ecomapper comes with a user-friendly dashboard. This removes complex models and calculations and allows them to interact with a simple interface where they can clearly see the impact of their selections.

Users can adjust inputs to focus and test different scenarios (for example changing the subpopulation they are aiming to target). A screenshot of the dashboard is shown below.
![](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/44ec70ae646c9cf369ecaba8f68f140fcb97b681/image7.png)


### Scalability
Ecomapper has been designed to be scalable in multiple ways, 
Though modelling choices, such as using reinforcement learning to iterate and improve upon the model output.
Through tool use, the dashboard can be optimised for multiple metrics, and hence users can test and adapt to different input scenarios.
Through Data choice, by choosing commonly found data for territories and cities, we believe that running the model in varying environments is entirely feasible. For example using deprivation indices from other countries (e.g. [scottish IMD](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)), twinned with open mapping data. Solar data is becoming more and more abundant, and the tool could even look to benefit from applications such as Google’s Project Sunroof. (https://sunroof.withgoogle.com/)


## 🌍 Social Impact Measurement

### Outcome (what good is it doing)
Ecomapper will allow the city of Gent to make better plans for targeting potential energy communities.
By understanding areas which could benefit from community installs, reliance on commercial energy providers (and unpredictable energy pricing) will decrease. 
By using the tool to find suitable energy communities, the households suggested could benefit from a greater sense of community and control, and hence a greater standard and quality of life.
Additionally, the tool will allow users to define and realise their impact on the environment, and guide communities in how best to reduce their emissions.

### Impact Metrics
Reduction in energy bills (and subsequent reduction in number of households at risk of energy poverty).
Reduction in harmful emissions from energy usage.
Number of target communities identified for potential as energy communities.
 
### Impact Measurement
From our MVP dashboard (See above), the top 16 energy communities have capacity to produce 97 MWh of electricity per year. This equates to a potential emission saving of 18 tCO2e  

The initial investment for these solar facilities would cost £142,000, but would come with a cost saving of £15,600 per year (saving on fuel bills). Thus, the installations could pay themself back in a little over 9 years.
The lack of reliance on commercial energy sources could aid in the reduction of energy poverty. A similar program in London gave energy advice to 175 households and had financial benefits for the communities of £31,000.

[Belgium fuel usage split](https://www.energuide.be/en/consumption-and-rates/consumption/10/)

[Fuel emission factors](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2022)

[Solar install costs]( https://www.greenbuildingrenewables.co.uk/solar-panels/)

[Repowering](https://www.energymonitor.ai/sectors/power/can-community-energy-save-lives-this-winter/)

[Fuel prices](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Natural_Gas_price_statistics)

