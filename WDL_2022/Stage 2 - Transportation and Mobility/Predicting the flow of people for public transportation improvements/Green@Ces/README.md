# World Data League 2022

## 🎯 Challenge
Predicting the flow of people for public transportation improvements

## 👥 Authors
Catarina Bento
Cátia Correia
José Luís Mourão
Lúcia Moreira
Pedro Fernandes

## ✨ Introduction (250 words max)

Porto tops the charts in the Iberian Peninsula for the worst traffic situation. The main reasons pointed are: 1- access to the city restricted to three bridges and two main highway merge points; 2- difficulty in urban planning due to Porto being an old city built on a hill; and 3- a public transport system that might be unable to meet community demands. 

With reason nr. 3 in mind, in the present challenge Green@CES team addressed the inter-municipality mobility of citizens at city of Porto in a attempt to help the Municipality to create a better public transport infrastructure. The goals are divided in 3 main tasks: a) develop a predictive model for the daily and monthly forecast of citizen's inter-municipality mobility; b) develop a framework for detecting the most probably crowded inter-municipality public transportation routes as well as the most probably underutilized in the upcoming days or months based on the forecast model; and c) create a user-friendly interface allowing the visualization of the inter-municipality public transport routes that might need intervention in the forseeing days and months as well as the forecasts for the global citizen inter-municipality mobility and the citizen inter-municipality mobility in the public transportation system.


## 🔢 Data (250 words max)

The primary data used to analyze the problem was provided by WDL, containing the hourly entries (and exits when available) validations for each route (bus and metro) at the public transportation system, the hourly Origin-Destination (OD) matrices for global citizen mobility from/to Porto from NOS telecom operator, such information available for the whole year of 2020, together with information about the Porto’s Metro and Public Bus System (STCP). 

We have complemented this data with Covid19 public restriction levels applied in some periods during 2020. Moreover, we have also complemented our dataset with weather information (rainny days aftect public transportation utilization by citizens), national and local holidays and temporal data such as season, weekend and etc. information. Also big events information such as futebol games occuring in Porto´s major stadiums, rock festivals and main municipal festivities would have been added if all massive gatherings have not been forbidden in Portugal due to Covid19 in 2020. This way, the framework herein presented might need to be used with caution when extrapolated for what we call, let´s say, a more "normal" year.


## 🧮 Methods and Techniques (250 words max)

We conducted exploratory analysis to get initial insights on the most inter-municipality global movements from Porto and to Porto.
We have also analyzed the global inter-municipality commuting as a time series using a LightGBM-based model for forecast the daily and monthly citizens expected movement, and, for each forecast point, an integrated SHAP analysis is also delivered aiming to decisors/users infer what are the main drivers found by the model that might explain such population movement, e.g. rainny day, holiday, full covid restrictions, and etc. We have used the exactly same approach for the daily and monthly forecasts of the public transportation inter-municipality commuting.

Our framework compared the forecast of daily and month citizen´s commuting to Porto with the provided capacity of the public transportation system. We were able to calculate the number of people using public transportations divided by the public transportations maximum capacity for each period, together with coverage, i.e,  public transportat maximum capacity divided by the total mobility flow. And finally, the expected usage of the public transport system by dividing the people using public transportations with the total mobility flow.

The User Interface (UI) provided was developed in PBI and allows for end users and decisors to inspect what are the forecasts (as well as historical data) for people commuting globably and using public transports up to the following 7 days or in the next month. In the UI we can also see public transport expected usage in comparsion to both transport maximum capacity and the expected flow mobility, and the coverage of the public transport system in comparison to all the citizens commuting to Porto by transport provider. A color coded process is also used as an alert system.


## 💡 Main Insights (300 words max)

We found out that most commuters arriving and leaving to Porto in 2020 came from Vila Nova de Gaia followed by Matosinhos, with all the 4 neighboring municipalities on the top 4. Moreover, the OD Vila Nova de Gaia-Porto pair acounts for more that 20 milion people traveling in each way in 2020 alone. The same figures are observed for the OD Matosinhos-Porto pair. 

Our forcaste model took into account for instance, that 1- higher commuting occurs on week days and lower commuting levels were observed for the months at starting of pandemic or when higher restrictions were applied; 2- COVID restrictions highly affect commuting, most commuting to Porto occurs in Summer or in Winter season before pandemic; 3- precipitation seems to affect commuting rates in the opposite direction and 4- COVID starting highly affected public transport usage, while STCP and Metro usage are balanced.

Globally, public tarnsport offered capacity is enough for the amount of people commuting to Porto but some specific lines might be more crowded in some hours of the day, but an hourly analysis was not performed. This way, a better redistribution of the transports routes offered might be considered.



## 🛠️ Product
### Definition

User interface that classifies the inter-municipality public transport routes that need the most intervention in the forseeing days and months as well as the forecasts for the global citizen inter-municipality mobility and the citizen inter-municipality mobility in the public transportation system in the following days and months.

### Users

Decision makers can use model forecasts for the operational and strategic management of the public transportation fleet but also take decisions in order to improve inter-municipality mobility constrains affecting citizens.
For example, increase/decrease metro and bus frequencies (better management of respective drivers working hours and fleet management by decreasing green house gas emissions and wasteless fuel consumption), guide traffic controlers to the more critical traffic zones when bigher citizen movements are expected (or attribute other type of tasks to such traffic controllers when smaller movements are expected), decrease/increse traffic lights red/green times in critical street merging points.

Additionally, if more detailed and complete information from route mobility validations is available our framework can be easily adapted for the citizens also to use the user interface for taking decisions regarding which transport system should they use. For instance, a citizen can take an informed decision regarding if a certain route in a certain hour can be used in detriment of a private transportation option thus improving the goal of achieving a more sustainable city.

### Activities

Classifies the most probably crowed public transport routes in Porto Municipality for a given day and month. Predicts the number of commuting citizens arriving at Porto using private and public transports for a given day and month. Predicts the number of commuting citizens arriving at Porto using only public transports for a given day and month.

### Output

A UI with the main forecasts and historical data as well, indicating the number of citizens commuting to Porto together with public transport expected usage on the same period.



## 🌍 Social Impact Measurement

We expect that our product leads to a better public transportation management by decision makers at Porto Municipality. Citizens commuting will be offered a higher quality public transport management suitable for each situation taking into account the expected number citizen commuting by public transports. Further this can improve public transport usage by decreasing gas hous emissions when citizens use their private transports.


### Impact Metrics

Comparison of transport usage levels before and after deployment of the dashboard and decisions taken based on the information provided:

•	Number of days with acceptable/unacceptable public transport offerings.
•	Percentage of public transport usage after deployment of our product.


### Impact Measurement

Our intention is to help with a more user-friendly public transport management system aiming a more targeted offer when is most needed (through the use of our final product, the dashboard).