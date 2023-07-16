World Data League 2023 - Second Phase

🎯 Challenge
Avencas Marine Protected Area: Predict the future of the local ecosystem and its species


Team Name
Random Graphers

👥 Authors
José Almeida
Juliana Machado
Marta Colaço
Rui Santos

 ✨ Introduction 
Marine Protected Areas (MPAs) are marine spaces entirely delimited in ocean waters, with the purpose of reinforcing the conservation of nature and marine biodiversity. The origin of this concept takes us back to 1962, to the World Congress on National Parks, when it was first formalized the need to protect important habits and species of marine life and to foster policies and programs to preserve marine species. 
After 6 decades of investing in investigation and implementing both global and local policies to promote the sustainability of marine biodiversity, several milestones were already possible to achieve - in the EU for example, marine protected area coverage more than doubled between 2012 and 2021, reaching a value of approximately 12% - however, marine biodiversity sustainability targets still fall short to what is possible to achieve, and with the increased investment on data science and AI models “there is no sea we can not sail”.
It’s hard to believe that the majority of threats biodiversity faces nowadays are a direct and indirect result of a species that is the culmination of species’ evolution itself - the Human kind.
Our ways of living are certainly the biggest threat to biodiversity sustainability, due the pollution, overexploitation and habitat loss that our day to day activities generate to the ecosystem that surrounds us, that also leads to climate change and promotes invasive species growth.
It’s critical to stop and assess the impact we have on the ones that surround us, besides our neighbors, and even though it might not be visible on our daily “terrestrial” life, our actions have a huge impact on marine biodiversity.
Following the challenge presented by Cascais Municipality team, our group analyzed several sources of data to identify variables that might impact Avencas Marine Protected Area (AMPA) ecosystem and aimed to build a data model to predict endangered and invasive species evolution over time.


🔢 Data 
To build our model, we used the following datasets:
Provided by Cascais City Council team:
% coverage with sessile species in samples taken between 2011 - 2020 in AMPA;
A reference list of which species are considered invasive and which are considered endangered according to the IUCN (note that for some species the Portugal-specific conservation status assigned by the IUCN is given).
Datasets from NASA Earth Observations (NEO) consisting of satellite data containing monthly measurements of different variables with a resolution of 0.1 degrees:
Carbon Monoxide (MOP_CO_M);
Chlorophyll Concentration (MY1DMM_CHLORA);
Nitrogen Dioxide (AURA_NO2_M).


 🧮 Methods and Techniques 
This challenge constituted a time series problem in which the end goal was to predict the variation of invasive/endangered species. However, this could not be tackled as a simple univariate time series problem since it was important to decipher any variables contributing to the variation of species at the AMPA. Thus, we used a model that is capable of forecasting time series using additional exogenous variables -  SARIMAX. This model derives from the SARIMA model, which is a variation of ARIMA (Autoregressive Integrated Moving Average). ARIMA models are commonly used to predict time series, however, they are unable to deal with seasonal data - a gap that SARIMA can treat. SARIMAX is a SARIMA model evolution, and perfect for our challenge, since it is capable of dealing simultaneously with seasonality and exogenous variables, which allow us to consider relative prevalence of other species or environmental aspects on our model. Therefore, we used the ARIMA as the baseline model and we compared the SARIMAX results with it. 
The main dataset (% coverage with sessile species in samples taken between 2011 - 2020 in AMPA) had to be processed prior to its use in model training, since the observations were not equally distributed over time, which is a prerequisite for any temporal model. Therefore, we had to aggregate the dataset into monthly periods by averaging observations for the same month and species. We also dealt with some missing values and discrepancies in the dataset, which made us exclude periods without any observations. In addition to this, we used a set of variables of interest from the NEO website at the closest coordinates to the AMPA.
SARIMAX contains several parameters that had to be configured. One corresponds to the number of time steps in one seasonal period, which was set to 12. The other parameters were either estimated through correlation plots or defined as sensible values. After selecting suitable parameters, the model was fitted to the data and its performance evaluated. In our analysis of seven scenarios for invasive species, which involved modeling with ARIMA, SARIMA, and SARIMAX, we consistently observed that SARIMAX outperformed the baseline model (ARIMA) in all cases.





💡 Main Insights 
The data is very sparse for most species, which can be due to their low density/frequency or to the sampling process which selects random locations at different time points inside the AMPA for the measurements. Since the process is random, some of these locations might contain less diversity/concentration of species. These facts pose additional challenges for time series forecasting models.
Five species in the main dataset are defined as being invasive. Interestingly, not a single species is marked as being endangered according to the IUCN. There are, however, species marked as being commercially threatened or insufficiently known.
Regarding the invasive species, they are all algae. Some are practically nonexistent at the AMPA, like Osmundea pinnatifida and Codium sp., while some are quite abundant (Cladophora sp.).
The commercially threatened species are very rarely found at the AMPA, which might be due to excessive fishing. This obviously prevents these species from being used in predictive models.
There is a clear seasonal variation in the data, which was taken into account by the model. This is particularly noticeable for Cladophora sp. in the intertidal region, with increasing numbers during the summer months.
It is possible to see variations of the measurements according to the zone in which they were made or depending on whether the measurement was performed in a supratidal or intertidal region (species more dependent on water, as expected, are preferentially present in intertidal areas). Examples are Coralina elongata which is mostly present in the intertidal region or Chthamalus sp. which is usually found in the supratidal region.
SARIMAX models performed better than ARIMA models for all the seven scenarios tested.
Using SARIMAX models, we were able to see how different environmental aspects retrieve by circulating NASA satellites associate with changes in different invasive species.


 🛠️ Product
Our product consists in a model capable of predicting future variations of the species located at the AMPA, using the considered time series and exogenous variables. Predicting this variation is of considerable importance, since it allows preemptive actions to reverse the decline of specific species, to increase small recovery rates (something pointed out by the Cascais Municipality) or to deal with the spread of invasive species. By using exogenous variables, it is possible to achieve more reliable predictions while at the same time measuring the importance of each one. These importances are obtained by studying the coefficients of the model, which reveal the significance of each variable and if they have a positive or negative impact. Therefore, preemptive actions should be focused on mitigating the effects of these variables.
Obviously, not every variable is easily shaped to favor the recovery of species. Nevertheless, this model offers new insights that can serve as inspiration for future and more practical measures.

 Users
Cascais Municipality team
Biologists and scientific community
Start-ups and businesses focused on conservation and ecological transition


Activities
Our product offers a good tool to complement the monitoring of species in marine ecosystems. It indicates exogenous variables of importance which could start being measured locally and not via satellite for obtaining more precise values. It also indicates the need to change the data collection protocol to focus on larger sampling areas in order to decrease the sparsity of the data.

Output
Our model outputs expected percentage values of coverage of sessile species in the AMPA at future time points. It is possible to see the model fit to the data (relative to a given species) and assess the coefficients which function as a measure of the impact of specific variables. Our variables are environment-related and consist of water temperatures and molecular concentrations of different substances in the ocean, which are easily obtained. We also attempted to correlate the data for different species, since there might be symbiotic relationships like mutualism, amensalism and predation, but the sparsity of the data hindered our work (the creation of higher quality datasets is therefore essential for the discovery and inclusion of more variables, which would improve the output of our product).
Through our descriptive analysis it was also possible to draw some observations from the data that point towards the proliferation of invasive species like Cladophora sp. and reveal the scarcity of commercially threatened species. Overall, the measured values for native species are considerably low which indeed calls for preservation efforts and further policies.

Scalability
The product is easily scalable in terms of including additional exogenous variables. It is also applicable in other world areas, requiring only measurements across time regarding the species of interest. The other features, the exogenous variables, are available at the NEO website for the entire globe and spanning a large time period (the satellite data is still being collected every month). 


🌍 Social Impact Measurement
By predicting the probable evolution of endangered and invasive species within Avencas Marine Protected Area we can develop preventive measures and plan a set of actions to mitigate that growth,  preserve marine biodiversity and promote a more sustainable ecosystem to all species in general. In an ideal world, our model would be the guidebook to daily micro actions that would gradually  lead to small changes on the marine ecosystem evolution, and would promote a sustainable growth of several species. 

Impact Metrics
The model's impact relies on its quantification of the impacts of different variables and the real-world implications for marine conservation efforts. Due to its scalability, the model can be efficiently adapted to various scenarios, increasing its utility across different environments. In addition, the model's ability to predict the trajectory of species over time significantly enhances its ecological relevance. This predictive capacity may catalyze shifts in conservation policies and management strategies, ultimately contributing to improved species preservation and mitigation of invasive species proliferation.
Regarding specific metrics used to evaluate the model performance, in the accompanying notebook it is possible to see the Akaike Information Criterion (AIC) values for ARIMA, SARIMA and SARIMAX, which estimate the prediction error and thereby relative quality of statistical models for the dataset. SARIMAX outperformed the baseline model (ARIMA) for all seven scenarios tested.

Impact Measurement
The model has the capacity to play a critical role in shaping evidence-based policies. By providing robust and scientifically sound predictions about the future developments of endangered and invasive marine species, it aids in informed decision-making processes. Policymakers, with the aid of these predictive insights, can make better-informed decisions about where to focus conservation efforts. The model also offers a valuable tool for monitoring and evaluating the effectiveness of current policies and interventions, a crucial aspect of adaptive management. 
