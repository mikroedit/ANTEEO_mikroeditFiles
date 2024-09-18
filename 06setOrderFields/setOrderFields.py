import requests
import json
import base64
from orderFieldsData import fieldsData

# Wczytanie obrazu
with open(fieldsData.box_image, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Dodanie prefiksu "data:"
encoded_image = "data:" + encoded_image

# Parametry w formacie JSON
parameters = {
    "order_id": fieldsData.order_id,
    "custom_extra_fields": {
        fieldsData.extra_field_id: 
        {
            "title": fieldsData.title,
            "file": encoded_image
        }
    }
}

# Dane do wysłania w żądaniu POST
data = {
    'token': fieldsData.api_key,
    'method': 'setOrderFields',
    'parameters': json.dumps(parameters)
}

# Wysyłanie żądania POST
response = requests.post(fieldsData.url, data=data)

# Sprawdzanie odpowiedzi
if response.status_code == 200:
    print('Sukces:', response.json())
else:
    print('Błąd:', response.status_code, response.text)
    try:
        print('Szczegóły błędu:', response.json())
    except json.JSONDecodeError:
        print('Nie można zdekodować odpowiedzi JSON')
