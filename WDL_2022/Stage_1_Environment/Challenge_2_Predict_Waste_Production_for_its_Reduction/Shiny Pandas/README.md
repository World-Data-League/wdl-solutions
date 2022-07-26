
# World Data League 2022

## 🎯 Challenge

Predict Waste Production for its Reduction

## 👥 Authors

- Imre Boda
- Zsolt Kegyes-Brassai
- Peter Michaletzky

## ✨ Introduction

Back in 2011 the city of Austin, TX committed to a strategic goal of reaching Zero Waste production by 2040 in their [Zero Waste Master Plan](https://www.austintexas.gov/sites/default/files/files/Trash_and_Recycling/MasterPlan_Final_12.30.pdf), forecasting 75% recycling ratio by 2020, while garbage collection statistics show a stagnating 24% ratio since 2012.
Population in the city is expected to grow from 1.00 million to 1.28 million by 2040, possibly further aggravating the "garbage situation", together with the increasing consumption per capita which also has the potential of contributing to more waste generated per inhabitant.
Careful planning of recycling plant and landfill (where non-recycled waste is buried), and also transport vehicle capacity and personnel is the interest from the city budget point of view.
Our approach was two-fold:

1. We wanted to give a tool to waste management planning that can forecast waste volume on the short run, i.e. down to weekly basis, allowing the precise planning of transport capacity per waste collection zone
2. Investigate long-term trends by taking into account social, economic, cultural factors in the "production" of garbage

## 🔢 Data

Data sources:

1. [Waste Collection & Diversion Report (daily)](https://data.austintexas.gov/resource/mbnu-4wq9) - daily report providing waste collection information
2. [Tax on retail consumption and Consumer price index](https://data.texas.gov/resource/karz-jr5v) - monthly dataset covering entire state of Texas; we could not find similar data with regards to Austin
3. [Garbage collection route boundaries](https://data.austintexas.gov/api/geospatial/azhh-4hg8) - map data for the garbage collection routes
4. [Recycle collection route boundaries](https://data.austintexas.gov/api/geospatial/7tin-f8k2)- map data for the recycling collection routes
5. [Zipcodes of Austin](https://www.zipdatamaps.com/zipcodes-austin-tx)
6. [Statistics of U.S. Businesses](https://api.census.gov/data/2017/zbp?get=EMP,EMPSZES,EMPSZES_LABEL,PAYANN,ESTAB&for=zipcode:78613) - stats for business establishments with paid employees and enterprise size

We found several problems with the data, just to name a few:

-  Recording of an event in dataset `1.` there are obvious errors around the dates when garbage collection occurred vs. when it was reported in the system.

-  There are missing garbage load values in dataset `1.` And there has been really erroneous outliers in our target variable (unexplainable spikes in waste weight).

-  Route names between datasets `1.` - `3.` and `1.` - `4.` were inconsistent.
    Obviously there has been several route re-naming, route merges, etc. along the years, but various sources were completely inconsistent (location information may not be available in a reliable manner).

Related to data, surprisingly we found very few historical social and economic data on zip level.

Improvement proposals:

1. the data source owner could publish the full route history, so one can trace back exact route boundaries for historical data
2. the dataset `1.` could contain the route map information already when the data is collected.

## 🧮 Methods and Techniques

### Long-term causality analysis

Time Series analysis to establish causal relationship between one or more explanatory variables and target variable: the volume of garbage and recycled waste.
We assumed we can find explanatory variables on ZIP code level, we looked for social, economical, etc. data.
Ever changing garbage collection routes does not seem ideal for finding socio-economical statistics.
We assigned garbage routes to zip codes based on a number of principles, the most important ones are these: 70% of the zip code is covered by collection routes; routes are split on zip area boundaries by the ratio of intersection.
We found a showstopper issue with regards to our zip code level data: actually we found none in the huge Census database or other free public databases that had decent quality samples for all Austin zips for the entire analysis period.

### Short-term forecast

The short term analysis aims at providing the Garbage Management department with a tool in order to help organizing cost efficient and effective garbage collection.
Predicting the expected garbage volume on a collection route could be possible from the previous few weeks' data on the same and a few neighbouring routes; also taking into account seasonality.
We used time embedding to create our dataset, this way we transform Time Series problem to "ordinary" ML problem.
The reason why can do this is that we believe that only a few preceding lag data correlates with the target variable.
We used XGBoost for modelling and predicting.

## 💡 Main Insights

We built ML model to predict next week waste based on historical data, and we trained on two different time intervals: 2018 - 2020 and 2012 - 2020, and the evaluation was done in both cases on 2021H1 data.
In both periods we followed two approaches: one was to build model on individual garbage routes (small area followed by the truck at one collection), the other was to build model on 5 larger Austin areas.

The mean absolute error for larger area models is about 20% of the mean target value.
Having huge variation in data, this might be considerable.

We faced two major difficulties:

- We have major data quality concerns: there are considerably number of extreme values and other major inconsistencies in the data.

- Scarcity of useable features in the resources listed in the Challenge description, other Austin city open data and external datasets.
  Therefore, our explanatory variables were barely more than historical and spatial garbage and recycle information.
  Having better understanding on some local specifics (e.g. festivals, major construction works, garbage collection campaigns, etc.) could be valuable information greatly improving the model's accuracy.

We also worked on doing a Long Term Time Series analysis connecting waste data to social and economical etc. data on zip level for identifying relevant causal relationships.

Apart from data quality, we made several other observations:

- Recycling to garbage ratio has been stagnating the past years, and this combined with growing population and retail consumption forecast will pose a challenge to reach zero waste goal.

- In 2020 there were over 5000 cases when the same garbage route had to be re-visited outside the normal service day.
  Part of this might be due to suboptimal truck allocation.

The latter is the problem we wanted to solve with our Short Term ML model.

## 🛠️ Product

### Definition

A garbage and recycling load predictor system that would indicate to the Waste Management department if and when coverage of a particular route needs to be increased (more vehicles) or decreased (less vehicles would suffice), reducing cost when possible, or ensuring all garbage is picked up properly.

### Users

The [Austin Resource Recovery](https://www.austintexas.gov/department/austin-resource-recovery/services) capacity planning staff can organize the garbage collection in a cost efficient and effective way.

### Activities

Based on historical data, our model predicts the garbage/recycle collection volume for the following week(s).

### Output

The predicted garbage/recycle volume forecast is presented.
By using additional data (like actual transport), this can be enhanced in future to suggest the optimal number of trucks required in next week(s).

## 🌍 Social Impact Measurement

### Outcome

With our short term model to enable more efficient garbage collection, by optimizing the number of trucks needed on a given week to the given area.

### Impact Metrics

- Number of extra collection days saved (i.e. no need to re-send trucks because planned number were not enough to transport quantity)

- Reduced number of surplus allocated trucks (i.e. more cars allocated to a given area than necessary)

### Impact Measurement

As we have no information on the actual transport, only on the transported quantity (i.e. we know the collected waste weight but not the number of allocated trucks), we could estimate the saved extra days of collection for the same area on the same week. 

In 2020 there has been **5220** repeated garbage collection on the same route on the same week. We do not know the exact reason for that, we assume that portion of this is due to wrongly estimated needed transport capacity. So we can say that Austin Waste management could prevent less than 5220 repeated collection with our predictive tool. 

Worth noting that avoiding repeated collection is not a real saving yet, as these collections must take place anyhow. However, with better allocation there is no need to re-schedule extra collections on the same routes for other dates of the week.
How this is translated to money, this would require deeper understanding on Austin's waste management.
