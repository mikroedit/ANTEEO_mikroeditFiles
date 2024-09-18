import requests
import json

# Twój klucz API Baselinker
api_key = '5005673-5020614-ZSH4Q8KPB4FX6Z0T51VVJK1IJRXCEENGRT64NKBIL1FI7CPJJEXIIMK8NF8PRTN3'

# URL endpointu API
url = 'https://api.baselinker.com/connector.php'

# Parametry w formacie JSON
parameters = {
    'order_status_id': "125983",
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

