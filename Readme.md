
# Acronyms

| name | meaning                 |
|------|-------------------------|
| FWI  | Fire Weather Index      |
| FFMC | Fine Fuel Moisture Code |
| DMC  | Duff Moisture Code      |
| DC   | Drought Code            |
| ISI  | Initial Spread Index    |
| BUI  | Buildup Index           |

## Fine Fuel Moisture Code 

The Fine Fuel Moisture Code (FFMC) is a numeric rating of the moisture content of litter and other cured fine fuels. This code is an indicator of the relative ease of ignition and the flammability of fine fuel. 

## Drought Code 

The Drought Code (DC) is a numeric rating of the average moisture content of deep, compact organic layers. This code is a useful indicator of seasonal drought effects on forest fuels and the amount of smoldering in deep duff layers and large logs. 

## Initial Spread Index 

The Initial Spread Index (ISI) is a numeric rating of the expected rate of fire spread. It is based on wind speed and FFMC. Like the rest of the FWI system components, ISI does not take fuel type into account. Actual spread rates vary between fuel types at the same ISI.

# Variable list

| Attribute   | Description                             |
|-------------|-----------------------------------------|
| X           | x-axis coordinate (from 1 to 9)         |
| Y           | y-axis coordinate (from 1 to 9)         |
| month       | Month of the year (January to December) |
| day         | Day of the week (Monday to Sunday)      |
| ----------- | --------------------------------------- |
| FFMC        | FFMC code                               |
| DMC         | DMC code                                |
| DC          | DC code                                 |
| ISI         | ISI index                               |
| ----------- | --------------------------------------- |
| temp        | Outside temperature (in ◦C)             |
| RH          | Outside relative humidity (in %)        |
| wind        | Outside winnd sp                        |
| rain        | Outside rain (in mm/m2)                 |
| ----------- | --------------------------------------- |
| area        | Total burned area (in ha)               |

# Todo list

- [ ] Solve a regression problem
- [ ] Address the issue of positive skewness of the data
