# World Data League 2023

## Team Name

JKL & Frank

## 👥 Authors

* Joydeep Chatterjee
* Kate Crawford
* Lara Strachan
* Frank Novak

## ✨ Introduction 

We aim to develop a predictive model that provides insights into the ecological factors that impact the density of mobile species found in the Avencas Marine Protected Area (AMPA).

A short-term evaluation (starting in 2010) resulted in the reduction of anthropogenic stress through data collection, fishing community input, and visitor education. For long-term efforts, researchers strongly advised the establishment of a monitoring program. Our model aims to support these efforts, providing insights on ecological factors related to species abundance. Understanding influential factors is essential for effective coastal zone management in response to climate change.

## 🔢 Data 

Our model utilizes climatological covariates based on almost a decade of observations, providing sufficient data for estimating changes in species abundance and the long-term condition of the MPA.
While acknowledging the limitations of current sampling methods and the potential biases in our models and predictions, we were informed by the initial analysis conducted by the researchers who provided the dataset. They observed a decrease in densities of mobile species between 2013 and 2015, potentially influenced by the Hercules storm of 2014. 

## 🧮 Methods and Techniques 

Our primary objective was to prepare the data for forecasting regressors that could offer valuable insights into ecological factors that have a larger effect on predicted species occurences. To achieve this, we initially focused on ecological factors and removed individual species occurrences, as models with high dimensions are challenging to analyze effectively. 

We manually partitioned the data into training and validation sets to specify a cutoff date to model the recovery trends of the AMPA after the Hercules storm. By splitting the data in half, we were able to create a point (23-05-2016) to represent when the pier was re-established in the Summer of 2016.

A pipeline for preprocessing and modeling was then constructed for reproducability. We evaluated two classifiers, namely a linear regressor and a random forest regressor from scikit-learn's library. The latter generated a tree structure, enabling the calculation of feature importances and identifying the key factors that influence the abundance of mobile species.

To create a compelling and accurate visual aid to better understand abundance through time, the data had to be preprocessed and parsed into observations by zone and then joined to the corresponding shapefile in ArcGIS. This enables exploration by time, geographic location, and observation data. An interactive web app was then created and deployed, with additional layers added, including Healthy Beach Program locations and Coastal Zone Potential initiatives to better illustrate the environmental factors potentially impacting the area.


## 💡 Main Insights

One significant finding pertained to Cladophora sp., an invasive species known for its aggressive behavior and high mortality impact on rival organisms. What stood out was its ability to generate elevated concentrations of dissolved phosphorus, a vital nutrient for algae growth.

Further research highlighted the potential implications of Cladophora sp.'s invasion. Its dominance in aquatic ecosystems can disrupt the balance of nutrient availability, potentially leading to harmful algal blooms and the decline of native species. Understanding the mechanisms driving Cladophora sp.'s invasiveness and its ecological impacts will be crucial for effective management and conservation efforts in affected areas.

Secondly, we examined the effects of extreme weather events, specifically the impact of storms like Hercules in 2014, on a AMPA. This investigation revealed compelling evidence of how such storms can significantly influence the environment and species within the AMPA. Seen in the data, it required almost 6 months after the storm passed for the number of observed mobile species to reach levels they once were in the area.

## 🛠️ Product

Utilizing both forecasting and visualization, an end product that could be of benefit to the protection of the Avencas area would be a map that illustrates areas of predicted low species abundance and/or high invasive species prevalence. Predictions from the forecasting model could be fed into the ArcGIS map, and researchers or other advocates for the area could launch a preemptive intervention by limiting fishing or recreational activities in the area, or doing invasive species mitigation. 

Further refinement of the model, and therefore accuracy of the predictions, could be gained by installing permanent sensors in the area to measure tide levels and water temperature. Making access to this map publicly and widely available could help impart ownership to the residents of this area. Having public buy-in to the protection and restoration efforts is imperative to any initiative’s long-term success. 

Factors beyond the control of any individual or community include the impacts of climate change. Extreme weather events, global temperature increases, and rising ocean levels are all existential threats to the ecosystem of Avencas and beyond. While regional efforts are necessary and beneficial, large-scale changes by the organizations and industries responsible for significant environmental harms must be a part of coastal management efforts.

### Definition

A real-time and predictive interactive map that visualizes the abundance of endangered and invasive species within protected zones.

### Users

Residents of the area, fishing communities, and people involved in the tourism/boating industry could all use the map to plan their activities in a way that has the least negative impact on the ecosystem. Researchers, policymakers, and environmental protectors could use this to inform any potential interventions or monitoring programs.

### Activities

* Predicts the most likely ecological factors for mobile species abundance.
* Suggests the how storms, like Hercules in 2014, impacted the environment and species in the MPA.
* Maps the abundance of species within different areas of the AMPA.

### Output

Location of mobile species within various protected zones over time. See a historical map [here](https://lstrachan.maps.arcgis.com/apps/instant/slider/index.html?appid=5b02eae0a86f438783c6b082ab4a5209&locale=en-us). 

### Scalability

This solution could certainly be expanded to encompass any areas where observations are being collected. Further efforts could be made to ease the labor costs of collecting these observations, such as using sensors, underwater cameras, and satellite observations. Computational costs would increase as the size and scope of the data increase. 

Different habitats can have wildly different factors that impact them, and different criteria defining what “healthy” looks like, so that could pose a challenge. Training models on only the relevant data for that area, as opposed to broader regions, could mitigate this.

## 🌍 Social Impact Measurement

### Outcome

To increase the abundance of mobile species in the area and decrease the spread of invasive species.

### Impact Metrics

* Average Abundance (ind/m2) by month
* Total coverage of an invasive species 

### Impact Measurement

The model had predicted that mobile species would have an abundance value of 0.33 for one of the final dates in November 2020. To test the affect of temperatures and tides on species occurences, data was fabricated to model conditions in December 2020 if they were above average values for the tide and water temperature. Additionally, the test data models a higher percentage of sessile coverage in Zone. 

The result of this test was a predicted value that fell below the predicted trend line by 0.17 units and above the actual observed value by 0.08 units (as seen above). By adjusting the conditions to reflect above above average measurements of ecological features, the model was able to predict more accurate results. This is in spite of a 0.25 unit difference between the actual value and fitted value the predicted with using the real test data. 

* Based on model predictions*: Rising tides, water temp, and more invasive species have been causing the AMPA to not return to normal levels.
* Based on the results of [this study](https://www.science.org/doi/10.1126/sciadv.abc6434), if declining native flora and fauna were reintroduced into the area, Avencas fauna communities could be indistinguishable from a healthy, or “natural”, area in 3 years.


### Citations

Cuddington, K., M.-J. Fortin, L. R. Gerber, A. Hastings, A. Liebhold, M. O'Connor, and C. Ray. 2013. Process-based models are required to manage ecological systems in a changing world. Ecosphere 4(2):20. http://dx.doi.org/10.1890/ES12-00178.1

Ferreira, A, Alves, AS, Marques, JC, Seixas, S. Ecosystem response to different management options in Marine Protected Areas (MPA): A case study of intertidal rocky shore communities, Ecological Indicators, Volume 81, 2017, Pages 471-480, ISSN 1470-160X, https://doi.org/10.1016/j.ecolind.2017.06.028.

Mannocci, L, Boustany, AM, Roberts, JJ, et al. Temporal resolutions in species distribution models of highly mobile marine animals: Recommendations for ecologists and managers. Diversity Distrib. 2017; 23: 1098– 1109. https://doi.org/10.1111/ddi.12609

Robert J. Orth et al., Restoration of seagrass habitat leads to rapid recovery of coastal ecosystem services. Sci. Adv.6,eabc6434(2020). DOI:10.1126/sciadv.abc6434 https://www.science.org/doi/10.1126/sciadv.abc6434
