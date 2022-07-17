# World Data League 2022

## 🎯 Challenge
**Predicting a safety score for Women in Costa Rica** by Urbanalytica

## Team Name: DataBased

## 👥 Authors
* André Luís
* Rui Monteiro
* José Diogo Castro

## ✨ Introduction

Violence against women is "any act or conduct, based on gender, which causes death or physical, sexual or psychological harm or suffering to women, whether in the public or the private sphere" (source: [Inter-American Convention on the Prevention, Punishment, and Eradication of Violence against Women](https://www.oas.org/juridico/english/treaties/a-61.html)).

According to the United Nations, the lack of adequate urban infrastructure, policies, and governance models exacerbate gender violence in cities (source: [United Nations Entity for Gender Equality and the Empowerment of Women](https://www.unwomen.org/en/digital-library/publications/2017/10/safe-cities-and-safe-public-spaces-global-results-report)). Thus, addressing the main obstacles women face regarding their right to an inclusive and safe city, becomes a priority.

Urbanalytica, the challenge provider, is worried about the safety of women in Costa Rica. Gender violence in cities, specifically in public spaces, has become an increasingly issue, especially in Latin America.

This is why we, DataBased, should help working on a mapping tool to identify and report cases when women feel like their right to enjoy public spaces is being threatened. To fulfill the goals of this project, we should create a safety index based on the data in Costa Rica, and predict the trend of the safety index per city district by trimester and by year.

The Women's Safety Index we are going to use on this project is mainly based on the crime data from the *costa_rica_crimes_english.csv* file. This is because one of the goals is to predict the safety index by trimester and by year, so we need to use time series data. Thus, the proxy we will use for women security is the total number of crimes against women.

## 🔢 Data

We used two main sources of data. 

The [ZIP file with Costa Rica's data](https://wdl-data.fra1.digitaloceanspaces.com/urbanalytica/urbanalytica_datasets.zip) containing ArcGIS Zoning, Districts, Crimes and Street harassment data. And also the [ZIP file with Google reviews for parks and transit stations in Costa Rica](https://wdl-data.fra1.digitaloceanspaces.com/urbanalytica/google_reviews.zip).

Regarding improvements to the collected data, in our opinion, if more data about street harassment reports was stored, then the *costa_rica_street_harassment_english.csv* file could be used for more analysis. At the moment, there is not much data to use regarding the important issue of harassment (probably because the *Law Against Street Sexual Harassment* was approved in Costa Rica only 2 years ago, and some women still do not know about it).

## 🧮 Methods and Techniques

We started by **Importing** the data and assessing the main characteristics on each source.

Then, we performed an **Exploratory Data Analysis**, where we analysed each of the sources of data. We used barplots to check how San Jose is in terms of public infrastructure, to check each of the San Jose's districts (to understand some of their main socioeconomic characteristics regarding Crime rate, Social Development Index, Population density and Social security), and to check Street Harassment in San Jose. We also checked the crimes in San Jose where women are the victim, using barplots, a table and a stacked bar chart. Finally, Park and Transit Stations Reviews were analyzed with word clouds.

Next, we moved to the **Modelling** stage, where we created the time series (by trimester and by year) for two San Jose districts. These had data for the crimes against women, which was the security proxy we wanted to predict. To do this, we followed a traditional time series approach, starting by checking for stationarity and autocorrelation using the Dickey-Fuller test, and further applying ARIMA models to get the desired forecasts.

To calculate our final Women's Safety Index, we combined the crime forecasts with socioeconomic variables (from the district data).

## 💡 Main Insights

The main insights derived from our analysis were:
- The top-3 districts with the most public areas (per km2) is the same as the one for green areas: Carmen in first, Catedral in second, and Mata Redonda in third. The 3 with the least areas is almost the same as well, with districts like Hospital, Merced, and Pavas.
- Carmen is the district with the lowest population density and the highest crime rate. Hatillo is the most densely populated district and the one with the lowest crime rate. Thus, this might indicate population density is important to understand the districts' crime rates.
- Variables that seem to influence crime against women: time of the day (most crimes happen between 12pm-9pm) and year (2018 and 2019 had many crimes, but from 2020 on they reduced).
- On the word cloud for transit stations we can see words like "terrible", "dangerous" and "unsafe", which indicates these public stations migh be insecure. In the parks word cloud, it seems like the words that represent insecurity are less frequent.
- Many time series (used to predict crimes against women) are Non-Stationary, so we had to apply transformations on the data in order to apply ARIMA models.

## 🛠️ Product
### Definition

A Safety Map depicting our predictions for the Women’s Safety Index in each city district

### Users

Two main users: women living in the city, and the City Council. 

Women would use it to check the safety predictions for each district.

Urbanalytica can try to encourage the City Council to access this information, in order to raise awareness among policymakers.

### Activities

- Displays the predictions for our Women's Safety Index in each city district for the next 4 trimesters
- Gives suggestions into how (un)safe each district will be in the future (based on it, women can try to avoid passing too much time in the dangerous districts). 

### Output

A Safety Map with predictions for the Women’s Safety Index, and locations of street harassment incidents. Suggests how (un)safe each city district might be in the future.

Mockup:

![Safety Map](https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/2012_Crime_Rate_against_Women_per_100000_in_India_by_its_States_and_Union_Territories%2C_VAW_Map.svg/1200px-2012_Crime_Rate_against_Women_per_100000_in_India_by_its_States_and_Union_Territories%2C_VAW_Map.svg.png)

## 🌍 Social Impact Measurement
### Outcome

To create a tool that people (especially women) can use to avoid dangerous areas. This comes with an effort to reduce crimes against women, as they have the right to an inclusive and safe city.

Measures:
- Encourage women to **check our Safety Map**;
- Some **campaigns** could be done to educate citizens, using flyers, outdoor posters, and most importantly, social media. This would explain how women can access and use the online platform to check our Safety Index predictions;
- To tackle the issue of **street harassment**, we recommend police stations to start sharing anonymous data about these types of crime. If we had the coordinates of where a street harassment crime occured, and a short description of it (keeping the reports anonymous), we could pinpoint it on our Safety Map. Then, women could check which roads/streets were more prone to have people committing street harassment.

### Impact Metrics

- Number of crimes against women per city district (per 10k inhabitants)
- Number of reports of street harassment per city district (per 10k inhabitants)

### Impact Measurement

- Based on the model predictions presented in the Safety Map we suggest, women and girls will be more conscious about walking in San Jose, which can bring benefits in the long term regarding the inclusivity and safety of this city.
- Based on examples like the [**Women, Peace and Security Index**](https://genderchampions.com/news/the-women-peace-and-security-index-2021-highlights-policy-recommendations), the [**Women Safety Index of Delhi and its neighbouring cities (India)**](https://www.ijrte.org/wp-content/uploads/papers/v7i6/F2368037619.pdf), and the [**Women's Safety Index of Seoul (South Korea)**](https://www.slideshare.net/GRFDavos/development-of-a-women-s-safety-index-on-genderbased-violence-a-crossregional-analysis-of-risk-factors-in-seoul-city-mihye-chang), we believe our index could assist on changing agents, policy makers, NGOs, urban local bodies, municipalities, state transport authorities, police, and emergency response officials for the improvement of women safety in cities.