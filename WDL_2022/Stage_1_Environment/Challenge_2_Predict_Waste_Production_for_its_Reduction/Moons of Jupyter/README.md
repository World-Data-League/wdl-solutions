# World Data League 2022

## 🎯 Challenge
Predict waste production for its reduction

## 👥 Authors
Ajit Gupta
Cristian Castro 
Gabrijela Juresic
Tejas Choudekar

## ✨ Introduction (250 words max)
Waste generation is a worldwide problem in the face of global warming and the ecosystems preservation. The reduction of the amount of waste generation helps not only managing the disposal of waste in landfills (direct negative impact), but also the indirect CO2 emissions to the atmosphere that the waste management produces (indirect negative impact). In 2016, for example, the solid waste generated around the world accounted to around 0.74 Kg/day according to the World Bank (https://datatopics.worldbank.org/what-a-waste/). This number is expected to reach 3.4 billion tonnes in total by 2050. In this context, this challenge takes place in Austin, Texas (USA). Its goal is to find trends in future waste production to its reduction using historical data. Since 2005 and aiming to become a zero-waste city in 2040, Austin city has committed several efforts towards this goal, which includes: the Urban Environmental Accords (2005), the Zero Waste Strategic Plan (2009) and the Austin Resource Recovery Master Plan (2011) (https://www.epa.gov/transforming-waste-tool/zero-waste-case-study-austin). These consecutive efforts look forward to the reducing of waste going to landfills by waste diversion in association with the residents and the industries of Austin. Aligned with this roadmap, the following challenge provides a model that predicts trends in waste production up to year 2025. This model may be used not only to directly quantify the amount of waste production in Austin, but also to assess the success of the above-mentioned programs. This model contributs in Austin’s path of waste reduction, towards a cleaner environment promoted by public policies.

## 🔢 Data (250 words max)
The model was built based on the “Data Waste Collection Report for Austin Texas”, wich was a dataset provided by WDL. The model built was based on a time series model, which was only trained on this dataset.

As a Team, we believe that this model can be fairly improved by adding more information, that because of time we couldn’t study properly enough. In our opinion, the improvements may consider:
1.	The data does not show where this waste was generated (households or industries for example). This additional information could help us in further optimizing the waste management by dividing the resources as per the source of generation.
2.	There are estimators that we believe can be correlated with the amount of waste production, as our understanding of the problem is. These estimators to be included in future improvements are:
a.	Austin population (per year)
b.	Austin median income per capita (per year)
c.	Season of the year (Summer, winter, autumn and spring).



## 🧮 Methods and Techniques (250 words max)
We used time series forecasting using Prophet model (https://facebook.github.io/prophet/docs/quick_start.html). During exploration of the data we observed that the data is divided into 22 categories but on further analysis we understood that some categories can be merged into one and some categories were not making much impact on the total collection of data so such categories are then discarded. Below are the final categories and our model's performance on these categories:
Note: Model's performance is based on MAPE (mean absolute percentage error) score 
1. Sweeping
2. Recycling (Consisting of single stream recycling and previous types of recycling befor 2011)
3. Reusable (Consisting of Bulk and Tires)
4. Garbage Collection 
5. Compostable (Consisting of Brush, Organics, Yard trimming and Dead Animal)

## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.
Most of the garbage production happened either in Holiday seasons i.e between October and Decenber or at the start of spring during months of April-June. In comparision to other type of waste, Garbage percentage is higher. 
TDS - Texas Disposal System, is the main Dropoff site which contributes more than 50% of waste disposal alone, to reach the zero-waste-goal by 2040, we need to divert this to MRF - Material Recovery Facility.
Some more Interesting fact: 1) Trends in waste production is depended on seasonality ( like months, holidays etc)
                            2) Sweeping Load Type have ~81% missing values.

## 🛠️ Product
### Definition
Define in **one sentence** what product(s) could be built out of the code you produced.
A dashboard that assists in waste collection, we can forecast how much waste of different types are likely to be generated and optimize the collection accordingly. 

### Users
Describe who would be the users of your product and for what purpose would they use it.
Waste management authorities use the dashboard during their work to better plan where,when and which category of waste to collect

### Activities
Describe what features your product has.
1. Predicts the time of collecting waste per category
2. Predicts the weight of each type of waste that needs to be collected and processed

### Output
Describe what the product outputs to the users and how it does that. You can add mockups and/or visualisations.
It outputs the weight of every category. It does so based on the historical data that has been collected. It also suggests the time line to collect each category, for example some categories of waste can be collected bi-weekly and some once every month.

## 🌍 Social Impact Measurement
### Outcome
If the outputs are your immediate results, describe your long-term results. What do you want your product to achieve? What ''good'' are you creating?
The output of our model will help in optimising the trips waste collection trucks takes, this will reduce the pollution caused by those trucks. Our model will also help in optimising the waste processing, since it tells us the predicted weight of waste that will be produced in that particular week.

### Impact Metrics
From the outcome, define **2 to 4 metrics** that measure if you are achieving that outcome or not.
Mean absolute percentage error of every category will tell us how good our model is working. The lower this value the better. 
An upward increasing trend for each category

### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.
Our model estimates the increase in waste production by December 2025, as per our forecast each category of waste will see,
1) 1.18 % increase in Garbage Collection
2) 15 % increase in Compostable
3) 116 % increase in Reusable
4) 442 % increase in Sweeping 
5) 800 % increase in Reusable.