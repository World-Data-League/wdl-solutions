# World Data League 2022

## 🎯 Challenge
Predicting a safety score for Women in Costa Rica

## 👥 Authors
Catarina Bento
Cátia Correia
José Luís Mourão
Lúcia Moreira

## ✨ Introduction (250 words max)

The challenge proposed is one of serious importance: safety for women (in this particular case, women of Costa Rica).
In 2022, we still see flagrant signs of violence against women and the numbers don't seem to be improving in a desirable way (1).
What's worse, these crimes happen in broad daylight and in public spaces.
Looking at the study by COMESCO (3), we can surmise that crimes against women are very particular in their nature: a sense of power over the victim and of impunity
turns the attackers bold, which is why the work of improving women's safety in public spaces is of paramount significance.
Protecting women's dignity and freedom to live unemcumbered will have many positive effects on society (economical, social and cultural) but most importantly,
will give them their right to exist free of fear.

References:

(1) https://www.unwomen.org/en/digital-library/publications/2017/10/safe-cities-and-safe-public-spaces-global-results-report
(2) https://observatoriodegenero.poder-judicial.go.cr/
(3) https://infosegura.org/en/2021/06/18/violence-against-women-costa-rica-2020/


## 🔢 Data (250 words max)

We used all of the data provided by WDL:

- geographical data: looking at the data, we opted to use only the variables we felt could have an impact on our analysis -
	areas of public use, commercial centers, education, entertainment, green areas, healthcare and security where a simple counter with the number of available areas per dictrict is used.
- sexual harassment: this dataset was analyzed but ultimately discarded since the data was only for crimes reported in 2021
	and the volume of data very low (only 3 districts out of the 11 in San Jose).
- crimes against women: since this was the only dataset where we had records year by year, we used it as the "main source" for our analysis, and only selected crimes against women. For each 'crime' category we have summed the number of crimes reported by district and in a year (or tirmester).
- social-economic/demographic data: we believe that the status of a population will have some impact on the actions taken by it, so we also used the rates and index values
	in our analysis

## 🧮 Methods and Techniques (250 words max)

We have constrained our analytical analysis to San Jose due to higher availability of data. We have focused to predict the index at a district level. For that, initially we have used standard data analysis to gain insights towards the data.
To reduce the dimensionality of data, we used factor analysis of mixed data (FAMD). From the more than 40 variables in our work,
	we were able to reduce dimensions to only 6/7 features and we were able to create an index out of the two first dimensions and then further normalizing it between 0 and 1. Where 1 means an insecure district in San José and 0 a district with no secuirty issues in general for women.
To predict the index into the future, we used a lightGBM model where the input variables were the district, year, index and the indexes from previous years. We were able to predict the index with an average MAPE of around 40 % so there is still room for improvements but mostly we need to infer if the index we have proposed is relevant. For that, we have compared the districts from San Jose with highest crime rates and our index is able to capture such trend.


## 💡 Main Insights (300 words max)

- the **most frequent crimes** against women are **theft and assault**, while homicide is very rare (not ignoring the more brutal aspect of this crime in relation to theft)
- the **top 5 subtypes of crimes** against women are **pickpocketing, 'due to neglect', firearm, outburst and cold weapon**, which coincides with the previous conclusion
- the grand majority of crimes are perpetrated against people (66%), followed by houses/builidings (20%) and then vehicles belonging to women (13%)
- most crimes were committed against Costa Rican women and then Nicaraguan women, which makes sense since it's a neighbouring country
- there has been an **increase in crimes since 2012**, with a **decrease in 2020**:
    - since we are dealing with reported crimes, it doesn't mean that crimes have increased but rather that women are reporting them more. Without more information, we can't conclude anything about the real number of crimes; nonetheless, we believe there has been a change in costumes, leading to more women feeling comfortable reporting crimes
    - the sharp decrease in 2020 can be explained by the Covid-19 pandemic, since it led to people staying inside; our analysis is going to be focused on public spaces but we acknowledge that crimes committed inside the household may have increased (domestic violence)
- as the **day progresses from morning to night**, the **number of crimes also increases**: the fact that there's less light gives more protection to the assailants
- **almost all of the crimes** were commited against **women with ages between 18 and 60**, with the number of crimes against elder women basically the same as the number of crimes against women with less than 18 years

From the FAMD analysis, we can clearly see the separation of the different districts using only two principal components, the first component (explains 25 % of variance) involves majorly the numer of crimes against women by district while the second principal component (acounts for 21 % of the variance) is more related  with social-economic and demographic information by district. These two componenets were then used to create our index.

Our forecast model can still be further improved but due to time contrains we are still getting around 50 % MAPE for our index forecast for year 2022 and around 30 % MAPE for quarter prediction.

## 🛠️ Product
### Definition

A dashboard that can inform the Women Security Index (WSI, index created by us) to both the agents of authority (policy makers/government/police) and the public.

### Users

Based on the WSI Policy makers and the government can use the dashboard to improve security in zones and times where women might not feel safe.
Security forces (police) can use it to monitor certain areas that are more at risk.
The public can consult the dashboard to take extra precautions in certain districts or during certain times. When we talk about public,
we are also including the men, who should be allies in this fight.

### Activities
a) Gathering of all the relevant data and exploratory data analysis
b) Make a correlation between all the different variables and squeeze the most relevant ones into fewer dimensions for discriminating the most insecure districts for women in San Jose, this further helps decrease any biases from our analysis.
c) From the two first dimensions, that explain ca. 50 % of the variance in our dataset, we have created a index that may allow a simpler interpretation for the index.
d) Time series analysis using a machine learning model allows to forecast the most likely unsecure districts for women is San Jose in 2022. 


### Output
A dashboard is created for easy dissimination of the outcome of the model that can be shared by relevant police makers that can easily analyze trends and improve security measures in the most problematics districts from San Jose. The dashborad if public can also be used by the overall population worried with the women in their lives.
Our product also allow bring awareness of the insecurity for women of the main districts where one lives, works or have leasure so that overall population can make pressure on police makers to tackle such issues in their neighborhood.

## 🌍 Social Impact Measurement

By warning people of possible dangers, we believe that reports of crimes will decrease due to the decrease of the crimes themselves.
We also believe that this kind of transparency of our work and product will empower women to report crimes when they happen.

### Impact Metrics

1 - Comparison of our WSI values before and after deployment of the dashboard - deviation from the predictions.


### Impact Measurement

Based on the predictions by district and by trimester maybe already start focusing on the most problematic areas until the end of 2022. 
And make an analysis of the trend by dsitrict, if the trend still points upwards further focus on such districts aiming decrease women insecurity levels.
