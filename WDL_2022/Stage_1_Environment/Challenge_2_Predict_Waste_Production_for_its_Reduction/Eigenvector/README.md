# World Data League 2022

## 🎯 Challenge

## **Predict Waste Production for its Reduction**

## 👥 Authors

- Daniel Tan
- Benjamin Chew
- Kenneth Goh

## ✨ Introduction (250 words max)

According to the World Bank, in 2016 cities generated 2.01 billion tons of solid waste. Per person, this is around 0.74 kg/day. With the rapid growth of cities, this number is only expected to increase. In the city of Austin, average waste is around 0.66 kg/day. As cities are growing, it is urgent that optimization processes for waste processing and more targeted public education on waste management and separation.

## 🔢 Data (250 words max)

We used the Daily Waste Collection Report for Austin Texas from 2003 to 2021, Austin Weather Data from 2013 to 2017, Austin Pollutant Report from 2014 to 2021, and Austin Median Household Income from 2005 to 2020.

For the weather and pollutant datasets, we feel that the granularity of the data could be improved upon to the extent where we can optimize routes for waste collection hourly and reduce incidents of pollutant spills across the city. By pre-empting changes in weather (e.g. temperature) at a finer scale, we could reduce loads due to animal deaths or debris by taking action beforehand. Furthermore, having more years of historical data available would have been useful for the accuracy of predictions.

For the income dataset, we feel that having geospatial data points associated with zones across Austin would have allowed us to suggest policies that could specifically target zones with increased pollutants and waste and decreased instances of recycling as we observed some relationships between load weights and recycling trends.

## 🧮 Methods and Techniques (250 words max)

Gradient boosting with K-fold Cross Validation across windows.
The largest negative mean absolute error we have obtained is **_-139789.946_**, with a window of **180 days**.

## 💡 Main Insights (300 words max)

We observe that recycling is positively correlated with income. This is interesting as previous studies has shown a negative correlation between income and recycling (for example, see "Household Knowledge, Attitudes and Practices in Solid Waste Segregation and Recycling: The Case of Urban Kampala" by Margaret Banga of Makerere University in May 2011). In essence, higher income households can afford to pay for waste collection services, and thus do not have to bother with separating waste into recyclable and non-recyclable waste beforehand.

Perhaps the positive correlation comes from the fact that higher income households spend more proportionately on waste that can be recycled e.g. plastic bottles from bottled mineral water. Moreover, as earlier observed, Texas's Zero Waste Strategic Plan from 2008-2009 could have encouraged such households to proactively segregate their waste into recyclable and non-recyclable waste.

## 🛠️ Product

### Definition

A dashboard which predicts the next day's load weight, shows the trends of various load types happening in the previous day across the city.

### Users

The city planners can use the data and trends to guide their decisions on possible relocation of collection sites. The load weight can be used to guide the planning of the number of collection trucks required.

### Activities

- Predicts the next day's load weight.

### Output

At the moment, our product outputs a prediction of the garbage load weight for the coming days to optimize the dispatch of garbage trucks. In the future, by combining the location and pollutant types on the map, we will be able to suggest the fastest route for cleanup vehicles to offload pollutants at appropriate dropoff sites.

## 🌍 Social Impact Measurement

### Outcome

We hope to be able to improve urban planning with the load prediction and load weight /load type prediction, which will help to decide which type of waste commonly appear together and their sites can be co-located.

### Impact Metrics

- Average Distance traveled by Garbage Truck
- Average Sum spent on Trucks / Pounds of Waste

### Impact Measurement

We can extend the model to predict sub-categories of trash. More accurate forecasts of each trash category can lead to more efficient planning of waste disposal resources for each trash category. For instance, if recycled trash (e.g. “Recycling - Single Stream” category) requires specialized facilities for processing, then accurate forecasts of such trash can help the authorities plan adequate constructions of such specialized facilities in the future. Additionally, some dropoff sites also experience low and sporadic trash loads which may suggest that some consolidation of sites could be implemented in the future to optimize waste processing.
