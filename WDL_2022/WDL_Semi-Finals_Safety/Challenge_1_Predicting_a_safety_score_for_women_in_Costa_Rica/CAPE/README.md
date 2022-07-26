\# World Data League 2022



\## 🎯 Challenge



Predicting a safety score for women in Costa Rica



\## 👥 Authors

\* Akshay Punjabi

\* Pablo Izquierdo Ayala



\## ✨ Introduction (250 words max)



We live in a world where violence towards women is on the rise, and this is especially true for the country of Costa Rica in South America.



Already in the first 10 months of 2021, Costa Rican authorities reported a number of 4047 victims of direct violence, encompasing sexual abuse, psychological abuse, physical abuse, negligency and other misstreatments. All of this without taking into account other types of crimes. 11 femicides were also reported in these 10 months.



Another issue is fear. There may be many more cases, but victims are afraid of speaking up and reporting them



This is a trend that must be stopped. 



Being able to accurately predict areas of conflict and applying precise efforts is a must in order to enforce positive action.



\## 🔢 Data (250 words max)



We will be using different types of data.



After looking at the data provided by WDL, we focus on the crimes dataset. This is by far the most complete dataset and with the finest level of granularity. It contains district level information of the crimes, the type of crimes, type of victims, etc.



We also created several shape files of Costa Rica to create meaningful plots. With these shape files we can create a map over which we can plot our results and ease the visual understanding.



Aside from this, we also used data on the population by district and we extracted topological and local information of the different districts using the osmnx library





\## 🧮 Methods and Techniques (250 words max)



Our whole analysis is done in Python. We used some popular Python libraries (numpy, pandas, matplotlib, plotlib, sklearn, xgboost, stata). 



We created a meaningful analysis, carefully sharing our thought process along the way. 



Regarding methods and algorithms:

\-  We performed a seasonal decomposition of the time series to understand trends and seasonality. 

\-  We analyzed the stationarity by performing a Dickey-Fuller test. 

\-  We analyzed the daily distribution of the data.

\-  We performed a thorough feature engineering process that included computing Mutual Information, Permutation Importance, PCA and SHAP

\-  We used osmnx to better understand the local and topological features of each of the districts. This lead to interesting results.

\-  We added different range lags to convert the timeseries to improve the predictive performance of our models

\-  We built two multiregressors, one for the general dataset and one using only female victims and compared both of them using RMSE as our metric.





\## 💡 Main Insights (300 words max)



There are several main findings we would like to share:



Crime pattern theory suggests that rather than actively searching for crime opportunities in locations that are unfamiliar, offenders commit offenses in areas that are already known to them.



Also, from a crime pattern theory perspective, more crime would be expected to occur on (or near to) more “central” (to use the terminology of graph theory) street segments.



This might be a bit counterintuitive at first but it seemed to be especially true when looking at our dataset. 



First, most of the victims are pedestrians. This implies that the distribution of the streets in a district should play a crucial role in the prediction of crimes.



This proved to be true. We analyzed said distribution and districts with straighter roads tend to have a higher number of crimes. 



One might think that having less straight roads could lead to more escape routes for the criminals. However, having straight roads can also lead to easier victim targeting and faster escape paths when using motorized vehicles or bikes. It also implies that there are more crossroads.



Another aspect we found interesting is the timeframe in which these crimes are mostly committed, from 6pm to 9pm. One could expect most crimes to be committed at night, but this does not seem to be the case.



Finally, it was surprising to note that there is no correlation between population and number of crimes. This was a strong assumption we had at the beginning of our challenge.





\## 🛠️ Product

\### Definition



In depth and comprehensive analysis of crime in the canton of San José and several regression models.



\### Users



Police authorities to predict where they must center their efforts.

Women that can identify which areas to avoid.



\### Activities



We created a comprehensive analysis of crime in San José. This includes which areas to avoid, which types of roads to avoid and which times are the most conflictive .



All of this information can be used to improve the road layout and create a safer system for women.



\### Output



Meaningful visualizations and future predictions.



\## 🌍 Social Impact Measurement

\### Outcome



Improving the understanding of crime in San José by providing an in-depth analysis of the main areas of crime and the topology of these areas and our regression models can have a direct impact on the safety of women, as it can help allocate resources better, create safer pathways and also alert and inform the population.



\### Impact Metrics



- Prediction of number of crimes per region on any basis (daily, monthly, trimetral and yearly)
- Entropy of the street distribution, which can be used to improve the way in which new roads are created or position police effectively.



\### Impact Measurement



Impact can be measured in many different ways. One could be following our same approach in a year and checking how the model performs. This can then be compared to previous years and used to improve the model towards the future.



Another idea is understanding the types of crimes. Computing the amount of crimes of type “assault” can be a way of measuring impact.



Finally, our models can be used to allocate police forces effectively which can be an indirect impact measurement (such as number of crimes prevented)