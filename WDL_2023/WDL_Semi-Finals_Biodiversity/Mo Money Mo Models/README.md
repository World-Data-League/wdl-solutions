# World Data League 2023


## 🎯 Challenge
Avencas Marine Protected Area: Predict the future of the local ecosystem and its species


## Team Name
Mo Money, Mo Models


## 👥 Authors
* David Raposo
* Duarte Pereira
* Martim Chaves
* Paulo Sousa


## ✨ Introduction
Avencas, near Lisbon, Portugal, was classified as a Biophysical Interest Zone (ZIBA) in 1998 due to its **high intertidal biodiversity**.

This classification **sparked controversy and conflict with locals**, leading to **non-compliance** with regulations. In 2016, after concerted efforts from local authorities, Avencas was reclassified as a Marine Protected Area (MPA). Marine Protected Areas (MPAs) constitute coastal management tools that aim to mitigate threats to the functioning of the areas and can be planned according to diﬀerent speciﬁc objectives.

Along with the reclassification, **public participation sessions and environmental awareness** activities were carried out, **improving regulation compliance**, particularly within the **fishing community**.

Certain activities, including aquaculture, water motor sports, fishing, and collection of animals, are prohibited unless authorized for scientific studies. (From Ferreira et al. 2017)

#### A Success Story
User management actions, including the implementation of pathways and information spots with area-specific rules at the beach entrance, have yielded positive results. An impressive 84% of visitors view the information spots favorably, and 76% agree with the location of the access pathways. (Challenge Brief)

#### A Problem Arises…
The intertidal ecosystem's recovery is slower than expected despite successful local usage control and reduced anthropogenic stress on the small Marine Protected Area (MPA). This slower recovery may be influenced by other factors, possibly related to the global climate changes observed. (Challenge Brief)


## 🔢 Data
The data used was from the AMPA_Data_Sample.xlsx file. We used the data of the sessile and mobile species. We also used air quality for openaq, but only for a very brief analysis.

Processing and cleaning was done:
- Date and Hour columns were processed due to sometimes different formats
- Joined the Sessile and Mobile species dataframes to create a single dataframe
- Spelling issues were found and resolved
- Removed columns that were mostly missing values or repeated species
- Changed data types of certain columns to numeric
- Analyzed values distribution
- Filled missing values with the previous chronological value

We tried adding air quality (to convey anthropogenic stress), but there wasn’t enough air quality data to do that, so only light analysis was done.

We created **two new features**, which were the number of days to the middle of the summer and the number of hours till 3 pm. From Ferreira et al. 2017 it was understood that the seasons had a great effect on the biodiversity of the MPA. So, to somehow encapsulate this, we added the number of days to the middle of summer as a feature. We also added the number of hours till 3 pm to encapsulate the effect that hour of the day might have, focusing on the, usually, hottest hour.

By doing all of these processing steps, we expect this to lead to a better solution, as we’re cleaning, standardizing, and adding information to the data. This way, it should be easier to use and retrieve insights.

## 🧮 Methods and Techniques
After performing some EDA, we modeled the presence of each specie based on the measured conditions (such as weather, water temperature and tidal information) and time related information was achieved by using a simple artificial neural network with some dropout layers since the model was prone to overfitting. Four different variants were tested by changing both the set of features provided and the targets. Solely based on the measured conditions and time information the three first models in the notebook were trained to predict either the concentration of each specie individually or groups of species. The fourth and final model received additional information about the more recent measurements of the species concentration to enrich the input information.

## 💡 Main Insights
Data formatting was very irregular and hard to process, with several fields being (probably) manually introduced. One of the biggest culprits of this issue were the species’ names. In order to provide better analysis in the future with less overhead on the data scientist’s side, we recommend standardization procedures to be implemented to these field reports.

When trying to predict species count, we obtained the following results (2nd model): 
- Mean Squared Error (MSE)  0.026536
- Root Mean Squared Error (RMSE)  0.162899
- Mean Absolute Error (MAE)  0.101349
- R-squared (R2)  0.070531
These were the feature importances obtained:
![Feat_imp_1](images/feat_imp1.png)


We can see that our engineered features time_to_15h and days_to_mid_summer_day had the largest impact in model performance. Supra/Middle tidal zones also have a significant impact on species' count.

As the results did not seem very promising, we also tried to predict the count by groups, with the addition of recent measurements of the species concentration to enrich the input information (4th model):

- Mean Squared Error (MSE)  0.030928
- Root Mean Squared Error (RMSE)  0.175865
- Mean Absolute Error (MAE)  0.095063
- R-squared (R2) -0.844035

![Feat_imp_2](images/feat_imp2.png)

We can observe again that our engineered features time_to_15h and days_to_mid_summer_day had a large impact in model performance, together with Supra/Middle tidal zones. Groups 1, 3, and 4 also had a significant impact.

Both the model and the input/output selection must be rethought, however several approaches were investigated here as a proof of concept.



## 🛠️ Product

Introducing our innovative **interactive app**, designed to visually represent the coverage of marine species in the Avencas Marine Protected Area (MPA). This powerful tool not only enhances public relations but also contributes to the improvement of biodiversity, ensuring the long-term health and sustainability of the MPA.

The **primary objective** of this app is to captivate and engage both locals and visitors, emphasizing the significance of marine life and motivating them to become champions of environmentally friendly causes. By doing so, we aim to create a collective pressure on policymakers to drive meaningful, large-scale changes.

Marine beings within the MPA play crucial roles in multiple ways, which can be highlighted through the app:

* Biodiversity: The ocean is a remarkable ecosystem, hosting diverse sessile organisms such as algae, coral, and sea slugs. These organisms create intricate neighborhoods that support a wide array of life. Coral reefs, often referred to as "rainforests of the sea," are particularly rich in biodiversity, offering a fascinating sight to behold.

* Food Source: Each organism within these complex marine neighborhoods plays a vital role. Some serve as food sources for larger beings, such as algae, mussels, and barnacles, while others function as efficient clean-up crews, like the remarkable fungi. Recognizing the importance of every organism is crucial for maintaining the cleanliness and health of the marine environment.

* Carbon Sequestration: Algae and coral also play a significant role in carbon sequestration. They absorb carbon dioxide and release oxygen, actively contributing to the fight against climate change. These organisms not only exhibit beauty but also work diligently to keep our planet cool.

To ensure accessibility, the app will be web-based, offering a public website with dashboard functionalities. Researchers and biologists will have the opportunity to access additional features through credential-based authentication, enabling them to update and consult the website's information. Additionally, we can develop other interactive applications, such as a sea-side screen, to further disseminate knowledge and engage the public.

Together, we can leverage technology to raise awareness, foster environmental stewardship, and safeguard the precious marine life in the Avencas MPA. We can make a significant impact on the preservation of our oceans and the planet as a whole.


### Definition
An **interactive, sea-side screen** and an **online web app* that assist in species’ tracking and public knowledge dissemination.


### Users
Researchers and biologists will be able to use this app to keep track of the species residing in the Avencas MPA.

Visitors, locals, and the general populace can be informed of the importance of the marine ecosystems through our app, which could have a positive impact in policy making.


### Activities
* Predicts species’ count
* Predicts species’ grouping


### Output
Describe what the product outputs to the users and how it does that. You can add mockups and/or visualizations.
Example: Location of the accident on a map and suggest the fastest route from the dispatch center.


### Scalability
Our interactive app for representing sessile species coverage in the Avencas Marine Protected Area (MPA) is highly scalable. It is web-based, ensuring easy access and distribution across various platforms and devices. The app caters to both the general public and researchers, with credential-based authentication granting access to additional functionalities for data collection and analysis. Furthermore, the potential for developing physical interactive applications, such as sea-side screens, expands the app's reach. The solution can be continually updated and expanded to incorporate new research and data, ensuring its long-term relevance and scalability. 


## 🌍 Social Impact Measurement
* User Engagement - monitoring app usage, such as website visits and other interactions.
* Public Awareness and Perception - conduct surveys or polls to assess the public’s knowledge and awareness of the importance of marine life and the MPA.

### Outcome
Pressure policy makers and population to support the improvement of biodiversity.

### Impact Metrics
* Long-term Biodiversity Trends -  long-term trends in species’ coverage and biodiversity within the Avencas MPA;
* Policy Influence - policy discussions and changes related to marine conservation and protection in the Avencas MPA;
* Community Involvement Trends - participation in conservation activities, such as volunteering, beach clean-ups, or advocacy initiatives.

### Impact Measurement
We have not found information on similar app’s influence. It seems to be an innovative technology. :)

