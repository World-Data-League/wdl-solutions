# World Data League 2022

## 🎯 Challenge
*Predicting the flow of people for public transportation improvements*

## 👥 Authors
* Antonio Oliveira
* Any Pereira
* Hayanne Oliveira
* Israel Souza
* Martim Chaves

## ✨ Introduction
Porto is a wonderful city, with many fantastic qualities. Traffic, however, is not one of them. Porto has a worse traffic index when compared to larger cities, such as Lisbon, Madrid, and Barcelona.
The reasons for this are many, but, essentially, this means that public transportation has to be very efficient, serving the population's needs well.
Thus, we aimed to study the flow of people, in order to improve the public transports.

## 🔢 Data
The data that was used was the Validation data on rail public transport (validation per stop per hour). This data was deemed quite complete and easy to work with.
For the future, as always, it would be fantastic to reduce the number of missing values, as that is always detrimental to training a model.
Using made up numbers can decrease the performance, as it's essentially corrupting the dataset. However, discard several entries if there are missing values means a small dataset which is also not good.

## 🧮 Methods and Techniques
Initially, exploratory data analysis (EDA) was done to better understand the structure of the data, i.e. if there were any trends. Further EDA should've been carried out, such as decomposing the signal into its several components.
This should be done to ensure that the signal is stationary, however, time was scarce for that. After EDA, some very simple feature engineering was done to replace the missing values.
Finally, an LSTM was used to model the data, obtaining decent results.

## 💡 Main Insights
From this study, it is quite clear that there is a very strong weakly seasonality associated with the subway in Porto. We think that this seasonality allows for the creation of decent models, that could perhaps aid in determining the necessary size of the available fleet (in terms of subway trains or carriages).
The data that was used allowed us to visualize the impact that the pandemic had on the usage of public transports. Perhaps with more people adopting remote or hybrid work environments, traffic could also be reduced.

## 🛠️ Product
### Definition
A dashboard that assists in determining the size of the available subway fleet in each line.

### Users
People responsible for the number of subway trains would use this tool to better determine how many subway trains, or how many subway carriages should be available to the public at a given moment.

### Activities
* Predicts the number of validations at a given subway station
* Calculates the expected increase of validations in relation with previous hours

### Output
The product would determine how many more subway trains or carriages are needed at each subway station.
By predicting the expected increase of validations at a station, and how the fleet that was available in the past hours was serving the population, the product would use that information to determine the number of subway trains required.
Other things would have to be taken into account, such as the cost and time required to add/remove carriages to subways (future work).

## 🌍 Social Impact Measurement
### Outcome
The long term result is to create a more attractive subway service that better serves the population, decreasing the necessity for personal transport.
Another outcome would be reducing the amount of energy used (considering that the amount of carriages could be better adapted to the current needs).

### Impact Metrics
* Overall number of subway users
* Number of efficiently used subway trains (given a subway train, without too much room to spare while containing everyone that needed that transport)
* Reduced air pollution in the municipality (less cars - personal transport)

### Impact Measurement
To estimate the impact, it would first be necessary to know how efficient the subway trains currently are (considering the number of carriages that they use and the number of people that they transport).
Assuming, from personal experience, that at peak hours subways are quite full, and at other times, there is a lot of room available, an increase of at least 5% in term os efficiency seems conservatively appropriate.