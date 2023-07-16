# World Data League 2023

## 🎯 Challenge

Avencas Marine Protected Area: Predict the Future of the Local Ecosystem and Its Species

## Team Name
The Bayes Bunch

## 👥 Authors
* Mitra Ganeson
* Roisin Holmes
* Samantha Hakes
* Stuart McGibbon
* Zhen-Yen Chan

## ✨ Introduction
Our work is oriented towards identifying variables potentially impacting the marine ecosystem of the Avencas Marine Protected Area (AMPA) and predict further developments with a special focus on endangered and invasive species. This will create opportunities for improvement in the conservation of native and endangered species within AMPA and other ecosystems where similar data has been collected, as well as highlight insights which positively impact them.

The intended outcome of this project is:
- a better understanding and visualization of environmental and climate pressures that affect a marine ecosystem.
- a predictive model that provides insights into future developments of endangered and invasive species, applicable in AMPA and similar coastal areas.
- identification of potential insights which can improve sustainable management of marine and coastal ecosystems, hence positively impacting its resilience and restoration.

Our work entailed development of 3 time series models which forecasted the number of invasive species, the number of endangered species, and the Shannon-Wiener Index (biodiversity index). Through analysis and use of these models, we were able to identify key variables which impact our targets, quantifying the importance of each. We then aimed to understand the effects of these variables changing, for example through ocean acidification. We modelled these different scenarios over a period of 10 years to visualise the impact of changes on our targets.

## 🔢 Data
We used 6 datasources in this project for our feature engineering.
1. AMPA: WDL challenge brief
2. Land, sea and air monthly anomaly temperatures: University East Anglia Climate Data; ‘https://www.uea.ac.uk/groups-and-centres/climatic-research-unit/data’
3. Open Meteo: https://open-meteo.com/
4. Marine Geochemical Data: https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/description ; https://data.marine.copernicus.eu/product/IBI_MULTIYEAR_BGC_005_003/description
5. Air Quality Index Data: https://waqi.info/#/c/8.407/9.026/2.2zy
6. Ocean Health Index Data: https://oceanhealthindex.org/global-scores/data-download/

Our choice of data was motivated by our goal of merging the physical and chemical characteristics of the region with data science techniques. We were driven to gather an in-depth understanding of historical environmental conditions and climate pressures, explained by scientific metrics, to inform our model. We strived to collect data sources as close to the chosen region in Cascais as possible, and otherwise obtained data related to the general Cascais region or Portugal as a whole.

We were interested in the years 2012-2018, chosen as they had consistent data we could use in modelling. We chose to aggregate to date level for ease of use and compatibility with other data sources.

The data above were used to obtain some key metrics, number of invasive and endangered species and the Shannon-Wiener Index.

Suggested improvements:
Data on chemical and pollutant reading could be obtained nearer to the site of interest, e.g. by setting up a monitoring station near Cascais.

## 🧮 Methods and Techniques
Initially we derived our target biodiversity label (Shannon-Wiener Index; [https://www.sciencedirect.com/science/article/abs/pii/S1470160X17303709](https://www.sciencedirect.com/science/article/abs/pii/S1470160X17303709)) from the sessile and mobile abundance data

This biodiversity index was calculated as follows:

H=−∑[(pi)×log(pi)]

Where H is the Shannon diversity index, and  pi  is the proportion of individuals of ith species in the population. (https://www.omnicalculator.com/ecology/shannon-index)

To allow for both percentage coverage and abundance counts to be used in the Shannon Index Calculations, the percentage coverage needed to be represented by a count. The methodology for this is shown in this paper ([https://www.researchgate.net/publication/262458621_Human_Disturbance_in_a_Tropical_Rocky_Shore_Reduces_Species_Diversity](https://www.researchgate.net/publication/262458621_Human_Disturbance_in_a_Tropical_Rocky_Shore_Reduces_Species_Diversity))

We then combined with other datasets to include and engineer potentially impactful features.

Structured time-series analysis was carried out on the biodiversity index, to discover patterns and extract trends. The analysis was then used to derive SARIMA models to forecast the target variables.

Residual analysis on the model was conducted to understand how external features interact with the label (after time components like seasonality are removed). Using the features discovered in the residual analysis, the time series models were fitted and tested, allowing us to understand feature importance.

Shifts in external features were realised by modelling scenarios and evaluating how biodiversity was impacted. This was done by using historic feature data to create synthetic values for our external variables (based on long-term scenarios).

## 💡 Main Insights
The below plot shows estimates of each feature’s impact on biodiversity. The highest correlated of which are ocean health indexes for Portugal. While these features may not be useful for the model (due to their similarity to the label) it is nevertheless interesting to know how the biodiversity in this small area is similar to the overall health of Portugal’s oceans, possibly suggesting that the lack of recovery in this zone may be caused by much more global factors.


![](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/main/Feature%20Selection%20-%20Shannon%20Index.png?raw=true) 

Our other labels (invasive and endangered species) were shown to be impacted by different features. Invasive species was shown to be impacted by increased chlorine levels and temperature based features were shown to have a potential impact on endangered species counts.

The below plots show how biodiversity changes over time in the data, as well as the estimated trend after the modeled effects of seasonality are removed. It is clear there is no obvious uptick in biodiversity in the years evaluated.
![](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/main/PythonplotShannonIndex.png?raw=true)

Included below is a table showing the performance of our model compared with several benchmarks (with the caveat that the small range of dates reduces confidence in the results). While the SARIMA from auto ARIMA performed the best, the SARIMAX (5) model was chosen for scenario forecasting. This is because it showed reasonable performance on the test sample and because it was built using features shown to be important for biodiversity forecasting. This should make it suited to estimating how changes to external variable distributions impact the long term biodiversity.
![](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/main/ModelPerformance.png?raw=true)


## 🛠️ Product

### Definition
There are two parts to the product we are proposing:
1.  An interactive dashboard, POC built using Streamlit and Flourish, showing our time series model results, feature importance, and simulations of changing environmental variables.
    
2.  A reusable and scalable Python package that the open source community can use for modelling different marine ecosystems

### Users
-   Marine protected area managers/environmental workers (use dashboard to understand features which heavily impact biodiveristy and species counts)
    
-   Researchers (use dashboard and/or python package to visualise impacts of changing environmental vairables, and plan for remediation)
    
-   People interested in using Python to model different marine ecosystems (use python package to perform exploratory work on regions of interest)

### Activities

-   Provides alerts for impact on species, for example decreasing species trend
    
-   Highlights features (such as pH) which are of particular importance to the region’s biodiversity management
    
-   Show simulation outputs from hypothetical inputs. For example, what would the impact of an increased oxygen content be on the number of endangered species?
    
-   Recommend actions to be taken to improve biodiversity
  
### Output (what the user sees)
1.  Dashboard
-   Find key points of interest to focus on (diagnostic element of tool) 
-   Assess impact of environmental changes (simulation)
-   Available at https://mitrag-beautiful-sea-streamlit-d-beautiful-sea-streamlit-on6bwj.streamlit.app/
![](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/main/Product%20Page%203%20-%20Forecast.png?raw=true)
    
2.  Python package
-   Open source python package available for people to use in exploratory modelling
-   Available at https://github.com/StuartJMc/beautiful-sea

### Scalability
This model has been designed to be scalable for similar coastal areas. The data should be as granular to the area as possible, and also have similar metrics available (especially species data and bathymetry data). Some data such as ocean geochemical levels could be obtained by using information from the wider region.

A mockup product which focuses on descriptive statistics and one forecasting scenario has been created for this challenge. However, initial work would need to be done in improving the modelling used throughout, and developing a fuller user interface, this could be expanded up to a full dashboarding tool with expansive functionality.

If this solution were to be taken further, one recommendation would be to integrate it with the Sinay data solution, SeaLife Impact. ([https://sinay.ai/en/sinay-hub/sealife-impact/](https://sinay.ai/en/sinay-hub/sealife-impact/)) Sinay’s SeaLife impact dashboard provides real-time alerts to predict and prevent negative sealife impact from maritime industry activities. This would be a great tool for coastal areas populated with shipping activities, such as port development, etc. Adapting our tool to be compatible with Sinay’s functionality could allow for increased understanding in decisions on shipping routes, construction projects at ports, etc.  

## 🌍 Social Impact Measurement

### Outcome (what good is it doing)

1.  Increased biodiversity in Cascais

As one of the EU sustainable development goals (Sustainable Development Goal 14, Conserve and sustainably use the oceans, seas and marine resources for sustainable development, [https://sdgs.un.org/goals/goal14](https://sdgs.un.org/goals/goal14)), it is important that Oceans and marine regions are managed and maintained.  By understanding what features are involved in causing drops in biodiversity, plans can be made to combat these aspects. Better action plans for remediation of environments will result in a reduction in harmful ecological changes.

2.  Use of tool in other marine areas

We aim for our product to be fully utilised in areas outwith Cascais, this will allow for greater outcomes, and will aid in achieving the EU’s biodiversity strategy of having 30% of the seas to be under protection by 2030 https://www.frontiersin.org/articles/10.3389/fmars.2022.1002677/full#B40

3.  Public and government awareness of biodiversity

Our tool could be used as a facilitator and educator on the topic of environmental awareness. As well as helping to demonstrate the impact of lobbying and fundraising, it could be used as a general education tool, including the general public in biodiversity conservation.

### Impact Metrics

-   Endangered species count  
-   Invasive species count    
-   Biodiversity index (Shannon Index)    
-   Number of users of the dashboard/python package   
-   General awareness of general public of areas of importance    
-   Percentage of coastal regions/seas which are under conservation
 
### Impact Measurement
-   The IPCC predicts that the oceans will acidify further under every RCP scenario ([https://ar5-syr.ipcc.ch/topic_futurechanges.php](https://ar5-syr.ipcc.ch/topic_futurechanges.php)). Our tool could be used to plan mitigation measures to tackle this. By returning oceans to their natural pH level, species growth can be increased by 7% ([https://www.nature.com/articles/nature.2016.19410](https://www.nature.com/articles/nature.2016.19410)). Our model predicts an increase (compared to 2020 data) of 7.8% in the biodiversity index from returning ph to its natural levels (8.10).
    
-   Increased ecotourism to areas of biological importance can help drive income and employment in key regions, whilst educating and involving the public in ecological management ([https://www.frontiersin.org/articles/10.3389/fmars.2022.1002677/full](https://www.frontiersin.org/articles/10.3389/fmars.2022.1002677/full)). This tool could help drive engagement, capturing the ecotourism market which has been growing by 20-30% per year (https://www.cbi.eu/market-information/tourism/ecotourism/market-potential#:~:text=In%20recent%20years%2C%20the%20demand,by%20only%204.3%25%20per%20year.)
  
-   This tool has the potential to support in increasing the public and governmental awareness of biodiversity as an important issue impacting many people. From 2016 to 2020 the searches for nature loss and biodiversity had increased by 16% ([https://www.weforum.org/agenda/2021/05/concern-over-nature-loss-surging-in-developing-nations-online-trends-show/#:~:text=Research%20by%20the%20Economist%20Intelligence,biodiversity%20increased%20by%2016%25%20worldwide](https://www.weforum.org/agenda/2021/05/concern-over-nature-loss-surging-in-developing-nations-online-trends-show/#:~:text=Research%20by%20the%20Economist%20Intelligence,biodiversity%20increased%20by%2016%25%20worldwide).). The tool has the capability to capture this audience, increasing familiarity and learning, and thus driving engagement (https://www.pnas.org/doi/10.1073/pnas.0802599105).
