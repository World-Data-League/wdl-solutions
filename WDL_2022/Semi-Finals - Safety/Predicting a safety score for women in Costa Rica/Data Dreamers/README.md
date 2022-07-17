# World Data League 2022

## 🎯 Challenge
*Predicting a safety score for Women in Costa Rica*

## Team Name
Data Dreamers

## 👥 Authors
* Luckshan Sivakumar
* Nikhil Kulkarni
* Sourabh Hujare
* Roney Mathew

## ✨ Introduction (250 words max)

* According to a study by the United Nations Entity for Gender Equality and the
Empowerment of Women, Gender violence in cities, specifically in public spaces, has
become an increasingly public issue, especially in Latin America. The lack of adequate
urban infrastructure, policies, and governance models exacerbates it. Thus, addressing the
main obstacles women face regarding their right to an inclusive and safe city, becomes a
Priority.
Police statistics have shown that 70.6% of the complaints of street sexual harassment in
Costa Rica in 2019 were submitted by women. Many assaults are not even reported due to fear of further violence or recrimination.
While no current strategy from the public authorities is in place, women are raising their voices creating awareness groups on social
media to report aggressions, missing persons, etc. This is why we wish to give women a
mapping tool to identify but also report whenever they feel like their right to enjoy public
spaces without being harassed is being threatened.*

## 🔢 Data (250 words max)

* The following data sets were used:*
* Reported crimes Data  provided by WDL
* External data from OpenStreetMaps for POIs data and Shape file data using Qgis tool.
* We got the Census data from external online sources.

## 🧮 Methods and Techniques (250 words max)

* We chose a very simple and easy to understand metric as our safety indicator and it is the crime rate on women per 10k population in the district. The higher it is then less safe the district is and vice versa.*
* We used Prophet model to predict the trend of this index for every district*
* We used Linear Regression , Decision Trees and Generalized Optimal Sparse Decision tree models to explain the crime rate in various districts to the authorities.*

## 💡 Main Insights (300 words max)
 
* 1) Most common type of crime against female in public places is Assault. A close second is `Theft` crime in public spaces Assault crimes on women are maximum in the late evenings i.e after 6 pm and before 10 pm.
2) The total crimes per year saw a decreasing trend from 2019 to 2021 and to 2022. This can be attributed to Corona and quarantine rules and hence it is understandable that public spaces were not used much during this time .
3) In general, we see that the crime rate on women has an increasing trend for majority of the districts*

## 🛠️ Product
### Definition

** Our product is a mobile app that shows how safe the district is for a woman and allows for reporting crimes using it which will be visible to authorities and users.** 

### Users

Primary users would be women who will use it to check the safety level for the location they are interested in and they can follow the tips given on the app to stay more safe.
Authorities can use the app to act on reported crimes.

### Activities

* Easy reporting feature of app helps to better the app’s performance over time.
* Feature to give suggestions/tips to fellow women and thus the App suggests crowdsourced tips to stay safer, eg: Do not walk alone after 6 PM, etc.

### Output

The output is a coloring of districts based on their safety level so that it is easy for the user to understand at once glance.

A simple explainable model is also published on the app as a way for Women and government authorities to understand what makes a district unsafe.

## 🌍 Social Impact Measurement
### Outcome

To decrease the crimes inflicted upon women by warning them in advance to stay safer by following tips.
To reduce crime rate by helping authorities understand its root causes and thus Optimising budgets to more effectively allocate resources.

### Impact Metrics

Average crime rate on women per 10k population of a district.
Number of crimes reported by women. This should see an increase due to ease of reporting via the app.


### Impact Measurement

* *Based on proxy products*: Similar apps in other countries like the Safecity app show that there’s an increase in crime reporting and thus helps policy formation and resource allocation to improve the conditions.


