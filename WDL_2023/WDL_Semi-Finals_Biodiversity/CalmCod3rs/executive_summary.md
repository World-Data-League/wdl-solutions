# World Data League 2023




## 🎯 Challenge


Avencas Marine Protected Area: Predict the future of the local ecosystem and its species




## 👥 Authors


* Ana Luiza Kaori Akiyama
* Luiz Gustavo Moniz
* Guilherme Caixeta


## ✨ Introduction (250 words max)


A marine protected area (MPA) is a section of the ocean where a government has placed limits on human activity. Many MPAs allow people to use the area in ways that do not damage the environment. Some ban fishing. A few do not allow people to enter the area at all. The main focus of many MPAs is to protect marine habitats and the variety of life that they support. [1]


The rocky shore area of Avencas, located in the Cascais council, was designated as a Marine Protected Area (MPA) in 2016, after being a Biophysical Interest Zone (ZIBA) since 1998. Some management actions were taken, including putting up signs, creating rope paths, and holding public meetings. Positive results point to the success of this approach, as visitors either agreed or respected the various management actions implemented.[2]


The local usages are now under control, so in theory the intertidal ecosystem should be recovering at a faster rate than what is being recorded. One factor that deserves further exploration is the impact of climate change on the intertidal communities of Avencas.


CalmCod3rs team aims to help the Cascais Municipality to understand the
influence of environmental variables in the biodiversity and abundance of the species composition of this Marine Protected Area. To this end, we developed a ML based web app project that aims to provide tools to understand the most important variables impacting the local marine ecosystem. From that, it is possible to plan management actions, to hopefully recover the intertidal ecosystem.












## 🔢 Data (250 words max)


1- Sessil (% Coverage):
* Occurence of a list of sessile species in the AMPA area (Nov 2011 - Nov 2020)


2- Mobil (nº individuals):
* Occurence of a list of mobile species in the AMPA area (Nov 2011 - Nov 2020)


3- Invasive_conservat species list:
* Information about invasiveness and conservation status of individual species. 2 Datasets: one for sessil, one for mobile species.




4- OceanSODA-ETHZ: 
* A global gridded dataset of the surface ocean carbonate system for seasonal to decadal studies of ocean acidification [3]


5- Daily Fishing Effort at 10th Degree Resolution by MMSI, version 2.0, 2012-2020:
* Fishing effort and vessel presence is binned into grid cells 0.1 degrees on a side, and measured in units of hours. [4]


6- Sampling study area Shapefile:
* Four sampling sections (A, B, D, E), which were stratiﬁed in supratidal and middle-intertidal areas. Sections B and D were located inside the ZIBA, while sections A and E were located outside the ZIBA.






## 🧮 Methods and Techniques (250 words max)[a][b]


### Visualizations 


In the exploratory data analysis we use hvplot library to present interactive visualizations on html, and most of the geospatial dataset was manipulated using geopandas. All of the animated chronological maps were created using plotly express.




### Dimension Reduction
PCA (Principal Component Analysis) is a technique that transforms a data set with many features into a smaller one with fewer features called PCs. PCs are new features that capture most of the variation in the data. PCA takes advantage of multicollinearity and combines the highly correlated variables into a set of uncorrelated variables. Therefore, PCA can effectively eliminate multicollinearity between features.


### Gradient boosting algorithm on decision trees
We use catboost decision trees algorithm to model the dataset. In order to interpret the models, we use SHAP values, which is a measure of how much a feature contributes to the prediction of a machine learning model. SHAP values can be used to explain individual predictions or global patterns in the model.


### Association rule mining


Association rule mining is a technique that finds patterns and relationships between data species of the same sample that was collected.






## 💡 Main Insights (300 words max)[c]


In the initial analysis of the mobile species data, we noticed that the summer season has the highest average number of species for most years, except for 2017 and 2018. 


The average number of species declined significantly from 2016 to 2018, reaching the lowest values in autumn (0.00) and summer (0.70) of 2018.


Using the OceanSODA-ETHZ dataset, we could see which variables are most strongly correlated with Yearly-Average Number of Mobile Species. The Number of Mobile Species has a strong positive relationship (2012-2015) with water temperature, spco2, and sfco2, and a strong negative relationship with ph_total. 


Using PCA with Water Temperature and PH, we can see how the data are distributed and clustered in a two-dimensional space. This suggests that there is a clear difference or contrast between these two groups of data points along the PCs from 2011 to 2015. After this period (2016 to 2020), the correlation between Species number and features approached close to zero, meaning that they have a very weak linear relationship.


Another approach that could try to explain why the average number of species declined significantly from 2016 to 2018 is using fishing data. Analyzing this dataset, we noticed that the number of vessels (and fishing hours) shows a gradual increase from 2012 to 2015, followed by a sharp rise from 2015 to 2018. This period corresponds to the peak of fishing activity around the MPA. Using moving average of 5 periods with fishing hours improved PCA fit of high and low number of species samples.


We did not find a direct correlation between the fishing hours and the Average Number of Mobile Species, as we understand that the impact is not immediate. However, making the moving average it is possible to observe that this relationship is better captured.






## 🛠️ Product
### Definition


An Analytics Web App for the Cascais Municipality to understand the most important variables impacting the local marine ecosystem, analyze species individually and assist in decision making.


In this Web App, it is possible to simulate scenarios that can help authorities to make decisions:


1- Measure the importance of a variable to the local marine ecosystem


* It is possible to use the tool in order to understand the impact of each variable on the local marine ecosystem.


2- Optimize management actions on the MPA:


* If there is a variable indicating impact on the ecosystem, it is possible to draw up an action plan in the tool and make centralized notes of the actions taken.


3- Analyze species individually:
* Relationship with other species, weather conditions that appear the most, trend in the number of individuals.




### Users


Cascais Municipality can use the tool to understand the importance of variables, simulate scenarios, see forecasts, and plan management actions.




### Activities


* Analyze the importance of a variable to the local marine ecosystem;


![Feature Importance Dashboard](https://drive.google.com/uc?id=17JZhAkYLFBm232EE8_anExWpleTbX6Jz)


* Simulate scenarios by changing the trend of each variable;


* Provide insights into future developments of species in the AMPA; 


* Analyze species individually;


![Individual Specie Dashboard](https://drive.google.com/uc?id=1vQR7dTQy3UsQch-ayLpM5SmtuAvlhs0Y)


* Input data (reduce type errors)


![Forms](https://drive.google.com/uc?id=1yscoG2s2BUxF-j8S9ZAJ0OYLAnYDiRzp)




### Output


Generates insights that may help Cascais Municipality to improve decision making process.




### Scalability


This product depends on data quality and quantity. In order to implement real time analysis it is necessary to use a database that is capable of handling a high amount of data, which may increase the costs.




## 🌍 Social Impact Measurement
### Outcome


The idea of this product is to facilitate and speed up the process of analyzing the variables that can impact the ecosystem. It also creates a predictive model that provides insights into future developments of endangered and invasive species in the AMPA.


Having a good analysis, the respective responsible ones can take appropriate measures to improve the biodiversity and abundance of the species composition of the Marine Protected Area.


In addition, the same analyzes and models could be used in other marine ecosystems where similar data has been collected.




### Impact Metrics




* Biodiversity: 


* How does the MPA affect the diversity and abundance of marine species and habitats? 
* How does it protect endangered or threatened species and ecosystems? 
* How does it maintain or restore ecological processes and functions? 


Biodiversity can be measured by indicators such as:


* species richness
* species biomass 
* species density
* population size
* genetic diversity


Besides that, the product aims to:
* reduce data collection errors






### Impact Measurement



A paper by Edgar et al. (2014) used data from 87 MPAs around the world and 39 control sites to examine how six factors affect the effectiveness of MPAs: age, size, level of protection, isolation, enforcement, and fishing pressure(nature.com). The paper found that MPAs that met five key criteria (no-take, well enforced, old, large, and isolated) had significantly higher biomass, density, species richness, size, and trophic structure of fish populations than fished areas(nature.com). The paper also found that most MPAs do not meet these criteria and have limited benefits for biodiversity conservation.






REFERENCES:


[1]https://education.nationalgeographic.org/resource/importance-marine-protected-areas/




[2] Ferreira, Ana, et al. "Ecosystem Response to Different Management Options in Marine Protected Areas (MPA): A Case Study of Intertidal Rocky Shore Communities." 




[3] Gregor, Luke; Gruber, Nicolas (2020). OceanSODA-ETHZ: A global gridded dataset of the surface ocean carbonate system for seasonal to decadal studies of ocean acidification (v2021) (NCEI Accession 0220059). [indicate subset used]. NOAA National Centers for Environmental Information. Dataset. https://doi.org/10.25921/m5wx-ja34. Accessed [2023-05-14]


[4] D.A. Kroodsma, J. Mayorga, T. Hochberg, N.A. Miller, K. Boerder, F. Ferretti, A. Wilson, B. Bergman, T.D. White, B.A. Block, P. Woods, B. Sullivan, C. Costello, and B. Worm. "Tracking the global footprint of fisheries." Science 361.6378 (2018).


