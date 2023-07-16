# World Data League 2023



## 🎯 Challenge: Avencas Marine Protected Area: Predict the future of the local ecosystem and its species

## Challenge Provider: City of Cascais

## Team Name: K-MENA Team


## 👥 Authors
* Sara Sabzikari
* Mine Yasemin 


## ✨ Introduction (250 words max)

Certainly! Here's the corrected text in a solid format:

The Marine Protected Area (MPA) of interest is a small (605,002 m2) rocky shore area of Avencas, near Lisbon. This MPA has had biodiversity monitoring between 2011 and 2020, sampling the sessile and mobile species during this time period. The area was originally designated a Biophysical Interest Zone in 1998 but was reclassified as an MPA in 2016. While it was only recently classified as an MPA, the marine life of this classified area was hypothesized to have benefited from changes in the habits of the local communities of people, fishers, and beach lovers, either due to regulation or community guidelines.

Initial studies looked at the effectiveness of Marine Protected Areas (MPAs) in protecting intertidal biodiversity of Avencas in Portugal. The researchers monitored coastal sea animals and organisms in the area before and after the reclassification and found that a strong storm named 'Hercules' from January 5th to 7th, 2014, which triggered strong sea waves, had a significant impact on the biodiversity, which did not recover as expected. Studies suggest that longer data series are needed to account for natural variability and that the size of an MPA affects how biodiversity is impacted by external factors. Some studies recommend an increase in the protected area, a new fishing regime, and an adequate monitoring program to evaluate the effectiveness of the new management scheme.

The K-MENA team's aim was to produce a method that would identify the features of most importance in relation to species coverage of the MPA, a scalable forecasting model that is fed input on the features of significance and predicts future trends in species coverage, and a product that can be used by stakeholders in local policy, research and development, and conservation to identify and mitigate risks to biodiversity.

Our product, which would be an interactive dashboard, has the potential to provide accurate predictive insights when fed weather forecasting data and can even be used to create contingency plans for different extreme weather scenarios.

 

## 🔢 Data (250 words max)

The main dataset used for monitoring sessile species in the MPA was the 'AMPA_Data_Sample,' which contained information on the percentage coverage of sessile species. However, our attempt to find external datasets on water environment, such as salinity or acidity, for the feature importance analysis proved unsuccessful. We could not locate datasets that covered the same location within a reasonable distance and timeframe, making it difficult to obtain accurate results.

To address this limitation, we recommend recording as many factors as possible alongside the samples when they are taken, including geographic coordinates. This comprehensive approach would allow for monitoring and plotting the distribution of these populations. These improvements would serve several purposes:
- Create better awareness and benchmarking of environmental conditions in the MPA.
- Monitor conservation strategies over time for the specific locations and species of interest.
- Highlight correlations between species distribution and recorded environmental factors, such as acidity.

By implementing these enhancements, we can gain deeper insights into the MPA's environmental conditions, track the effectiveness of conservation efforts, and identify potential connections between species distribution and specific environmental factors like acidity.


## 🧮 Methods and Techniques (250 words max)


We propose a simulation tool for forecasting the future coverage of species in spatially classified area. We create a predictive model that can take several parameters (weather, tide level, temperature, etc.) in training, the number of inputs can be increased/descreased according to performance of the model and user preferences, therefore the model is scalable.

We define the problem as predicting the coverage of species given variables. Therefore it is a regression problem. We first pre-processed the data before setting our model. We convert the variables (Weather, Zone, intertidal, Substrate, species) to categorical variables. We compared a variety of regression models using PyCaret, an open-source machine learning library. To improve the overall effectiveness of the model, we used an ensemble machine learning technique that uses a machine learning model to learn how to combine the predictions from multiple contributing ensemble member models in the most effective way. 


## 💡 Main Insights (300 words max)

#### Observations:
- In terms of average coverage throughout the duration of sampling, Red Algae was the predominant kingdom in this data, followed by Animalia and Green Algae.
- After normalising total coverage throughout time, the highest total coverage for Animalia, Fungi and Red Algae occured before 2014. After 2014 the numbers drop and continue to drop, with the exception of fluctuations. However, the general trend is downwards.


## 🛠️ Product

### Definition
Interactive map that will predict the coverage of species as far in as input data from the weather predictions go!

### Users

Public sector stakeholders and research organisations can review the visualisation to anticipate how species coverage will change with time. They can also use it to model slightly more extreme weather scenarios to see what the predicted impact could be on biodiversity. We hope this product can be used to inform changes in policy/infrastructure/conservation strategies etc.

### Activities

#### Features of Product:
* Provides predictions of species biodiversity, either grouped by Kingdom, other classfication systems such as 'invasive' or 'endangered', depending on the category of species fed in as the input for the model. 
* It can also be used to understand how extreme scenarios, such as the Hercules storm, can impact biodiversity, especially as inputs become more robust.

We encourage a data contract to be produced between the weather, water temperature and tide measures data providers such as operational meteorologists/forecasters and the product owners so that a frequent frequency of data is provided.

These metrics help scientists, policymakers, and conservationists assess the current state of marine ecosystems, identify specific challenges, and guide management and conservation efforts to address them effectively.

### Output
Describe what the product outputs to the users and how it does that. You can add mockups and/or visualisations.

As shown in our notebook submission and pitch, using geo coordinates recorded per sample, the predicted distributions of organism categories can be visualised.

### Scalability

We feel the product itself is scalable, applicable for other areas and wide scope of scenarios. Bottlenecks could include: 
- reliability of weather, water temperature and tide measures
- quality of data - we concluded that the current datasets are not comprehensive enough to product the most reliable outputs, but this can be remedied with time and improved sampling.


## 🌍 Social Impact Measurement

### Outcome

The long term outcome of our results are:
- A sustained recovery of biodiversity with MPA
- Understanding of the impact of various factors on inhibiting or improving the above
- Increasing research and scoping capacity of the research organisations looking to use this area for conservation and biology research
- Implementing interventions for the factors that negatively impact biodiversity, such as water temperature and tide, and measuring impact of these intervations through observing biodiversity recovery.


### Impact Metrics
Marine Species Extinction Risk Index will be calculated based on three metrics.
Habitat Loss Index: the extent of habitat degradation or destruction within a marine ecosystem.
Biodiversity Index: the diversity and abundance of species within a marine ecosystem.
Invasive Species Impact Score:  the degree of negative impact caused by invasive species in the marine ecosystem.

These metrics help scientists, policymakers, and conservationists assess the current state of marine ecosystems, identify specific challenges, and guide management and conservation efforts to address them effectively.

#### Our metrics to define whether we are achieving our outcome: 
* Increased total % coverage month by month of species of interest
* Retrospective Actual vs Predicted coverage comparison (% difference) to provide confidence that the product provides impactful insights 

### Impact Measurement

The ocean acts absorbs about 31% of the CO2 emissions released into the atmosphere according to Gruber et al., 2019. Retaining and improving the biodiversity within our oceans is a viable solution to tackling climate change, as these systems function as natural carbon sinks, providing so-called nature-based solutions to climate change.

In addition, mapping tools are becoming increasingly popular within conservation efforts - e.g. http://www.sparc-website.org/ is a GIS-based mapping tool used to build a global picture of the movement of all known plants, birds and mammals in response to climate change. It has so far allowed governments to make crucial predictions about where climate change will impact species. We see parallel opportunities here with the product we have produced.


References:

Gruber, N., Clement, D., Carter, B. R., Feely, R. A., van Heuven, S., Hoppema, M., … Wanninkhof, R. (2019). The oceanic sink for anthropogenic co&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; from 1994 to 2007. Science, 363(6432), 1193–1199. doi:10.1126/science.aau5153 
