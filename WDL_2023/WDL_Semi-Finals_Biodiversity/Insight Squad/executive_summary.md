# World Data League 2023


## 🎯 Challenge
Avencas Marine Protected Area: Predict the future of the local ecosystem and its species


## Team Name
Insight Squad 💡


## 👥 Authors
* Maria Manuel Castro
* Rodrigo Miguel Ferreira
* Ricardo Ângelo Filipe
* Catarina Campos Rocha
* Eduardo Daniel VIcente


## ✨ Introduction (250 words max)

According to [\[1\]][2] and [\[2\]][3], from 13th to 21th of May occurs in Spain and Portugal the week of 'Semana sobre especies invasoras' (i.e. week about invasive species).
According to the same sites invasive species have three main impacts:
 1. Economic - studies from 2019 show an economic impact of more than 1 billion Euros due to productivity and control costs on invasive species.
 2. Ecosystem - Invasive species change the natural cycles (carbon, ozone, water, etc), change the natural food chain due to their rapid multiplication, and reduce the biodiversity.
 3. Human Health - some invasive species are toxic to humans or can carry plagues or deceases harmful  to humans.


Taking into consideration the aforementioned  topics, the proposed WDL challenge is in line with the main concerns of Portugal.

To identify variables potentially impacting the marine ecosystem of the Avencas Marine Protected Area and predict further developments, is an important task. Moreover, we want to pinpoint endangered and invasive species. Additionally, unbeknown to data analyst, parameters like sea level temperature, salinity and oxygen may have a huge impact on the aforementioned  species.

Hence, this challenge will try to create a tool to predict the future of the Avencas Marine Protected Area in the area of Cascais.

The goal is simple: predict the future of one of our main natural resources available in Portugal: the marine ecosystem.




## 🔢 Data (250 words max)
From the datasets provided by WDL we used the following:

* Sessil (% Coverage): Occurrence  of a list of sessile species in the AMPA area.
* Mobil (nº individuals): Occurrence  of a list of mobile species in the AMPA area.
* Invasive_conservat species list: Information about invasiveness and conservation status of individual species.

Due to lack of time, we didn't use any external dataset.

Data Processing (due to summary length, we only focus on the main aspects):

* Sessil:
1. we added more date fields (e.g. year, week, season...)
2. Missing Values - to all measurements with value ' ' we replace with 0
3. All measurements with "NÃO FOI REALIZADO DEVIDO À MARÉ" were dropped.
4. "Water tempeature (ºC)" for day 2014-05-15 was missing and we filled with value 16º ( value close to the ones from previous and next days).
5. Field 'Supratidal/Middle Intertidal' changed to have two possible values: SUPRA and MEDIUM.
6. Changed value of field "Chthamalus sp." with wrong format.
7. Due to previous point we recalculated field 'TOTAL'
8. Dropped Duplicated lines (16)

* Mobil:
1. made the same operations of 1, 2, 3, 4, 5, 8 of Sessil dataset.
2. Trimmed field Zone with additional ' '
3. Field Tide had some inconsistencies (e.g. character ',' or ';' has decimal separator)
	
We then merged dataset Sessil and Mobil with dataset Invasive_conservat species list.
Then, we made some Feature Engineering creating metrics such as Quantity of Invasive Species/ Non-Invasive Species, Conservat/Non-conservat quantity.



## 🧮 Methods and Techniques (250 words max)

First, we used the standard tool belt for data scientists: pandas, scikit and numpy. The goal was to clean, detect missing data, duplicated lines and make a quick benchmark of our data.
Secondly, we used Pandas Profiling to understand better the data.

We also tried some heatmaps with time-lapse for invasive species using Folium , but the results weren't promising. Hence, they weren't published in the notebook.

Finally, for our predictive model we used time series (with LSTM) . We used data from our merged dataset to predict the future of invasive and non-invasive species.


## 💡 Main Insights (300 words max)

The Main Insights discovered by our squad were:

* There is missing data in several datasets provided by WDL. 
E.g. ![Ploy By zone and Week](https://peaceful-sherbet-485f81.netlify.app/zones_week.png)

* We have some spikes of outliers for some measurements.
* The invasive species have a lower tolerance to change in sea level temperature compared to non-invasive species🌍🌡️
E.g. ![Boxplot grouped by temp range](https://peaceful-sherbet-485f81.netlify.app/boxplot_sessil_invasive.png)

* We have a high correlation between some species.
E.g. Osmedia/Ipomenia and also Diplodius Sargus/Diplodius Cervinus identified with black circles in the below image:
![Correlation Matrix](https://peaceful-sherbet-485f81.netlify.app/matrix.png)


## 🛠️ Product
We deliver two artefacts to better understand Avencas Marine Protected Area in Cascais. 

First, a data analysis throughout the gathered data. Understanding the data and pinpointing parameters that impact invasive and endangered species may have a significant benefit for the environmental policies of the city. 

Secondly, a predictive model that aims to detect evolution of the species through a time series. The model can be integrated in a dashboard to help Cascais City politicians avoid wrong decisions for a better and sustainable Avencas Marine Protected Area




### Definition
A data analysis and a predictive model that assists Cascais Governance in environmental strategies.


### Users

To have a holistic solution to the Avencas Marine Protected Area challenge, the solution must address two users:
*  Environmental Politics that uses the predictive model and the data analysis. The predictive model and dashboards may be available through a dashboard as the one presented [here][10]  in the first challenge. Having heatmaps associated with invasive species, tables  and visualizations associated with the time series evolution to understand how the Avencas Marine Protected Area evolve is very important. We aim to pinpoint the overall species evolution and enlighten possible environmental politics changes to swiftly change the future of the local species.
* City Population. The orerall population will have access to visualizations and report from the work. Hence, a more environmental conscience, specially associated to parameters that everyone can contribute may have a significant impact in the ecosystem. 💧💚


### Activities
Features that our product has:
1. Model *prediction* of future of  Avencas Marine Protected Area
2. Visualization Report of aggregated and cleaned data from the collected datasets.


### Output
The output will be a better understanding of the Avencas Marine Protected Area. 
Citing Albert Einstein [\[4\]][4]: 
> If you want to know the future, look at the past.

Hence, the main output of this work are:
1. Looking to the Past: 
	1. Exploratory Data Analysis (EDA) of WDL datasets
	2. This way we can understand better the parameters and evolution of the species and the past from this Protected Area
2. Know the future:
	1. Predictive Model based on time-series using LSTM [\[5\]][5]



### Scalability
To endeavor a tool that has scalability to retrieve a vision of the Avencas Marine Protected Area there are some concerns that need to be address:

1. *Data Collection and Cleaning*: currently the tool/notebook is in *offline* state. To have the fastest response (and probably a near real-time dashboard) we need a stream of data processed in near real time. This may be a challenge both for the data producers and also to our processing logic.
2. *Environmental Management Strategies*: based on our insights/dashboard, environmental  policies may pinpoint  areas that need intervention. 
However, the question arise: is the overall Cascais  population prepared to active environmental management strategies that don't exist nowadays?
It may be needed some education and advertising campaign in Cascais for new policies as the one presented in [\[3\]][1] 
3. *Model prediction adoption*: one of our product features is the prediction of the future of conservative and invasive species. Hence, we are assuming that the model will be adequate to Cascais. However, if that do not occur, we will need to redefine the model - probably with more feature engineering or merging the data with other data sources.


## 🌍 Social Impact Measurement
Our product aims to gather a complete history about Avencas Marine Protected Area.

### Outcome
The first direct outcome is the analysis of the WDL datasets and the research to pinpoint correlations regarding the species and parameters that may change their propagation. Taking into consideration the studies conducted in [\[1\]][2] and [\[2\]][3] we can conclude that identification of parameters (and creation of possible guidelines) about invasive and conservative species is a major plus.

Invasive species impacts deeply negatively in the economy, overall ecosystem and maybe even in our health.

Regarding the benefits of identifying the parameters that impact negatively invasive species, citing the authors of [\[6\]][6]: 
>  A 2021 study estimated that invasive species have cost North America $2 billion per year in the early 1960s to over $26 billion per year since 2010.

And the following Image from  cost versus species:

![Cost Vs Species](https://ars.els-cdn.com/content/image/1-s2.0-S0048969721003041-ga1.jpg)


And taking into consideration some of our own graphs. E.g. 
![Boxplot grouped by temp range](https://peaceful-sherbet-485f81.netlify.app/boxplot_sessil_invasive.png)

We know that Invasive species don't like lower sea level temperatatures.
Assuming that we can decrease the ocean temperature near the Avencas Marine Protected Area (we know it's an  herculean task 🌊 🏋💪), we can expect:
* cost reduction (or at least an optimization) related with invasive species policies
* a better ecosystem

The question that arises is: Can we indeed decrease sea level temperature?

Well, it turns out that some experiments and scientific research has been made in this area. One of the most interesting is the black plastic 'shade balls'.
![shade balls](https://www.sciencealert.com/images/2019-05/processed/veritasium_1024.jpg)

According to [here][9] 
>  while evaporation was not the original reason these balls were used, they do in fact keep the water below much cooler. So for all of these reasons, shade balls reduce evaporation by 80 to 90 percent

So, perhaps some sort of dam with shade balls ⚫ may be the solution to reduce invasive species at this Protected Area.

We also know that exists other parameters along the sea temperature that may impact the result, but taking into consideration Occam's razor ("the simplest explanation that will account for a circumstance or event is most likely the correct explanation.") we start to focus only on Sea Level Temperature. 

### Impact Metrics
We can define the following 4 metrics to understand whether we are achieving the previous outcome or not:

* Mean Absolute Error between the predicted and real value for the LSTM predictive model
* Evolution of Invasive species in Avencas Marine Protected Area
* Evolution of Conservative species in Avencas Marine Protected Area
* Money saved by Cascais using a more fine-grained invasive species policies

### Impact Measurement

Taking into consideration some of the graphs show in this executive summary and notebook, and assuming that:

1. We indeed can decrease 1ºC in the water near the Avencas Marine Protected Area 
2. The 1ºC reduces in 25% the total of Invasive species.
3. There is a linearity between handling Invasive species and the budget associated with Avencas Marine Protected Area (e.g. reducing 25% invasive species will reduce in 25% the budget)
4. The budget for Avencas Marine Protected Area is 10% of Cascais Nature Management Budget
5. Cascais Nature Management Budget for 2023 was 33335124€   (see  [\[8\]][8])


Than, We can conclude that: 

* Reducing 1ºC will have an yearly budget impact of = (33335124€\*0.1)\*(0.25) = 833378 € / anual


Hence the direct Impact for Cascais would be a reduction of 833378 € / anual in costs.

For the reasons and assumptions presented above, the impact measurement may change significantly, since depends on assumptions and baselines that we don't control.




[1]: https://www.epa.gov/arc-x/climate-impacts-water-management-and-ecosystem-protection "Climate Impacts on Water Management and Ecosystem Protection"
[2]: https://invasoras.pt/ "Plataforma de informação e ciência-cidadã sobre plantas invasoras em Portugal"
[3]: https://www.speco.pt/pt/iniciativas/semana-sobre-especies-invasoras-2023 "Activities invasoras"
[4]: https://www.goodreads.com/book/show/50343749-if-you-want-to-know-the-future-look-at-the-past "If you want to know the future, look at the past."
[5]: https://en.wikipedia.org/wiki/Long_short-term_memory "Long short-term memory"
[6]: https://www.invasivespeciesinfo.gov/subject/economic-and-social-impacts "Economic and Social Impacts"
[7]: https://www.sciencedirect.com/science/article/pii/S0048969721003041 "Global economic costs of aquatic invasive alien species"
[8]: https://ambiente.cascais.pt/pt/page/cascais-ambiente-gestao-do-ambiente-terrestre-maritimo-0 "Cascais Ambiente - Gestão do ambiente terrestre e marítimo"
[9]: https://www.sciencealert.com/here-s-what-s-really-going-on-with-those-black-balls-in-the-la-reservoir "Those 96 Million Black Balls in LA's Reservoir Are Not Just There to Save Water"
[10]: https://peaceful-sherbet-485f81.netlify.app/ "Dashboard"
