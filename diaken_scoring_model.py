import urllib.request
import json
import os
from dotenv import load_dotenv


def azure_scoring_model(data):

    load_dotenv()

    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
    # data = {
    #   "Inputs": {
    #     "WebServiceInput0": [
    #       {
    #         "Age": 28,
    #         "Gender": "Female",
    #         "Polyuria": "No",
    #         "Polydipsia": "No",
    #         "sudden weight loss": "No",
    #         "weakness": "No",
    #         "Polyphagia": "No",
    #         "Genital thrush": "No",
    #         "visual blurring": "No",
    #         "Itching": "No",
    #         "Irritability": "No",
    #         "delayed healing": "No",
    #         "partial paresis": "No",
    #         "muscle stiffness": "No",
    #         "Alopecia": "No",
    #         "Obesity": "No",
    #       },
    #       {
    #         "Age": 38,
    #         "Gender": "Male",
    #         "Polyuria": "No",
    #         "Polydipsia": "No",
    #         "sudden weight loss": "No",
    #         "weakness": "No",
    #         "Polyphagia": "No",
    #         "Genital thrush": "No",
    #         "visual blurring": "No",
    #         "Itching": "No",
    #         "Irritability": "No",
    #         "delayed healing": "No",
    #         "partial paresis": "NO",
    #         "muscle stiffness": "No",
    #         "Alopecia": "No",
    #         "Obesity": "No",
    #       },
    #       {
    #         "Age": 51,
    #         "Gender": "Female",
    #         "Polyuria": "No",
    #         "Polydipsia": "No",
    #         "sudden weight loss": "No",
    #         "weakness": "NO",
    #         "Polyphagia": "No",
    #         "Genital thrush": "No",
    #         "visual blurring": "No",
    #         "Itching": "No",
    #         "Irritability": "No",
    #         "delayed healing": "No",
    #         "partial paresis": "No",
    #         "muscle stiffness": "No",
    #         "Alopecia": "No",
    #         "Obesity": "No",
    #       },
    #       {
    #         "Age": 45,
    #         "Gender": "Male",
    #         "Polyuria": "No",
    #         "Polydipsia": "No",
    #         "sudden weight loss": "No",
    #         "weakness": "No",
    #         "Polyphagia": "No",
    #         "Genital thrush": "No",
    #         "visual blurring": "No",
    #         "Itching": "No",
    #         "Irritability": "No",
    #         "delayed healing": "No",
    #         "partial paresis": "No",
    #         "muscle stiffness": "No",
    #         "Alopecia": "No",
    #         "Obesity": "No",
    #       }
    #     ]
    #   },
    #   "GlobalParameters": {}
    # }

    # --- Input From USSD ---
    body = str.encode(json.dumps(data))

    # --- Azure Configuration ---
    # saved in an env for security
    api_key= os.getenv("api_key") 
    url= os.getenv("url")

    # Raise Error if API Key is not available or Expired
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # --- Calls the deployed Azure ML ACI endpoint. ---
    headers = {'Content-Type':'application/json', 'Accept': 'application/json', 'Authorization':('Bearer '+ api_key)}

    # --- POST Request ---
    # request is setup
    req = urllib.request.Request(url, body, headers)

    try:
        # --- Post request is made ---
        response = urllib.request.urlopen(req)
        
        # --- Reponse from Azure Endpoint ---
        
        # Read response
        result = response.read()
        print(result)

        # Get label and probability
        score_label= result["Scored Labels"]
        score_probabilities= result["Scored Probabilities"]
        return score_label, score_probabilities
    
    # --- Prints Error If request fails with status code ---
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))