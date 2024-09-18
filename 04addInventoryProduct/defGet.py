# defGet
import requests
import json

# Twój klucz API Baselinker (przechowywany w zmiennej środowiskowej)
api_key = '5005673-5020614-ZSH4Q8KPB4FX6Z0T51VVJK1IJRXCEENGRT64NKBIL1FI7CPJJEXIIMK8NF8PRTN3'

# URL endpointu API
url = 'https://api.baselinker.com/connector.php'

def get_inventories():
    data = {
        'token': api_key,
        'method': 'getInventories'
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print('Błąd:', response.status_code, response.text)
        return None

def get_inventory_categories():
    data = {
        'token': api_key,
        'method': 'getInventoryCategories'
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print('Błąd:', response.status_code, response.text)
        return None