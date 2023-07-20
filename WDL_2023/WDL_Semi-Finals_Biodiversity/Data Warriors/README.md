# World Data League 2023


## 🎯 Challenge
Avencas Marine Protected Area: Predict the future of the local ecosystem and its species


## Team Name
Data Warriors


## 👥 Authors
* Clara Pedroso
* Gonçalo Ferreira
* João Anacleto
* Madalena Diniz


## ✨ Introduction
Marine Protected Areas (MPAs) play a critical role in global conservation efforts by safeguarding marine ecosystems and their biodiversity. Effective MPAs exhibit certain characteristics at a global scale to ensure their impact and sustainability. They must accurately represent the biogeographical area they encompass, functioning as integral parts of larger networks. Furthermore, designating approximately 20% of the total area as a "no fishing" zone is a crucial aspect of effective MPAs.
The Avencas Marine Protected Area (*AMPA*) in Cascais, Portugal, covering approximately 2.07% of the oceanic area worldwide, was reclassified as a MPA in 2018. However, the ecosystem recovery in the AMPA has been slower than initially anticipated, highlighting the *need for further investigation*.
Long-term monitoring efforts between 2011 and 2020 have focused on sessile species coverage and the number of mobile species within the AMPA.
It is crucial to understand the potential *impact of climate change* on the local rocky shore and its implications for the biodiversity and abundance of species within the MPA. Some *climate change indicators* including the effects of pollutants, salinity, or pH levels, and the analysis of this dataset can provide valuable insights into the potential impacts on the future development of the ecosystem.
The findings from this study will not only contribute to the *effective management of the AMPA* but will also have broader *implications* for *global conservation* efforts and the vital role of MPAs in preserving marine resources for future generations.


## 🔢 Data
*WDL* datasets used:
*Sessil*: Occurrence and percentage coverage of a list of sessile species in the AMPA area from November 2011 to the present (2020).
*Mobil*: Occurrence and count of a list of mobile species in the AMPA area from November 2011 to the present (2020).
*Invasive_conservat species list*: Information on the invasiveness and conservation status of individual species in two separate datasets, one for sessile and another for mobile species.
*External* datasets used:
*Meteorological*: Weather conditions such as *temperature* (mean temperature at 2m elevation), *precipitation* (total precipitation of the day), *cloud cover* (percentage of sky covered by clouds), *longwave radiation* (radiation emitted by the Earth's surface and atmosphere), and *UV radiation* (solar radiation affecting marine organisms).
*Ocean conditions*: Variables such as *average fCO2* (indicating carbon dioxide concentration), *average sea surface temperature* (indicating temperature conditions), and *average salinity* (indicating salt concentration).
*Extra Variables*: Includes the *Index of Coastal Eutrophication* (measuring nutrient enrichment in coastal waters), *Air Pollutant Compliance* (assessing adherence to air quality standards), *Pollutants in Water* (cumulative amount of discharged pollutants), and *Waste in Water* (quantity of waste disposed into aquatic environments).

To improve these datasets, the temporal coverage and granularity of data could be enhanced. Additionally, incorporating more specific location data within the AMPA area would enable spatial analyses and better identification of localised trends and patterns. These improvements would lead to a better comprehension of the environmental variables, species composition, and ecosystem dynamics within the AMPA.


## 🧮 Methods and Techniques
During Data preprocessing, techniques such as dummy variable creation, data type conversion and variable encoding were used to ensure our data was compatible with the models we were going to use.
Furthermore, in order to reduce noise in the data and identify the most impactful features for better accuracy in the models we used different *feature selection* techniques like *RFE*, *ANOVA* and *Decision Trees*.
For the modelling part, we selected the following *Models*: *ARIMA*, *Sarimax*, *LTSM* and *XGBoost*.
The Arima model was used to facilitate the examination of the long-term trends and cyclic patterns in the populations of endangered and invasive species, enabling insights into the time-based variations and evolutionary processes. Due to the seasonal pattern expected in our Data, we complemented the insight with the SARIMAX model considering the various environmental factors and changing conditions. The LSTM model was used to complement our analysis taking into account its effectiveness in capturing long-term dependencies in sequential data. Lastly, the XGBoost was selected to complement the analysis due to the complexity of the variables that were selected for the models.
This approach allows for a more comprehensive analysis, potentially uncovering valuable insights and improving the accuracy of predictions for the time variance and evolution of endangered and invasive species under different conditions.



## 💡 Main Insights
Currently, *less than 1% of the world's oceans are protected*, despite global commitments to safeguarding 10% of marine areas. This target has had slow progress and, at the current rate, it would take 100 years to achieve this goal. This highlights the urgent need to accelerate conservation efforts and increase the extent of marine protected areas (MPAs) worldwide.
One remarkable finding is the significant difference in fish abundance between MPAs and areas outside these protected zones where bottom-towed fishing is still permitted. Studies indicate that *within MPAs*, there is an astonishing *370% more fish* compared to similar *areas subjected to fishing activities*. This demonstrates the effectiveness of MPAs in allowing fish populations to thrive without the pressures of exploitation.
The immediate benefits of MPAs lie in their ability to *provide natural areas with reduced human impacts*. Many species and biological communities have evolved mechanisms to withstand and recover from periodic stresses such as fluctuations in salinity, temperature, or severe storms. Notably, research on coral reefs suggests that *corals located in areas with minimal human disturbance* display a *greater resilience to high-temperature-induced coral bleaching*. These less stressed corals have a higher capacity to recover and are less susceptible to severe damage or mortality during bleaching events. Preserving representative marine ecosystems in their pristine state, enabling them to be self-sustaining and adaptable to incremental changes in ocean climate, is a wise *investment for the future*.
These insights shed light on the *importance of expanding marine protected areas*, not only to meet global conservation targets but also to preserve biodiversity, promote ecosystem resilience, and provide a refuge for marine species to thrive. *Accelerating* the establishment and *effective management of MPAs* is *crucial* for safeguarding our oceans and ensuring their *long-term health and productivity*.


## 🛠️ Product

### Definition
A *dashboard* that enables the user to change variables and see its result on the quantity of species in AMPA during the next year.


### Users
The users of the product would primarily be the *biologists* and *researchers* responsible for managing and studying the ecosystem within the AMPA. They would leverage the dashboard to explore the relationship between environmental variables and the number of species in the AMPA. They would be able to interactively *manipulate variables* such as temperature, precipitation, salinity, pollution levels, and other relevant factors. By doing so, they could observe the *effects of these* variables on the quantity of mobil and sessil species.
This information would guide biologists and researchers decision-making process in adapting *management actions* and *conservation strategies* to *protect* and *restore* the marine ecosystem effectively.
Additionally, the dashboard would *facilitate communication* and collaboration among *stakeholders* involved in the management of the AMPA. It would serve as a *tool* for *sharing data*, visualisations, and findings, enabling discussions, informed decision-making, and coordination among scientists and policymakers, for example.


### Activities
* *Variable Manipulation*: The ability for users to interactively vary environmental variables such as temperature, precipitation, salinity, pollution levels, and other relevant factors to observe their impact on the number of species within the AMPA.
* *Predictive Modelling*: The use of predictive models to estimate and forecast the future developments of species. This would provide insights into the potential trajectory of the ecosystem.
* *Shapley Values Visualization*: The visualisation of Shapley values, a technique used to understand the contributions of each variable to the prediction outcome. This feature would enable users to analyse and interpret the specific effects of different environmental variables on the biodiversity and abundance of species composition.
* *Data Integration*: The integration of various datasets, besides the ones already present. This feature would ensure comprehensive and relevant information for analysis and modelling.
* *Collaboration and Sharing*: The ability to facilitate collaboration and knowledge sharing among stakeholders involved in the management of the AMPA. The dashboard would provide features for data sharing, visualisations, and discussions, fostering communication and informed decision-making.


### Output
The product outputs *manipulative cards* that allow users to change the variables of interest, and a *graph with a timeline* that predicts the number of species based on the selected variable values.
Besides this, the dashboard would also include additional *visualisations* or *mockups* that would illustrate the *relationship* between the manipulated *variables* and the *predicted number of species*. This could involve graphical representations, such as line charts, heatmaps, or scatter plots, depending on the nature of the data and the specific insights being conveyed.


### Scalability
The dashboard can be *scalable and adaptable* to other marine ecosystems with similar data availability, demonstrating the potential for wider application beyond this one, enabling the *transfer of knowledge* and insights gained from the AMPA to other marine ecosystems facing similar challenges.
Additionally, the *data integration* feature is useful to do further improvements in the model. As the time passes, more data is being collected and with it, *more accuracy* to these models.

In spite of the results, there were also some *challenges* faced. It is always *hard* to *understand* which *variables* impact the total number of species. There were some *extra variables* that we thought about but it was not possible to find available data, such as the amount of *fishing* in the area and the *fish birds* that can be affecting the disappearance of the mobil species.
Besides this, we also tried to predict the total of *endangered* species and *invasive* species, however the *models* were very *weak*. We were not able to find relevant variables that would impact these models in a positive way even though this could be a very interesting feature to have in the dashboard as well.


## 🌍 Social Impact Measurement

### Outcome
The long-term result and ultimate goal of our product is to *contribute* to the *preservation* and sustainable management of *marine ecosystems*, particularly within the Avencas Marine Protected Area, by *increasing the TOTAL number of all species*. By providing biologists and researchers with a powerful dashboard equipped with predictive capabilities, we aim to *facilitate informed decision-making* and enhance understanding of the complex interactions between environmental variables and the biodiversity of the area.
Through the use of our product, we strive to empower stakeholders, including marine biologists, policymakers, and conservationists, to make data-driven decisions that promote the well-being of the AMPA and its surrounding ecosystems. This can include *laws, restrictions* and other things that will change the *variables* that contribute to the *creation of species*.
Ultimately, we hope that our solution will contribute to the *long-term sustainability* and resilience of marine habitats, ensuring the protection of valuable species and their habitats for future generations.


### Impact Metrics
* *Average number of species* present within the Avencas Marine Protected Area (AMPA) over a specified time period.
* *Average number of endangered species* present within the Avencas Marine Protected Area (AMPA) over a specified time period.
* *Values* for the levels of *water quality*, *nutrients* present and *pollution*. 
* Monthly *views* and *average session duration* of the dashboard by biologists, researchers, and other stakeholders involved in the management of the AMPA. This allows us to measure the level of engagement of the stakeholders with the product.

### Impact Measurement
In the context of the conservation and management of marine ecosystems, estimating the impact can be challenging due to the complexity of ecological systems and the long-term nature of ecosystem dynamics. However, we can make estimations based on the predictions of our model and available research in the field, such as:

* *Based on model predictions*: Our model predicts that if the variables keep constant, the AMPA could potentially see an increase in number of total mobil species by 100% over 2 months.

* *Based on research in similar locations*: Studies conducted in other marine protected areas with similar characteristics have shown that effective management strategies can lead to a 15% increase in species abundance within a ten-year period. By extrapolating these findings, we can estimate a similar positive impact on species abundance in the AMPA.
