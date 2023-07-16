# World Data League 2023


## Executive Summary

## 🎯 Challenge
Avencas Marine Protected Area: Predict the future of the local ecosystem and its species


## Team Name
AI Wonder Girls


## 👥 Authors
* Divya Kamat
* Emma Roscow
* Ernitia Paramasari
* Pankaja Shankar


## ✨ Introduction
The Avencas Marine Protected Area (MPA) is home to a rich ecosystem of intertidal marine species [1], but faces stressors owing to its urban location popular for fishing and tourism, and climate change. Loss of biodiversity is a major concern, and despite initiatives put into place since 2016 to protect the area from anthropogenic stressors, the density and diversity of species has not recovered as much as anticipated [2]. In order to put in place good management options to protect these populations, the Cascais municipality needs to better understand how environmental variables affect the community's biodiversity. To meet this goal, we have sourced a range of open-source environmental data that have been hypothesised to impact marine biodiversity and trained machine learning models to find the most important factors that influence species abundance in the Avencas MPA, using extensive data on species abundance over 9 years provided for the challenge. Informed by the academic literature on marine conservation and our own data analysis, we have engineered a set of features that can be applied to any marine protected area for which there is a similar dataset. We show that this approach can be used to understand how weather affects marine ecosystem diversity.

[1] https://www.mpas-europe.org/mainland-overiew/blog-post-title-four-k74bc

[2] Ferreira et al. (2017). Ecosystem response to different management options in Marine Protected Areas (MPA): A case study of intertidal rocky shore communities. Ecological Indicators, 21, 471-480.


## 🔢 Data
Two datasets of marine species abundance observations in the Avencas MPA were provided for the challenge, which we used as targets for our machine learning models:
* Sessile species data
* Mobile species data
In addition to the abundance, these datasets include the tide height, weather, water temperature, tidal location and substrate where the observation was made which we used as features for our models.

The purpose of our models was to identify how environmental variables affect biodiversity, so we complemented these features with additional open-source weather data [1]. Previous research [2, 3, 4] has identified wave exposure, light availability and salinity as important factors for marine biodiversity, so we used this to inform our choice of features. Wave exposure physically affects intertidal marine habitats, and in turn is influenced by wind strength and wind direction, so we included historical data on these two factors. Light availability also affects the marine ecosystem because it supports flora photosynthesis, so we also included features for cloud cover, direct radiation, diffuse radiation and direct normal irradiance. Salinity is another important factor, which is affected by rainfall, so we included precipitation and evapotranspiration. Finally, to capture other weather patterns that might affect the marine habitat physically and chemically, we included relative humidity, sea level pressure, and vapour pressure deficit.

For future development of the product, it is critical to source other types of data, particularly those capturing human factors and pollution, in order to capture non-climatic pressures on intertidal communities: for example, water pollution, number of people at the beach, and fishing activity. We were unable to find suitable open-source data for these variables, so we did not include them.

[1] https://open-meteo.com/en/docs/historical-weather-api

[2] Soldal et al. (2009). Predictive Probability Modelling of Marine Habitats - A Case Study from the West Coast of Norway. In: Integrated Coastal Zone Management.

[3] Worachananant et al. (2007). Impacts of the 2004 Tsunami on Surin Marine National Park, Thailand. Coastal Management, 35, 399-412.

[4] Poloczanksa et al. (2007). Climate change and Australian marine life. Oceanography and Marine Biology: An Annual Review, 45, 407-478.


## 🧮 Methods and Techniques
**EDA**
Initial exploratory data analysis showed a lot of issues with the data, including missing values and improperly formatted dates, which we cleaned.

**Feature selection**
We first used our background research to select a wide range of features which might be relevant for predicting the number or coverage of a species, as described above. To reduce this to a more manageable number of features, we then used regression to select the most important features for further analysis. This was done by training on three subsets of data: one for sessile flora, one for sessile fauna, and one for mobile species. Using a variety of approaches, we evaluated each feature for how important it was to the model prediction of species abundance. The features with the lowest importance were discarded as irrelevant, in order to reduce the complexity of the time series model that we trained subsequently.

**Model selection**
There are many ways to implement a regression model to predict species abundance. Because of our uncertainty about which features were important and the overall objective of using the model to understand the influences on biodiversity, we chose three models which are known to deal well with high dimensionality and multicollinearity and have high explainability: LASSO regression, gradient boosting regressors, and random forests. We trained all models on the same data, and selected the one with the lowest error.

**Feature importance**
With our final model selected, we ran partial dependence plots (PDPs) to give qualitative insight into how the most important variables affect species abundance.

**Time series model**
After selecting the most relevant features, we trained a time series model on these features to predict the abundace of each species for a quantitative prediction.


## 💡 Main Insights
Despite various ways of engineering the environmental weather data we collected, we did not find a strong relationship between these features and species abundance or diversity. This could relate to poor data quality either in the species sampling or in the weather data (for example, the rocky Cascais coast may create a microclimate whose conditions are not well reflected in data from nearby weather stations). However, we propose that it is more likely to be due to other types of features that contribute to the decline in biodiversity: pollution of the habitat including plastic pollution [1], acidification [2], and non-compliance with local conservation regulations [3]. Our main insight is that weather factors are not responsible for the unexpected ecosystem dynamics in the Avencas MPA, and researchers should focus on measuring anthropogenic stressors to understand the causes of biodiversity loss. For example, remote sensing of the water quality [4] could identify trends in pollution and nutrient availability that are predictive of species density and diversity.

[1] Galloway & Lewis (2016). Marine microplastics spell big problems for future generations, PNAS, 113 (9), 2331-2333.

[2] Hale et al. (2011). Predicted levels of future ocean acidifi cation and temperature rise could alter community structure and biodiversity in marine benthic communities. Oikos, 120, 661–674.

[3] Ferreira et al. (2015). Bottom-up management approach to coastal marine protected areas in Portugal. Ocean & Coastal Management, 118(B), 275-281.

[4] https://ajuntament.barcelona.cat/ecologiaurbana/en/services/the-city-works/maintenance-of-public-areas/comprehensive-water-management/coastal-management


## 🛠️ Product

### Definition
Our model can be used as an environmental management tool, applied to any MPA to show the most important environmental variables that influence marine species abundance: when used in conjunction with expert knowledge on climate change and local anthropogenic stressors, decision-makers can use it to prioritise conservation efforts by targeting the environmental mediators that have the strongest effect on biodiversity. The availability and quality of data is the most important aspects determining the usefulness of the product.


### Users
Resarchers, policy-makers and conservationists in Cascais municipality can use it to understand the biggest stressors on local intertidal communities.

### Activities
* Users can use the product to gather insights on feature importance for each species' abundance
* Further extensions to the product could allow them to predict species abundance in the future, based on weather/climate forecasts or the anticipated impacts of interventions aimed at protecting the area

### Output
* Importance values of each feature, focusing on weather conditions, for each species' abundance
* Predicted abundance of each species in the future according to expected conditions

### Scalability
Our solution is scalable to any MPA for which similar abundance data on marine species is available, and can be used to understand any local environmental variables that influence local biodiversity. It is also flexible enough to include or exclude features according to what is relevant or available at the MPA of interest: for example, data on human presence in the area or fishing activity. The external weather data sources we have used are freely available from an API worldwide.


## 🌍 Social Impact Measurement

### Outcome
Through greater understanding of which environmental variables impact the abundance of which species, Cascais municipality should be able to better target their conservation initiatives to protect these ecosystems. The long-term outcome should be increased resilience of the ecosystem through implementation of appropriate conservation measures, measured by increased diversity and density of species.


### Impact Metrics
* Diversity of species in the Avencas MPA
* Density of species in the Avencas MPA


### Impact Measurement
The intended impact of our model is to empower Cascais municipality to implement more effective measures in the Avencas MPA for protecting marine biodiversity. Research has shown that the effectiveness of MPAs worldwide is highly variable, but when designed and managed well they can have twice as many fish species [1, 2]. Understanding what drives the dynamics in Avencas' intertidal populations is crucial to identifying the best policies for conserving them.

[1] Edgar et al. (2014). Global conservation outcomes depend on marine protected areas with five key features. Nature 506, 216–220.

[2] Gill et al. (2017). Capacity shortfalls hinder the performance of marine protected areas globally. Nature volume 543, 665–669.
