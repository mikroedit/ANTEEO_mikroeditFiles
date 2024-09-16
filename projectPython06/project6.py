import requests

# Twoje dane autoryzacyjne
api_token = '5005339-5019417-QRJNYQEGHEDF69PWCJ2SE9JA2OLTJOS74S7IPVGFTIKYAEB8RGK3N2L2NPC5X41L'
order_id = '4225134'
pdf_file_path = r'C:\mikroeditFiles\baselinkerFiles\box\paczka.pdf'

# URL API BaseLinker
url = 'https://api.baselinker.com/connector.php'

# Otwórz plik PDF w trybie binarnym
with open(pdf_file_path, 'rb') as pdf_file:
    pdf_data = pdf_file.read()

# Parametry zapytania
params = {
    'token': api_token,
    'method': 'addOrderReceiptFile',
    'parameters': {
        'order_id': order_id,
        'file': pdf_data,
        'file_name': 'receipt.pdf'
    }
}

# Wykonaj zapytanie POST
response = requests.post(url, data=params)

# Sprawdź odpowiedź
if response.status_code == 200:
    print('Plik PDF został pomyślnie dodany do zamówienia.')
else:
    print('Wystąpił błąd:', response.text)
