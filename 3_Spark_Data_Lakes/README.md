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
      
      As some of the users have accepted to share their information, the data available should only be the one related to those users.
      The following scripts create glue jobs that only leaves the information of these users on customers, accelerometer and step trainer tables:
      
      - [customer_landing_to_trusted.py](scripts/customer_landing_to_trusted.py)
      - [accelerometer_landing_to_trusted.py](scripts/accelerometer_landing_to_trusted.py)
      - [step_trainer_landing_to_trusted.py](scripts/step_trainer_landing_to_trusted.py)

3. **Curated zones:**

     Finally, for the customers, the need data is the one from the users who agreed to share their data and also have received their sensor.
     - [customer_trusted_to_curated.py](scripts/customer_trusted_to_curated.py)
     
     With these tables created, the final data that will be available for the analytics team will be created with the following script:
     - [machine_learning_curated.py](scripts/machine_learning_curated.py)
