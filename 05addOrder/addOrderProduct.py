import requests
import json
from Data import orderData

api_key = '5005673-5020614-ZSH4Q8KPB4FX6Z0T51VVJK1IJRXCEENGRT64NKBIL1FI7CPJJEXIIMK8NF8PRTN3'
url = 'https://api.baselinker.com/connector.php'

parameters = {
    "order_id": orderData.order_id,
    "storage": orderData.storage,
    "storage_id": orderData.storage_id,
    "product_id": orderData.product_id,
    # "variant_id": orderData.variant_id,
    "name": orderData.name,
    # "sku": orderData.sku,
    # "ean": orderData.ean,
    # "location": orderData.location,
    # "attributes": orderData.attributes,
    "price_brutto": orderData.price_brutto,
    "tax_rate": orderData.tax_rate,
    "quantity": orderData.amount,
    # "weight": orderData.weight
}

data = {
    'token': api_key,
    'method': 'addOrderProduct',
    'parameters': json.dumps(parameters)
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print('Sukces:', response.json())
else:
    print('Błąd:', response.status_code, response.text)