# World Data League 2022

## 🎯 Challenge
*_Waste Production Prediction_*

## 👥 Authors

-   Mohamed Taha

## ✨ Introduction (250 words max)

*Worldwide, waste generated per person per day averages 0.74 kilogram but ranges widely, from 0.11 to 4.54 kilograms.   Though they only account for 16 percent of the world’s population, high-income countries generate about 34 percent, or 683 million tonnes, of the world’s waste.  
We tried to gather data from cities all around the world about waste production, types of solid waste population, education level, income level, and other economic factors.
We tried to find out which of these features are most related to waste production.
Globally, most waste is currently dumped or disposed of in some form of a landfill. 
Lower-income countries generally rely on open dumping; 93 percent of waste is dumped in low-income countries and only 2 percent in high-income countries. 
Our goal also is to understand how economic, and social changes would affect waste production, to help make plans and predictions of the required infrastructure.*

## 🔢 Data (250 words max)
*We decided not to use the Austin dataset as we wanted a dataset of cities all around the world.
We used the 'Trends in Solid Waste Management' dataset from The World Bank. It contains data about data collection methods, waste composition, data management systems, collection costs, and waste treatment methods for 734 cities all around the world.
But unfortunately, the dataset had too many null values.
We merged the previous dataset with another dataset also from The World Bank but for countries, including national income, population distribution, % of agricultural land, birth rate, electricity production, employment rates, Gini index, GDP, and urban population percent of the population. which also had null values.
The output dataset was of about 400 records. We removed the features that contained more than 20% of null values.
The Austin dataset is great. but it might not reflect on cities located in other regional areas.*


## 🧮 Methods and Techniques (250 words max)
*We created a regression model using CatBoost. 
CatBoost can better deal with null values and isn't affected much by bad features.*

## 💡 Main Insights (300 words max)
*Most of the features aren't closely correlated with the amount of waste produced.
The most influencing feature is the population and percentage of non-children in the city, which makes sense.
The composition of waste also has some influence, waste produced increases if the composition of glass or metal material increases.
There is a positive correlation between waste generation and income level. *

## 🛠️ Product
### Definition
*A model that can help in waste management* 
### Users
**Waste management  companies:** Helping Waste management  companies to scale by estimating the number of trucks and equipment, for waste management jobs in new locations.


### Activities

* Collecting data about the new city.
* Predicting the amount of waste

### Output
* Prediction of the amount of waste



## 🌍 Social Impact Measurement
### Outcome
* To reduce uncertainty when a company wants to scale its operations in another region and to increase efficiency of resources usage.
* To understand how economic conditions affect the waste production.

### Impact Metrics
From the outcome, define **2 to 4 metrics** that measure if you are achieving that outcome or not.
Example:
* Risk or losses accociated with working in a new region,
* Amount of accumulated waste in the city.

### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.

Example:
* *Based on model predictions*: Our model estimates a that the city of Alexandria, Egypt produces 40% less waste than Cairo,Egypt. So, if you need to expand there you can estimate the resources that you'll need.
Executive Summary Template.md

Open with

[![](https://lh3.googleusercontent.com/ogw/ADea4I4ANPYswZjF26kPEHLAgNGqdz2kmmdbg5HLkz3p=s32-c-mo)](https://accounts.google.com/SignOutOptions?hl=en&continue=https://drive.google.com/file/d/1sl7xOd2C1x-sREfOaS4AoR4sdTP5MZaP/view&service=writely)

Displaying Executive Summary Template.md.