import requests
import json

# Twój klucz API Baselinker
api_key = '5005339-5019417-QRJNYQEGHEDF69PWCJ2SE9JA2OLTJOS74S7IPVGFTIKYAEB8RGK3N2L2NPC5X41L'

# URL endpointu API
url = 'https://api.baselinker.com/connector.php'

# Parametry w formacie JSON
parameters = {
    "inventory_id": "24822",
    "product_id": "",
    "is_bundle": False,
    "prices": {
        "21676": 20,
    },
    "stock": {
        "bl_42335": 10,
    },
    "images": {
        "0": "url:https://amso.pl/pol_pl_Karta-Sieciowa-LAN-10-100-RJ-45-Single-Port-Zlacze-PCI-Wysoki-Profil-44566_1.png",
    },
    "text_fields": {
        "name": "karta sieciowa",
        "description": "Basic",
    },
}

# Dane do wysłania w żądaniu POST
data = {
    'token': api_key,
    'method': 'addInventoryProduct',
    'parameters': json.dumps(parameters)
}

# Wysyłanie żądania POST
response = requests.post(url, data=data)

# Sprawdzanie odpowiedzi
if response.status_code == 200:
    print('Sukces:', response.json())
else:
    print('Błąd:', response.status_code, response.text)
