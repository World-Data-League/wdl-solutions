# World Data League 2022

## 🎯 Challenge
Predicting the flow of people for public transportation improvements.

## Team Name
Padrão dos Descobrimentos

## 👥 Authors
Alexandra Serras

## ✨ Introduction (250 words max)
Provide a contextualization of the problem, together with an estimation of its size using real numbers and references.

Increasing air quality is of the utmost urgency since air pollution affects communities in low-, middle-, and high-income countries. In 2016, it was estimated that this major environmental health issue [caused 4.2 million premature deaths](https://www.who.int/news-room/fact-sheets/detail/ambient-%28outdoor%29-air-quality-and-health) worldwide per year. This mortality rate is mostly due to exposure to fine particulate matter (PM2.5), which can cause cardiovascular and respiratory diseases, as well as cancers.

One of the main culprits for this is car usage. In 2013, transportation contributed to more than half of the carbon dioxide emitted into our air. According to Tomtom’s traffic index, if a person were to drive every day during rush hours (typical commuter time) instead of non rush hours that person would spend an extra 4 whole days inside of their car. 

The solution to these problems was already created: public transportation. It was found that when compared to cars, public transportation produces 95% less carbon dioxide and 92% fewer volatile organic compounds. But this isn’t the only way public transportation wins over cars, researchers from the university of east anglia found that people who used their car to go to work were 13 per cent more likely to feel unable to concentrate.

This solution aims to analyse and propose routes to be looked at by the stakeholders. By providing insight into which routes are under-utilised the stakeholders can make informed decisions to help public transportation be widely used. If the changes are successful we can expect an increase in public transportation usage in the short term, and in the long term a decrease in the number of traffic jams and increase in air quality.


## 🔢 Data (250 words max)
Explain what data you used (both provided by WDL and external) and improvements you suggest to those datasets. Explain how those improvements would lead to a better solution.
For this analysis we used the following WDL provided datasets:
- MOD validations
- GTFS datasets both for bus and metro
- Flow of people between municipalities

And the following outside datasets:
- Weather data provided by meteostat
- Holiday dates provided by https://pypi.org/project/holidays/

Regarding improvements, our suggestion would be to not use 2020 as a baseline for the analysis since it was such an unusual and non representative year due to covid, many people that did use public transportation before would rather use a car just to be safe during that time. Also, in order to have a good monthly forecasting model, we would benefit from having more than a year of samples (12 samples where we had to remove 2 due to being lockdown months).

## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.

Since the data provided was created every 2 hours, we converted the grain to a daily and monthly basis and then added date and weather features to allow for further context to our analysis.

The analysis explored stationarity, moving averages (MA) and lagged values of the time series we were provided with. 
- Stationarity:  we applied the Augmented Dickey-Fuller to confirm the data was stationary;
- Moving averages: from our analysis we concluded we would benefit from having the moving average of two days as an input to the model.
- Lagged values: we concluded we would benefit from having one lagged feature. 

We used correlation matrices to verify which component affects which - from this analysis, where we correlated with moving averages, weather, dates and lagged features, we saw that it would be beneficial to use MA of two days as they were the ones with the highest correlation. 

For modeling the time series, we dropped duplicates and missing values and applied a linear regression mode. We used the estimator to forecast the daily and monthly inflow and outflow from surrounding municipalities to Porto and vice versa.

We then cross checked the real inflow/outflow data with the validation data provided and identified which zones used public transportation the least. With that zone we then identified the routes that either started or went through it and either ended or went through Porto, the routes with the lowest ratio of validations to real inflow would be flagged for review.


## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.
An analysis of the inflow and outflow of people from the Porto municipality shows a drop in months that were in either full lockdown (march - may) or in partial lockdown (november onwards).
By cross checking the validation data with the flow data we also found that the analysis needs to be repeated in more relevant years given that some of the routes in the output were routes to the airports, and as such only realy underutilized during covid times.
By analysing the validation data we can also notice that the winter season is the one that sees the most public transportation usage, followed by summer, autumn and finally spring.
Since the dataset provided was from 2020, we can see that the amount of validations increase during the morning from 6 to 8 and in the afternoon from 16 to 18. This is due to the fact that our dataset only really possesses the pattern of commuters, since leisure travelling hit a record low in that year. In order to verify if this trend continues we must analyse the dataset but for either 2021, or ideally, 2022.


## 🛠️ Product
### Definition
Define in **one sentence** what product(s) could be built out of the code you produced.
A tool to alert to low utilisation routes that need to be reviewed.

### Users
Describe who would be the users of your product and for what purpose would they use it.

The users of the tool would be the public office, which would use it to find out which routes it should focus on in order to increase public transportation usage.


### Activities
Describe what features your product has.

- Predicts future inflow and outflow in the Porto municipality
- Suggests routes that need reviewing

### Output
Describe what the product outputs to the users and how it does that. You can add mockups and/or visualisations.

The product outputs the routes that have to be looked at by the public office, it also shows a graph to check the occupation rates of each route per zone. 

## 🌍 Social Impact Measurement
### Outcome
If the outputs are your immediate results, describe your long-term results. What do you want your product to achieve? What ''good'' are you creating?

In the long term our aim is to increase the usage of public transportation by changing the routes that are used the least into more convenient routes for the passengers. As a consequence of the success we have we also aim to decrease the actual number of cars on the road, the number of traffic jams and increase the air quality.

### Impact Metrics
From the outcome, define **2 to 4 metrics** that measure if you are achieving that outcome or not.

- Average usage of each route/zone
- Number of cars on the road in the Porto municipality
- Number of traffic jams
- Average time spent in a traffic jam


### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.

Using the model output we can increase the efficiency of low performing routes and promote the usage of public transportation.
In the long term we can decrease the air pollution created by cars since people will prefer taking public transportation.
