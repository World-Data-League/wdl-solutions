# World Data League 2023

## 🎯 Challenge
*Energy communities inclusive of residents vulnerable to energy poverty*


## Team Name
AI Wonder Girls


## 👥 Authors
* Divya Kamat
* Emma Roscow
* Ernitia Paramasari
* Pankaja Shankar


## ✨ Introduction

In Europe, up to 80 million households struggle to pay their energy bills [1]. The pressures of climate change combined with economic and geopolitical challenges have created an urgent need to turn away from traditional hybrid energy sources and towards more renewable energy solutions. "Renewable energy communities" (RECs) have been embraced as a solution which meets these challanges: defined loosely as groups of residents and/or businesses united in a goal to generate renewable energy, RECs are being promoted in the EU as part of its renewable energy directive for 2018-2030 [3] to energy security for its members, affordability and environmental sustainability [2]. In the Flanders region of Belgium, it has been estimated that energy communities could reduce members' costs by up to 26% and greenhouse gas emissions by up to 13% [4]. While RECs have seen success in Belgium already, there is considerable scope to increase participation. Research on REC participation elsewhere in Europe has shown that members tend to be older, wealthier and more educated, leaving other groups who are more vulnerable to energy poverty underrepresented [1]. Barriers to joining energy communities include a range of financial, educational, social and attitudinal factors [2, 4, 6], which are often heightened among poorer households [1], so our solution attempts to make it as easy as possible for households vulnerable to energy poverty to establish or join energy communities, convince them of the benefits, and recommend an energy community that best suits their needs. In this challenge, we have used a suite of modelling methods to optimise the clustering of households in Ghent into recommended energy communities, dervied recommendations for the municipality about how to promote them, and built an app to encourage local participation.

[1] Hanke, F., Guyet, R., & Feenstra, M. (2021). Do renewable energy communities deliver energy justice? Exploring insights from 71 European cases. Energy Research & Social Science, 80, 102244.

[2] Gjorgievski, V. Z., Cundeva, S., &  Georghiou, G. E. (2021). Social arrangements, technical designs and  impacts of energy communities: A review. Renewable Energy, 169, 1138-1156.

[3] https://energy.ec.europa.eu/topics/renewable-energy/renewable-energy-directive-targets-and-rules/renewable-energy-directive_en

[4] Felice et al. (2022). Renewable energy communities: Do they have a business case in Flanders? Applied Energy 322, 119419.

[5] Bauwens, T. (2019). Analyzing the determinants of the size of investments by community renewable energy members: Findings and policy implications from Flanders. Energy Policy, 129,841-852.

[6] Conradie, P. D., De Ruyck, O., Saldien, J., & Ponnet, K. (2021). Who wants to join a renewable energy community in Flanders? Applying an extended model of Theory of Planned Behaviour to understand intent to participate. Energy Policy, 151, 112121.


## 🔢 Data
We used the following datasets from WDL:
* energy_consumption_street_level which provides the data on annual energy consumption for individual streets and the number of energy supply access points for each street
* Gent_SOL_v3 which provides the data on building types, building location, rooftop area, and an estimated amount of energy that would be generated by a solar installation

We also performed some literature research and used the following external factors, formulae, and data:
* Typical installation cost of solar panels
* Typical energy tariff in Belgium
* Hours of sunshine in Ghent

We made various assumptions and inferences using these data to produce our solution, and we recommend using data with higher spatial and temporal fidelity in the future to improve the recommendations, while acknowledging that sharing such data poses privacy problems. Specifically, per-household energy consumption would allow better clustering of households into energy communities based on their needs, and data on consumption throughout the day would allow modelling of demand load shift and consideration of the interaction between solar power generation, immediate consumption, and battery storage.


## 🧮 Methods and Techniques
In order to recommend the best configuration of energy communities in Ghent, we first identified key performance indicators (KPIs) that could be used to quantify them based on the data available and assumptions we could make. Among the many KPIs we identified, we selected four to optimise on:
* the annualised profitability for each member of the REC
* the size in terms of number of members
* the start-up capital required
* the geographical proximity of the members.

This prioritises the financial and social aspects of an REC, but we recommend that other logistical, environmental and socioeconomic KPIs could be used as well. These KPIs were combined into a single objective function used to quantify and optimise the (mean of the) recommended RECs depending on the number and consumption of their proposed members, and the potential electricity generation from recommended solar panel installations.

For the simplicity of our proof-of-concept model, our focus was on households (rather than businesses), included all households in the city or a region of the city, and we assumed a fixed energy cooperative model in which all members invest the same amount.

With this objective function, we used three methods to perform optimisation of the energy communities:
1. The baseline, a simple random assignment of the communities, against which the other two could be compared
2. An unsupervised method using K-means clustering, which minimised the distances between members and solar panels
3. Our own tiered optimisation algorithm which iteratively optimises the assignment of members and solar panels to energy communities until it reaches convergence

The first two models were chosen for their simplicity and, in the case of k-means, its guarantee to reach convergence. The third model was chosen to be more tailored to the data and objectives we have.

## 💡 Main Insights
With the right optimisation, energy communities in Ghent can be profitable, local, and not too financially burdensome to start up. Our modelling predicted energy communities with around 10 members, optimised correctly, can save each one over €1000 on average. However, the question of financial affordability is an important one for the municipality of Ghent to consider: higher returns can be obtained with greater start-up capital, which is exactly what energy-poor households lack. By considering different models of financing solar panel installation, energy communities can be developed which are inclusive, fair to all members, efficient, profitable and sustainable. Our modelling and analysis can be used as a tool to explore these considerations.


## 🛠️ Product

### Definition
Primarily, our product is a web app that recommends neighbours with whom to form a REC, location(s) at which to install solar panels, expected costs and returns (financial, environmental, and otherwise), and information on how to get started.

As a secondary feature, Ghent authorities can use our modelling to analyse where to focus their effors to support the use of RECs for fighting energy poverty, for example the financial burdens and barriers.

### Users
Primarily, the residents of the city of Ghent: especially those vulnerable to energy poverty who may never before have considered forming an energy community with their neighbours.

### Activities
* Recommends nearby households with which you can form a high-quality energy community, and locations for solar panels
* Provides information on the potential monetary saving per household
* Provides information on the potential carbon emission reduction per household
* Directs to other resources to support the formation of an energy community

### Output
* A list of addresses of the recommended energy community for the user based on their input
* A value of the potential monetary saving per household
* A value of the potential carbon emission reduction per household

### Scalability
We have designed our models for Ghent and analysed the Malem region of Ghent, but it is scalable to any similar urban environment where similar data is available, and easily retrainable for such purposes. It is also scalable to different considerations even within Ghent: for example different financing models or participation of non-residential members.

## 🌍 Social Impact Measurement

### Outcome
We recognise that that technical challenge of matching people with each other and with optimal locations for solar panel installation is only part of the issue. The other part is persuading residents of the problem of unsustainable energy and energy insecurity, persuading them of the solution that energy communities offer, and removing barriers that discourage them from participating. The intended outcome is that as many Ghent residents as possible join energy communities, that they reduce their energy bills as much as possible, and that they reduce their carbon emissions as much as possible. This will alleviate energy poverty in the city and meet sustainable development goals. In the best case it will also enhance social cohesion and a sense of community and empowerment among members as secondary benefits [1].

### Impact Metrics
Our KPIs measure the impact that energy communities could have. In particular, given the goals of sustainability and fighting energy poverty, we recommend focusing on:
* Total reduction in members' energy bills (compared to not being a member of an energy community)
* Total reduction in members' carbon emissions (compared to getting all electricity from the Belgian grid)

### Impact Measurement
Similar analysis of the potential for energy communities in Belgium have shown that costs could be reduced by 10-26% and emissions by 5-13% [2], but the challenge is in the numbers: breaking down barriers to persuade more people to join energy communities [1, 2]. Our modelling suggests that members of the energy communities we recommend could save over €1000 each in energy bills per year, if the right ratio of members to solar electricity generation is obtained.


[1] Hanke, F., & Lowitzsch, J. (2020). Empowering vulnerable consumers to join renewable energy communities—Towards an inclusive design of the clean energy package. Energies, 13(7), 1615.

[2] Felice et al. (2022). Renewable energy communities: Do they have a business case in Flanders? Applied Energy 322, 119419.
