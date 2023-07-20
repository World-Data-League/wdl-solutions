# World Data League 2023

## 🎯 Challenge
Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data


## Team Name
The Bayes Bunch

## 👥 Authors
* Samantha Hakes
* Mitra Ganeson
* Zhen-Yen Chan
* Stuart McGibbon
* Roisin Holmes


## ✨ Introduction
The intensification of private vehicle usage and significant decrease in public transport usage in Lisbon over the recent years has hindered the city's prospects to ensure convergence with the goals of the Paris Agreement, namely carbon neutrality, by 2050. (https://www.statista.com/statistics/452097/portugal-number-of-cars-per-1000-inhabitants/)

Our work is oriented towards analysing traffic data within Lisbon and utilising this to enhance understanding of traffic movement. This will create opportunities for improvement in the flow of people throughout Lisbon, and could be applied to other areas which also wish to better realise the impacts of traffic flow. 

The intended outcome of this project is:
- a better understanding and visualization of how people use traffic within a specified grid of Lisbon 
- a model that can predict the future impact, using information about the existing transport infrastructure, and 
- identification of potential interventions which can improve the commuting experience of people in Lisbon, favouring sustainable modes of mobility.

Our model was able to predict an indicative view of the number of traffic jams in Lisbon over time, outperforming naive benchmarks used in analysis. 

## 🔢 Data
We used 4 datasources in this project. These are listed below alongside their sources:
1. Mobile device data, source: WDL challenge brief
2. Grid data, source: WDL challenge brief
3. Bus data, source: https://transitfeeds.com/p/carris/1000
4. Waze traffic jam data, source: WDL challenge brief

Our choice of data was motivated by our goal of understanding the existing infrastructure of Lisbon and how the movement of transport is impacted by it. To simplify the problem, and given the good source of data, we focused on buses as a representation of the public transport infrastructure. 

For our analysis, we were interested in November data only due to the changes in the Waze data structure month on month (given that we would ultimately be building a forecasting model). This also helped reduce the amount of data we were handling, which was causing performance issues when carrying out analysis/modelling. 

The information above was used to analyse some key metrics:
- The flow of mobile phone users through a grid cell
- The ‘jam level' in a given grid cell 
- The number of jams in a given grid cell

Suggested improvements: There should be availability of individual user data, this would allow us to model flow more accurately.


## 🧮 Methods and Techniques
The datasets were loaded, cleaned and transformed. Features were engineered for use in modelling:
- We utilised existing geospatial data in Datasets 2, 3, and 4 to create geometry columns for easier spatial analysis, the grid centroid points were padded to create grid cell polygons.
- We matched the polygon of each recorded jam to the grid polygons.
- We indexed the data by date-time (rounded to 15 minute intervals to match the mobile data) and grid ID (corresponding to the centroids in the mobile data). This allowed metrics to be plotted for each 200mx200m grid cell over time.
- We matched recorded bus stops to each grid cell (for every 15 minute period).

Additional metrics were created based on the data from the datasets above:
- Flow, derived from mobile device data, as the movement within grid cells in Lisbon
- Jam level, derived from traffic jam data, as the intensity of traffic jams within grid cells 
- Number of Jams, lifted straight from the traffic data.

As we were attempting to predict these metrics on future days, we benchmarked a number of time-series models (using the features and metrics defined above). These included:
-Naive benchmarks (Last Value Repeating & Last Cycle Repeating)
-A neural network based on a single input time step (Using tensorflow Dense layers)
-A recurrent neural network using the whole history of the training data (Using tensorflow LSTM layers)

Two label types were used. One a net value for the entirety of Lisbon and the other a multi-label approach (grid cell level).


## 💡 Main Insights

We were able to predict the overall number of jams (in Lisbon) over time, with the best performance coming from an approach using only the label and derived time features. This outperformed the benchmarks listed above. Below is an example of the predictions made by this model:

[Forecast](https://github.com/StuartJMc/wdl_bayes_bunch_resources/blob/main/lstm_test_forecast.png)

The other approaches (using bus data as features) showed lower performance than both this approach and the ‘Last Cycle Repeated’ benchmark. Benchmark results are listed below:


| Model | Loss (MSE) | Metric (MAE) |
|---------|----------|---------|
|Baseline_Last|1.27|0.76|
|Baseline_Repeat|0.42 | 0.35|,
|No_Bus_LSTM |0.25| 0.32|
|No_Bus_Dense|0.42|0.43|
|Bus_LSTM|0.31|0.36|
|Bus_Dense |0.29|0.3|
|LSMT_bus_multilabel|0.70| 0.53|

The high performance of the ‘Last Cycle Repeated’ benchmark emphasizes the cyclical nature of the traffic impact (mainly due to rush hour), but does indicate some benefit in using an ML approach over simply analysing past performance.

While the bus data didn’t improve performance, we have demonstrated an approach to use public transport data as part of traffic forecasting. With further public transport information and more granular movement data, we could continue to add to our ‘picture’ of Lisbon and find relationships that will help predict traffic impact.

We also attempted to forecast at a more local level (using a multi-label approach). However, this proved less successful, in part due to the sparsity of our metrics when split across multiple grid cells.


## 🛠️ Product

### Definition
We see the outcome of our modelling as key in helping urban planners predict movement. As the model is using transport infrastructure to predict future traffic impact, the model can be used to score the effectiveness of potential public transport plans (as part of a larger optimization approach). Answering questions such as… ‘What would happen if the bus stopped more frequently?’ or ‘Would this new route help ease congestion in the city center?’.
Therefore, the model could be utilised in an online tool, where users could interact with the different route configurations to understand how changing inputs could impact flow throughout an area. Or simply view expected traffic issues in an area and make plans to ease it.


### Users
Urban planning professionals would interact with the tool in order to test out ideas for city improvements and changes they may be interested in making.


### Activities
- Predict area of high traffic impact
- Predict what changes in the geographic spread of population will have on movement
- Predict what impact changes public transport options would entail
- Predict what areas traffic enforcement/calming could be applied
- Predict the effects of increasing flow to a certain area (ie building a new centre for working)


### Output
We envision an online portal, showing the desired area, along with functionality to ‘test’ different plans for change. By using this tool, users with no technical experience can reap the benefits of predictive modelling, without having to delve into modelling themselves. This will visualise for the user the benefits of a given scenario, and provide important evidence when considering whether to proceed with designs for pilots and POCs.


### Scalability
- In order to reasonably predict flow through an area, having access to high quality data is imperative. This data should be granular in area, and also in activity (for example number of users, number of cars etc). If data is unavailable, it could be created using information from public transport networks, road network cameras (ANPR), along with many other places. 
- There would have to be some investment in improving the modelling used. With initial funding, an MVP product could be created which focuses on one or two use cases only. This could then be expanded up to a full tool with additional functionality.
- As we are using a deep learning approach, the model should be easily scalable to include richer inputs. This could include satellite images of the area.
- Throughout development, model outputs would have to be twinned with real evidence for changes, using documented example cases to feedback into workings . 


## 🌍 Social Impact Measurement
This section will help to guide you on how to measure the impact of your product. Make sure that measurement is thoroughly quantitative, even if you need to estimate some of the numbers.
### Outcome
- Increased mobility throughout the area
- Easier prediction of where ‘sticking points’ in the road network may arise
- Better planning of new infrastructure and building developments
- Reduce GHG emissions from vehicular transport


### Impact Metrics
- Average time people stuck in traffic jams
- Average commuting time
- GHG Emissions


### Impact Measurement
Our tool could be used to highlight routes for public transport establishment. Using a bus rather than a car would reduce CO2e emissions by 20% per passenger km (2022 DEFRA emission factor: https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2022, assuming 1.45 passengers per car:https://www.eea.europa.eu/data-and-maps/indicators/occupancy-rates-of-passenger-vehicles/occupancy-rates-of-passenger-vehicles)

Through use of traffic flow measures such as SCOOT-controlled traffic lights, time in traffic jams could be reduced by up to 13%. Our model could help predict areas of effectiveness for traffic measures: (https://tfl.gov.uk/info-for/media/press-releases/2018/june/delivering-the-next-generation-of-urban-traffic-management)

Using our modelling, we can currently predict the number of traffic jams 10.5% more accurately than using a naive baseline. This could allow for better resource allocation leading to reduced time in traffic and incentivised alternative methods of transport.
