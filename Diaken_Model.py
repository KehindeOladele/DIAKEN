import urllib.request
import json

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
        "Inputs": {
          "WebServiceInput0": [
            {
              "Age": 40,
              "Gender": "Female",
              "Polyuria": 'True',
              "Polydipsia": 'True',
              "sudden weight loss": 'True',
              "weakness": 'True',
              "Polyphagia": 'True',
              "Genital thrush": 'False',
              "visual blurring": 'True',
              "Itching": 'True',
              "Irritability": 'False',
              "delayed healing": 'True',
              "partial paresis": 'False',
              "muscle stiffness": 'True',
              "Alopecia": 'True',
              "Obesity": 'True',
            },
            {
              "Age": 58,
              "Gender": "Male",
              "Polyuria": 'False',
              "Polydipsia": 'False',
              "sudden weight loss": 'False',
              "weakness": 'True',
              "Polyphagia": 'False',
              "Genital thrush": 'False',
              "visual blurring": 'True',
              "Itching": 'False',
              "Irritability": 'False',
              "delayed healing": 'False',
              "partial paresis": 'True',
              "muscle stiffness": 'False',
              "Alopecia": 'True',
              "Obesity": 'False',
            },
            {
              "Age": 41,
              "Gender": "Male",
              "Polyuria": 'True',
              "Polydipsia": 'False',
              "sudden weight loss": 'False',
              "weakness": 'True',
              "Polyphagia": 'True',
              "Genital thrush": 'False',
              "visual blurring": 'False',
              "Itching": 'True',
              "Irritability": 'False',
              "delayed healing": 'True',
              "partial paresis": 'False',
              "muscle stiffness": 'True',
              "Alopecia": 'True',
              "Obesity": 'False',
            }
          ]
        },
        "GlobalParameters": {

        }
      }

body = str.encode(json.dumps(data))

url = 'http://a0c66db6-1d28-49b6-ad37-41629f4d800c.eastus2.azurecontainer.io/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'jwOl9UWWMX6U0OKzpDcgDTrVLkFYmaMB'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Accept': 'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))