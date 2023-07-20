# World Data League 2023

## 🎯 Challenge

Determining The Main Mobility Flows in the City of Lisbon Based on Mobile Device Data

## Team Name

FhPioneers

## 👥 Authors

Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.

- Eduardo Silva
- Pedro Lopes
- Tomás Pereira

## ✨ Introduction (250 words max)
In recent decades, the Lisbon Metropolitan Area (AML) has experienced significant urban, social, and economic changes that have influenced mobility patterns and the modality of transports. Statistics show that even though Lisbon residents declined from 800.000 to 500.000, inhabitants in AML increased to 2.871.133 in 2021 (Censos 2021).

Considering the several approaches there could be to look into the mobility patterns in Lisbon Metropolitan Area (AML), our team choose to **look into the public transport system** and **how changes to it can affect the mobility** from and to the city of Lisbon. By analysing and modelling the characteristics of distinct areas regarding their public transport offer and traffic status, it is possible to better predict the impact the public transport improvements could have on people's mobility.

Our solution aims to create a model which can predict the flow of people for specific areas within the city of Lisbon. This prediction can provide important insights on the mobility of the city, and consequently can lead to better decision making by policy-makers.

## 🔢 Data (250 words max)
In order to create our model, we utilized a few of the datasets provided by WSL:

- **DS1 - DISPOSITIVOS MOVEIS GRELHA**: This dataset was used as the base for the remaining datasets, as in order to analyse the mobility within the city, we decided to adopt the strategy of dividing the map into a squared grid.
  **DS3 - DISPOSITIVOS MOVEIS QUADRICULAS**: This dataset provided us time series data regarding the disperson of mobile devices across the map grid, as we can assume the great majority of people crossing Lisbon have some sort of mobile device with them continuously. From this dataset and **DS1**, we also infered mobile device data regarding the adjancent squares of each grid square, which enabled us to consider the inter-square mobility relation.\

Moreover, we also extracted [data](https://dados.cm-lisboa.pt/dataset/estacoes-de-metro) regarding the subway/metro system in Lisbon, which enabled to create features for each of the square grids from **DS1**.

As for potential improvements, we can recommend the adoption of the hexagon as the space divider for future datasets. According to literature, dividing the a region in squares is not the most effective strategy as the centroids between adjacent squares can have different distances. With a grid of hexagons, the centroids have the same distance for all adjacent areas.

## 🧮 Methods and Techniques (250 words max)
The model developed aims at solving the regression problem of predicting the total number of active terminals in a grid square at a particular moment in time. It also makes uses of the minimum distance (in grid squares) to a metro station and the flow of adjacent grid squares.

For this purpose, we opted to use a LightGBM regressor model. LightGBM is a powerful and efficient gradient boosting framework that excels at handling large-scale datasets. It uses a tree-based learning algorithm, which is well suited for predicting numerical outcomes, making it a strong candidate for regression problems.

The algorithm also includes advanced features such as categorical features handling, early stopping, and monotonic constraints. These features can help improve the model's performance and prevent overfitting, which is especially important when dealing with high-dimensional datasets such as the ones used.

Additionally, LightGBM's ability to handle large datasets in a scalable way can save computational resources and reduce training time. If more features were incorporated in the future, LightGBM's ability to handle high-dimensional data and complex feature interactions could also be highly beneficial, as the models can identify important features that contribute to the target variable, allowing it to make accurate predictions.

As for the hyperparameter tuning, a 10 iteration hyper-parameter Bayesian optimization operation with Gaussian Processes was performed in which the following parameters were optimized: learning rate, maximum depth, number of leaves and estimator number. There are other customizable hyperparameters as well, however, their influence is not as noticeable as these one's, and as such only this group was selected for the optimization process.

## 💡 Main Insights (300 words max)
Our model achieved a MAE (mean absolute error) of 2.60, and considering that the total number of active terminals in a grid square can vary drastically from tens to thousands, we find this result very good. It is worth noting, however, this was obtained on only a portion of the data (around 1 million samples, with an 80/20% split for trainin and testing) due to computational and time restrictions. As such, the model's performance might differ, even increase, when trained with a greater amount of data (provided the proportions between features and the predicted variable do not change significantly), especially if accompanied by more rounds of hyperparameter optimization.

## 🛠️ Product
### Definition

An interactive dashboard which provides insights on the impact of modifications to the metro transport system.

### Users

Policy makers and public transport infrastructure teams could use the dashboard to better plan where to improve the metro transport system.

### Activities

* Predict the impact of modifications to the metro network in mobility flow;

### Output

A mockup of the product can be seen below.


![product mockup](https://lh3.googleusercontent.com/drive-viewer/AAOQEOTmxiFmIXmQOqwAlbdtmkjKWOKpzo5kou8NMlcE3ZSMUCplgwKY13Uz3-tlghhKOliqKwb4oGdLAj_AUH6P2b2jOyMVGg=w1826-h992)

As previously described, the product is an interactive dashboard application, where users could explore the map as Lisbon and evaluate the mobility flow dynamics. Our model would provide prediction on the flow of people for areas specificaly selected by the user, where there would be the chance to modify the current characteristics of the metro transport system of the areas. These changes could be adding a metro station or varying the frequency of tranportion on existing stations.

### Scalability

We believe our solution has great potential to provide insightful data on the impact of modifications to the current metro transport system, and would be more or less straightforward to implement on a real-world scenario. There is also the possibility to improve the current solution's performance and capacity, by adding more data regarding other transport modalities (bus) data, more demographic data (area total inhabitants), and ambiental parameter data (weather status, polution levels, air quality, etc.).

Moreover, our strategy to study the problem could also be extended to the creation of a longitudional model, which would consider the variation of such data across time, enabling policy-makers not only to study the impact of changes on a particular time instance, but also how it could affect the mobility flows across time.

Nevertheless, we forsee one of the road blocks could be the high flow variation between different times of the day, areas with very distinct demographic characteristics and even between seasons (winter versus summer), as the model could be unable to generalize well across the entire data distribution. A solution we could propose would be to create models fine-tuned to more strict scenarios, which could also provide the most insights on particular areas or times of day.

## 🌍 Social Impact Measurement

### Outcome

As the output of our product would allow policy makers to identify opportunities for improving the offer of public transport through the metro system to people which live, work or simply go to and form Lisbon.

Moreover, improving the public transport system could also lead to a decrease in the dependance on private car tranportation a great majority of people currently have. With this trend, waterfall of consequences would follow, as the relieve of pressure from Lisbon main access axis, the decrease in levels of polution and, at last, the improvement in quality of life for thousands of citizens from the Lisbon Metropolitan Area.

### Impact Metrics

We could measure the impact of our solution by looking into several metrics:

- Infrastructure improvements: How many metro stations are built, what is the reach of the metro distance in terms of area (square kilometers);
- Transport Accessibility: Average distance for inhabitants of a particular area to the public transports;
- Traffic improvements: Average delays in traffic in the main axis of Lisbon;

### Impact Measurement

Since our solution would be applied ideally on a case to case basis, to measure the impact one would need to measure the flow in key areas of the city as is, and then compare it to alternative versions in which, for instance, a grid square was changed so it would contain a metro station. In this manner, it would be possible to see how the flow changed in the different parts of the city.
