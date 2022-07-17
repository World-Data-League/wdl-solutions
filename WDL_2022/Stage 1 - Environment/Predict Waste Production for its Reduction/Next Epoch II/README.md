# World Data League 2022

## 🎯 Challenge
**Predict Waste Production for its Reduction**

## 👥 Authors
Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.
* Nicholas Sistovaris
* Sai Pravallika Myneni
* Wiem Borchani
* Neha Shaah

## ✨ Introduction (250 words max)
In today’s time, we have pressures to minimize the carbon footprint and other environmental effects caused by their businesses – Waste management and disposal is one of the most important issues for them. In today’s world, waste management and disposal is a big challenge not only for the industries, but also for the communities in general. It is not an issue restricted to any particular region or country, but is a global challenge across countries and continents. The challenge is real as increase in global population and commercial activity is only likely to increase in waste. Globally, various governments and businesses are working to find innovative ways to minimize the waste generation as well as to find and implement effective and efficient ways of waste disposal; recycling is one of the effective and widely adopted methods.

Estimation of the waste production is for the successful planning of efficient waste management system, their further sustainable development and optimization.

## 🔢 Data (250 words max)
We started with the Austin garbage collection data that was provided with the challenge. Through over literature survey we found that it would be wise to include weather and air pollution data in our analysis. The pollution data that we have is pm25 numbers while weather data includes information about temperatures, wind and precipation. We also used open street map data for our analysis. It would be great to see the geographic co-ordinates mapped and also include block wise census data to further support our analysis. We have grouped the data for each week as we got to know from locals that major waste management operations happen weekly. Also we focused on the years 2014-2019 (the pre-covid years) for our analysis. We also wanted to understand the impact of holidays on waste generation, we used Holidays python library. 

## 🧮 Methods and Techniques (250 words max)
We started by performing data analysis to understand the given data. 
Data Analysis Steps:
 * We started with understanding how each column is distributed with some descriptive statistics and visulaizations
 * we tried to understand how the garbage collection is per each category of load type as well as for each drop off site
 * Further, we analysed the relation between load type and route type.
 * We tried an alternative of looking on at 2021 data for for route numbers. This is because routes are more likely to change on an annual basis. 
 * Next, we focused on how the waste generated varied by year, month, day and hour
 * Finally we decided do forecast garbage collected on weekly basis after merging the data with holiday data, pollution and weather data
 
For forcasting the weekly waste generated (load weight) we have used the time series analysis and forecasting algorithm ARIMA. We have also tried a few regression techniques, relatively ARIMA performed better based on the evaluation metric Mean Absolute Error. 

## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.
1. From the data, we understood that the largest category of type of waste collected comes under garbage collections followed by recycling
2. The route numbers PW and PH prefer garbage colleection usually going towards TDS lanfill
3. Waste generated does not show any significant trends with respect to weather conditions - temperatures, pressure or precipitation
4. lots of yard trimmings in the spring

## 🛠️ Product
### Definition
A dashboard that assists in forecasting the load weights for various types of garbage across the city of Austin

### Users
Waste managers or garbage collectors use the dashboard when planning a trip to collect garbage from various sites. The truck type can be selected based on the estimated load weight and type of waste. 

### Activities
* Predicts the load weight for a given day at a given site
* Suggests a truck type for garbage collection for a given site

### Output
The product outputs the estimate of the weekly waste generated along with plots to give an idea about the trends in recent times. 

## 🌍 Social Impact Measurement
### Outcome
Estimating quantities of waste produced in a region is critical for designing and operating the waste management system. Understanding maximum waste generated in a city allows managers to estimate required facilities related to waste collection and disposal accurately at the highest demand. 

### Impact Metrics
* Maximum waste generated in a week
* Understanding which category of waste is generated the most (garbage, recycling)
* Most active route number

### Impact Measurement

* Similar study in city of Austin itself in Zero Waste program shows that the diversion rate at the end of fiscal year 2021 was decreased to 41.96%
