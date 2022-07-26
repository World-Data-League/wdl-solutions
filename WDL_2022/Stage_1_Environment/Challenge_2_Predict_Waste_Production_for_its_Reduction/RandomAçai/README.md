World Data League 2022
======================

🎯 Challenge
-----------

Predict Waste Production for its reduction

👥 Authors
---------

José Maurício Nunes de Oliveira Júnior Júlia Schubert Peixoto Renata
Costa Victor Manuel Martinez Alvarez

✨ Introduction (250 words max)
------------------------------

Provide a contextualization of the problem, together with an estimation
of its size using real numbers and references. *Write here*

🔢 Data (250 words max)
----------------------

We used Waste Collection & Diversion Report (daily) data from the
Official City of Austin Texas Data Portal
(https://data.austintexas.gov/Utilities-and-City-Services/Waste-Collection-Diversion-Report-daily-/mbnu-4wq9),
we also tried to use weather data (OpenWeather API) and route data
(https://data.austintexas.gov/Locations-and-Maps/Garbage-Routes/azhh-4hg8),
however only the first data was included in our final model. The present
model we created 6 different timeseries models to estimate waste
production in the following years, however our initial idea was to
create multiple models separated by waste type and localization using
the routes from waste collection. However the route data
(https://data.austintexas.gov/Locations-and-Maps/Garbage-Routes/azhh-4hg8)
doesn't have a complete documentation, there are many routes (and waste
types) which are not included in this table. There's also a field called
"old route" which brings a lot of questions about the state of data and
how much it does reflect the real world. Our suggestions to stratify the
primary key from Garbage Route only to Garbage Route and date of
creation with all the other fields (except "old route"). The weather
data wasn't included because it did not help the model at first and we
didn't have the time to create an ensemble model, however if we had more
time we would also try: population data (by location would be better)
and real estate data. Another suggestion with the original dataset to
uniformize data about garbage type. We also used holidays from the
holidays library in python.

🧮 Methods and Techniques (250 words max)
----------------------------------------

We approached this problem as a basic time series problem. The first
thing we did was to transform this dataset to a dataset with daily index
(filling in the missing days) and columns being a waste type load. We
removed one very specific outlier then we used interpolation to fill the
missing values. Then we propose two different baselines to help us
measure our model's impact. The early baseline uses data from 14 days
shift, meaning that for example on day 15 of june of 2020 we assumed
that the same amount of waste from 1 of june of 2020 would be produced,
and a late baseline using a 365 days shift. For each different waste
type we trained a model using the "prophet" library using python. We
trained the models using data prior to 2018 and used the data from years
2018 and 2019 to measure the results.

💡 Main Insights (300 words max)
-------------------------------

Garbage collection is increasing overall and can be hard to predict.
However we can't know for sure if it's garbage
which was not previously collected and measured or actual increase of
waste production. Waste collection however has specific trends for many
garbage types, a very obvious one's yard trimming with an increase in
the middle of the year (probably because of fall).
More "humane" waste production (garbage
collection and recycling) has a more stable behavior throughout the year
but with some seasonalities. The model was
able to surpass the baselines proposed here, without needing to update
our predictions, showing that it's possible to predict waste production
for the next few years and so to create policies and directives to
improve waste management. The table below shows the average daily error
of lbs collected for each model and each garbage type, showing that in
general our model works better than baselines.
Using our model we predicted the variation weekly, monthly and yearly in
waste production. The model presented that in 2018
there could be a 1.89% increase in waste load compared to 2017, but a
decrease of 0.57% in recycling which's overall a bad thing. We would
advise to boost recycling campaigns or create mechanisms to facilitate
recycling so at least we have a comparable increase in recycling.

🛠️ Product
----------

### Definition

A dashboard that assists decision making to waste management, predicting
the weekly, monthly and yearly variation in waste production and a
timeline pointing out possible spikes in waste production.

### Users

Environmental agents responsible for waste management. Example: Traffic
controllers use the dashboard during their work to better plan where to
dispatch resources

### Activities

-   Predicts waste management throughout the time
-   Predicts waste variation from a reference

### Output

Timeseries graphical representation and a table showing the model's
performance and the possible variations

🌍 Social Impact Measurement
---------------------------

### Outcome

Boost the decision making power from environmental agents, increase
waste management effectiveness therefore reducing waste produced through
social policies.

### Impact Metrics

\* Waste load produced \* Waste
load variation

### Impact Measurement

-   Based on model predictions\*: Our model estimates a 1.89% increase
    in garbage collection waste load in 2018 compared to 2017 and a
    decrease by 0.57% on recycling waste collection.
-   As garbage collection represents almost 52% of all waste collected
    we would advise to improve recycling policies.
