#zamowienia
nowe_zamówienie = 125981
do_wysłania = 125982
wyslane = 125983
anulowane = 125984
przykladowy_status = 125985

#produkty
crewneck = 109193241
hoodie = 109195638
jacket = 109198316
pants = 109198676
tshirt = 109199124

class personData:
    status_id = wyslane
    currency = 'PLN'
    email = 'klient@example.com'
    fullname = 'Kacper Warszyński'
    address = 'ul. Przykładowa 1'
    postcode = '00-000'
    city = 'Warszawa'
    country_code = 'PL'
    comments = 'Opis zamówienia!!!'

class orderData:
    order_id = 4301533
    storage = "db"
    storage_id = 0
    product_id = hoodie
    # variant_id = 52124
    name = "HOODIE"
    # sku = ""
    # ean = ""
    # location = "A1-13-7"
    # attributes = "colour red"
    price_brutto = 80
    tax_rate = 23
    amount = 1
    # weight = 1