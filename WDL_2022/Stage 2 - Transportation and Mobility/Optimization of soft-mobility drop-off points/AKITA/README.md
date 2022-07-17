# World Data League 2022

## 🎯 Challenge
Optimization of Soft-Mobility Drop-off Points

## Team Name
AKITA

## 👥 Authors
Include all the authors that have worked on this submission. It is not obligatory to include all the team members if not everyone has worked on it. This will not impact the evaluation in any way.
* Hongyu Ao
* Yu Luo
* Xiaoxiao Ma
* Yuanliu Wanghan

## ✨ Introduction (250 words max)
Escooters, like bike-sharing, has become a newer form of shared-mobility but with more freedom. In this project, we aim to advance the dropoff locations of escooters in the City of Porto through optimization. We analyzed the demand for escooters by real life data, then coincide with population flow and public transportation data to upgrade the distribution of existing escooters. 

## 🔢 Data (250 words max)
* OpenStreetMap
  * City of Porto boundary data
  * City of Porto neighborhood boundary data
*  Validation data on road public transport - validation per stop per hour
*  Validation data on rail public transport - validation per stop per hour
*  E-Scooter Transport Data
*  E-Scooter Location Data
*  GTFS for E-Scooter Parking and Metro Stations

## 🧮 Methods and Techniques (250 words max)
* Geospatial analysis
  * Determine boundaries and neighborhoods incorporated with demand
* Origin/destination matrix
  * Filter trip-related records and transform slices of information into unified trip records
* Standardization
  *  Trip duration and passenger flow in bus/metro stations are highly skewed
* Linear Optimization
  * With demand weight calculated from public transportation data and trip data 
     * Passenger flow, trip duration, trip start/end locations 

## 💡 Main Insights (300 words max)
* The demand for escooters is mainly from commuters and tourists
* The recommended distance between stations is 200 meters
* According to research on the current regulations on e-scooters in the City ot Porto, the operation of such scooters is not allowed from 10pm to 6am, and during this time the maintenance can pick up and drop off. However the data records trips during that time and the majority of dropoff records are outside the time frame. 


## 🛠️ Product
### Definition
A heat map shows the capacity of demand overlaid with optimized drop-off locations. 

### Users
The City of Porto transportation and city planning. 

### Activities
Gives an optimized plan of the locations of dropoff points based on demand flow. 

### Output
A map with locations of optimized dropoff points (optional: layered with demand concentration)

## 🌍 Social Impact Measurement
### Impact Metrics
* Cost of maintenance
 * Pickups and dropoffs: the amount of escooters needed to be relocated
 * Lifespan of escooters


### Impact Measurement
With the optimized dropoff/parking locations for escooters, users will generally be more willing to park close to or even in the designated areas to reduce the relocation effort. Since the existing escooters are more practically distributed across the city, as users' awareness and technology advance, the lifespan of escooters is expected to be lenghthened so that they can be veritably environmentally friendly. 

