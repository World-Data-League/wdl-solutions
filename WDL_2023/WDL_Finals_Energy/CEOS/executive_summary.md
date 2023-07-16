# World Data League 2023

## 🎯 Challenge
*Energy communities inclusive of residents vulnerable to energy poverty*


## Team Name
CEOS - Champions Engineer their Own Science


## 👥 Authors
* Ana Maria Sousa
* Duarte Rodrigues
* Mariana Sousa
* Mariana Xavier
* Ricardo Brioso


## ✨ Introduction 
The world faces a severe **energy crisis** with the price of natural gas, electricity and oil reaching record highs. Higher energy prices have resulted in painfully high inflation, leading to factory closures and pushing families into **poverty**. The current crisis could accelerate the adoption of cleaner and sustainable **renewable energy** like wind and **solar**, as well as invest in improving the robustness and independence of the energy production and supply infrastructure to better serve local communities and reduce the inequalities observed. This falls under three Sustainable Development Goals (SDGs) defined by the United Nations:
* affordable and clean energy;
* reduce inequalities;
* sustainable cities and communities. 

The city of Ghent is no stranger to these problems as it has huge ambitions in the fields of energy efficiency and **sustainability** and has been one of the ambassadors to help announce and implement the SDGs in Belgium. The city intends to study and propose the creation of **energy communities**, which are an effective way to allocate and distribute energy in an equitable manner. The creation of these communities has to take into account a considerable amount of variables: the opportunities for clean energy production (from roof properties and solar exposure), energy usage and financial conditions of those benefiting from these communities.

At CEOS, we set ourselves to do exactly this! Our goal is to leverage the data to propose how energy communities can be formed within the city, mitigating the two presented problems: unsustainability of current energy production and energy poverty.


## 🔢 Data
The data provided by the city of Ghent and the energy company Fluvius includes:
* **3D model of Ghent:** Geographical data along with building characteristics to assess sun irradiation and potential for energy production. This is the main dataset for the challenge, as it provides meaningful information along with the necessary geographical notions;
* **Energy consumption:** Three datasets - by economic sector, month and street. Street-level consumption data provides insights into consumption trends in specific locations in Ghent that are of great importance, while the remaining two lacked location-specific information;
 * *Energy production:** Four datasets - local and decentralized energy production, storage devices and EV charging points. Only decentralized energy production and EV charging points were utilized due to the lack of location-specific information in the remaining datasets;
* **Financial factors:** One dataset on average income per sector and one dataset on current rent prices in different locations, which together allow us to predict the economic situation of the people living in each location.

As seen above, there was plenty of information that in the end could not be considered for the solution as there was no way to merge it with the geographical locations. Therefore, a suggestion would be to improve these datasets by adding an extra level of granularity which would enrich the solution. Moreover, along with buildings, it could be worth having 3D data of open spaces such as fields and parking areas, which could be potential candidates for the placement of solar panels and energy production.


## 🧮 Methods and Techniques
The development started with an exploratory data analysis (EDA) which allowed us to identify the datasets that could be merged together to form the final dataset and also the most useful features for the upcoming model. Data cleaning was also performed along with filtering for Ghent only.

The main goal was to propose different energy communities that could be formed within the city. This was interpreted as a **clustering** problem along with the **optimization** of the number of clusters which define the number of proposed communities.

The methodology uses the **k-means algorithm** to perform the clustering task. However, this algorithm could not be simply applied since it uses the Euclidean distance which does not fit our goal. For instance, in the same cluster/community, we want the geographical distance to be small, but we want to have a large variety of housing types and financial backgrounds to have a balanced community. Thus, a **custom score function** was developed that decreases with geographical proximity and with rent/income/estimated energy produced/energy consumption increased diversity. A set of weights was given to each of these features when computing the distance, to control their importance. Moreover, the score value is further decreased if there is energy to spare between the buildings it is comparing (reward system). Finally, the **Elbow method** was used to determine the optimal number of clusters.

In the end, we were able to obtain a possible division of Ghent municipality in **8 sustainable communities**.


## 💡 Main Insights
During the EDA of the various datasets, several intriguing findings emerged:
* **Differences in average income:** From the average income by postal code values we found that there are considerable differences between the different areas: higher incomes are seen in the postal codes 9031 and 9051, while lower incomes are seen in postal code 9040 which can mark it as an area of possible lower financial capacity. In addition, at 9031, a major social discrepancy is seen in terms of income, marking it as an area of big social inequalities, worsened by the fact that it presents the highest income values at the same time.
* **Higher power consumption by personal infrastructures:** Considering the power consumed by personal vs company infrastructures, it was observed that personal access points have a higher need for power as they consume around 1/3 of the total energy but only account for 1/7 of the total access points. Thus, the application of alternative renewable sources of energy (like solar power) should ideally be made on personal infrastructure.
* **Seasonality in gas consumption:** The consumption per month clearly shows a higher gas consumption in winter and spring months suggesting that gas was likely used for heating purposes.
* **Varying storage capacities:** Considering energy storage systems, we verified that from 2019 to 2021 the capacity values were quite stable and from then on the storage capacity started to vary and increased significantly.
* **High production of solar energy:** Regarding local energy production, we observed that solar energy constitutes around 99.5% of production devices, being by far the most used type of technology and also the one that has the highest mean of installed power.


## 🛠️ Product
The product is a **customizable tool** for *identifying and forming energy communities in different cities or locations**. This tool enables users to enter data that's similar to the types previously described, specifically data concerning potential buildings or entities suitable for renewable energy implementation. The tool utilizes the established model to execute a clustering analysis to identify the most efficient groupings, thereby optimizing the formation of energy communities. The product provides flexibility by allowing users to choose between optimizing the number of clusters (energy communities) or selecting a fixed number. Additionally, users can customize the importance of each feature to define what constitutes a good energy community based on their specific requirements and goals.


### Definition
The product is a web-based platform or **website** that offers a user-friendly interface for **energy community planning, clustering, customization and visualization**.


### Users
The primary users of this product would be **urban planners, energy consultants, local government officials (OCMW), and stakeholders** involved in sustainable energy planning and community development. They would utilize the tool to analyze and identify potential energy communities within a city or location based on available data. The product allows users to assess and evaluate the feasibility and effectiveness of different energy community configurations, considering factors such as proximity, energy generation potential, energy consumption patterns, and other relevant features.


### Activities
The product features of the web-based platform include:
* **Data Input:** Users can upload or input relevant data related to potential buildings or entities, such as location coordinates, energy consumption, energy generation potential, building types, and other relevant attributes.
* **Customization**: Customization of the importance and weights of different features to define the criteria for forming energy communities. Define also the number of ideal clusters or opt for optimization instead.
* **Optimization:** The product can output what it considers to be the optimal number of clusters to be formed.
* **Clustering Analysis:** The product performs clustering analysis using k-means to group the potential buildings into energy communities.
* **Visualization:** The results are visually presented on an interactive map or dashboard.
* **Export:** Users can export the results, including the clustering outcomes, community characteristics, and associated data, for further analysis or reporting purposes.

Please find in the Jupyter Notebook, in the Visualisations section, a link to a support diagram of our idea.


### Output
The product outputs a **visual representation of the potential energy communities** within a city or location. It shows visualizations that depict the clustering based on the user-defined parameters, such as feature values and the number of communities. If the resulting layout of the communities is of interest, a list of which building belongs to each group can be exported.


### Scalability
The solution is designed to be **highly scalable** and easily implemented. The modular nature of the code allows for the **integration of additional datasets** and the **customization** of clustering algorithms. Besides, although it was developed for Ghent city, there is **no constraint on geographical location**. Therefore, the solution can be adapted to different cities or locations by providing the necessary data inputs specific to each area. However, scalability may be affected by the availability and quality of data for different locations. Ensuring data availability and correctness, as well as incorporating local context and regulations, may require additional effort and collaboration with relevant stakeholders.


## 🌍 Social Impact Measurement

### Outcome
Our solution aims to assist Ghent municipality in understanding and better visualizing how they can implement the desired energy communities in the city. With our current product and results, they can control parameters such as feature importance and the number of communities and visualize the impact it has on the proposal. In the end, the outcome are **important and meaningful insights in the form of community proposals**. These communities layout encompass the entire city, promoting the innovation of the city's energy grid and eletricity distribution. This optimization will advance towards climate transition and ecological/environmental sustainability. It is important to note that although it was developed for Ghent municipality, there are no location constraints, making the product highly scalable and bringing an even bigger impact by being used for different cities.


### Impact Metrics
* Number of energy communities formed
* Percentage of energy consumed/produced that is shifted to renewables
* Decrease in energy prices
* Decrease in the number of people dealing with energy poverty


### Impact Measurement
As stated in the recent State of the Energy Union report, at least 2 million people in the EU are already involved in more than 7700 energy communities. As the end users understand the outputs of our product and start to apply them, this number is expected to increase at a varying rate. As a consequence, there should be an increase in the usage of renewable energy sources at a rate at least higher than the current one (16% per year).

From what has been seen in energy communities implemented so far, it is expected a decrease of around 30% in energy prices, giving many people facing poverty the ability to afford it.

The references to the numbers mentioned can be found in the Jupyter Notebook, in the dedicated Reference section.