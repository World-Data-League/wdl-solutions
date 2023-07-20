# World Data League 2023

## 🎯 Challenge
*Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data*


## Team Name
Random Fourest


## 👥 Authors
* Alina Carvalho
* João Almeida
* José Sousa
* Xavier Silva


## ✨ Introduction
The city of Lisbon has experienced a decline in its population since the early 1980s, having its population drop from 800k to 500k (in 2017). At the same time, there was registered an increase in car usage for daily commuting, and a decrease of the use of public transportation (e.g., journeys that start and end in the city have dropped from 46% to 22%), causing an overload of the road network and parking spaces, and impacting the safety and quality of life of its inhabitants.

The city aims to change this paradigm and promote solutions to reduce dependence on private vehicles, improve the quality of life and health of its citizens, and meet the objectives of the Paris Agreement (namely, carbon neutrality by 2050). The City Council's goals for the 2023-2027 period include boosting soft mobility modes, making public transportation more accessible and affordable, and promoting an integrated, connected, and accessible multimodal ecosystem.

To achieve these goals, it is important to know the main flows in the inner city, especially during rush hours (7:00 to 10:00 AM and 05:00 to 08:00 PM).
Using data representing the devices entering and leaving the connections with the metropolitan area, and representing the mobile devices in the territory, this challenge was designed to acquire a deeper understanding of the flows generated between squares and with access axes to the city.


## 🔢 Data
The data provided contains eight different datasets related to the city of Lisbon. Set 1 contains information on the number of mobile phones that enter, exit, and remain within a 200m/200m square of the city in a 15-minute interval. This data is collected between September and November 2022. Set 2 provides details on the number of mobile phones entering and leaving the city every 15 minutes through its main 11 entry points. Set 3 contains the coordinates of the centroids of the 200m/200m squares. Set 4 gives information on the 11 points of entry and exit to the city. Set 5 contains data on the road network, used to calculate entry and exists. Set 6 represents the mapping of the road network. Set 8 contains the traffic level data collected from the WAZE platform, and Set 8 provides information on the traffic conditions and restrictions in the city.

Analysing the data, one can find a discrepancy of 2.56% between entries and exits in Lisbon, representing 777,900 terminals, indicating exits from main roads or by boat/plane. On weekends, there are proportionally more people in certain areas, such as the Colombo Shopping Center and Humberto Delgado airport. These datasets are incredibly useful for anyone studying Lisbon's traffic and mobility patterns, and could be improved by surveying POIs in Lisbon and associating people's movements with their locations and contexts.


## 🧮 Methods and Techniques
The data analysis involved several steps to extract meaningful insights. First, the raw data was processed to achieve a analyzable structure. This involved cleaning and organizing the data into a suitable format that allowed for efficient querying and filtering. Once the data was properly structured, heuristic algorithms were implemented to analyze it and extract meaningful patterns and insights - exploratory data analysis (EDA). This allowed the development of visualizations over the data and a deeper understanding of the data and its issues or anomalies that needed to be addressed.

In addition, Kepler, a geospatial analysis tool, was used to over the provided geographic data to generate visualizations of the traffic evolution over time, helping to identify patterns in the data that were not immediately apparent from tabular data. These visualizations include maps showing the changes in traffic volume at different times of the day, providing insights into traffic patterns in the city.

Due to time-related constraints, our team was not able to implement two ideas: the first one would be creating a predictive model that associates events with patterns, and predicts the impact of these events in the N hours before and after they occur. The model input would be the state of the city grid and streets, before and after the events (or only the time after, if the event does not allow the time before); the output would have a similar structure. The second idea was to integrate Kepler into a tool that provides smoother real-time visualizations.


## 💡 Main Insights
Addressing this problem, several findings were identified. The data has missing or corrupted readings, making it difficult to clean. For example, on September 19, there was a significant unexplained increase in the statistical counters of the data. Also, the data shows that there are more people entering than leaving when looking at the main road axes. Also, on November 1st between 6 pm and 2 am, there were changes in the Beato area without any correlation with any justifiable event.

It was possible to detect that the number of people in the city reaches its maximum around noon, decreasing after 3:30 pm and reaching the minimum between 4 and 5 am. The increase in the number of people (morning-hours) occurs at a higher speed, indicating a higher concentration per unit of time, and in the afternoon, the number of people disperses more over time.

Weekend attendance is about half of the weekday attendance, with a pattern of increase and decrease similar to week days. Football matches have a significant impact on the areas surrounding the stadiums, with Lumiar being affected by matches at Alvalade and São Domingos de Benfica by Benfica games.

The Web Summit had an impact on the Parque das Nações area, but there was not a significant change in the surrounding areas. Some areas have more traffic during the week, such as Picoas, Cais do Sodré, Colombo, Airport, and Parque das Nações, while others have more occupancy on weekends, such as the Praça do Comércio area, Cais do Sodré, Elevador Santa Justa, and Colombo Shopping Center. The areas and hours with the highest entrances, exits, and occupancy are, thus, pretty identifiable.

## 🛠️ Product

### Definition
Our solution contains two products, including a Jupyter notebook dashboard featuring multiple visualizations and information key points, and a Kepler dashboard displaying traffic conditions over time.


### Users
Three types of users could benefit from this solution:
+ Politicians responsible for managing and administering the city can have access to information that allows them to optimize the management of public transportation and city infrastructure; 
+ People impacted by traffic could have insights about how the traffic flows in the city and use this information to support their traffic choices;
+ Business people could understand in a better way how people move in the city and make thoughtful decisions about new businesses and employment opportunities.


### Activities
* Provide charts and graphs displaying the data in a way that was easy to interpret, understand, and extract meaningful insights. 
* A tool with dynamic visualizations of the traffic evolution over time, including maps showing the changes in traffic volume at different times of the day.


### Output
The Jupyter Notebook dashboard includes exploratory data analysis and visualizations of traffic, points of interest, and mobile device data in the city.
The dashboard provides insights into the relationships and patterns between the data sources.
![Jupyter Notebook Dashboard](https://imgur.com/f38uLMN.png)

The Kepler dashboard allows the visualization of traffic conditions over time in the city. 
Users can interact with the map, filter by specific locations or time periods, and analyze the data.
![Kepler Dashboard](https://imgur.com/jX4IcPg.png)


### Scalability
Given the current state of the solution, designing for scalability is not particularly relevant since there is no final product or model. The current tool only serves the purpose of allowing single users to access visualizations and information, and understand the data in a better way.


## 🌍 Social Impact Measurement
### Outcome
The current state contains a set of visualizations. However, in the future, there are plans to develop a model that can predict how events on certain POIs affect mobility and infrastructure on the surrounding area, after and before its occurrence. 
This information would help politicians identify problematic areas and gain a better understanding of the city's infrastructure. With this, it would be possible to improve the infrastructure and reduce the number of problems in the long run.


### Impact Metrics
The outcomes could be measured by the impact of an event or point of interest (POI), according to the influx of people. To do this, two methods would be used:
+ Counting the number of people at the POI and in the surrounding area before and after the event - this method involves using the data regarding the number of people at the POI and in the surrounding area before and after the event to determine the change in traffic. By doing this, we can assess the impact of the event on the local area in both space and time.
+ Measuring the duration of abnormal occupancy of a location - this method involves analyzing how long a location is occupied by people in relation to its normal occupancy time. This method can provide insights into the event's impact on specific locations and help us understand which areas are affected the most.


### Impact Measurement
Based on the insights obtained and our ideas, we estimate the following impact:
+ The solution would be capable of predicting the impacts of a specific event in terms of time and space at a particular point of interest.
+ This information could aid in understanding the necessity of improving public transportation routes.
+ It would also help recognize the need to improve certain roads/infrastructures.
+ Additionally, this information could lead to a reconsideration of the use of alternative transportation systems.