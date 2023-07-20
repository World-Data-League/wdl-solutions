# Executive Summary - World Data League 2023

## 🎯 Challenge
Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data

## Team: JKL & Frank
## 👥 Authors
* Joydeep Chatterjee
* Kate Crawford
* Lara Strachan
* Frank Novak

## ✨ Introduction

This document discusses the problem of traffic congestion during morning and afternoon rush hours at entry and exit points in the City of Lisbon. This is a significant issue that affects many urban areas worldwide, with estimates suggesting that congestion costs country economies significant amounts of money annually and increases CO2 emissions. To address this problem, city planners and transportation agencies need to identify areas where they can implement soft mobility initiatives, such as bike lanes or pedestrian walkways. Our product provides a model and visualizations to assist in these efforts.

## 🔢 Data (250 words max)

The product utilizes the given data sources, including mobile device data from September through November 2022. Geospatial data for roads and entry and exit points were also used. 

In addition, several groupings were made based on time. The day of the week and hour of the day were the main focus of this research. It is noted that the given data has the potential for even more granularity, as each event was recorded in 15-minute intervals. 

Anomalies such as floods or holidays could have impacted the data. Features were also created to measure non-roaming devices within the grid, with the goal of removing potential tourist cell data from the inputs.

While this data provided a robust foundation for the project, there are several potential areas for improvement. For example, incorporating more recent data could help ensure that the project's findings are up-to-date. Adding data on public transportation could provide an even more comprehensive view of mobility patterns in each grid area. 

Refining the filtering process used to identify non-tourist cells could help ensure that the project's conclusions are as accurate as possible. By taking these steps, the product could potentially improve the quality of its data and the insights they are able to draw from it.

## 🧮 Methods and Techniques (250 words max)

Since our main objective with modeling was to be able to predict the volume of terminals in a given grid at a specific time, we decided to use a regression model that would have high predictive accuracy - XGBoost. Our features were grid ID, relative change in non-roaming terminals, hour of the day, and day of the week (as a one-hot-encoded categorical feature). Using Grid Search, the the best hyperparameters were identified and we achieved a nearly 52% improvement in the mean squared error over baseline. The most impactful feature was 'relative change in non-roaming terminals', followed by grid ID and hour of the day, suggesting that both location and time is meaningful for traffic congestion.

## 💡 Main Insights (300 words max)

As the months progress from September through November, there are fewer roaming terminals across the entire grid. At the same time, there are increased overall terminals. This indicates that there are fewer foreign travelers or tourists in the later months of the year. 

The relative change in terminals by the hour also indicated that people stayed in one are of the grid for longer if it was September versus November.

As the day progresses by the hour, the greatest rate of change in the number of terminals in happens during the morning rush hour. The peak of the total number of terminals occurs between 0900 and 1100 and remains within a 20 terminal difference until after 1800 for all months used int his product.

## 🛠️ Product

Based on assumptions from device movement, our product predicts the total number of people at entry and exit points throughout the day.

### Definition

A model that estimates the total number of terminals within a grid area at a given time.

### Users

The user of the product could be city planners and local transportation agencies. City planners may use this information to determine where to deploy alternative mobility structures other than road access to the city center.

One initiative that we were inspired by was ‘Park & Rides’ in places like Denver, Colorado USA. The mapping provided could guide where city planners may decide to place parking areas or docking stations for other forms of mobility. 

Transportation agencies may develop dashboards with the predictive features of our product. The provided heatmaps may also benefit these efforts.

### Activities

Our product Features a model that predicts the total number of terminals within a given grid space.

### Output

Interactive map of total terminals moving across the grid.

### Scalability

Our product serves as the foundation for finding locations to implement soft mobility solutions for areas with high traffic congestion to improve the commute of domestic travelers into the city center.

## 🌍 Social Impact Measurement

### Outcome

To understand the volume of people moving through entry and exit points during morning and afternoon rush hour periods so that locations for alternative methods of mobility could be deployed in high-congestion areas.

### Impact Metrics

From the outcome, the mean squared error was used to determine improvement and performance.

### Impact Measurement

If more time could be allotted, similar studies would have been evaluated to estimate the impact of this product. Based on our model’s predictions, with a 52% reduction in estimation error over baseline of where congestion will be in a grid square at a given hour, we could focus resources and interventions in these locations with higher traffic. By providing resources such as enhanced bus service in ideal locations & times, which is a cost effective intervention, bus ridership could increase by 10% (https://nacto.org/wp-content/uploads/2022/08/MoveThatBus-FINAL.pdf).
"""
