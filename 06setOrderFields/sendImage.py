import requests
import json
import base64

def sendImage(api_key, url, order_id, box_image, title, extra_field_id2):
    # Wczytanie obrazu
    with open(box_image, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Dodanie prefiksu "data:"
    encoded_image = "data:" + encoded_image

    # Parametry w formacie JSON
    parameters = {
        "order_id": order_id,
        "custom_extra_fields": {
            extra_field_id2: 
            {
                "title": title,
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
