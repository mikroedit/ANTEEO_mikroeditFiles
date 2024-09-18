import requests
import json

# Twój klucz API Baselinker
api_key = '5005673-5020614-ZSH4Q8KPB4FX6Z0T51VVJK1IJRXCEENGRT64NKBIL1FI7CPJJEXIIMK8NF8PRTN3'

# URL endpointu API
url = 'https://api.baselinker.com/connector.php'

# Parametry w formacie JSON
parameters = {
    'product_id': '108343700'     # ID produktu do usunięcia
}

# Dane do wysłania w żądaniu POST
data = {
    'token': api_key,
    'method': 'deleteInventoryProduct',
    'parameters': json.dumps(parameters)
}

# Wysyłanie żądania POST
response = requests.post(url, data=data)

# Sprawdzanie odpowiedzi
if response.status_code == 200:
    print('Sukces:', response.json())
else:
    print('Błąd:', response.status_code, response.text)
