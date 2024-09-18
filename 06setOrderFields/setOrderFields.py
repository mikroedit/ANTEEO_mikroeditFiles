import requests
import json
import base64

# Twój klucz API Baselinker
api_key = '5005673-5020614-ZSH4Q8KPB4FX6Z0T51VVJK1IJRXCEENGRT64NKBIL1FI7CPJJEXIIMK8NF8PRTN3'

# URL endpointu API
url = 'https://api.baselinker.com/connector.php'

# ID zamówienia, które chcesz zaktualizować
order_id = '4275688'

# Wczytanie obrazu
with open("C:\\mikroeditFiles\\00baselinkerFiles\\box\\paczka.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Dodanie prefiksu "data:"
encoded_image = "data:" + encoded_image

# Parametry w formacie JSON
parameters = {
    "order_id": order_id,
    "custom_extra_fields": {
        "45317": 
        {
            "title": "paczka.png",
            "file": encoded_image
        }
    }
}

# Dane do wysłania w żądaniu POST
data = {
    'token': api_key,
    'method': 'setOrderFields',
    'parameters': json.dumps(parameters)
}

# Wysyłanie żądania POST
response = requests.post(url, data=data)

# Sprawdzanie odpowiedzi
if response.status_code == 200:
    print('Sukces:', response.json())
else:
    print('Błąd:', response.status_code, response.text)
    try:
        print('Szczegóły błędu:', response.json())
    except json.JSONDecodeError:
        print('Nie można zdekodować odpowiedzi JSON')
