# World Data League 2023

## 🎯 Challenge

Energy communities inclusive of residents vulnerable to energy poverty


## Team Name

Data Warriors


## 👥 Authors

* Clara Pedroso

* Gonçalo Ferreira

* João Anacleto

* Madalena Diniz


## ✨ Introduction 

Ghent, Belgium, is a city with a population of approximately 260,000, that is dedicated to building a greener and more sustainable future. The city has set ambitious climate mitigation and adaptation goals and aims to achieve all Sustainable Development Goals (SDGs), with a particular focus on SDG 7 - affordable and clean energy. Since 2017, Ghent has actively promoted the SDGs and has implemented various initiatives to increase energy efficiency, promote sustainable practices, and address energy poverty.

To further contribute to these goals, Ghent is exploring the formation of energy communities, which play a key role in promoting equitable energy allocation and distribution. By combining data on energy consumption, vulnerability, and green energy potential, Ghent aims to identify the optimal locations for establishing these communities. The insights gained from this analysis will inform decision-making processes and help guide the city's efforts to form energy communities successfully.

Overall, Ghent is committed to its energy transition journey and recognizes the importance of engaging citizens, organisations, the business community, and educational institutes to achieve sustainable action. The city's initiatives, including the formation of energy communities, are critical steps towards creating a more sustainable and resilient future for all its residents.


## 🔢 Data

*WDL* Datasets used:

- *energy_consumption_street_level*: Consumption data per street: consumption data per energy (electricity/gas), (in/out) and per main municipality at street level per year. 2011-2021
- *energy_decentral_production*: List of decentralised energy production installations linked to the distribution network 
- *energy_storage_systems*: Energy storage systems connected to the distribution network 
- *ghent_rent_prices*: Rent price information for Ghent zip codes

*External* datasets used:

- *Ghent shapefile*: geopandas shapefile that divides the city of Ghent into polygons

To improve the solution, it would be beneficial to have a postal code column in all datasets for easier merging. Additionally, we wanted to include the income in our solution, however the dataset had many missing values and we had no way to connect it to the remaining datasets. Also, it would’ve been beneficial if the income dataset had more details, beyond sector categorization. 

On another note, considering additional socioeconomic indicators would offer a more comprehensive understanding of energy community formation. These improvements would lead to better-informed decision-making and optimal location selection for energy communities in Ghent.


## 🧮 Methods and Techniques

During data preprocessing, we had to merge all the files that information that we considered valuable into one using variables like “Postal code” and “Year” to do so. After we finally managed to complete that a new variable,that we found relevant for the whole context of the problem, was created, ”money spent on energy %” which corresponds to the percentage of the rent that is allocated to energy expenses and that is something we wanted to minimise. To conclude the preprocessing, we scaled the data, using standardScaler, to make the clusters. Using the k-means method we made the clusters that we needed to separate the communities based on the variables we chose, but these were not the final cluster since they were separated into “good” and “bad” groups and that is not our objective. To solve this problem we had to optimise those clusters, so they represented sustainable communities.


## 💡 Main Insights

After investigating the problem and searching for better results, we discovered a strong relation between the variables used to evaluate and form the energy communities in Ghent. Specifically, we observed that areas that were *more sustainable* in terms of energy usage, as well as areas with *lower sustainability*, were *closely located with each other* based on their postal codes. These patterns are closely related to the *rent prices in the area*, and consequently also related to the *percentage of rent allocated to energy expenses*. Additionally, the distribution of maximum power took into account the energy consumption in each area, which didn’t leave us much room to improve each specific area in Ghent. 

After noticing these interrelations, at the time of creating the clusters, we tried to optimise the creation of the communities, but we didn’t get better results, in fact, they got worse. That’s why we believe that the communities should be the initial 3, displayed on the map, without any need to be optimised since that would not only worsen the energy situation but also create communities with areas that are not close to each other which doesn’t make sense.  


## 🛠️ Product

### Definition

A *dashboard* featuring a map that showcases the energy communities and provides data on their pre- and post-community energy statistics production and consumption, energy exchanges with other communities, and cost savings.


### Users

The users would include *city officials, policymakers, researchers, energy experts*, and *community members*. They would utilise the dashboard to gain insights into the performance and impact of the energy communities, assess the effectiveness of energy transition initiatives, and make informed decisions regarding community development and resource allocation. 

This would enable users to *monitor* energy production and consumption patterns, analyse the success of energy exchanges between communities, evaluate cost savings achieved, and identify best practices for replication in other areas. 

Ultimately, the users would employ the dashboard as a tool to *promote transparency, facilitate data-driven decision-making*, and *foster community engagement* in sustainable energy practices.


### Activities

The dashboard would include the following key features:

1. *Map Visualization*: Visual representation of energy communities on a map, allowing users to easily locate and explore different communities.
1. *Pre- and Post-Community Energy Data*: Information about the energy situation before and after the formation of each community, with data on energy produced, consumed, and changes in energy usage patterns.
1. *Energy Exchanges*: Access to data on energy exchanges between communities, such as energy sent or received from other communities, to provide insights into collaborative energy sharing and distribution.
1. *Cost Savings Analysis*: Monetary savings achieved in terms of the percentage of rent allocated to energy expenses, enabling users to evaluate the financial impact of community formation.
1. *Comparative Analysis*: Compare the performance and outcomes of different communities, facilitating the identification of best practices and lessons learned for replication in other areas.
1. *Data Filters and Customization*: Filter and customise the data based on specific criteria, such as time periods, location, or community characteristics, to tailor the analysis to the user’s specific needs.


### Output

Here are the product outputs and how they are delivered to the users:

1. *Energy Community Locations*: The map displays markers or icons indicating the locations of energy communities within Ghent. Users can visually identify the communities on the map.
1. *Information Pop-ups*: When users click on a specific energy community marker, a pop-up window appears, providing information about that community. This includes data on energy production, consumption, energy exchanges, and cost savings.
1. *Comparative Analysis*: Section that allows users to select and compare multiple energy communities, based on the statistics of each.
1. *Data Filters and Customization*: Interactive controls for users to filter and customise the displayed information. Users can apply filters based on specific metrics, or community characteristics. The visualisations and data on the dashboard dynamically update based on the selected filters, allowing users to focus on the desired information.
1. *Insights and Trends*: The dashboard could include additional visualisations, such as trend lines or heat maps, to present insights and trends in energy production, consumption, and savings over time. These visual representations help users identify patterns, assess progress, and make informed decisions.

Overall, the output would be a *map* with *energy community markers, interactive pop-ups* with detailed data, and *side-by-side visual comparisons*, to enhance the user experience and facilitate data interpretation.


### Scalability

The dashboard can be *scalable* and *adaptable* to help other cities *implement their own energy communities*, provided they have similar data availability. However, like any project, there are some important steps and possible issues with implementation to consider:

1. *Scalability*: This can be achieved by optimising data storage and retrieval processes, leveraging efficient data visualisation techniques, and utilising scalable infrastructure resources.
1. *Data Integration*: The integration of diverse datasets from different sources while ensuring data compatibility, data quality, and real-time data updates can be challenging. Implementing robust data integration processes and data standardisation techniques can help address these issues.
1. *User Adoption*: Encouraging user adoption and engagement with the dashboard is essential for its success. Educating and training users on how to effectively utilise the dashboard, interpret the visualisations, and extract meaningful insights are crucial steps. Conducting user feedback sessions and incorporating user suggestions for improvements can enhance usability and increase user adoption rates.
1. *Data Privacy and Security*: Safeguarding sensitive data is vital. Implementing robust security measures, encryption techniques, and user access controls can protect the privacy of individuals and prevent unauthorised access to sensitive data.
1. *Collaboration and Stakeholder Engagement*: Collaboration among stakeholders is crucial for successful implementation. Regular communication, workshops, and engagement initiatives can facilitate collaboration and ensure that the solution aligns with the needs and objectives of all stakeholders.

Addressing these challenges requires careful planning, collaboration, and continuous improvement. Regular monitoring and evaluation of the solution's performance, feedback from users, and adapting to changing requirements will contribute to its long-term success and scalability within the scope of the energy communities in Ghent.

## 🌍 Social Impact Measurement

### Outcome

The long-term results of the dashboard aim to *contribute* to the creation of a *sustainable and equitable energy landscape* within Ghent and create positive change. Here are the desired outcomes:

1. *Increased Adoption of Renewable Energy* by providing transparent information on energy communities' performance and showcasing the *benefits and savings achieved* through community-based renewable energy production.
1. *Energy Efficiency and Demand Reduction*, users can identify best practices, learn from successful energy communities, and make informed decisions to optimise their energy usage, leading to *reduced energy consumption and environmental impact*.
1. *Enhanced Social Equity* by highlighting the positive impacts on communities' energy situations and cost savings, the product can contribute to bridging the energy divide and ensuring that vulnerable populations have access to affordable, clean energy solutions.
1. *Community Engagement and Empowerment* by providing the users with valuable information about energy communities, fostering community engagement and encouraging active participation in the energy transition. 
1. *Decision Support for Policy and Planning*, by providing comprehensive data and insights, decision-makers can make evidence-based decisions, allocate resources effectively, and shape policies that support the growth of energy communities, renewable energy generation, and sustainable practices.


### Impact Metrics

Based on the desired outcomes outlined earlier, these metrics can be used to measure whether the product is achieving those outcomes:

1. *Average % of rent allocated to energy expenses* to analyse if the energy expenses are diminishing and the monetary savings the community is achieving in a monthly basis over time. The goal is to minimise this metric
1. *Average Energy Savings* achieved by energy communities, to reflect the cost-effectiveness and efficiency of the community-based renewable energy initiatives over a specific period, ideally monthly basis.
1. *Average Energy Consumption* to reflect the effectiveness of energy efficiency measures implemented by communities and indicate the success in reducing overall energy demand over time.
1. *Average Energy Production*, similarly, this reflects the success of community-driven renewable energy initiatives and the contribution towards achieving sustainable energy goals.
1. *Community Engagement and Participation* to measure the extent to which residents, businesses, and organisations actively contribute to energy communities, are willing to participate in decision-making, and adopt sustainable practices, which can be evaluated through surveys, participation rates in community meetings, and the number of individuals involved in governance or management tasks within energy communities.


### Impact Measurement

In the context of the creation of energy communities in Ghent, here are some estimations regarding the outcomes of this solution in terms of:



* *Based on our model* we intend to minimise the percentage of rent that is allocated to energy expenses and we estimate that this percentage could decrease in a range of 5% to 10%, initially.

* *Based on similar initiatives* the energy savings achieved by participating communities ranged from 10% to 20% and the consumption could be reduced up to 20%, through the implementation of renewable energy generation, energy efficiency measures, and optimised energy consumption patterns. This initiative could also lead to an increase in local renewable energy production within these communities ranging from 10% to 20%, taking into account the implementation of solar installations, and other renewable energy technologies.

These estimations simply provide a general indication of the potential impact of the product. However, to obtain more accurate estimations and assess the actual impact on energy savings, consumption, and renewable energy generation in the context of Ghent, further research, specific data analysis, and consultation with experts are necessary.

