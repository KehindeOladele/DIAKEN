
# DIAKEN: A USSD Based Diabetes Risk Prediction Tool

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/043cfde9-6c4c-4c88-b581-cea8793d646b" />

## Description
We developed an accessible, low-barrier solution: a USSD-based Diabetes Risk Prediction Tool. This tool allows any individual, regardless of their phone or internet access, to input key health metrics via a simple USSD dial code. The input is used to create a data-frame which is fed into a diabetes prediction model.

## Features
• creation of the Model on azure Machine Learning.

• Creation of an app backend using Azure Feature App.

• Conecting it with a USSD API from Africa's Talking

• Testing the diabetes prediction tool, prototype and demo.

## Dataset
The [dataset](https://github.com/KehindeOladele/DIAKEN/blob/main/Data/diabetes_risk_prediction_dataset_1.csv) that was used is a diabetes risk prediction dataset from Kaggle. This was uploaded into Azure Cloud Storage and cleaned. Then the columns with string and boolean datatypes were converted to categorical data. The categorical data columns were one hot encoded (Except for the target column) to prevent bias. 

## Model
The diabetes risk prediction [model](https://github.com/KehindeOladele/DIAKEN/blob/main/Diaken_Model.py) was created using the Decision Tree Algorithm, an inference pipeline was made. The inference pipeline was adjusted to ensure that the target column is not inputed to get a prediction and the model was deployed.
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/3b67475e-a85a-4af9-bd3f-c39668ec11a0" />

## Backend
The [backend]() was created using Python and Azure Function App.

## Prototype
The [prototype](https://github.com/KehindeOladele/DIAKEN/blob/main/developers.africastalking.com.jpeg) was created using Africa's Talking.
![Image](https://github.com/user-attachments/assets/c62c2656-9c4c-4873-87de-f5aa5bb35e4b)

## Results
The predictions if its a 0 for no diabetes, the message on the screen should be: "You are at low risk of having diabetes, please contact your nearest hospital for confirmation". If its a 1 for yes diabetes, the message ont he screen should be: "You are at high risk of having diabetes, please visit the nearest hospital as soon as possible".

## Tools Used
* Azure Machine Learning - For data cleaning, preprocessing, model training and deployment.

* VS code - For model testing and building of the backend.

* Azure Function app - For the backend.

* Github - For Documentation.

* Microsoft Edge - For research and collaboration.

* Zoom - For recording the demo video.

* Google chrome, drive, docs for research, workflow and documentation.

* Chat GPT for creating the cover page.

## Creators
### Team Lead

Kehinde Olukosi 

FE/23/81584328

kenoladanolu@gmail.com

07034642217

### Co-Creator

Jeffrey Esedo 

FE/23/48137946

jiesedo@gmail.com

08035666968

