# World Data League 2023



## 🎯 Challenge
*Avencas Marine Protected Area: Predict the future of the local ecosystem and its species*


## Team Name
* CEOS - Champions Engineer their Own Science *


## 👥 Authors
* Ana Maria Sousa
* Duarte Rodrigues
* Mariana Sousa
* Mariana Xavier
* Ricardo Brioso


## ✨ Introduction 
*The coastal line of Cascais holds immense potential for marine biodiversity, with a unique combination of environmental conditions that can make it one of the world's most vibrant ecosystems. A diverse range of species thrives in this area, including potentially endangered species. However, around 37% of all marine mammals worldwide are at risk of extinction and the trend is for this value to worsen. Here lies the importance of maintaining and enhancing the biodiversity present. 

The zone of Avencas, Cascais, is a "Marine Protected Area", where regulations are applied for its preservation. However, the abundance of marine life has not developed as expected in recent years. Multiple challenges affect the AMPA, from the fishing for the local restaurants to the famous beach in the area and the proximity to a bustling marina. All these factors led scientists to question the main reasons behind the lack of biodiversity and abundance growth in fauna and flora. Hence, they seek a solution that enables a deeper understanding of the area, leading to new insights.

At CEOS, we set ourselves to do exactly this! Our goal is to evaluate the behaviour of the species over time, comprehending what are the key factors that influence their growth or decline. In particular, our focus tended to analyze the species that are facing a very high risk of extinction, known as endangered, and the species that are known to take advantage of the resources available in the area, preventing native species from growing, known as invasive.*



## 🔢 Data
*Our goal is to assess the dynamics of species population levels over time, understand what environmental variables influence these dynamics and predict future developments, focusing on endangered and invasive species.

The first data information assessed was a list identifying the invasiveness and conservation status of the species present in AMPA. From here, we were able to limit our focus group and dedicate attention to the key species that the Cascais biology team are keener on understanding.

Although these groups are divided into two wildlife types (sessile and mobile), the data regarding their presence in AMPA over the years is very similar, simply changing the metric used to describe its presence: percentage of coverage vs abundance. From here we were able to extract key conditions that could explain the evolution and modulate the fluctuations of the species, such as tide height, substrate, weather conditions and water temperature. Based on the time of the measurements, we engineered two new features: season and moon phase.

An important note is that the dataset provided was collected manually, which inadvertently introduced several data-related challenges from the beginning. A suggestion would be to implement a digital system where the data could be input. This could offer immediate data standardization and give warnings for invalid data. Another recommendation would be to settle a solid sampling periodicity. In our analysis, we found it much more valuable to have data in a short temporal granularity, than having bigger time intervals with plenty of replicates in the same day.*



## 🧮 Methods and Techniques
*The development started with an exploratory data analysis (EDA) which allowed us to narrow down the dataset for further analysis by identifying the most relevant species. Data cleaning was also performed, uncovering characteristics like the prevalence of samples collected in sunny weather and on a rock substrate. The Cladophora sp. emerged as the primary species of interest, given its extensive data spanning nine years, making it an ideal candidate for proof-of-concept AI models.

The main goal was to understand the behaviour of this specie, leading to a time-series regression problem. By training a model using the specie's coverage over the past nine years and the prevailing environmental conditions, it became possible to predict the population levels in the future based on new scenarios or sample data.

The methodology adopted initially involved applying simpler machine learning algorithms, including Random Forest, Gradient Boosting, and XGB Regressors, to establish a benchmark and assess if these models could learn from the data. Although the latter two models appeared to fit the training data better, they suffered from overfitting on the test data, performing worse than the Random Forest.

The second approach explored two more complex custom deep learning approaches: the first considering only past coverage information, and the second together with the conditions. While both showed lower training scores, they exhibited better test scores: an R-squared value of 0.41. This indicates the model's ability to generalize well to unseen data despite its weaker performance on the training set.*



## 💡 Main Insights
*During the EDA of the AMPA dataset, several intriguing findings emerged. Firstly, it was observed that all the species considered invasive are from the sessile type and all the species endangered are from the mobile type.

The following endangered species were identified: Diplodus sp., Diplodus sargus, Diplodus vulgaris, Diplodus cervinus, Lipophrys pholis, Gobius sp. It was noted that the number of endangered individuals appears at very specific points in time.

The following invasive species were identified: Asparagopsis armata, Osmundea pinnatifida, Cladophora sp., Codium sp.,Colpomenia sinuosa. Contrarily to what was said before, most of the invasive species have some data continuity.

It is worth noting that there was a noticeable change in the sampling regime in 2016 for all species. Since then, there has been a decrease in data points with larger intervals between them.

From the Random Forest Regressor, the importance and dependence of each feature for the selected proof-of-concept species, Cladophora sp., was estimated granting interesting results. For example, our model predictions and subsequent visualizations indicated that these algae preferred a sandy substrate and water temperatures around 16ºC to have a bigger coverage. Nevertheless, it is important to note that the biggest importance is given to the coverage value measured before.

We have proven that our model can be generalized not only to other zones with similar characteristics to the ones it has been trained on but also to other species making it possible to analyze which conditions are more adequate for each species to grow there.
These findings lay the foundation for deeper analysis and investigations into the ecological dynamics and requirements of different species within the AMPA; however, it is remarkable how such a model can understand the details of a species and predict their abundance in the future rather accurately.*



## 🛠️ Product

### Definition
A platform to indicate the expected biodiversity and abundance of a specie, based on the environmental conditions.

### Users
The main users of the platform would be the biology team that is scouting the AMPA and collecting samples. They would have a real-time data-driven baseline of the abundance value to be expected of a certain specie, considering the environmental conditions, in a certain zone of the protected area. Thus, they could attempt at controlling these conditions to enhance the growth of certain species.
Researchers and data scientists could also be end-users, as they can compare the circumstances that the platform indicates are propitious for a species to the gold standard of marine biology thus giving even more insights into the observed phenomena.
In the long term, if new features are added - for example, noise volume as it is verified to be correlated with the appearance/decline of abundance - the regulation/policy makers could be indirect users, as they can manage the city and create rules to make the area more suitable to the development of the biodiversity.

### Activities

* Predicts the coverage/abundance value for a specific species according to a set of conditions
* Tracks the abundance over the last years, giving an evolution feedback
* Estimates what are the specific conditions a certain species prefers


### Output
By receiving the past information on the evolution of a specie over time and conditions, the product returns a prediction of that specie's growth in the near future, according to the predicted conditions - e.g. weather and tide forecasts.
Moreover, the product also indicates which conditions are more favourable to that specie's growth by assessing the importances given by the predictive model.


### Scalability
We have proved that our solution can not only be scaled into other marine zones but also to multiple species. This way, it would lead to a more complete, flexible and accurate solution.
The way to upgrade the product would be to fine-tune it with various species and conditions in order to make it fully generalizable and allow it to be used in plenty of situations.


## 🌍 Social Impact Measurement

### Outcome
Our solution aims to assist everyone involved in not only maintaining but also growing the Avencas Marine Protected Area in terms of biodiversity. In the future, they would be able to observe the expected species' growth and understand which conditions are mostly affecting that growth, allowing them to develop a plan to control these conditions and optimize them according to what they want - for example, potentiate the growth of endangered species. In the end, the outcome is important and meaningful insights that they would not have otherwise.


### Impact Metrics
* Correcteness of the prediction evaluated by the R-squared value (predictions vs observed values)
* Usage and evolution of species' growth


### Impact Measurement
From what has been seen up until now, it is estimated that the model is able to predict the species evolution with an R-squared value of aroun 0.4. Also, if the product is used as intended, it is estimated that the biologists will be able to control some variables in order to potentiate species's growth, which will be observed
