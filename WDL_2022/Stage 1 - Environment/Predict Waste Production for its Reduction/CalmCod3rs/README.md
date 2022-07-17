# World Data League 2022

## 🎯 Challenge

UrbanAI Challenge

## 👥 Authors

* Ana Luiza Kaori Akiyama
* Luiz Gustavo Moniz
* Guilherme Caixeta


## ✨ Introduction (250 words max)

In 2011 the city of Austin adopted the Austin Resource Recovery Master Plan [[1](https://www.austintexas.gov/sites/default/files/files/Trash_and_Recycling/MasterPlan_Final_12.30.pdf)], aiming to implement a strategic plan to reach the Zero Waste goal by 2040. In this plan there were established goals for every five years, until 2040, aiming to gradually reduce the waste disposed in landfills and incinerators at the same time that they were trying to increase the waste diversion, in other words, the waste that is reused, recycled and compost. According with the goals, it was stipulated a 75-25 percentage to the residential waste in the year of 2020, that means 75% of waste diversion and 25% of garbage waste (p.230) . In our analysis we identified that this goal wasn’t reached, 51,22% of the waste went to landfills or incinerators and 48,78% were waste diversion. We verified that one of the disposal categories that didn’t reach their goal was recycling; it was expected the collect of 75.0000 tons in the year of 2015 and 80.0000 in 2020 (p.230), but it collected only 57.1494 and 63.9098 tons respectively. In that way, our analysis conducted us to the objective of trying to increase the number of recycle material collected through the building of a model and a ChatBot that helps the citizens to identify if the disposal is recyclable or not, since this misinformation is appointed as a key factor causing the low recycling rate (p.246).


## 🔢 Data (250 words max)

* Daily Waste Collection Report for Austin
* Population per year (1840-2016)
* Garbage routes for the City of Austin (shp / geojson file)
* Kaggle Waste Classification Dataset (22500 images)
* Sales tax & retail sales (from Texas Comptroller of Public Accounts)
* Annual Budgets (from Austin Finance Online)

On the `Daily Waste Collection Report for Austin` dataset, the `Load Type` column with the value `RECYCLING - SINGLE STREAM` is the largest portion of recycling. It would be nice to have another dataset indicating which proportion of recycling materials were separated, in order to help recognize recycling patterns (e.g.: what are the most frequent types, contaminated materials percentage). This could help to analyze how the population is doing in recycling.

A column of the `district` where the waste collection was taken, could be useful to analyze if there is some correlation between the `Load Weight` and the location (socio-economic situation, close to commercial areas..). 

The garbage route map contains only the TDS routes. We have found a shapefile which contains some recycling routes, but it would be nicer if others site routes could be together as well in order to find new patterns.

We used Kaggle Waste Classification Dataset to train a chatbot to classify the images. 

We made use of the 'Annual Budgets' dataset to explore the relationship between the Waste Diversion budget and waste production.

We also used the Sales tax & retail sales dataset to explore a bit about the correlation between the Austin retail sales and waste production.


## 🧮 Methods and Techniques (250 words max)

We decided to use NeuralProphet to create a prediction model. It combines Facebook Prophet and AR-Net, which is a hybrid forecasting framework based on PyTorch and trained with standard deep learning methods. It uses Prophet capabilities to model trend and seasonality as well it can model covariates and auto-regression as AR-Nets.

In order to create the proposed solution (the chatbot app), we choose Rasa Framework which is a Open source machine learning tool for developers to build, improve, and deploy text, image and voice-based chatbots and assistants. Our solution can recognise and classify images using pytorch. The training was performed using a high-level framework “FASTAI”.

We created Value-By-Alpha Maps, which makes possible to analyze which areas contain high populations with low recycling rate and areas with high landfill disposal and low recycling.To build this graphics we used three datasets with geometry. The first one was the zip code dataset, the zip code polygon was our base of analysis and we added to this dataset the population by zip code. The second dataset was the recycle collection routes. The third dataset was the garbage collection routes. We used a GIS software to plot this three datasets and then we used a geoprocessing tool called intersection to intersect the geometry of the garbage and recycle route with the zip code geometry. That allowed us to have a zip code geometry with their information and the information of the garbage and recycle routes that were inside of this zip code.


## 💡 Main Insights (300 words max)

* When the Austin Resource Recovery Master Plan started, we noticed a significant increase in materials being recycled over the subsequent 3 years. Although the 2015 target was almost reached, we noticed from 2015 to 2020 the growth rate decreased and consequently the target was not reached in 2020.
* COVID-19 impact on the production of waste: There has been an increase in waste production, probably because people spent more time at home. In addition, recycling increased slightly and other types of collection decreased at the beginning of the pandemic, as some services were suspended for some time.
* Using the `Annual Budgets` dataset, we verify the correlation between the Waste Diversion Budget and the different types of waste (RECYCLING, ORGANICS AND DISPOSAL). The correlation of ORGANICS with budget was 0.5, indicating that the organics grew with the increase of the budget. The correlation with Disposal was -0.33, which could indicate that there was a decrease in disposal production as the budget increased. Finally, the correlation with recycling was -0.03, indicating that the recycling did not have a strong dependence on budget. 
* The ORGANICS goals were met, while the RECYCLING weren't. Maybe because organics are easier to separate, while recyclables have many more categories. Therefore, a solution would be making the recycling process easier for the population.
* Using Value-by-alpha maps it was possible to localize regions in Austin where the recycling weight is low and the waste disposal is high. It was also possible to find regions where population is high and recycling weight is low.

## 🛠️ Product
### Definition

A ChatBot App model that helps the citizens to identify if the waste can be recycled or not.


### Users

Citizens of Austin would use the ChatBot App in their everyday life to understand if the waste that they produce can be recycled or not. This can be an easy and interactive way for people to learn how to recycle.


### Activities

* Classifies whether the user's garbage is recyclable or not (by photo or text) 
* Suggests the the best destination depending on the garbage
* Schedules collection
* Send alerts about new projects


### Output

Classification of the user’s garbage (whether it is recyclable or not) and suggest the best destination for it.


## 🌍 Social Impact Measurement
### Outcome

The idea of this product is to help the city of Austin to reach their Austin Resource Recovery Plan goal of Zero Waste by 2040 increasing the recycling collection percentage and therefore the waste diversion collection percentage.


### Impact Metrics

* The growth of recycling collection
* The growth of the waste diversion collection
* The decrease of residential waste disposal


### Impact Measurement

There is a similar tool developed by the company Smarter Sorting that helps local governments and retailers determine what to do with their waste—from whether to move it on for reuse, to knowing how to dispose of it, or how to ship it. 

Eric Michaels (Salt Lake County Health Department household hazardous waste program manager) estimates that with the technology, in about a year and half, 47,000 pounds have been categorized and identified for reuse that would have otherwise been incinerated [[1](https://www.waste360.com/fleets-technology/smarter-sorting-leverages-technology-data-support-waste-operations)].




