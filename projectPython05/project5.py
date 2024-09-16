import requests
import json

# Twój klucz API Baselinker
api_key = '5005339-5019417-QRJNYQEGHEDF69PWCJ2SE9JA2OLTJOS74S7IPVGFTIKYAEB8RGK3N2L2NPC5X41L'

# URL endpointu API
url = 'https://api.baselinker.com/connector.php'

# Parametry w formacie JSON
parameters = {
    'order_status_id': "118416",
    'currency': 'PLN',
    'email': 'klient@example.com',
    'delivery_fullname': 'Jan Kowalski',
    'delivery_address': 'ul. Przykładowa 1',
    'delivery_postcode': '00-000',
    'delivery_city': 'Warszawa',
    'delivery_country_code': 'PL',
    'admin_comments': 'Opis zamówienia!!!',
}

# Dane do wysłania w żądaniu POST
data = {
    'token': api_key,
    'method': 'addOrder',
    'parameters': json.dumps(parameters)
}

# Wysyłanie żądania POST
response = requests.post(url, data=data)

# Sprawdzanie odpowiedzi
if response.status_code == 200:
    print('Sukces:', response.json())
else:
    print('Błąd:', response.status_code, response.text)
