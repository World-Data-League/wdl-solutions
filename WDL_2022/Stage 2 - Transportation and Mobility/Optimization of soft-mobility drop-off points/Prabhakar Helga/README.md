# World Data League 2022

## Executive Summary

## 🎯 Challenge

_SoftMobility: E-Scooters in the City of Porto_

## 👥 Authors

- Lukas Mölschl
- Ivan Vrkic
- Manuel Bürgler

## ✨ Introduction

The chosen challenge focuses on _E-Scooters_ in the City of _Porto, Portugal_.
Such E-Scooters offer not only a fun and joyful ride but can also be a climate friendly _last mile_ solution for different types of travelers. Unfortunately, the handling of such E-Scooter fleets has led to new challenges for city authorities. [**Cluttering**](https://www.theage.com.au/national/victoria/e-scooters-cluttering-footpaths-challenging-vision-impaired-20211015-p590al.html), [**oversupply and vandalism**](https://edition.cnn.com/2019/08/30/tech/scooter-management/index.html) and many more issues have led to a great deal of frustration in the past.
The City of Porto already tackled some of the issues mentioned by establishing fixed pick-up / drop-off points as well as restricting the overall number of E-scooters in the city. Porto is a pretty hilly city and even though none of the team members has visited the city yet it may be assumed that walking up & down the whole day can be quite exhausting. An e-scooter is therefor a very comfortable alternative in our eyes and we also would seriously consider this as an alternative way of getting around the city as tourist.

## 🔢 Data

Explain what data you used (both provided by WDL and external) and improvements you suggest to those datasets. Explain how those improvements would lead to a better solution.

Our main datasets used are the _E-Scooter OD_ and _E-Scooter Parks_ datasets.

**E-Scooter OD**

- The dataset consists of data following the [**MDS STANDARD**](https://github.com/openmobilityfoundation/mobility-data-specification) according to our research. Details about the standard may be found in the link above.

  > Improvements in the dataset could be made in providing a larger timeframe of data.

**E-Scooter Parks**

- The dataset contains all the scooter parks in Porto as a GeoJSON.

  > Improvements in the dataset could be made in providing an english dataset.

## 🧮 Methods and Techniques

Tell us what methods and algorithms you used and the results you obtained.

As a first step to break down complexity and degrees of freedom, the location data from the `trip-start` & `trip-end` was bound to the scooter parks. This was achieved using a distance function which had to be built in `numpy` to achieve high calculation performance.

After this critical ETL step, we showed on interactive maps not only the total traffic per scooter park but also the main routes between scooter parks. As there are ~ 10k possible route combinations between scooter parks, a special focus on readability & clear messaging in the map of the main routes was set.

--> Algo for identifying underutilized scooter parks. Identify "pair" stations where one scooter park is heavily underutilzed for potential concentration.

## 💡 Main Insights

Looking into the results some things are clearly observable:

1.  The Hotspots are in the old town & near the coast which is an indicator for touristy use.

2.  The distribution of utilization of the Scooter parks is very uneven throughout the city. This indicates the possibility for consolidation in scooter parks which are in close distance to each other.

3.  Even though there seem to be some popular _standard routes_ between the old-town and the promenade as well as at the campus, traffic outside this areas seems to be very diversified.

But let's go through the points one by one.

Firstly, it was somewhat expected that very high traffic areas are found in the old town/city center. The stop with the most traffic in Sao Nicolau / 'RNALF0' is a perfect example. Located next to a bus stop/tourist parking area it is the perfect spot to either start exploring the city center to the north, down the promenade to the west, or the restaurants to the east.
The scooter park with the second-most traffic is right next to the main subway/train station "Sao Bento". This indicates that the scooters are also used for "last mile" trips. What's positive about the Sao Bento scooter park is the increased capacity of 20 scooters.
Other high-traffic areas are near the beach / promenade.

Secondly, speaking of distribution it comes clear that there is only a very "uneven" usage & traffic distribution through the city. Especially the parks in the industrial zone don't seem to be used at all. This clearly shows some room for improvement in the future. Additionally, we observed that often there is a very underutilized scooter park nearby which could be removed. We identified **12** such neighboring parks which would free up 120 scooter spots for high traffic areas.

Thirdly, the already mentioned _standard routes_ indicate tourist use at the promenade and commuting between buildings at the university camps.

## 🛠️ Product

We propose a system that allows the city planner to identify underutilized drop-off zones that experienced less than `x` in- and outbound `organic traffic`. In the next step our algorithm computes based on this input:

The results are visualized in a way that allows the planner to quickly identify potential replacements/weaknesses in the system. The sum can be used by the planner to identify if the replacement drop-off zone would overflow with the additional load that is coming from the removed zone.

### Definition

> Scooter stations that are underutilizer or not ideally placed are identified and a subsitute for the one is found, in addition it finds the top-k stations that are over utilized that should be increased.

### Users

- `City Planners` - To plan capacity / scooter parks around the city
- `Decision maker` - To react to trends and developments in traffic and usage of e-scooters.
- `Authorities` - To check for potential traffic / littering related issues on high traffic routes / scooter parks.

### Activities

- Shows current utilization of scooter parks based on historical data on a comprehensive map.
- Makes suggestions for underutilized stations which could be consolidated / (re)moved.
- Shows current routes / movement patterns around the city on a map.

### Output

The main output is done via a webinterface and could be implemented using e.g. [**_Streamlit_**](https://streamlit.io/). Our already described maps would be very easy implementable in such dashboard.
