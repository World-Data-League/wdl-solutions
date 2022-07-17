# World Data League 2022

## Executive Summary by GeoNEAS

## 🎯 Challenge

*Predicting a safety score for women in Costa Rica*

## 👥 Authors

* Juan Diego Arango

* Melissa Montes Martin

* Santiago Cardona Urrea

* Irune Lansorena Sanchez

* David Gamba

## ✨ Introduction

Gender-based violence problems have been one of the greatest social plights in Latin America. According to the UN, between 60% and 76% of women (around 2 out of every 3) has been the victim of at least one type of gender-based violence. In addition, 1 out of every 3 women that has been a victim of physical, psychological and/or sexual violence, has suffered it at the hands of a perpetrator who is her intimate partner. [1]

Authorities have to deal with the fact that gender-based crimes are heavily underreported [2, 3]. One of the reasons is the fact that judicial system often lacks understanding about the nature of the crimes, leading to situations that often make women suffer revictimizing situations [4].

Some progress has been made to mitigate this, both in awareness and strengthening of laws. To accelerate this, it would be ideal to provide data tools that aid the reporting and policy making to both women and local authorities [5]. Although there are some existing datasets that aggregate crimes in Costa Rica, the current datasets lack granularity in both time and space to allow a more comprehensive understanding of gender violence.

Our team, GeoNEAS, is proposing a tool to empower women with data, allowing them to report gender-based crimes at a coordinate granularity. Women will be able to identify in which zones of a city are they at most risk, and authorities will have this information available to formulate public policies related to this issue.





## 🔢 Data

One crucial part of this project was to prepare the data shared by Urban Analytica to conduct Exploratory Data Analysis (EDA), forecast, and analysis. From this data source, we obtained an aggregated report of crime incidents in Costa Rica, reported at the canton and district level. The statistics are available for the year 2021.

Furthermore, we collected additional data points from different sources such as:

* Point of interests (POIs) from Open Street Map.

* Geographic Data of San Jose from Urban Analytica

* Population from official Census.

In addition to the datasets mentioned earlier, we propose an enhancement to the collection of the data, that will allow the authorities to have more granular data about the crimes in Costa Rica. We simulated a sample dataset for the city of San Jose that will contain reported crimes with a geographical coordinate granularity. Such granularity allows us to create more informative visualizations and models, which will ultimately be more useful for the authorities and the victims of gender-based victims.

## 🧮 Methods and Techniques

Forecast gender crime incidents in the city at a high level.

* We performed a data analysis process in which the crimes that affect women are determined over the total crimes in San Jose. After that, we used this information to construct time series of crimes for each one of the 11 districts of San Jose. We cross-validate and train a model with this data. This model is then used to create monthly predictions of the selected crimes over the 11 district of San Jose. Compared to a naive prediction, our model is better by around 10% (The model obtained a MAE of 3.16, while the naive prediction was 3.8).

Cases simulation, risk score and spatial model.

* The spatial model was built in three steps: crime cases simulation, checking OLS and spatial autocorrelation and choosing the spatial model. The crime cases simulation considered the construction of environment variables and a qualitative safety index. We propose a collaborative mapping to geolocated crimes in Costa Rica to enrich the data. On the other hand, we built environment variables through geographical datasets. We check spatial autocorrelation to choose the best spatial model for the data, which was chosen considering the presence of residual spatial autocorrelation [6]. As this model is for explanatory purposes consequently we do not need to cross validate. Findings show us that roads and public space could increase the number of crimes (based on the simulation) and the land use combination of institutional, commercial, residential could increase safety.

## 💡 Main Insights

Mos of the crimes are related theft (31%), assault (28.8%), and robbery (23.1%). Homicides reaches 0.71% of the crimes. Analysis per year, month, and day shows trends in their behaviour. Firstly, an increase in the total number of crimes per year is observed between 2010 and 2018 when a decrease starts. Total numbers in 2020 could be affected because of Covid-19 pandemic, however in 2021 the total number are not very different to the previous year. On the other hand, total numbers are similar through weekday and month, Costa Rica does not have a month or day of week when crimes are higher than other.

**Number of Crimes per category**

![Number_crimes_general.png](https://storage.googleapis.com/geoneas-bucket/gender-s3/images_resized/Number_crimes_general.png)

  

Regarding gender-based violence dataset we do not find granularity to conduct an analysis per year, month, and hour. Besides, we found 56 rows with geographic information. Finally, exhibitionism and sexual harassment have the highest rates among gender-based violence crimes.

  

**Sexual harassment crimes**

![Crimes_per_province_sexualharassment.png](https://storage.googleapis.com/geoneas-bucket/gender-s3/images_resized/Crimes_per_province_sexualharassment.png)

  

We identify some crimes categories that has more proportion of female than male, e.g, outburst (64%), feminicide (96%), and domestic violence (59%). We will generate a gender crime if it is higher than the mean of female proportion plus half of standard deviation. An analusis per year, month, and hoes shows trends in the behaviour of the number of female crimes. Firstly, some crimes shows similar trends that the general ones; however, some of them like feminicide or domestic violence do not show trends related to years, they have an irregular behaviour through them. Furthermore, an increase of domestic violence crimes during 2020 is show, they could be explained because of the pandemic and lockdowns. Those behaviours in the trends are similar in the analysis per month where feminicide and domestic violence does not show similar trends in the months such us the other subcategories. January and February have higher cases of domestic violence than other months while March, September and October are critical months for Feminicides. Finally, the analysis per day shows that crimes decrease during the weekend; ATM WITHDRAWL increase friday and DOMESTIC VIOLENCE has an increase trend between monday and thursday when a peak is shown. Finally, most of the FEMINICIDES happened on monday or wednesday.

  

Spatial autocorrelation was found from simulated gender-based violence points consequently we train an spatial error model with built environment variables finding strong correlation of presence of road infrastructure, properties, and heritage buildings with the increase of crimes. On the contrary, recreational areas, institutional, commercial, and mixed land use and population increase the safety in the space.

**Risk Score Index and Lag variables**

  

![Risk_score_general.png](https://storage.googleapis.com/geoneas-bucket/gender-s3/images_resized/Risk_score_general.png)

  

**Coefficient variables**

  

![demo_model_coefficients.png](https://storage.googleapis.com/geoneas-bucket/gender-s3/images_resized/demo_model_coefficients.png)

  

## 🛠️ Product

### Definition

A web application that displays maps, statistics and forecasts about gender-based crimes in Costa Rica, and allows future crime reporting and forecasting. Check the demo of the product in the following link: https://gender-s3-7kvbiho2qa-uc.a.run.app/

### Users

We designed our tool with two users in mind:

* Women: Women can use the dashboard to inform themselves on the most dangerous zones of San Jose, based on factors like location and time of the day. They will also be able to report future crimes, which helps to tackle crime underreporting.

* Authorities: Authorities can use our product to identify the areas with a high rate of gender crimes, forecast the crime tendency, and create public policies to decrease such rates.

### Activities

Our product has several components that allow the users to 1) explore the current state of risk and its distribution in the city, 2) identify how different factors in the area correlate with risk, so it might be possible to devise strategies to improve safety for women and 3) forecast incidents in the city at a high level. The product can be further leveraged by a model that feeds itself with new reported incidents. As these databases contain sensitive information, it is needed to also work on data protection and safety.

Understanding of the current state of gender violence in Costa Rica:

* Our first proposal is a risk map that women can use to identify how risky is an area at the block level.

* Then, we developed an explanatory spatial model that shows the factors that are correlated with the index of gender based crime. This model will help to the creation of strategies for improving safety of women, tackling the factors that are more important according to the model. The model takes into account factors such presence of police and general geographic and population information, and it also accounts for the fact that crimes tend to form hotspots and spatial aggregations. What we get, is a measure of the correlation of each factor with the prevalence of cases. The model also outputs which factors have more weight and wether those are correlated with more risk or less crime.

Predicting crime trends at the district level:

* Model that forecasts the crime trend, taking into account historical violence data at the district level.

Improve gender incident reporting:

* Finally, we provide a new form, designed to have a better and more granular reporting of gender incidents for women. This form can be implemented in the platform, as well as in police stations when women report new cases.

### Output

  

Solution is divided in three parts:

1. A risk map based on the previous experiences of women across San Jose is showed in the first section. High risk zones have historically a high prevalence of violence cases against women. We hope this map can help women to stay safe and to empower it to ask for safest places to decission-makers.

  

** Safety index map**

![demo_risk_map_women.png](https://storage.googleapis.com/geoneas-bucket/gender-s3/images_resized/demo_risk_map_women.png)

  

2. The second section was built for decission-makers analysis. An interactive risk map where you can click to explore context data for each of the hexagons is showed. Moreover, the results of a spatial model that correlates each factor with increased or decreased risk (as measure by prevalence of cases) is observed. Decission-makers could check the score of each variable per hexagon and their influence in the crimes trends to define solutions. Finally, trends of violence in each of San Jose´s district and a forecast of monthly cases for a year is showed. Decission-makers could monitorate each district.

  

**Reporting crimes**

![demo_report_intro.png](https://storage.googleapis.com/geoneas-bucket/gender-s3/images_resized/demo_report_intro.png)

  
  

## 🌍 Social Impact Measurement

### Outcome

With our tool, we hope to help women not only to find safe spaces for their public activities, but involve them in facilitating the understanding of risk. This will potentially enable the implementation of mitigation initiatives, which ultimately aims to create safer places for themselves and other women.

Additional, we hope to provide an insightful and easy-to-understand tool for authorities to create public policies and projects to address the gender-based violence incidents in the country, especially for areas with the highest incident rates.

### Impact Metrics

Based on the objectives stated throughout this document, our impact metrics are:

* Number of reports of gender-based crime incidents

* Number of areas with a decrease of gender-based crime incidents

### Impact Measurement

* Number of reports of gender-based crime incidents: As one of the main objectives of our project is to improve reporting of gender crimes, the number of reports is a good indicator of whether we are incentivizing the reporting with our platform. Another interesting metric to look at will be the average users/views of the platform. Although that metric does not completely depend on the product itself (ie. There are some other factors that influence views, like promotion and awareness of the tool), it can give us good insights to improve the underreporting problem.

* Number of areas with a decrease of gender-based crime incidents: The final goal of the entire project is to decrease the gender crime incidents in Costa Rica. Therefore it makes sense to consider the number of areas with a decrease of crime incidents as successful areas. However, we do need to be careful to link such reduction of cases to the policies that can be implemented with the platform, rather than to underreporting or other external factors. At the beginning of the implementation we might even see an increase of the metric, but ideally we can link the increase to the improvement of reporting. Having said so, and once the reporting is more normalized, a decrease of gender-based crime incidents will indicate that the platform is successful.

# References

[1] Report from ECLAC (Economic Commission for Latin America and the Caribbean) on violence against women and girls.

(https://www.cepal.org/en/pressreleases/eclac-persistence-violence-against-women-and-girls-region-and-femicide-its-maximum)

[2] Garfias Royo, M., Parikh, P., & Belur, J. (2020). Using heat maps to identify areas prone to violence against women in the public sphere. _Crime Science_, _9_(1), 1–15. https://doi.org/10.1186/s40163-020-00125-6

[3] Sánchez, Y. (2021). _Implementation of a spatial database for the calculation of safety indexes for women in public spaces_. _20_(1), 3550–3555. https://doi.org/10.17051/ilkonline.2021.01.400

[4] Rodas-Zuleta, M. del M., Cardona, S., & Escobar, D. A. (2022). Gender-based violence and Women’s mobility, findings from a medium-sized Colombian city: A quantitative approach. _Journal of Transport & Health_, _25_(April), 101376. https://doi.org/10.1016/j.jth.2022.101376

[5] Manazir, S. H., Govind, M., & Rubina. (2019). My safetipin mobile phone application: Case study of e-participation platform for women safety in India. _Journal of Scientometric Research_, _8_(1), 47–53. https://doi.org/10.5530/jscires.8.1.7

[6] Rey, S.J, Arribas-Bel, D, & Wolff, L.J. (2020). Geographic Data Science with Python. Retrieved from: https://geographicdata.science/book/intro.html

