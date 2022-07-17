# World Data League 2022

## Executive Summary

## 🎯 Challenge
Predict Waste Production for its Reduction

## 👥 Authors
Bruno Silva
José Cerqueira
Pedro Fernandes

## ✨ Introduction (250 words max)
Waste management is a huge worldwide problem.
Based on the Waste Collection Report, the city of Austin generated 424M tons of waste during 2020. This value increased on average 2% yearly for the last 15 years, which means the weight of waste can easily surpass 570M yearly tons on the next 15 years.
Analyzing the dataset, one can notice that recycling types of garbage changed in 2008 from paper, metal and plastic to single bin. This was caused by the introduction of the single bin policy in this year.
We built two products, that aim to help waste management and aid decision making on policies that could decrease waste generation per capita, in the future:
 • Garbage and social economic dispersion visualization: this product aims to visualize not only the garbage generated over the different Austin geographical areas but also to visualize factors that can help understand why some areas generate more waste than others.
 • Garbage prediction model: this product aims to forecast future waste generation as well as estimate which are the economic social factors that are deeply connected to waste generation.

## 🔢 Data (250 words max)
Waste Collection Diversion Report - Austin Daily Waste Collection Data, containing weight, types of waste and routes.
Active Sales Tax Permit Holders - list of taxpayers who hold an active sales tax permit, indicating a measure for sales volumes.
Crime Statistics - list of crimes commited in Austin, as well as their severity.
Short Term Rental Locations - The general neighborhood and zip code location of short term rentals (including type) across Austin, TX.
City of Austin Affordable Housing Inventory - The City of Austin Affordable Housing Inventory (AHI) includes all income-restricted affordable units in developments funded through the Housing Development Assistance Programs sand incentivized through Development Incentive Programs that are currently affordable.
2014 Housing Market Analysis Data by Zip Code - The purpose of this data is to provide a snapshot of housing affordability along with indicators of demographic diversity, gentrification, transportation costs, and transit access at the neighborhood level. 
Boundaries Zip Code Tabulation Areas 2017 - Includes zip code tabulation area (ZCTA) boundaries for 2017 that intersect the City of Austin.
Socioeconomic Status of CDC Social Vulnerability Index - A set of metrics that describe the social economic situation of the population (education, poverty, etc.)


## 🧮 Methods and Techniques (250 words max)
Exploratory Data Analysis of the social economical factors, which made it easy to notice that factors should be looked at on a region level.
ARIMA - was used to predict the garbage time series, but it is not enough to do a root cause analysis.
Parallel tree boosting - Explainable features and fast conversion rate


## 💡 Main Insights (300 words max)
During the EDA, some observations were made:
 • Since 2008, recycling has increased significantly. This was caused by the introduction of a policy to use a single bin for recycling. Naturally since this year paper, metal and plastic recycling become single stream.
 • Waste generation shows sazonality throughout the year. Waste peak generation occurs during Spring.
 • With the visualization tool, one can see that the number of manufacturing establishments and the total population have a correlation with garbage generated.
 • %Population living in poverty and income per capity are factors that have a strong impact on waste generation.


## 🛠️ Product
### Definition
A report that estimates the impact on Waste Generation of policies and investments in specific areas of governance, for a given region of Austin.

### Users
The user of our product would be the Austin City Council and any other institutions in charge of managing waste and waste related investments.
They would use the product to guide their decision making of key areas to invest in order to reduce per capita waste.

### Activities
Allows for visual representation of garbage generation vs important factors.
Predictis social economic factors that might influence garbage generation.
Estimates the most relevant social economic factors for garbage generation.
Predicts garbage generation.

### Output
There were two main products: Geographical Visualization of Social Economic Factors and Garbage Generation and Garbage Generation Prediction.
Geographical Visualization of Social Economic Factors and Garbage Generation - Allows the user to understand the impact of social economic factors on garbage generation.
Garbage Generation Prediction - Allows the user to predict different scenarios of waste generation based on social economic factors.

## 🌍 Social Impact Measurement
### Outcome
As an immediate result the Geographical Visualization of Social Economic Factors and Garbage Generation and Garbage Generation Prediction will improve how the Austin City Council applies its spending on projects that aim reduce garbage generation. As a consequence, with less generated garbage, the spending on waste management will reduce.
The main causes identified for waste generation are related with %population living in poverty and population income. Economical policies that incentivize creating of new jobs would definitelly result on an improvement.
Another possible solution would be to create tax incentives for sustainable consumption and waste reduction. For example, income tax reduction according to consumption in Sustainable Businesses (e.g. Green Business Leaders Austin).
Finally, it would be greate to have the values used on the Geographical Visualization Garbage Generation, to share this information with Austin habitants, and provide tax incentives for people living in areas with the less garbage generation.

### Impact Metrics
 • Amount spent on waste generation.
 • Amount spent on Sustainable Businesses
 • Amount saved by Austin habitants on green tax incentives.

### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.

Example:
* *Based on model predictions*: Our model estimates a decrease of 6 minutes of the average dispatch time and a decrease of the average distance of 200 meters
* *Based on proxy products*: Similar studies in other cities show that the dispatch time can be decreased by as much as 13 minutes, depending on the traffic intensity of that city.