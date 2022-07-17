# World Data League 2022

## Executive Summary Template
This executive summary is one of the mandatory deliverables when you submit your solution. Its structure follows the WDL evaluation criteria and it has dedicated sections where you should add information. Make sure your executive summary covers all the sections since it will be an integral part of the Insights Report and your evaluation. Make sure your content is relevant and straight to the point.
**There is no need to reach the maximum number of words.**

Instructions:

1. 🧱 Create a separate copy of this template and do not change the predefined structure
2. 👥 Fill in the Authors section with the name of each team member
3. ✏️ Write your executive summary - make sure you write to a non-technical crowd. You can refer to images that are in the Submission Notebook.
4. 📄 Fill in all the text sections
5. 🗑️ Remove this section (‘Executive Summary Template’) and any instructions inside other sections
6. ⬆️ Upload the .md file to the submission platform.

## 🎯 Challenge
Predict Waste Production for its Reduction

## 👥 Authors
Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.
Luís Ventura
Pedro Leal
José Sá

## ✨ Introduction (250 words max)
Provide a contextualization of the problem, together with an estimation of its size using real numbers and references.

As described in the introduction to the problem, the World Bank estimates that, in 2016, cities generated 2.01 billion tons of solid waste. Per
person, this is around 0.74 kg/day. We found that, in Austin (Texas), our estimates for the total amount of waste between 2012 and 2022 range around the 0.68-0.70 kg/day. 
Given that about half of the city's waste is undifferentiated trash that goes to the the LDS Landfill in Creedmoor, TX, and the population of Austin is about 1M people (in 2020), 
this corresponds to a total amount of 122199 tons of landfill waste in 2020. Removing this amount of waste requires resources (both time, money and space) that could be better utilized.

As it is only the 11th largest city in the United States, the problems displayed in the city of Austin are likely to be even more serious in larger counterparts as New York, Chicago or Los Angeles.


## 🔢 Data (250 words max)
Explain what data you used (both provided by WDL and external) and improvements you suggest to those datasets. Explain how those improvements would lead to a better solution.

We have used two datasets:

1. data.austintexas.gov - Waste Collection Diversion Daily Report. One problem with the dataset is that the "SWEEPING" category of "load_type" has a lot of missing values in "load_weight". We speculate
that this is the case because the "load_weight" of these waste collections might be too small individually to be recorded. To avoid this problem, we would suggest the city defines a minimum value, above which the pickup
is recorded with its actual weight and below this is capped at a minimum.

2. Google Mobility data for Travis county, where the city of Austin is. This was used in conjunction with the waste data from 2020 to ascertain whether the shifting consuming patterns (from goods and services to mostly goods)
resulted in an increased amount of waste. One problem with this dataset is that the reference point to which "mobility" is computed is unclear. It would be better to fix a mobility benchmark using the
2010-2019 (with level adjustments to make it consistent across years) and then compare mobility in 2020 with this.

## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.

Our team focused mainly on time-series analysis from an econometrics perspective. Our goal was to create a model for the garbage collection component of waste and use this as a proof of concept that could then be applied to other,
less relevant, components such as recycling and organics. To that effect, we have used (partial-) autocorrelation plots to uncover the autoregressive and seasonal structure of the data.

We then used a linear model, where a time-series is decomposed into trend, season and irregular parts to describe the data. Our quantitative metric was root mean squared error, combined with a qualitative assessment of the statistical
significance of the models coefficients. In our view, the performance of the model under the former is good, while only acceptable under the latter - there are several statistically insignificant coefficients which suggest that the model
misspecified (and overfitting the data). Nevertheless, we think that building the model from the ground-up is more insightful of the underlying data generating process.

## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.

1. The most relevant types of waste are garbage collections (undifferentiated waste directed to the landfill), yard trimming, recycling and organics.
2. The latter is a result of the adoption of a program by the city of Austin to distribute composting bins to households. The large increase in this component (as a percentage of total waste) since 2018 appears to suggest that
adoption has been considerable.
3. However, the percentage of garbage collections and recycling has remained relatively constant throughout the last 10y, suggesting that a larger emphasis needs to be placed in the importance of recycling.
4. The 2020 increase in waste can be explained from an economic perspective: as services close due to COVID-19 lockdown measures, economic agents shift their consumption to consumer goods. This leads to an increase in the amount of waste,
which (we speculate) is further enhanced by the fact that online-ordered consumer goods tend to be more package-intensive than those bought at a physical shop.
5. As a result, one should expect the amount of recycled waste to have increased beyond the garbage collections.
6. We computed the total amount of waste per person in the city of Austin in the last 10 years. Its downward trend suffered a large setback during the COVID-19 pandemic, highlighting the dilemma that policy makers have when addressing multiple problems with
interfering solutions.

# 🛠️ Product
### Definition
A waste management software solution providing a forecasting model for waste production with geographical information for route collection management and optimization.

Define in **one sentence** what product(s) could be built out of the code you produced.
Model that forecasts the monthly amount of waste. A 12-month ahead forecast can be generated at the start of the year to present policy makers with a benchmark, around which they can propose policies to drive waste reduction and increased acceptance of composting and recycling.

### Users
Waste collection companies can use this product in several ways, with examples being:
* Micro-level route planing in advance, making use of the forecasting geographical model, optimizing resource allocation during different periods of the year and distinct city zones;
* Management would be able to forecast and adjust company objectives and resources according to macro-level forecasts;

Besides this, policy makers would be able to use the forecasting model to understand current trends in waste collection throughout the city and adjust their policies and incentives towards their goals. This would also allow for keeping track of what progress is being made towards those objectives and adjust 'in real time', as opposed to only doing it at the end of the year.

Additionally, with our solution, city government and companies would be able to work together in order to adapt the route management to decisions made based on the forecasting model.


### Activities
* Keeps track of waste production and collection in a centralized place, with tools to make it's analysis easy and accessible. This allows for it's use at different skill levels
* Predicts the global forecast of waste production, in it's many categories, and also by geographical zone of the city. This allows for better resource allocation
* Automatic trend analysis and forecast for distinct types of waste production
* Prediction of whether current goals are going to be met by their deadline


### Output
Visualization of current waste production/collection in each area of the city. This can be daily, weekly and/or monthly metrics (averages, sums). 
Track of waste trends taking into account previous periods, using information stored in an internal database and visualized through several interactive dashboards.
Using this information and the underlying forecasting model, predict how the waste production will evolve in the future (for example in the next 12 months) in each city zone. This would also be presented to the user via dashboards with plots and metrics. Track the progress towards a predefined goal, for example, increase in recycling percentage in the whole city or decrease in the overall waste production in certain areas.



## 🌍 Social Impact Measurement
### Outcome
To create a system that allows for reducing the effort and resources used to collect waste produced in large scale, as the optimization of this industry can lead to massive reduction in carbon emissions.
Simultaneously, there is the goal of using these monitoring capabilities to set and track goals that aim to reduce waste produced and/or shift its treatment to more a sustainable one, for example, reducing the amount of waste that goes to a landfill and transfer it to a recycling facility. This entails the shift of behaviours by the population of a certain city (Austin as a pilot experiment), which would respond to policies being applied to waste production (targeting individuals) and waste management (targeting companies). Knowing what are the effects of certain policies, and being able to track it in real time, will allow for more effective policies to be maintained, leading to a more environmentally friendly city. 


### Impact Metrics
* Global waste production
* Local waste production
* Recycling increase
 

### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.

Example:
* *Based on model predictions*: Our model estimates a decrease of 6 minutes of the average dispatch time and a decrease of the average distance of 200 meters
* *Based on proxy products*: Similar studies in other cities show that the dispatch time can be decreased by as much as 13 minutes, depending on the traffic intensity of that city.