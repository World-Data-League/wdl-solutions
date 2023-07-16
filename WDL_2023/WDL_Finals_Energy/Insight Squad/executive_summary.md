# World Data League 2023


## 🎯 Challenge
Energy: Proposes energy communities in the city of Ghent, considering factors such as renewable energy production sites, energy consumption patterns, and the inclusion of residents vulnerable to energy poverty


## Team Name
Insight Squad 💡


## 👥 Authors
* Maria Manuel Castro
* Ricardo Ângelo Filipe
* Rodrigo Miguel Ferreira
* Catarina Campos Rocha
* Eduardo Daniel Vicente


## ✨ Introduction (250 words max)

51 billion tons. This is the number of greenhouse gas (GHG) globally added to the atmosphere in a typical year[\[1\]][1]. More importantly, this is the number we need to focus when we talk about zero emission politics. Additionally, when we breakdown this number into sectors, to see major contributors, we verify the following:
1. making things like cement, steel and plastic: 31%
2. Electricity: 27%
3. Agriculture and farming: 19%
4. Transportation: e.g. planes, ships, vehicles, trucks: 16%
5. Temperature regulation: heating, cooling, refrigeration: 7%

Surprisingly (at least for our team), although there is a lot of publicity, and government policies related with vehicles electrification, the overall contribution to climacteric changes is *only* 16%.
Taking into consideration that making electricity is the second category to GHG, energy communities may pave the way to reduce our ecological footprint.

To achieve this, World Data League challenged the finalists on the topic of Energy. 
The goal is simple: taking into consideration three factors - renewable energy production sites, energy consumption patterns, inclusion of residents vulnerable to energy poverty -, propose energy communities in Ghent and extrapolate to other cities with similar raw data.





## 🔢 Data (250 words max)


For each datasource we read it, made an assessment in terms of the quality of the data, and clean it up. Most of the data clean were based on a panda profile report runned over the original datasets. Based on that reports we remove the duplicates and treat the missing data. 

Sources that correspond to reference data will be worked together with the sources referring to the facts and measures taken.

From the datasets provided by WDL we used the following:

* average_income_per_sector.csv
* energy_consumption_monthly.csv
* energy_consumption_street_level.csv (enriched with location of Ghent Sector)
* energy_decentral_production.csv
* energy_local_production.csv
* energy_storage_systems.csv
* ev_points.csv (only data statistics)
* ent_SOL_v3.shp ( enriched with location of Ghent Sector)
* straten-gent.geojson

We also created a new dataset (WDL_sectors_info_external) to have populational density, area, polygon shape and population by sector using information from [\[2\]][2] and [\[3\]][3]


We also created a new dataset that acts has a summary by Sector for several characteristics (consume, potencial energy production, income, ...)

Concerning Feature Engineering, we created several new metrics such as ratios, averages per inhabitant and also a vulnerability score (please refer to the notebook, to a deeper knowledge about those metrics).


## 🧮 Methods and Techniques (250 words max)

First, we used the standard tool belt for data scientists: pandas, scikit and numpy. The goal was to clean, detect missing data, duplicated lines and make a quick benchmark of our data.
Secondly, we used Pandas Profiling to understand better the data.

We also made some heatmaps using Folium.

Also, we think it's important to have our work outside of the notebook, to be foreseign by more non-technical people. Hence, we created a small frontend using React and Typescript.

Finally, for our clustering algorithms we experimented some spatial clustering algorithms, such as DBSCAN, OPTICS or spatially extended versions of k-means. In this executive summary, due to space constraints, we will only focus on the most promising outputs.


## 💡 Main Insights (300 words max)

The Main Insights discovered by our squad were:

* The majority of top 10 sectors of vulnerability is associated with outskirts of the city (Tolhuis, Wondelgemstraat, Ledeberg - Centrum, Drongensteenweg, Van Bevereplein, Rooigem, Brugse Poort, Groendreef, Station, Heernis).
* We identified that population density is more correlated with gas consumption that with electricity consumption.
E.g. 
![Correlation Matrix](https://peaceful-sherbet-485f81.netlify.app/challenge3_confusion_matrix.png)

* In the winter, there is a spike in the consumption of gas energy. The consumption of electricity tends to be constant.
![Energy Cycle](https://peaceful-sherbet-485f81.netlify.app/challenge3_energy_cycle.png)
* There are already some Ghent Sectors that produce energy (30 out of 201 Ghent Sectors)
![Energy Production](https://peaceful-sherbet-485f81.netlify.app/challenge3_inject_electricity.png)
* Model clusters: For instance, one of the clusters is formed by 5 elements (Tolhuis, Wondelgemstraat, Blaisantvest, Niew Gent, Neermeersen). Interestingly, four of these elements belong to the top 20 most vulnerable sectors, occupying positions 1, 2, 13, and 17, respectively.


## 🛠️ Product
We deliver three artefacts to better understand this Energy challenge. 

First, a data analysis throughout the gathered data. Understanding the data and pinpointing parameters that may influence the creation of energy communities may have a significant benefit for the environmental policies of the city. 

, where similar community implementation strategies can be pursued

Secondly, a clustering model, which intention is to identify groups of sectors that have similar characteristics. With careful consideration of the sectors in each cluster, the Ghent City Council can outline a strategic plan for the implementation of a community pilot program. The model can be integrated in a dashboard to help Ghent City politicians avoid wrong decisions for a better and sustainable environment.

Finally, a small frontend with two pages: First page with some heatmaps of Ghent city for income, consumption, energy potencial and the result of our clustering model [\[4\]][4]. Secondly, to help energy communities foreseeing their environmental impact, we also created a environmental calculator [\[5\]][5]. This calculator quantifies the positive impact of solar panels installation in the environment for a range of outputs, such as carbon dioxid reduction, passenger car taken out of road. etc, and was based on [\[6\]][6], [\[7\]][7] and [\[8\]][8].


### Definition
A data analysis, a clustering model and a small frontend that assists Ghent Governance in energetical environmental strategies.


### Users

To have a holistic solution to the Energy challenge, the solution must address two users:
*  Ghent Politics that uses the clustering model and the data analysis. The clustering model and heatmaps may be available through a dashboard as the one presented [here][4]. Having heatmaps associated with the three main factors (income, consumption and energy potential) and tabled aggregated information may help to understand how the Ghent City should address this issue. We aim to describe the overall distribution of the aforementioned factors by sector and enlighten possible energy politics to swiftly improve the future of the local energy communities.
* City Population. The overall population should have access to visualizations and report from the work. Additionally, they should have access to the environmental calculator [\[5\]][5]. A more environmental conscience, specially associated to parameters that the energy communities can quantify may have a significant impact in Ghent city. ⚡💚



### Activities
Features that our product has:
1. Visualization Report of aggregated and cleaned data from the collected datasets.
2. Clustering model for the energy communities
3. Neat working frontend with the heatmaps and the environmental calculator


### Output
The output will be a better understanding for the energy communities for Ghent City. 
Citing Albert Einstein [\[9\]][9]: 
> If you want to know the future, look at the past.

Hence, the main output of this work are:
1. Looking to the Past: 
	1. Exploratory Data Analysis (EDA) of WDL datasets
	2. Frontend with the Heatmaps for the three main factors referred by Ghent City Council.
	3. This way we can understand better the factors that may contribute to the creation of energy communities
2. Know the future:
	1. Clustering Model based on OPTICS [\[10\]][10]



### Scalability
To endeavor a tool that has scalability to retrieve a vision of the energy communities (regardless of the city) there are some concerns that need to be address:

1. *Data Collection and Cleaning*: currently the tool/notebook is in *offline* state. To have the fastest response (and probably a near real-time dashboard) we need a stream of data processed in near real time. This may be a challenge both for the data producers and also to our processing logic.
2. *Environmental Management Strategies*: based on our insights/dashboard, environmental policies may pinpoint areas that can work has an energy community. 
However, the question arises: is the overall Ghent population prepared to actively create energy production clusters that don't exist nowadays? 
It may be needed some education, advertising campaign in Ghent for new policies (or even tax credits). Additionally, this problem also arises to other city locations.
3. *Model clustering adoption*: one of our product features is the clustering of energy communities. First, the number of clusters is not fixed, being a good feature to scalability. Hence, we are assuming that the model will be adequate to Ghent (or city with similar raw data). However, if that do not occur, we will need to redefine the model - probably with more feature engineering or merging the data with other data sources. 
4. *Environmental Calculator*: The calculator [\[5\]][5] is highly adptable to factors such as annual hours of sun light, energy cost or even billing invoice. Hence, it is a perfect fit to every energy community needs. 

## 🌍 Social Impact Measurement
Our product aims to understand the best energy communities *and* also present to the communities - using our calculator [\[5\]][5]-, the positive environmental impact related with the installation of the solar panels.

### Outcome
The first direct outcome is the analysis of the WDL datasets and the research to understand better Ghent City in terms of income, consumption and energy potential. Taking into consideration the studies conducted in [\[1\]][1] we can conclude that identification of parameters (and creation of energy communities) is a major plus to reduce our ecological footprint.

Secondly, we conducted experiments regarding clustering algorithms, to understand how Ghent Sectors would aggregate in terms of similarity. This may be a good feature/outcome, since it allows to a more autonomous algorithm to identify energy communities. 

Finally, our frontend may allow to more non-technical people to absorb  the knowledge created by us, and understand the benefits of a solar panel array in the environment using the supplied calculator.

The outcomes have a specific goal: to increase the number of energy communities and improve awareness of our impact in the environment.
Quoting Barack Obama:
>  Change will not come if we wait for some other person or some other time. We are the ones we've been waiting for. We are the change that we seek.


So, we need to present to the possible energy communities they can be the Change.



### Impact Metrics
We can define the following 4 metrics to understand whether we are achieving the previous outcome or not:

* Domain-specific evaluation of our clusters: in articulation with Ghent City council, we can try to evaluate the quality of the clustering (e.g. a pilot program). The effectiveness and achievements of this pilot program will serve as a determining factor for its potential application in other similar sectors (same cluster) or even cities with similar raw data.
* Evolution of Energy Communities in Ghent City
* Evolution of Energy Production in Ghent City
* Network traffic associated with the deployed frontend [\[4\]][4] and [\[5\]][5]

### Impact Measurement

We have two main impact measurement:

First for specific energy communities, they can see their environmental impact using [\[5\]][5] for a specific solar panel installation.


Secondly, thinking in terms of Ghent city (or other city with similar raw data) and taking into consideration some of the graphs shown in this executive summary and notebook, and assuming that:

1. We have a energy production potential of 958848637 kwh based on the datasets
2. We can install solar panels equivalent of 30% of 958848637 kwh
3. There is the following relation:  (see [\[6\]][6], [\[7\]][7] and [\[8\]][8])
	1. 100 kwh are equivalent to reducing 80 metric tons of CO2 by year
	2. 100 kwh are equivalent to 20 passenger cars taken off the road for 1 yr
	3. 100 kwh are equivalent to 1322 Tree seedlings grown for 10 yrs
	4. 100 kwh are equivalent to 3046 incandescent lamps switched to LEDs.



Then, We can conclude that: 

* Installing solar panels equivalent to 30% of 958848637 kwh in Ghent City will have an impact of:
1. reducing   230 123 673 metric tons of CO2 by year
2. reducing    57 530 918 passenger cars taken off the road for 1 yr
3. 3 802 793 694 Tree seedlings grown for 10 yrs
4. changing 8 761 958 844 incandescent lamps switched to LEDs.

For the reasons and assumptions presented above, the impact measurement may change significantly, since depends on assumptions and baselines that we don't control.



[1]: https://www.amazon.com/How-Avoid-Climate-Disaster-Breakthroughs/dp/059321577X "How to Avoid a Climate Disaster: The Solutions We Have and the Breakthroughs We Need"
[2]: https://stad.gent/sites/default/files/media/documents/51725-1679308738-Bevolkingsrapport%20Gent%202022-1973fe.pdf "population by sector of Ghent"
[3]: https://www.citypopulation.de/en/belgium/agglogent/admin/44021__gent/ "Location of each sector"
[4]: https://peaceful-sherbet-485f81.netlify.app/dashboard-two "Ghent Data"
[5]: https://peaceful-sherbet-485f81.netlify.app/pricing "Calculator"
[6]: https://www.eon.de/de/pk/solar.html "solar.html"
[7]: https://sunroof.withgoogle.com/ "sunroof project"
[8]: https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references#lbscoal "epa gov"
[9]: https://www.goodreads.com/book/show/50343749-if-you-want-to-know-the-future-look-at-the-past "If you want to know the future, look at the past."
[10]: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html "OPTICS"
