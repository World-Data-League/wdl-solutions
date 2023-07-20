# World Data League 2023


## 🎯 Challenge
Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data


## Team Name
Insight Squad 💡


## 👥 Authors
* Maria Manuel Castro
* Rodrigo Miguel Ferreira
* Ricardo Ângelo Filipe
* Catarina Campos Rocha
* Eduardo Daniel VIcente


## ✨ Introduction (250 words max)
To achieve a better understanding of city flows, entries and departures from axes to the city, is a herculean task. Moreover, unbeknown to drivers, there may be traffic restrictions  or jams, that compromise arrival time and create stress and decrease  population wellbeing.
This problem is even more critical during higher traffic hours (i.e. rush hours).

Hence, this challenge will try to create a visualization of the city and a model to predict jam areas.

The goal is simple: improve mobility on Lisbon City.




## 🔢 Data (250 words max)
From the 8 datasets provided by WDL we used all, except 6.

We merged dataset 1 with 3. 
We also merged dataset 2 with 4 and 5.

The main goal was to predict Jam quantity for a congested area (i.e. 'freguesia'), based on Jam quantity and devices on the Grid for that 'freguesia'.
Additionally, the merged datasets were used for the visualization presented [here][5] 



## 🧮 Methods and Techniques (250 words max)

First, we used the standard tool belt for data scientists: pandas, scikit and numpy. The goal was to clean, detect missing data and make a quick benchmark of our data.

Secondly, we used Pandas Profiling to understand better the data (results can be seen in [here][5]  through tab 'Data Analysis').

Third, for the heatmaps presented [here][5] we used Folium.

Finally, for our predictive model we used time series (linear regression). We used data from September (due to have a lower missing values) and from 'freguesia Parque das Nações' due to computational limitations.


## 💡 Main Insights (300 words max)

The Main Insights discovered by our squad were:

* There is missing data in several datasets provided by WDL
* We have some spikes of entries or departures in Lisbon (e.g. spike of departure 28/10, before an extended weekend)
* Sao Domingos de Benfica is the 'freguesia' with more perceived congestions during rush hours in October and November.
* From 26/10 to 15/11 we have low values from entries and departures from Lisbon.
* Bridge '25 de Abril' has a behavior in September and October in terms of entries and departures different to November.


## 🛠️ Product
We deliver two artefacts to better understand Mobility Flows in Lisbon. 

First, a visualization tool with several dashboards with (real) aggregated data from the provided datasets. Pinpointing mobility flow bottlenecks may have a significant benefit for the city flow governance.  

Secondly, a predictive model that aims to detect congestions of level 4 or 5 (maximum for the supplied dataset) one hour before it occurs. The model can be integrated in the aforementioned dashboard to help drivers avoid congested zones, or even route traffic directly from a control center using ⛔👮🚦

Despite the benefits, the visualization tool and model have the constraint to have access to real time data, to ensure timely traffic congestion notification and prediction.


### Definition
A tool that assists Lisbon Governance in traffic control and also drivers avoiding congested areas.


### Users

To have a holistic solution to the mobility flow challenge, the solution must address two users:
*  Traffic Controllers that uses the created dashboards. The dashboards have heatmaps to understand flows in Lisbon Grid, charts with departures and entries in the main axis and an overall characterization  for rush hours. We aim to pinpoint flows and enlighten possible routing changes to swiftly decrease Lisbon Traffic
* City Drivers. The drivers will have access to a tool that retrieves the prediction for congested areas for the next hour. Hence, the drivers may avoid those areas, or select a more friendly transportation vehicle (e.g., car sharing, bus, 🛴 or 🚴)


### Activities
Features that our product has:
1. *Predicts* congested areas for the next hour 
2. Visualization Tool with three Dashboards with *real* data and responsive for Desktop, Tablet and Smartphone
	1. Dashboard one - full timeline (link https://peaceful-sherbet-485f81.netlify.app/ )
	2. Dashboard two - rush hours (link https://peaceful-sherbet-485f81.netlify.app/dashboard-three)
	3. Dashboard three - Display information about traffic restrictions (link https://peaceful-sherbet-485f81.netlify.app/dashboard-four)
3. Some Easter Eggs 😉
	1. Administrator Name 👓 (hint: the administrator initials are CM )
	2. Dark theme available under the gear icon 😌🤓
	3. Team name at top left and bottom left	 
4. Some Data Analysis for our beloved Data Scientists 📊🕵🏼 (check Data Analysis Tab on https://peaceful-sherbet-485f81.netlify.app/apps/condicionamentos)


### Output
Better than describe a possible output is to have a gif illustration or a functional frontend with the features 😉

The traffic controllers  will have access to an Administration tool with several real-time visualization.

E.g.Heatmap with the more congested areas and identification of the main axis to enter or departure from Lisbon.
<img src="https://peaceful-sherbet-485f81.netlify.app/fe_dash.gif" width="1200" height="600"> 

The tool will have:
Visualization Tool with three Dashboards with *real* data responsive for Desktop, Tablet and Smartphone
1. Dashboard one (link https://peaceful-sherbet-485f81.netlify.app/ )
	1. Display heatmaps for the day 
	2. Display information about Entries and departures by main Road and Day 
	3. Top 10 Hotspots by Town Council and Month (areas with more connected devices by month with area filtering)
	4. Top 10 Entries or Departures by Month and Main Road
2. Dashboard two (link https://peaceful-sherbet-485f81.netlify.app/dashboard-three)
	1. Display heatmaps for the rush hours 
	2. Summary of Entries and Departures Congestion 07h-10h (filter by Axis)
	3. Summary of Entries and Departures Congestion 17h-20h (filter by Axis)
	4. Top 10 Hotspots by Town Council and Month (areas with more connected devices by month with area filtering)
3. Dashboard three - Display information about traffic restrictions  (link https://peaceful-sherbet-485f81.netlify.app/dashboard-four


Also, the predictive model should return the jammed areas for the next hour through the same tool or a dedicated App. Hence, the drivers can route to other less congested areas.


### Scalability
To endeavor a tool that has scalability to retrieve the right features to traffic controllers and also drivers there are some concerns that need to be address:

1. *Data Collection and Cleaning*: currently the tool is in *offline* state. To have the fastest response to jams we need a stream of data processed in near real time. This may be a challenge both for the data producers and also to our tool.
2. *Traffic Management Strategies*: based on our tool, traffic controllers may pinpoint jammed areas that need intervention. 
However, the question arise: is the overall driving population prepared to active traffic management strategies that don't exist nowadays in Lisbon?
It may be needed some education and advertising campaign in Lisbon for new traffic management strategies as the one presented in [\[1\]][1] 
3. *App adoption*: one of our product features is the prediction of congested areas for the next hour. Hence, we are assuming that the app will be viral in Lisbon. However, if that do not occur, we will also need advertising and marketing campaign to present the benefits of the app to the standard Lisbon Driver.


## 🌍 Social Impact Measurement
Our product aims to gather a visualization tool to the traffic controllers and also an App with predictive models for congested areas in one hour.

### Outcome
The first direct outcome is decrease number of jams using the combination of the visualization tool and the App. Taking into consideration the studies conducted in [\[2]\][2] and [\[3\]][3] we can conclude that jams impacts deeply negatively in the fatigue, physical and psychological  wellbeing  of the drivers. Hence, reducing the number of Jams will increase the overall wellbeing of Lisbon population.

Regarding the benefits in fuel reduction, citing the authors of [\[4\]][4]: 
> In a traffic jam, a vehicle consumes almost 20% more fuel. 

And the following Image for velocity vs fuel consumption:

![Fuel Vs Velocity](https://qph.cf2.quoracdn.net/main-qimg-ef6e6f41f59f57e73907b20a83c73911-pjlq)

We can expect a fuel reduction on the vehicles of Lisbon City subject to Jam conditions.




### Impact Metrics
We can define the following 3 metrics to understand whether we are achieving the previous outcome or not:
* Average Number of Jams Per Day and Lisbon Area
* Mean Absolute Error between the predicted and real value for congested areas
* Number of Downloads for the Driver App
* Number of saved gasoline
* Money saved for the Drivers

### Impact Measurement

Taking into consideration that in November we had an average of X Jams per 15 minutes, we could predict Y Jams with our model. Also, the average of connected devices in a jammed area is Z for the time window of 15 mins.

Assuming that:
1. We could react (and eliminate or reduce significantly) 20% of Y jams - has a baseline
2. Y will be predicted based on minimum error from the time series. We assume that we can predict 30% of level 4 and 5 Jams.
3. The average number of connected devices Z in the dataset is equal to 5% of the number of vehicles in the Jam
4. The aforementioned 20% more fuel, for an average vehicle and an average route in Lisbon represents an extra 1,5 liter of gasoline per vehicle
5. The price per liter of gasoline is 1,609 €/liter


Than, We can conclude that: 

* Number of saved gasoline liters per 15 minutes= (Y\*0.2)\*(Z\*0.05)\*1.5
* Overall Money saved for the Drivers per 15 minutes = (Y\*0.2)\*(Z\*0.05)\*1.5\*1,609

Taking into consideration the area of 'freguesia Parque das Nacoes' for September and our predictive model:

* X=13
* Y=13\*0.3= 3.9
* Z=36431

Hence for 'freguesia Parque das Nacoes':
* Number of saved gasoline= 2131 Liters/15mins
* Overall Money saved for the Drivers per 15 minutes= 3429 €/15mins

For the reasons presented above, the impact measurement may change significantly, since depends on assumptions and baselines that we don't control.




[1]: https://www.smatstraffic.com/2021/05/17/active-traffic-management-strategies/ "9 Active Traffic Management Strategies , retrieved in April 2023"
[2]: https://www.shs-conferences.org/articles/shsconf/pdf/2019/08/shsconf_NTI-UkrSURT2019_04005.pdf "Modeling the effect of traffic jam on driver's level of fatigue"
[3]: https://www.iomcworld.org/proceedings/traffic-congestion-and-long-driving-hours-impact-on-stress-emotional-and-physical-health-among-drivers-in-sharjah-49396.html "Traffic congestion and long driving hours: Impact on stress, emotional and physical health among drivers in Sharjah"
[4]: https://www.livemint.com/Money/tlifa0Dp55LFayFmq8xQIJ/How-expensive-is-a-traffic-jam-for-you.html "How expensive is a traffic jam for you?"
[5]: https://peaceful-sherbet-485f81.netlify.app/ "Insight Squad"
