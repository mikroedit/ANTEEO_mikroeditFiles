import requests
import json
import base64
from defGet import get_inventories, get_inventory_categories

# Twój klucz API Baselinker
api_key = '5005673-5020614-ZSH4Q8KPB4FX6Z0T51VVJK1IJRXCEENGRT64NKBIL1FI7CPJJEXIIMK8NF8PRTN3'

# URL endpointu API
url = 'https://api.baselinker.com/connector.php'

# Pobieranie danych z API
inventories_data = get_inventories()
categories_data = get_inventory_categories()

# Wybieranie wartości z pobranych danych
inventory_id = inventories_data['inventories'][1]['inventory_id'] #26370
prices_id = inventories_data['inventories'][1]['price_groups'][0] #23073
stock_id = inventories_data['inventories'][1]['warehouses'][0] #bl_44450
category_id = categories_data['categories'][0]['category_id'] #1490203

# Przykładowe wartości dla produktu
price = 50
stock_amount = 9
name_product = "T-SHIRT"
description = "Black tshirt"

# wczytanie obrazu
with open(r"C:\mikroeditFiles\00baselinkerFiles\clothes\tshirt1.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Dodanie prefiksu "data:image/png;base64,"
encoded_image = "data:" + encoded_image

# Parametry w formacie JSON
parameters = {
    "inventory_id": inventory_id,
    "product_id": "",
    "is_bundle": False,
    "category_id": category_id,
    "prices": {
        prices_id: price,
    },
    "stock": {
        stock_id: stock_amount,
    },
    "images": {
        "0": encoded_image,
    },
    "text_fields": {
        "name": name_product,
        "description": description,
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
    try:
        print('Szczegóły błędu:', response.json())
    except json.JSONDecodeError:
        print('Nie można zdekodować odpowiedzi JSON')
