# Project: STEDI Human Balance Analytics

## Description

The _STEDI_ Team has been hard at work developing a hardware _STEDI Step Trainer_ that:

- Trains the user to do a _STEDI_ balance exercise
- Has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
- Has a companion mobile app that collects customer data and interacts with the device sensors.

As many users have already purchased and adquired their step trainer, data from the phone's accelerometer and the motion sensor are starting to be gathered. The _STEDI_ team wants to use this data to train a machine learning model, but only data from the users who have agreed to share their data for research purposes should be made available for the _STEDI_ team. 

## Methodology

To only make available the data from users who agreed to share their data, the following steps will show how:

1. **Landing zones:**

      The first stage is to bring the data into a landing zone, where the raw information will be stored to later transform it.
      This is how the landing zones for the customers and accelerometer were created:
      
      - [customer-landing.sql](scripts/customer-landing.sql)
      - [accelerometer-landing.sql](scripts/accelerometer-landing.sql)

2. **Trusted zones:**
      
      

3. 
