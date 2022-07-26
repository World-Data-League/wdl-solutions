# World Data League 2022

## 🎯 Challenge
Predict Waste Production for its Reduction

Challenge Provider: UrbanAI

## 👥 Authors
Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.

* Juan Diego Arango
* Melissa Montes Martin
* Santiago Cardona Urrea
* Irune Lansorena Sanchez
* David Gamba


## ✨ Introduction

Waste is a significant **global** issue. This problem is getting worse as the global population rise. We just need to have a look into some reported figures (according to the World Bank, in 2016 cities generated 2.01 billion tons of solid waste, meaning around 0.74 kg/day!). To address this, cities need better programs for both waste processing and waste management.

We apply data analysis to aid such processes. In particular the city of Austin, TX has an ambitious [Zero Waste Program](https://www.austintexas.gov/zerowaste)[1] and within this program one major component is the optimization of the curbside recollection.

![Yearly curbside collection shares](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/total_waste_vs_curbside.png)

GeoNEAS team aims to help the strategic planning towards an Austin that recycles more. To this end, we developed a ML based Intelligent Decision Support System (IDSS) in order to support policy making processes by predicting futures trends on waste generation at particular areas in the city(census tracts)[2] and clustering these areas by socioeconomic factors which could help policy makers isolate what makes an area more effective at recycling or what kind of social context have a group of zones that might be susceptible to the same policies. Those policies could be from different nature (e.g, waste management educational and awareness campaigns, improving recycling guidelines and composting programs, desirable behavioral factors understanding... etc). Our product is the start of all these possibilities.

## 🔢 Data

Our product uses two big groups of datasets: one group to *forecast* waste trends of curbside collection and other which contains socioeconomic information. Here we detail both groups.

For waste prediction at the census tract level:

- [Austin waste daily report](https://data.austintexas.gov/Utilities-and-City-Services/Waste-Collection-Diversion-Report-daily-/mbnu-4wq9) Main source of data that logs the waste collected across many routes for the city. **Time Coverage:** 2004-2021. While the data is quite detailed, we noticed that at the individual route level the data might have gaps. One possible improvement of the data would be more accurate registration. This will allow our solution to estimate better future waste trends.

- [Garbage: Polygon routes of waste collection](https://data.austintexas.gov/Locations-and-Maps/Garbage-Routes/azhh-4hg8). To map the location of collected garbage. This data was specified only for one county. Having access to geospatial information for the rest of the city, our model could give estimates for more areas.

- [Recycling polygon routes of collection](https://data.austintexas.gov/api/geospatial/7tin-f8k2?method=export&format=GeoJSON) Same as above but registers routes for recycling collection.

On the second group, we focused on data to contextualize the zones/regions of Austin by multiple socioeconomic factors.

- [Census Socioeconomic Data](https://data.austintexas.gov/Health-and-Community-Services/Education-Access-and-Quality-Map/j7a9-vw9w): Socioeconomic information and geographic boundaries from the US census. We also used this data to form a basemap of the tracts and overlay the routes on top to find how much waste per route corresponds to each tract.

- [Vulnerability Data]( https://data.austintexas.gov/Health-and-Community-Services/Socioeconomic-Status-of-CDC-Social-Vulnerability-I/jnp3-n7ij): Similar to the socioeconomic data but includes information about vulnerable populations.

![Tracts Map](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/tracts_map.png)

Additional datasources that may improve our solution are datasets with past&current public policies plus KPIs. These may help correlate policies to already found interesting socioeconomical cluster factors and waste trends.

## 🧮 Methods and Techniques

### Spatial data preprocessing
We choose the census tract as out unit for analysis since it allows correlating waste with socioeconomic factors at small scales. To bring all data sources to the tract level, we performed spatial processing on the collection maps finding the attribution of waste to each tract.

Then, we performed analysis on waste patterns per tract to determine next steps for forecasts.

### Waste trend forecast
We started analyzing the monthly series of waste. Most tracts showed noisy patterns and autocorrelation analysis[3] suggested no strong seasonalities. Thus we used Prophet[4], a model that we could tune to model changes in trend while handling missing observations and that could give confidence intervals.

![Sample modeled trend and confidence intervals for a single tract series](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/prophet_model.png)

We also established a validation scheme and tuned the model such that we could guarantee certain performance metrics while mitigating overfitting[5]. then we used the ideal parameters to train forecasts models of total waste and percentage of recycling for all tracts.

### Cluster analysis
We used k-means[6] to cluster tracts by their socioeconomic attributes with the intention of generating 'cohorts' of tracts such that it could be easier for policy makers to perform analysis of waste and devise possible campaigns considering contextually similar tracts.

To validate the number of clusters, we balanced the results of a silhouette score analysis with intuition about what numbers policy makers could expect

### Joint analysis of waste and clusters
Here we used the clusters as cohorts and compared waste patterns. We also calculated how much recycling could be improved if all tracts in the cluster reached the performance of recycling of the best representative in each cluster.

## 💡 Main Insights

During initial analyses of waste data, we noticed a clear temporal evolution in the waste vs recycling patterns per tract and that it could make sense to focus on forecasting two KPIs: total waste and, percentage of recycling of that waste per tract(recycling share).

![Temporal evolution for a sample of tracts](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/temporal_evolution_recycling_share.png)

Then, after analyzing the tract's monthly waste patterns, we discovered that while the series tended to be quite noisy, they also had marked trends. We also discovered that the series lacked strong seasonal patterns. This shift our forecasting analysis to trend forecast.

![Sample series of total waste and recycling share](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/waste_and_recycling_share_samples.png)

On the clustering analysis, we found that the clusters had a strong spatial correlation and that they represented indeed distinct populations. For example, one of the clusters represented poor underdeveloped and minority prevalent tracts. Which also happen to be close spatially to each other.

By joining the information of clusters and waste forecasts for all tracts, we first calculated what could be the **improvement in future recycling percentage(and volume)** if all tracts reached the same recycling percentage of the best representative for their respective cohort. This number was projected as the **optimal of 17.5M lb of monthly recycling waste**, the predicted volume without thinking of this goal would have been 7.5M lb monthly, ~50% less. We believe that policy makers could use this optimized scenario as a possible strong goal to move forward during the medium term.

Even within the same cohort, not all tracts are in the same situation regarding waste trends. This is why we also added a quadrant analysis based on projected waste and recycling share, finding the set of tracts that produce more waste and recycle less(than the average). These have potential as low hanging fruits for improving recycling policy at high volume impact.

![Quadrant Analysis, total projected waste vs recycling share](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/quadrant_analysis_total_volume_vs_recycling_share.png)

As we could geo-reference all this information, we mapped projected total waste numbers, recycling shares(percentages) and also trends of these numbers(up/down). Such maps could be a valuable resource for policy makers to quickly understand areas of interest and urgency for waste management and policies.

## 🛠️ Product
### Definition
A machine learning based Intelligent Decision Support System(IDSS) for policy decision making process regarding waste trends.

Define in **one sentence** what product(s) could be built out of the code you produced.

Example: A dashboard that assists in traffic control

### Users
The end user(s) of the solution will be city managers and policy makers aiming to find the most effective way in developing sustainable strategies. They will be able to use the tool and visualizations for data driven decisions; not only for forecasting waste trends but also for *understanding* the socioeconomic context of the regions they analyze.

Describe who would be the users of your product and for what purpose would they use it.
Example: Traffic controllers use the dashboard during their work to better plan where to dispatch resources

### Activities
Main features of our product:

- Maps the waste generation in zones that can also be analyzed by their socioeconomic factors.
- *Forecasts* waste and recycling per zone within a tactical-strategical horizontal time
- Generates cohorts of zones based on socioeconomic factors which simplify further waste trend analyses/
- Provide macro-level KPIS and target waste metrics based on the performance of the zones that best perform regarding recycling
- Allows identification of problematic regions due to the rapid increase of waste generation and low recycling performance.

### Output

We offer an app where the information regarding socio-economical variables and their relations to trends of waste and recycling is clearly presented to the user. [A demo dashboard that serves this purpose](https://waste-s1-7kvbiho2qa-uc.a.run.app/).

![Screenshot of the demo](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/demo_screenshot.png)

The user can select a cluster and observe both average waste trends and socieoconomic context of the cluster tracts

![Screenshot of the demo](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/context_info.png)

Multiple maps add spatial information of waste trends at the tract level. The user can then decide where to focus

![Trend Maps](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/demo_maps.png)

Individual yearly trend forecast is shown and can be filtered to understand the waste trend of particular tracts of interest.
![Trends per fips](https://storage.googleapis.com/geoneas-bucket/waste-s1/images/trends_demo.png)

The analysis considering the contextual socioeconomic information could be replicated in many tracts and expanded upon by policy makers.


## 🌍 Social Impact Measurement
### Outcome

Policy makers will be able to use the tool and visualizations for data driven decisions; not only for waste prediction but also for *understanding* where to focus educational resources and educational campaigns that ultimately improve recycling efforts. They will be able to gauge desirable scenarios in which strategies were effective within some socioeconomic clusters and then possibly replicate those scenarios across different regions with similar socioeconomic descriptors. In the end, this will contribute to a cleaner, more sustainable city.


### Impact Metrics

* Curbside recycling share across tracts
* Curbside total waste share across tracts
* Trend percentage change of recycling share and total waste

### Impact Measurement

With our product, the best representative of all the city's zones can be identified with its socioeconomic descriptors. By applying similar waste strategies on other zones with similar parameters we estimate the following city-wide KPI: 9.63 million lb reduction in incinerated waste(MSW), translating in a considerable reduction of emissions (4368.094523 tonnes of waste reduction --> approx. an interval of 3057 - 7426 tonnes of carbon dioxide (CO2) emissions reduction [7,8,9]).


REFERENCES

[1] Austin Zero Waste Strategic Plan: https://www.austintexas.gov/sites/default/files/files/Trash_and_Recycling/Zero_Waste_Plan_-_full_version_-_Council_Adopted_w-resolution.pdf

[2] Neighborhood Typology (semantic IFPS) https://www.austintexas.gov/edims/document.cfm?id=299918

[3] Autocorrelation Function: https://towardsdatascience.com/a-step-by-step-guide-to-calculating-autocorrelation-and-partial-autocorrelation-8c4342b784e8

[4] Prophet: https://machinelearningmastery.com/time-series-forecasting-with-prophet-in-python/

[5] Cerqueira, V., Torgo, L., Mozetič, I. (2020). Evaluating time series forecasting models: an empirical study on performance estimation methods. Machine Learning, 109(11), 1997–2028. https://doi.org/10.1007/S10994-020-05910-7

[6] K-Means: https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1

[7] City Efforts to Reduce Carbon Emissions: https://www.austintexas.gov/sites/default/files/files/Auditor/Audit_Reports/City_Efforts_to_Reduce_Carbon_Emissions__Jan_2020_.pdf

[8] Net-zero community-wide greenhouse gases by 2040: https://www.austintexas.gov/department/climate-change

[9] Pollution inventory reporting – incineration activities guidance note: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/923125/Pollution-inventory-reporting-incineration-activities-guidance-note.pdf
