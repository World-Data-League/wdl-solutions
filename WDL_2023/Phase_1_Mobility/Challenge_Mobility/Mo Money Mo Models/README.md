# World Data League 2023

## 🎯 Challenge
First Phase!

Determining the mobility flow in the city of Lisbon based on mobile phone data


## Team: Mo Money, Mo Models
## 👥 Authors
* David Raposo
* Duarte Pereira
* Martim Chaves
* Paulo Sousa

## Team Name
Mo Money, Mo Models


## 👥 Authors
* David Raposo
* Duarte Pereira
* Martim Chaves
* Paulo Sousa


## ✨ Introduction (250 words max)

The problem that the CNN-LSTM model is aiming to solve is the issue of overcrowding in public spaces within the city of Lisbon. The growing population in the metropolitan area of Lisbon, which is estimated to be 3,001,000 in 2023 [1], poses a significant challenge for city managers to ensure public safety and comfort. This high population density can lead to overcrowding in public spaces such as public transportation, parks, and shopping centers. Overcrowding can cause discomfort and inconvenience for individuals and, in extreme cases, lead to safety hazards such as stampedes and accidents.

This trend is not limited to the city of Lisbon. According to an Harvard International Review Article [2], the global population is currently rising at a steady rate. Between the years 1800 and 2023, the population of Earth has increased significantly. In 1800, it was estimated that there were around 1 billion inhabitants, and by 1940, this number had risen to 2.3 billion. Over the next three decades, the population continued to grow rapidly, reaching 3.7 billion by 1970. As of 2023, the world's population is approximately 7.8 billion, showing the most significant increase in the Earth's population in the last five decades.

With this in mind, it is vital to provide city managers with tools to detect and prevent overcrowding events.

**References:**

[1] https://www.macrotrends.net/cities/22167/lisbon/population#:~:text=The%20current%20metro%20area%20population,a%200.51%25%20increase%20from%202020. - last accessed 18/04/2023

[2] https://hir.harvard.edu/public-health-and-overpopulation/ - last accessed 18/04/2023



## 🔢 Data (250 words max)

We used the datasets, provided by the WDL, regarding mobile devices.
With this data we created a grid map. For the grid cells where there was a train line or station a new identifier was added. These data were taken from the Lisboa Aberta portal [2].

We also explored climate data briefly - nominally precipitation and temperature - using climatelab to load the ERA5 reanalysis dataset [1], but we could only obtain one value for the entire city per hour, so we did not consider it a priority at the moment.

One of the datasets provided by the WDL that initially looked promising was the traffic conditions. However as this data were not real-time it were not relevant as inputs to the model. In the future it could be used to seek an explanation for certain phenomena observed by the data, or a dataset would have to be created, with time stamps for each 15 minutes, indicating whether or not there was a traffic condition.

In order to improve the quality of the data it would be interesting to standardise the type of files with the available data, as some are in .csv format and others in .xlsx. Also .geojson data has been used.

Finally, we noticed that the data from mobile devices had maxima much higher than the 99th percentile, which indicated that they were erroneous measurements. 

**References:**

[1] https://cds.climate.copernicus.eu/
[2] https://lisboaaberta.cm-lisboa.pt/

## 🧮 Methods and Techniques (250 words max)

For exploratory data analysis (EDA), we checked for missing and duplicate values, which were not found. After that, we checked the consistency of the frequency of the measurements. Next we used tables and histograms to visualize the distribution of the data. We removed possible anomalies by calculating modified z-scores for each, and using an optimal threshold to remove them. We used interpolation to fill the values that were removed. We looked into temporal and spatial understanding of the data, by plotting the grid map and the values of the features over time, creating an animation. From this, we were able to discern more popular zones, and higher intensity hours. We added information of hour, minute, and weekday to each measurement due to this.

The proposed CNN-LSTM architecture joins state-of-the-art deep learning models for image processing (CNN, Convolutional Neural Network) and time series forecasting (LSTM, Long Short-Term Memory). In theory, this model is able to leverage the spatial relationships within the city grid to provide better predictions based on neighbor relations, as well as the temporal dimension for forecasting. However, we encountered some challenges with time constraints in the training that limited performance, since we had to limit the learning rate, epochs, and batch size. We also had to follow a preliminar preprocessing pipeline, as we were performing EDA in parallel. Future work must focus on improving the experimental infrastructure, model architecture, integrating new data, and the preprocessing suggested in the EDA stage.

The transport data have been superimposed on the grid created earlier. For this it was necessary to find out the distance from each of the stations to the centroids of the grid cells. Then this grid was ordered and the cell with the shortest distance was the one most likely to have a station.


## 💡 Main Insights (300 words max).

We found that there were no missing or duplicate values in the data. However, there was some inconsistency regarding the frequency of the measurements. Between the start and end date, there were moments when there was no data for certain 15 minute blocks (unlike what was expected). We also discovered that the max values for each feature were much larger than the 99th percentile, which may indicate that sometimes there may be issues with data collection. Next, we discovered some patterns regarding day of the week, and time of day. As expected, weekdays and rush hour are more associated with a higher flux of people. We also discovered some spatial patterns. There seems to be a large flux of people around the Saldanha roundabout, the Lisbon Airport, and the Avenida Dom João II, next to the Moscavide station.

Our model aimed at predicting the number of persons in a given area x minutes in the future with a resolution of 15 minutes. To accomplish this task, the model ingested information from an amount of time in the past which defined the time window. How far in the future we want to predict was defined by the forecast range. These two parameters can have significant impact on the model performance since they have direct impact on the CNN-LSTM architecture, so it would be of interest to have not one with the best compromise between these parameters, but different models optimized for a given forecast goal.
During the development It was not possible to get the best compromise between these parameters, nor to train the model up until convergence, and do hyperparameter tunning due to optimizing heavy models in tight time constraints, however we still got preliminary insights which lead us to confirm that a greddy method of predicting too far in the future and with too much detail can be infisibly, but can give actianable insights in a reasonable window of time into the future. Predicting averaged conditions for large window of time (eg. the average number of persons in a given are at a rush hour given external conditions such as climate and day of the week) without trying to capture its unsteadiness could also add value, and can be done by post-processing our forecast models’ outputs. The model is expected to improve by receiving additional data to capture the most important predictores of people mobility, such as transports and climate data. 

## 🛠️ Product

Our product aims at providing actianable insights in managing the city traffic by the means of the EDA done, ie. providing insights about past data which can be used to developing strategies to cope with problems caught in the past, our routine can be used at any point of time to analyse past data given that it is in the same format. The other expected use of our product falls in the forecast model, or the multiple ones which can be obtained for specific goals. While the EDA routine will be helpful to long-term strategies, the forecast models are expected to be used to be able to act readily with on-time solutions.


### Definition

A dashboard that assists in public transport planning, or a dashboard that assists in policing by providing analysis on the available data and forecasts.


### Users

The expected user of our product would be:

Decision makers in transport companies, especially metro and rail, can use our dashboard and the forecasts our models provide to decide the human resources deployed for each moment of the day.
City councils can also use the predictions from our models to decide which events to promote in which part of town to promote a more dispersed population and thus a better quality of life for citizens.
The citizens of the city in general can also benefit from our predictions, in order to have a lifestyle more in tune with their personality. They can move to more crowded areas or to quieter areas, as they wish.
Traffic police can also perform better at resolving overcrowding situations preemptively, and ensure citizens’ safety.

### Activities

Predicts the most likely locations for overcrowding situations and would they evolve in time.

### Output

Population density predictions on a map for the next X hours with a selected time resolution (from the available data resolution up to 24 hours averages).

###  Scalability

For this solution to be employed in another environment, we would require it to have similar phone grid history. A expected large step forward would be on providing additional data such as transports and dowscaled climate as inputs to the forecast model, since those would add important events that severely impact peoples mobility which our current model is not aware of. Finally, given enough computationally resources, a larger and more complex model following our pipeline can trained with data from more locations could have more generalization capabilities.

## 🌍 Social Impact Measurement

The actions that the product enables are expected to improve quality of life by reducing the mental stress caused by traffic and constrained transportation options..  

In 2019, municipalities received **€104 million** in total from the State Budget to promote the use of public transport [1]. In 2010,  the Ministry of Internal Administration provided PSP with 655 million euros of budget [2]. Insights providing more efficient ways of acting can bring a more cost-effective managing of the public budget.

**References:**

[1] Portugal: Reducing the costs of daily commuting to
protect the environment and reduce inequalities
ESPN Flash Report 2019/21 (https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwihwpX3hLj-AhXXUqQEHTo2ABgQFnoECBAQAQ&url=https%3A%2F%2Fec.europa.eu%2Fsocial%2FBlobServlet%3FdocId%3D21071%26langId%3Den&usg=AOvVaw2rsoWR1shVW0zJUrbO1wgF - last accessed 18/04/2023)

[2]
https://www.portugalresident.com/police-budgets/ - last accessed 18/04/2023

### Outcome
To predict overcrowding situations and decrease response time so that cities are more secure and provide better quality of life for its citizens.

### Impact Metrics
In regards to the forecast model:
Average Response Time from Transportation Planning
Average Response Time From Police Stations

### Impact Measurement

We hope that our research can help prevent unfortunate accidents caused by overcrowding, such as stampedes [1], by predicting the events before they happen a sufficient amount of time in the future. Other study using ARIMA reached a forecasting of 135 minutes in the future with similar data [2]. More researched is needed to assert if we can reach this goal.

**References:**

[1] Shanghai: dozens killed and injured in stampede at new year celebrations | China | The Guardian - last accessed 18/04/2023

[2] Real-Time Monitoring and Forecast of Active Population Density Using Mobile Phone Data (researchgate.net) - last accessed 18/04/2023