# World Data League 2022

## 🎯 Challenge
*Predict Waste Production for its Reduction*

## 👥 Authors
* Lukas
* Ulas
* Houman
* Amit

## ✨ Introduction (250 words max)
Provide a contextualization of the problem, together with an estimation of its size using real numbers and references.
*To identify waste trends and to produce an explainable model for predicting future waste production*
Existing challenges:
Not able to predict well in advance
Lack of awareness - currently people are not aware about the pros of waste management
Scope for improvement in optimization in process


## 🔢 Data (250 words max)
Data used : Daily Waste Collection Report for Austin

## 🧮 Methods and Techniques (250 words max)
We used box plots and time series analysis during EDA
Did feature selection to see the variable importance
Used Shapley Values to analyze marginal contribution 
For modeling, we used Linear regression and XGBoost. XGBoost gave us better results.
Used tuning methods to improve our model : RandomizedSearchCV

## 💡 Main Insights (300 words max)
*Load Weight*
The Load Weight is in pounds. It is odd that its minimum is below 0. The maximum is also quite high: 1 562 821 pounds! 🤯 Apart from that, Austin produces quite a lot of waste: the median value is about 11 020 pounds 😶

*Type of variables*
We are only dealing with categorical variables, whereas our target is continous. So we went for a Regression task. ⚡

*Observations anomalies*
72624 observations of Loss Weight are either zero or null. 1 value is negative.

*Load type*
Regular garbage collections, single stream recycling, and yard trimmings are the most prominent types of loads in the dataset, making up about ~72% of the target variables.
Most of the waste is associated to the Load Type GARBAGE COLLECTIONS. 

*Dropoff sites*
TDS LANDFILL is by far the biggest dropoff site (TDS stands for Texas Disposal Systems). That is not a surprise since it is one of the largest solid waste collection, processing and disposal companies in the United States. 👥
Hornsby Bend at number 2 is a biowaste management plant.
MRF stands for Materials Recovery Facility. It's a special type of dropoff site from the TDS.

*Time series analysis*
It is also interesting to look at the data from a time series perspective ⏲. For instance, garbage collection is scheduled differently according to the individual districts. Also, organic waste may vary over the year ❄ 🌞

*Load Weight by Load Type*
Yard trimming seems to have a strong seasonal effect. This makes sense since the summers in Texas can be very extreme 🔥 The recycling stream, on the other hand, appears to be more stable. There is a small drop of garbage collections in the beginning of 2020- maybe that's related to COVID? 🦠

*Average Load Weight by Month and Load Type*
People in Austin do a lot of yard trimming in March and April 💚 In May tire changes are due 🚘 The other major Load Types don't seem to depend on the time of the year.

*Average Load Weight by Day of the Week and Load Type*
Other weight loads seem to be higher on Saturdays. That seems intuitive - most people work during the week and get their chores done on Saturday and Sunday ⛑

Recycling loads don't seem to have increased over the years. Which is surprising due to the increasing importance of climate change 🌳 Additionally, there doesn't seem to be a lot of data for the categories RECYCLING - COMINGLE and RECYCLING - PAPER.

## 🛠️ Product
### Definition
Our product will have fast and frequent prediction of waste production and will specify danger zones in map.
This will help management to take early actions optimizing resources waste management:
Green : Safe
Yellow : 70 – 80% capacity filled (our focus area as we have chances to avoid getting into red zones)
Red : Urgent attention needed

Ad-hoc advantages:
Better waste management will result in better traffic control
Incentivizing a green reward point system in neighborhood will involve public in making their neighborhood greener

### Users
The municipality and stakeholders involved in waste management operations

## 🌍 Social Impact Measurement
### Outcome
Improved efficiency in Operations
Get information ahead of critical events
Targeted maintenance in stead of periodic
Educating and involving public in waste management
Analytics savings 
Reduce False alarms