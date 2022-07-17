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
*UrbanAI: Predict Waste Production for its Reduction*

## 👥 Authors
Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.

* Lukas Mölschl
* Ivan Vrkic
* Manuel Bürgler

## ✨ Introduction 
Provide a contextualization of the problem, together with an estimation of its size using real numbers and references.

The chosen challenges focuses on **Garbage** in **Austin, TX**.
With the ongoing environmental challenges, it becomes clear that a circular economy and recycling will be even more important in the future. 

Where Europe, especially Germany & Austria have already gone great lengths in recycling in the early 70s, [Japan](https://earth.org/japan-waste-management/) being super restrictive on waste and [Sweden](https://www.blueoceanstrategy.com/blog/turning-waste-energy-sweden-recycling-revolution/) accomplishing that only 1% of their waste is being sent to landfills, the "recycling trend" lacks behind in the US. Especially very fast growing cities, such as Austin, have to manage high volumes of garbage (over 500 million pounds in 2020) and need to adjust their waste policies not only to have a positive environmental impact but also to be able to handle those waste streams in the future in a reliable manner. 
Austin, TX is located in the center of Texas and is to be said to become the new "Silicon Valley". This is mostly due to its openness and tech community. Austin’s waste strategy however does not reflect these trends as more than half (~ 300 mio pounds) of the total garbage still goes to the TDS landfill and is not recycled to our knowledge. 
We want to give an insight on the development of various waste streams over time and simulate further developments.


## 🔢 Data
Explain what data you used (both provided by WDL and external) and improvements you suggest to those datasets. Explain how those improvements would lead to a better solution.

**Waste collection data**

- [**Waste Collection & Diversion Report (daily)**](https://data.austintexas.gov/Utilities-and-City-Services/Waste-Collection-Diversion-Report-daily-/mbnu-4wq9)

    > Improvements in the dataset could be made by a better historical stringent classification of waste streams such as we have done. Additionally, we found various false and missing values and outliers. Those issues should be tackled on field level where the data is collected. Additionally, the data does not seem to be updated and lacks complete data in the last months. 

**Population Data**

For population data we are merging the official estimations on federal an city level:

- [Austin Demographics](https://www.austintexas.gov/sites/default/files/files/Planning/Demographics/population_history_pub.pdf)

- [Federal Census](https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/cities/SUB-EST2020_48.csv)
    
    > Improvements can be definitely made here in the data retrieval process as it is quite complex for such standard data. To make things easier, we decided to host a [prepared dataset](https://gist.githubusercontent.com/lumoe/f0c1589d1f9cf22101b00a26ac60aef0/raw/0da3101f929de60c9972f302736eaf365b10a282/csv) on GitHub. 

**Geo Data**

For geospatial analysis we use three datasets

- [Garbage Routes](https://data.austintexas.gov/Locations-and-Maps/Garbage-Routes/azhh-4hg8)
    > Represents a map of garbage routes for the City of Austin. Improvements could be made if a single shapefile for all waste route types would be available. 

- [2020 Census Redistricting Data 5 County Austin MSA - Tracts](https://data.austintexas.gov/dataset/2020-Census-Redistricting-Data-5-County-Austin-MSA/quyr-6u5e)
    > Provides a listing of census redistricting data for 5 Austin Counties by tracts. As the dataset described above is missing geoJSON geometries, all the required geometries were extracted from

- [Tract Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2020.html)


## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.

For this dataset we focused heavily on EDA. Doing so we tried to draw meaningful graphs in the first hand. Based on those insights we were able to further understand the data and come up with additional questions. We therefore used `plotly` a lot to generate those figures. 

For timeseries forecasting we used `prophet` in a out-of-the box approach. Additional steps to improve our results were done in resampling (D), outlier removal (.95 quantile) and putting seasonality effects of US holidays into consideration. Prediction is calculated for 10Y on a daily basis. We calculated the running mean on weekly, monthly and yearly basis although we only plot the weekly and yearly one. 


For our geospatial analysis we used `h3` [from Uber](https://github.com/uber/h3). This allowed us to tackle problems with different shape boundaries and geometries in an easy and fast forward way. H3's strength lays in creating a hierarchical geospatial indexing and unifying data layers based on a hexagonal shapes approach.
We used this technique to check the correlation between population and waste production in a geospatial dimension. 


## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.

While the overall environmental harmful `GARBAGE COLLECTION` stream is slightly declining, `RECYCLING` is expected to stay constant. A positive development is the predicted increase in `ORGANICS` as materials in this waste stream are most easily handled and environmental friendly. The decline in `OTHER` as well as `SWEEPING` indicates a better sorting of waste streams and can also be seen as a positive effect. 

A negativ development is currently expected in the category `BULK`. This was not expected by us in the first hand but is explainable given recent trends in ever shortening consumer cycles in furniture and appliances due to e.g. IKEA and cheap chinese electrical hardware imports. 

An interesting side note is how clearly the winter holiday season stands out in terms of seasonality effects. This really indicates the need for some awareness campaigns in those times of the year. 

Overall, we were able to forecast our defined garbage streams with a certain amount of confidence that those simulated developments really reflect the real world. 

Additionally, using the waste scheduling dataset, we have proved that the points map to the garbage routes almost perfectly. Furthermore, using unified spatial analysis we have proved a strong indication between the population density and the amount of waste produced. Moreover, the data indicates a higher frequency of pickups in densely populated areas.




## 🛠️ Product
### Definition
Define in **one sentence** what product(s) could be built out of the code you produced.

> Garbage stream dashboard to measure the effects of changes in garbage collection strategies. 

### Users

Describe who would be the users of your product and for what purpose would they use it.
- `City Planners` - To plan needed landfill space, garbage truck loads, waste stream developments etc.
- `Decision maker` - To react to trends and developments in certain waste streams and plan awareness campaigns to achieve long term goals. Also incentivizing of different waste stream types could be planned and measured with such product.
- `Authorities` - To detect unnatural waste streams indicating illegal waste disposal activities.

### Activities
Describe what features your product has.
Example:

* Predicts the future waste streams per category based on historical timeseries data
* Shows developments on maps 

### Output
Describe what the product outputs to the users and how it does that. You can add mockups and/or visualisations.
If the outputs are your immediate results, describe your long-term results. What do you want your product to achieve? What ''good'' are you creating?

The product shows graphs with predicted developments in waste streams enabling the Users to easily interact with the data and extract information in an explorative manner. This should in the first place create awareness and make changes in policies etc. trackable and observable by decision makers. 


## 🌍 Social Impact Measurement
### Outcome
If the outputs are your immediate results, describe your long-term results. What do you want your product to achieve? What ''good'' are you creating?

Our long-term results show that even though Austin is on a good way in some parts of its waste management other waste stream categories must be further optimized. We want our insights to provide hard-fact data on which streams have to be worked on and if certain e.g. awareness campaigns have the expected impact. Overall, `RECYLCING` as well as `ORGANIC` waste levels have to be further increased in relation to the overall waste amount.

### Impact Metrics
From the outcome, define **2 to 4 metrics** that measure if you are achieving that outcome or not.

* Total Amount of `RECYCLING` & ` ORGANIC ` waste. 
* Relation of `RECYCLING` & `ORGANIC` to total waste. 
* Measurement of problematic `BULK` waste.


### Impact Measurement

Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.
Based on our model predictions we see a strong incline in `ORGANIC` waste but also an incline in `BULK` waste. While the first development is rather positive, the second one should be tackled in the very near future. We guess that with an awareness campaign and the steps recommended in the analysis such as establishing secondhand markets and increasing the recycling for goods that already have a market value this level could be at least kept in todays area. 

Alternatively, when looking into Japan, a great reduction in waste may be only achievable with very high taxation on certain non-recyclable and nonorganic waste streams. It is expected, that the waste streams `ORGANIC` and `RECYLCING` would increase significantly as customers will become price sensitive at a certain point and be more aware of their waste separation in the first place.
