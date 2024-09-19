import requests
import json

def sendLink(api_key, url, order_id, extra_field_id2, link_video):

    # Parametry w formacie JSON
    parameters = {
        "order_id": order_id,
        "custom_extra_fields": {
            extra_field_id2: link_video
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