# World Data League 2022

## Executive Summary Template
This executive summary is one of the mandatory deliverables when you submit your solution. Its structure follows the WDL evaluation criteria and it has dedicated sections where you should add information. Make sure your executive summary covers all the sections since it will be an integral part of the Insights Report and your evaluation. Make sure your content is relevant and straight to the point.
**There is no need to reach the maximum number of words.**

Instructions:

1. 🧱 Create a separate copy of this template and do not change the predefined structure
2. 👥 Fill in the Authors section with the name of each team member
3. ✏️ Write your executive summary - make sure you write to a non-technical crowd. You can refer to images that are in the Submission Notebook.
4. 📄 Fill in all the text sections
5. 🗑️ Remove this section (‘Executive Summary Template’) and any instructions inside other sections
6. ⬆️ Upload the .md file to the submission platform.

## 🎯 Challenge
*Predict Waste Production for its Reduction

## 👥 Authors
Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.
*Gonçalo Carvalho
*Manuel Borges
*Mariana Martins
*Pedro Fonseca

## ✨ Introduction (250 words max)
Provide a contextualization of the problem, together with an estimation of its size using real numbers and references.
*Write here*

## 🔢 Data (250 words max)
Explain what data you used (both provided by WDL and external) and improvements you suggest to those datasets. Explain how those improvements would lead to a better solution.
*We used the data provided by WDL, the Waste Collection Diversion Report, and some external data especially the Population of Austin across the years. For the dataset provided by WDL we sugest that there a little bit more explaining about the columns. Maybe this could help us have a better understanding of what the values mean and how they correlate.

## 🧮 Methods and Techniques (250 words max)
Tell us what methods and algorithms you used and the results you obtained.
*We started by cleaning the dataset using built in functions in jupyter notebook. Fot the modeling itself we realized forecasting by weeks and we started by checking if the data had trend with a Augmented Dickey Fuller Test and it didnt. Then we moved to building a SARIMA model using SARIMAX and we achieved a prediction for Load Weight with an error of only 9,37%. To better our results we moved to a Rolling Forecast Origin which better our results and the error was AAAAAAAAAAAAAAAAAAAAAA

## 💡 Main Insights (300 words max)
Explain what you discovered from addressing this problem, such as interesting facts or statistics.
*Write here*

## 🛠️ Product
### Definition
Define in **one sentence** what product(s) could be built out of the code you produced.
Example: A dashboard that assists in traffic control
*We can build a dashboard that predicts the waste weight for the next days/weeks/period and with that try to better their routes and distribution of the garbage.

### Users
Describe who would be the users of your product and for what purpose would they use it.
Example: Traffic controllers use the dashboard during their work to better plan where to dispatch resources
*Law makers could use it to decide when and where to invest related to garbage collection. Companies could accomodate more or less collectiion devices on periods where its predicted to have less garbage weight which can translate in not spending money.

### Activities
Describe what features your product has.
*Predicts the load weight

### Output
Describe what the product outputs to the users and how it does that. You can add mockups and/or visualisations.
Example: Location of the accident on a map and suggest the fastest route from the dispatch centre.
*AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

## 🌍 Social Impact Measurement
### Outcome
If the outputs are your immediate results, describe your long-term results. What do you want your product to achieve? What ''good'' are you creating?
Example: To decrease response time from dispatchers so that people in urgent need receive help faster.

*Decrease transportations for garbage collection when there is not enough garbage that justifies the deslocation.
*Decrease times when there is too much garbage on the streets waiting to be collected.

### Impact Metrics
From the outcome, define **2 to 4 metrics** that measure if you are achieving that outcome or not.
Example:
* Average Dispatch Time
* Average Distance from Accident Location and Dispatch Center
*AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

### Impact Measurement
Since you cannot wait to see the impact of your product, estimate it. You can do that by either using the estimations/predictions of your model, market research, products from proxy industries and/or similar locations, etc.

Example:
* *Based on model predictions*: Our model estimates a decrease of 6 minutes of the average dispatch time and a decrease of the average distance of 200 meters
* *Based on proxy products*: Similar studies in other cities show that the dispatch time can be decreased by as much as 13 minutes, depending on the traffic intensity of that city.