
# DIAKEN: A USSD Based Diabetes Prediction Tool

## Description
This is an AI Powered USSD Based Diabetes Prediction Tool using the diabetes prediction model which I created earlier this is designed to recieve user input from patients and use it to create a dataframe which will be fed into the model which will now predict if the patient has a high or low chance of having diabetes.

## Features
• creation of the [model](https://github.com/KehindeOladele/AI_Powered_USSD_Based_Diabetes_Prediction_Tool/blob/main/Diabetes_Prediction_Model_USSD.ipynb) for prediction.

• Creation of a patient ID to identify each new patient data inputed.

• Collection of user input to form a dataframe and deploment of model to make predictions.

• Creation of a prototype.

## Model
The diabetes prediction model previously made was adjusted by removing the race columns and the encoding for the race columns The model remained 96% acurate even after removing the race columns. Then, it was saved into Jolib so it could easily be deployed in the future.

## Backend
In the [backend](https://github.com/KehindeOladele/AI_Powered_USSD_Based_Diabetes_Prediction_Tool/blob/main/Backend.ipynb), I created a unique patient Id for each user that inputs a new set of data. this helps to identify the patient data inputed. Then, I collect user input and converted the input into a dataframe. But before converting it into a dataframe, I encoded the gender and smking history to convert the values into readable integers (ones and zeros). then I deployed the model to make predictions from the user input.

## Prototype
The [prototype](https://github.com/KehindeOladele/AI_Powered_USSD_Based_Diabetes_Prediction_Tool/blob/main/Diaken_Wireframe.png) was created using Mirro.
<img width="1366" height="768" alt="Diaken_Wireframe" src="https://github.com/user-attachments/assets/702994a7-c7a7-4eee-b5de-6afb5967d357" />

## Results
The predictions if its a 0 for no diabetes, the message on the screen should be: "You are at low risk of having diabetes, please contact your nearest hospital for confirmation". If its a 1 for yes diabetes, the message ont he screen should be: "You are at high risk of having diabetes, please visit the nearest hospital as soon as possible".

## Acknowledgments
The [dataset](https://github.com/KehindeOladele/Diabetes_Prediction_Model/blob/main/diabetes_dataset.csv) for training the model was created by Priyam Choksi and was downloaded from Kaggle.
