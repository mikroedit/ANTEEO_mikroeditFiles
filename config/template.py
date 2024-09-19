# IMPORT
import requests
import json
import base64

# DANE API
api_key = ''
url = 'https://api.baselinker.com/connector.php'

# PARAMETRY ZAPYTANIA
parameters = {
    "": ,
}

# DANE ŻĄDANIA POST
data = {
    'token' = api_key,
    'method' = 'addOrder',
    'parameters' = json.dumps(parameters)
}

# WYSŁANIE ZAPYTANIA
response = requests.post(url, data=data)

# SPRAWDZANIE STATUSU
if response.status_code == 200:
    print("Sukces: ", response.json())
else:
    print("Error: ", response.status_code, response.text)
