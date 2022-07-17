# World Data League 2022

## 🎯 Challenge
Predicting a safety score for women in Costa Rica

## Team Name
Shiny Pandas

## 👥 Authors
* Imre Boda
* Zsolt Kegyes-Brassai
* Peter Michaletzk

## ✨ Introduction (250 words max)
Legislation in Costa Rica gradually implements measures for protecting women's rights starting from the 80s [Costa Rica, Violencia contra las mujeres a lo largo del ciclo de vida, 2020](https://infosegura.org/en/2021/06/18/violence-against-women-costa-rica-2020/), but violence against women is still significant, with close to 1000 victims of some kind of home violence each months. Femicides are in the range of 20-30 cases each year across entire Costa Rica.
Part of the problem is street violence, sexual harassement committed against women, representing 70% of all harassement cases.
The goal of this study is to provide an analysis framework for understanding where crime happens, in order to facilitate the achievement of UN Target 11.7: "Provide access to safe and inclusive green and public spaces"; i.e. that women can move freely without being at risk in public spaces.

## 🔢 Data (250 words max)

* Crime database - all crimes committed in Costa Rica between 2012 and 2022, with district level geographical resolution, where crimes and crime subtypes are distinguished, along with the gender of the victim
* San Jose map layers, containing details such as:
  * district boundaries
  * building zone designations (residential or commercial areas) and building regulations (size of setback (front garden), maximum building sizes, etc.)
  * rivers, lakes
  * public use areas
  * etc.
* google map reviews about parks and public transport services
* openstreetmap data about bars, pubs, etc.

## 🧮 Methods and Techniques (250 words max)
We focused our analysis on San Jose, making it feasible to apply a great level of geographical detail.
According to literature, crime is not spread evenly; it concentrates in micro hotspots, the size of a road intersection or street segment. We seeked through map features in order to find these hotspots, and validated these findings with historical crime data.
Our methodology:

1. Analyzing historical crime levels
2. Gathering raw geographical features that can explain differences in crime levels across districts (correlation)
  * challenge dataset map layers
  * openstreetmap - entertainment, hospitality-related locations
  * google reviews of public locations, and transport, including mentions of unsafe conditions
3. Space syntax analysis - a methodology used in urban planning, that has relevant results for crime probability at micro location levels
4. Placing relevant (positively correlated) geo features on map
5. Heatmap: Aggregation of these features to create a hotspot indicator per small locations

## 💡 Main Insights (300 words max)

It's interesting to see that there is a particular district in San Jose, Carmen, where disproportionately high volume of crimes happen both from the perspective of inhabitants of the area of the district. It seems like this is the downtown area, full of monuments and entertainment locations, where people go to have fun... and this attracts crime too.
The study also showed that the Commercial Zone 2 and the Mixed Commercial and Residencial Zone areas are positively correlated with crime density, i.e. they tend to favour the meeting of criminals and potential victims at locations appropriate for committing crime.
The centrality analysis of San Jose (part of space analysis) shows that from a street-network configuration point of view, the Western and the Eastern parts of the city are safer then the center. However, the Eastern district of San Francisco de Dos Ríos is significantly separated from its direct neighbouring areas by means of a city highway, making it also a lot safer.
The most polluted areas - from crime perspective - are the 4 downtown districts: Carmen, Catedral, Merced, Hospital.
Crime data was not very detailed, we had access to district level resolution only; better analysis could be carried if more precise location info was available.

## 🛠️ Product
### Definition
Crime hotspot heatmap of San Jose, with a resolution of about 60m, indicating the relative risk of each location on the scale of 0-7.

### Users

* Those who want to stay safe when travelling to unknown locations (especially women in this particular case). Our heatmap could very well complement [Red Dot Foundation's SafeCity webapp](https://www.reddotfoundation.org), where victims can indicate dangerous places. Our heatmap can help travelers and local citizens to avoid areas with potential threats, before bad things actually happen there. 
* City planners, municipalities: can learn from our heatmap which areas they need to focus on for efficient crime prevention. E.g. they can figure out where to place CCTV cameras, reinforce police presence or just improve street light coverage

### Activities
* Predicting the likelihood of becoming a victim around the city of San Jose (or in any city if appropriate data is provided), with a resolution of 60m

### Output
Our heatmap covers the city of San Jose with 60m-sized hexagons, each indicating the level of risk, consisting of the below components (at the moment; the methodology can incorporate more components as well).
Risk due to:

* inherent characteristics of the urban zone (commercial area)
* previous bad (unsafe) experience by google map users (reviews) in parks
* close proximity and high density of bars, pubs, etc. (locations where people go to have fun)
* people movement (criminals are more likely to commit a crime at locations they know well, and where they can find victims -> the areas that many people visit)

## 🌍 Social Impact Measurement
### Outcome

We would like 

* women to be aware of threats, so they can take conscious decisions to avoid risky locations
* help authorities to make risky locations safer for women

### Impact Metrics

* Violence Against Women case reduction ratio
* Violence Against Women as a focus area to appear on the agenda of the municipality of San Jose, possibly with a budget allocation

### Impact Measurement

Violence Against Women cases consists of violence on street cases but also of crimes within families or relationshipts. Our heatmap can help women to avoid sexual harassement on streets; representing around 1250 cases in 2019 in whole San Jose. We would be too optimistic to hope that we could eliminate all of these events, but some part of it at least.