# World Data League 2022

## 🎯 Challenge 3

_Predicting a safety score for Women in Costa Rica_

## 👥 Authors

- Lukas Mölschl
- Ivan Vrkic
- Manuel Bürgler

## ✨ Introduction

Costa Rica is one of the safest countries in central america and known for its high education rate. Given their strategic decision in 1949 to abandon their army in favor of “an army of teachers”. This decision was among the driving factors in enabling a solid economic position in the area. Those effects are also reflected in the HDI Index, where Costa Rica scores favorable in the last [**years.**](https://globaldatalab.org/shdi/maps/shdi/).

Subsequently, all those positive developments lead to the fact that Costa Rica was considered very safe in terms of crime in the past.

Unfortunately, things seem to have changed. In a public opinion [**poll**](https://books.google.at/books?id=jdTJDQAAQBAJ&q=In+a+public+opinion+poll+in+2011,+45+percent+of+Costa+Rican+respondents+said+that+crime+and+insecurity+were+the+country%E2%80%99s+biggest+social+problem&pg=PA115&redir_esc=y#v=snippet&q=In%20a%20public%20opinion%20poll%20in%202011%2C%2045%20percent%20of%20Costa%20Rican%20respondents%20said%20that%20crime%20and%20insecurity%20were%20the%20country%E2%80%99s%20biggest%20social%20problem&f=false) in 2011, 45% of the Costa Rican respondents said that crime and insecurity were the country’s biggest social problems. Additionally, the situation seems to be further getting worse as the severity of crime is increasing. Homicide e.g. almost reached a new peak in 2021 after probably COVID induced declines in the 3 years prior. In terms of the victim's gender another grim picture can be observed - crime against females rose at an alarming rate of approx. 5,73% yearly between 2010 and 2019, crime against males only rose 1,14% yearly.

Reasons for these developments may very likely be found in organized cime & drug trafficking. This is also indicated by looking into the subgroup of `FIREARMS` which also rose significantly in crimes with both male & female victims. Looking at current research and news articles, especially the coastal areas around Limon are plagued by small cartels and gangs. As said gangs and cartels are organized in a [**small structured**](https://insightcrime.org/news/brief/drug-bust-points-to-evolving-criminal-structures-in-costa-rica/) way we assume that a lot of crime in rural areas - such as [**Cordillera de Talamanca**](https://www.unodc.org/toc/en/reports/TOCTACentralAmerica-Caribbean.html) - is happening in various gray areas that are not observable by the authorities and therefore neither noticed nor registered in the data provided. This brings us to the conclusion that in our analysis a very strong focus should be placed on the urban metropolitan area of San Jose.
As the goal of our research is to provide potential solutions for a higher level of safety of women based on data, we think this is a suitable approach.

## 🔢 Data

We relied on the data provided by WDL. Unfortunately again, most of the data was only available in Spanish, making it difficult to work with for non native spanish speakers. Additionally, the shapes in the provided Data for San Jose was only available in a native and poorly documented ESRI ArcGIS format. Even though ArcGIS is one of the market leaders in the sector, other better export options such as WKT or GeoJSON would also have been available.

## 🧮 Methods and Techniques

1. Aggregation and merging to join the data from the various files
1. Time series prediction to predict the number of crimes for each district
1. Factor analysis to solve the collinearity problem, analyze the impact of each variable
1. Compute varimax matrix (rotation of factor analysis) to extract weights for the index
1. NLP and pre-trained transformer models to flag places as safe or unsafe

## 💡 Main Insights

Looking into the results some things are clearly observable:

1.  Crime has risen strongly
2.  Especially crime against women has risen unproportionally
3.  As expected some districts are more problematic than others
4.  Friday & Saturday are most heavy on Crime, Sundays seem to be ok
5.  Building an Index that really correlates with the real world is hard.

While the first 4 point are clearly observable in the notebook and may not need any more description here, we want to take the chance to get into detail in point 5.

One of the challenges main goals was to build an index which describes the safety of a district and which can also be forecasted. In our given problem this comes with various levels of difficulty.
Firstly, as already described in the intro, we focused on San Jose due to “real world implications” which we have no way to handle properly without going really deep into the issue. For this area, various economic data etc. was provided in a single year.
Especially when considering intrinsic factors for crime such as education and the economical position (disposable income etc.) of an individual we clearly have gone through troublesome times in the past and also those factors surely have changed over time. So we have the first constraint in the meaningfulness of our analysis as we only can use such intrinsic important factors in a single year. Additionally San Jose itself only consists of a very limited amount of districts where the data described above is provided. In the result this leads to very few observations making a statistically robust analysis very difficult.
Secondly, once we investigated our correlations, the question arose on how to calculate a meaningful index. Again this proved very hard and we settled for a simple solution in the end.

We also investigated the literature approaches provided in the task description but came to the conclusion that, when looking into the light issue e.g., no data with good enough granularity and time series quantity (e.g. from NOAA etc.) is easily available. Also it may be noted that we assume that due to the strong technological shift from classical lamps to LED lighting, the worldwide observable explosion in ambient light pollution would also be observable in San Jose resulting in a “real world” phenomenon reducing the information value of the data. This may also be true for the city layout analysis. While older towns in Europe have an uneven street layout, Costa Rican towns have basically been designed on the drawing board in a chessboard system - a result from its colonial past. This results in an even topology making street layout approaches questionable or at least very difficult in our eyes.

So our main insight in this challenge is that we don't seem a viable solution to the problem which reflects the real world environment and therefore settled for an simplified solution.

## 🛠️ Product

### Definition

> Mobile safety companion for women.

### Users

-- Women in the urban area of San Jose

### Activities

- Shows the safety index of each district
- Shows times in when certain districts should not be visited
- Provides an "telephone buddy" when walking in high danger areas & times
- Provides contact for a subsidised women taxi service to ensure safe transport at night
- Check if places are flagged as unsafe

### Output

The output is a very simple mobile map based application which could be based on [**Flutter**](https://flutter.dev/)

## 🌍 Social Impact Measurement

### Outcome

In the long term we hope to reduce occasional unprovoked crime against women by ensuring they are aware of their surroundings. Additional services such as a telephone service where the user is “walked home on the phone” have also proven very successful in the subjective security feeling of the user and overall likeliness in becoming a crime victim. Additionally we propose a subsidized women taxi with specialized female drivers for nightly high crime times. Such systems already exist in Europe and are very welcome and broadly used among young women. The deployment of such street side taxis could be done based on predicted crime data.

### Impact Metrics

- Absolute crime against women in San Jose
- YoY / CAGR development of crime data
- Taxi / Phone Service Users per month

### Impact Measurement

Based on the notes we gave above, we don’t think giving estimates on how big a potential impact on crimes would be the right thing to do. We would really hope for the country to be able to do a turnaround on the subject and tackle its issues. Various other reports, which have been drafted by way more specialized researchers, show that a real impact can only be made when the policing and juridical system is reformed in the country. Nevertheless if a data based system could prevent even one single crime it would be a success to us.
