# World Data League 2023

## 🎯 Challenge
Avencas Marine Protected Area: Predict the future of the local ecosystem and its species

## Team Name
Random Fourest


## 👥 Authors
* Alina Carvalho
* João Almeida
* José Sousa
* Xavier Silva


## ✨ Introduction (250 words max)
Cascais Municipality is a proactive local authority that promotes a sustainable future and coordinates the life of those who live, work, study, or visit the area by partnering with the right partners, encouraging public participation, and gathering knowledge. The municipality combines tradition and history with innovation by leveraging innovation hubs, co-creation projects, and sustainability to increase its pioneering spirit.

The Avencas Biophysical Interest Zone in Cascais, Portugal was classified in 1998 and reclassified as a Marine Protected Area in 2018. From 2010 to 2018, public participation assemblies and visual census were conducted to assess the effectiveness of management actions. A new regulation was implemented, including visitors' pathways and information spots displaying area specific rules. Positive results were found, with 84% of visitors looking favorable upon the information spots and 76% agreeing with the location of access pathways. Recreational fishers are mostly located outside the protected area, but some changes in regulation may be needed to improve compliance. A long-term analysis is still needed to evaluate the impact of the management approach.

Help is needed to understand the influence of environmental variables on the biodiversity of the Marine Protected Area. Once identified, management actions can be adapted to minimize the impact of climate change on this highly sensitive coastal zone.



## 🔢 Data (250 words max)
The main dataset used is provided by Municipality of Cascais, containing data from 2011 to 2020. The available data represents the % coverage with sessile species in AMPA, the number of mobile species in AMPA, a reference list of invasive and endangered species in Portugal - specific conservation status, and bathymetric data of AMPA. 

Avencas rocky shore area in Portugal was examined to prepare the dataset. The study monitored intertidal communities in the area before and after its reclassification as an MPA in 2016 and found that while a positive evolution was expected, a strong storm in 2014 had a significant impact on the intertidal communities. The study suggests that longer data series are necessary to obtain more robust data regarding natural variability and that size matters in terms of an MPA's susceptibility to external driving forces, and recommends an increase in the intertidal protected area, a new small-scale fishing regime, and an adequate monitoring program to evaluate the effectiveness of the new management scheme.

The data needs cleaning to provide better insights, like removing extra spaces entered in some fields by mistake, removing nulls or even changing certain values in order to maintain column patterns (and categorize the values, if needed).

In order to better understand the data provided and complement the dataset allowing for a more complete analysis, we gathered weather data for the AMPA region during the time considered.



## 🧮 Methods and Techniques (250 words max)
In order to extract meaningful insights from the data, a multi-step analysis was performed. First, the raw data was cleaned and organized into a suitable structure for efficient querying and filtering. Then, a study of the involved species was done and the knowledge applied for exploratory data analysis, resulting in visualizations and a deeper understanding of the data and its anomalies.

Another technique that was used in this approach was feature importance analysis. By training a model to identify scenarios where the species are (or are not) present, with the appropriate features, and then analyzing the feature importances of the trained model, it is possible to understand which factors contribute the most for the presence of the species. 

Also, with the objective of detecting if the measures that took place over time had the desired effect, a linear regression was used over the number of species, allowing for a trend analysis over the dataset selected scopes. 


## 💡 Main Insights (300 words max)
With the analysis of the provided data, several insights could be extracted from the first phase, which consisted in Exploratory Data Analysis.
These insights were:
* The sampling of the data provided is insuficient to provide an accurate and precise view over the specie populations.
* The year of 2015 saw an increase in population of mobil species, mostly due to "Palaemon serratus" species
* After 2016-01-01 we saw a disruption in the seasonal pattern of the mobil species, the amount of specimens was greatly reduced.

With the observation of the extracted weather data, we were able to make the following observations:
* At the beginning of 2014 there are severe wind gusts, this matches the "Hercules" storm described in the paper provided.
* At the beginning of 2013 and in December of 2018, we also have severe wind gusts
* In November of 2014 and September of 2020 there was intense rain.
* As expected in June, July and August there is little rain.
* Rain periods are more intense in October and November, even though the amount of water is only slighly higher.
* As expected temperature shows a visible correlation with the seasons.

By performing feature importance analysis in a preprocessed and aggregated dataset, we were also able to conclude that:
* While weather as its' importance it cannot explain the evolution of the ecossystem
* The lack of the precision in the input means that the output loses its value

Finally, the main conclusions provided by the linear regression analysis were:
* Due to a very sparse samples given after 2018, the Zone F, outside AMPA, appears to have a better evolution regarding to the number of individuals observed over time.

## 🛠️ Product

### Definition
A Jupyter notebook featuring multiple visualizations and information key points, including trend analysis before and after selected measures took place.


### Users
Cascais Municipality, through its team of biologists, would be able to understand the issues in a different way, and improve the way they manage and take care of the MPA. Also, the outputs provided may help policymakers deciding if certain measures that took place are resulting in the desired outcome.

### Activities

* Provides a deep analysis and useful visualizations over the data provided.
* Analyzes the factors that contribute the most for the presence of species, through feature importances attributed by a trained Machine Learning model.
* Calculates the linear regression over the number of species found over time, allowing for predictions and conclusions over measures performed in that area.

### Output

General insights about the marine species:
[Evolution of the specimens for the most notable species](https://imgur.com/l4V9L94)

Insights about the extracted weather data for the referred time period:
[Wind gusts depicting start of 2013, start of 2014 and end of 2017 storms](https://imgur.com/zw9WjdU)

Feature importance analysis:
[Most important features to explain Seabreams population](https://imgur.com/nbPFyk2)

Specimens number inference:
[Inference of the total number of specimens](https://imgur.com/XtoHihs)

Linear regression analysis:
[Trends for AMPA and F Zone](https://imgur.com/MkLWwld)


### Scalability
The model and analysis have been designed with the idea of making it adaptable to other marine ecosystems in mind. This way, the data on the new domains is intended go through a controlled Feature Engineering process, and adapted to the designed structure, before being used in the analysis and predictions. 


## 🌍 Social Impact Measurement

### Outcome

The product is a sophisticated system that combines complex data analysis and machine learning models to provide a comprehensive understanding of the Avencas Marine Protected Area (MPA). The system is designed to assist city politicians and biologists in making informed decisions about the management and conservation of the area, as well as providing projections for future trends.

The system is capable of processing large amounts of data and extracting valuable insights from it, and uses advanced algorithms to identify patterns and trends in the data, providing visualizations that help to better understand the area and its ecosystems.

The pipeline used is adaptable and can be used as a template for similar marine ecosystems in other locations. By providing a framework for data analysis and modeling, it can help researchers and policymakers in other areas to better understand their ecosystems, identify potential threats, and develop effective management strategies. Ultimately, the system is designed to help preserve and protect our marine ecosystems for future generations.


### Impact Metrics

Two metrics that can be very useful when analyzing if the applied measures are having the desired outcome are:
* Linear Regression slope / Number of species trend before the applied measures
* Linear Regression slope / Number of species trend after the applied measures

### Impact Measurement

By observing and comparing these two metrics, one can compare the trend before and after certain events of interest. If the slope is higher after that events, that should mean the event had a positive impact on the general number of species. A similar process can easily be applied for any specific species, using a similar pipeline.
