
# World Data League 2022

## 🎯 Challenge
Finals- Identification of Dark Ecological Corridors

## Team Name
Pablitos 

## 👥 Authors
* Joana Rocha Camargo 
* Hiba Laziri 
* Beatriz Barretto 
* Marcelo Moreno 

## ✨ Introduction 
With the concern of creating a more sustainable world, governments and individuals are seeking the most efficient and functional ways to implement changes in society to reach said goals. One of the concerns is artificial light pollution, where lights at night harm animal activity. Bats are especially impaired, as they have to avoid streetlights by maintaining a distance of “up to 50 meters”, decreasing their area to access food and other resources. There is also a consequence to humans, as the increase of “between 2 and 10 photopic lux” confuses the body’s system by simulating day, as it does with bats’, decreasing melatonin production (Challeat, 2021). Many countries have already addressed this issue, proving its importance. In Portugal, road lights in quieter areas are activated by movement, so that lights are switched on only when there is someone there to benefit. In the German village of Doerentrup, road lights are switched off at night to save energy and reduce carbon emissions, but residents can use their phones to switch them back on for short periods of time, if needed (The royal commission on environmental pollution, 2009). Taking into consideration that “88% of the European surface area” is affected by light pollution, we will be working with the Bristol City Council to decrease consequences by creating dark corridors, paths where streetlights will be kept off to lessen the human impact on the environment and increase and maintain the biodiversity of the city, with a focusing on bats (Falchi et al. 2016).

## 🔢 Data 
Data on observations of bats in the city of Bristol was the most important information to use as a starting point of which areas of the city should potentially have their lights turned off. Then, data on sightseeing of moths was used to determine where the bats need to go, as their main food source. Locations of trees and wildlife corridors in the city as well as data on streetlights was used to determine where bats could possibly hibernate or shelter, while taking into consideration that they tend to be around very diverse nature habitats, so random trees and bushes would not be beneficial to them. Improvements were made to these datasets by giving numerical values to categorical variables in the abundance column, such as “several”, “present” and “abundant”. It would have been beneficial to have more data points with different times of the year and areas of the city. We found that many years had only one datapoint or multiple around the same time of year, making it not representative of the seasons. A crime by ward in Bristol dataset and a traffic accidents dataset were also used to calculate safety scores for each of the grid references, to also take into account the possible impact on safety by turning off the lights. The traffic dataset was well structured for use, but the crime dataset could be improved by providing a more specific location for the crimes instead of just the ward where it happened. Because for all the other datasets we were using the grid reference, we had to include the general crime index of the ward each grid belonged to, making it less specific.

## 🧮 Methods and Techniques 
A fitness function was implemented to optimize light configurations in grids and a genetic algorithm was used to find the optimal solution for all grids in the city. Since bats go into hibernation during winter, we provided one solution for winter and one for summer, to account for the seasonality of bat’s movements.

The fitness function consisted of a bat friendly score, representing how appropriate for bats an area was, and a safety score, showing the safeness of the area. The fitness function was optimized to define the best light configuration for a grid containing bats and for its 8 neighboring grids, accounting both for bat well-being and citizen’s. Since the function can assign more than one configuration to the same grid, we also used a genetic algorithm to find the best scheme for all of the city’s grids at once. It assigns several random light configurations to the disagreeing grids, selects the options that wield the highest value for the fitness function, performs mutations and crossovers among those options, and finally selects the best combination.

For summer, there is also the need to create a path leading bats to their prey. First, we selected the grids that contained at least 100 moths or bats. Then, for the bat grids, we found the three closest moth grids and made a straight line connecting them. Finally, we found all of the grids the line would pass through and used their safety score to determine which line would be best to create the dark corridor.

## 💡 Main Insights 
While tackling this problem, we discovered that only a small amount of data was available to measure the presence of bats and moths in many areas. In fact, just 3 data points were available in 2021 and none for 2022. Greater data collecting for bats, and biodiversity in general, is critical for creating an accurate model and developing biodiversity preservation projects. Analyzing the data, we discovered that 68% of the bats were protected throughout the last 15 years and another 27% were local species, proving their importance to the city.

We also discovered that addressing biodiversity problems is challenging since many factors have to be considered, a reason why the dark corridors present in the city have yet only reached a small number of bat communities. To find the best possible light configuration, the abundance of bats in the region is not the only determinant factor, the safety of humans must be considered. These types of problems also require a deep understanding of bats’ habits and their relationships with the habitat, therefore, educating people about these matters and the importance of animals in sustaining a balanced ecosystem is critical to raise awareness and promote the conservation and development of friendly projects.

It is also clear how natural life is starting to get intertwined with urban life. Creating dark corridors should only be a temporary solution to protect bats since cities are gradually expanding their borders. The ideal option would be to have bats in green areas where they can thrive without being impacted by urbanization. Dark corridors are also not the only measure that can be taken to help decrease bat impact, other measures like reducing the trespassing of light, decreasing light intensity, installing lights at lower heights so that it illuminates only the target area, and even the reflectiveness of surfaces which contributes to the spread of light (The royal commission on environmental pollution, 2009).

## 🛠️ Product
### Definition
An informative website explaining the objective of the project and its importance, supported with a map of Bristol which indicates the lights that will be turned off depending on seasons to increase the number of dark corridors for bats and decrease light pollution, ultimately increasing biodiversity.

### Users
The users of our product would be citizens of Bristol and the Bristol City Council. These individuals would be able to inform themselves about the bat community around them and discover the streets of Bristol which have the lights turned off during the night. Furthermore, there will be a section of the website where users can potentially turn on the light in their current location in case of emergencies, in an effort to maintain citizen’s safety. It is expected that citizens will make an effort to contribute to the project and its goals by avoiding the designated dark areas at night and only turning on the lights when strictly necessary.

### Activities
* A map of Bristol showing which areas have the lights turned off at different times of the year.

* Information about the bats in Bristol and their benefits to the environment.

* A feedback area where citizens can make complaints/comments with important considerations, a place where they could potentially explain why lights in a certain region shouldn’t be turned off or where they can suggest new places to turn the lights off.

* A page where users can turn on the lights on specific streets, in the case of danger or an emergency. To do this individuals will have to add their email, name and street address or light code and later fill a questionnaire explaining why the lights had to be turned on, as this is something that should be done only when strictly necessary. The website would be connected to the centralized management system (CSM) so that the lights can be activated through there.

### Output
The product outputs the user's personalized safety score by processing the information inputted by the user into the app and utilizing the safety index as well as other variables to predict this value.

## 🌍 Social Impact Measurement
### Outcome
We hope our product and algorithm will increase the level of support from citizens of the community, increase the biodiversity of the city and increase populations of bats as the artificial light pollution decreases.

### Impact Metrics
* Increase in number of bat sightings and populations in the community, hence decreasing the number of moths.

* Increase in number of official dark corridors.

* Decrease in artificial light pollution by measuring the brightness of the sky and visibility during the night.

* Increase in biodiversity, analyzing the number of different species and abundance of species.

* Decrease in the city’s electrical expenses. The cost of implementing the CSM should be reimbursed in 4 to 5 years (The royal commission on environmental pollution, 2009).

* The law that protects all bat species, their breeding sites and resting places will be better respected ([gov.uk](https://www.gov.uk/guidance/bats-protection-surveys-and-licences#:~:text=All%20bat%20species%2C%20their%20breeding,to%20survey%20or%20conserve%20them)).

### Impact Measurement
Based on the market research, we expect the bat populations to increase and artificial light pollution to decrease as we add numerous dark corridors to the city. As mentioned in the Grasping Darkness paper by Samuel Challeat and others, “species depend on regular day and night alterations” and light pollution can extend past cities due to the “light halo phenomena”. With the use of our model, the halo will become smaller and the true day and night alterations become clearer, creating a better environment for the bats and other species to take on their everyday tasks such as hunting, pollinating and preparing themselves for winter hibernation. As these changes take place, the natural habitats around Bristol will increase in diversity and prosper as it has not done in hundreds of years, taking into account that “outdoor lighting has grown by between 3% and 6% per year during the second half of the 20th century” (Hölker et al. 2010). In fact, the implementation of these night corridors will extend the activity duration of rodents, which are mostly nocturnal, and whose activity tends to be reduced by nighttime lighting, while that of diurnal birds was prolonged, with singing and foraging starting earlier, thus disturbing the food chain. This project will also enhance the health of the people of Bristol since several studies have shown that light pollution has a negative impact on our sleep and anxiety which may result in headaches, anxiety and fatigue. ALAN can lead to even more serious illness since light pollution is thought to disrupt the hormonal system and melatonin secretion in humans, affecting sleep, libido, aging, and the potential development of a tumor. “LAN acts directly on physiology, or indirectly by causing sleep disorders and deprivation, that may have negative effects on several disorders such as diabetes, obesity and others” (Haus and Smolensky, 2006, Bass and Turek, 2005). In conclusion, we predict that with this project the lives of the bats, wildlife and citizens of Bristol will improve significantly and become healthier due to the changes in conditions caused by the dark areas created by our model.



**Resources:**

[https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/228832/9780108508547.pdf.pdf](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/228832/9780108508547.pdf.pdf)

  

[Ecology and Society: Grasping darkness: the dark ecological network as a social-ecological framework to limit the impacts of light pollution on biodiversity](https://www.ecologyandsociety.org/vol26/iss1/art15/)


