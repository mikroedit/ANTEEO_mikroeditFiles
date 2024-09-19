from orderData import fieldsData
from sendImage import sendImage
from sendLink import sendLink

# funkcja wysyłająca zdjęcie
sendImage(fieldsData.api_key, fieldsData.url, fieldsData.order_id, fieldsData.box_image, fieldsData.title, fieldsData.extra_field_id)

# funkcja zmieniająca opis (dodaje link)
sendLink(fieldsData.api_key, fieldsData.url, fieldsData.order_id, fieldsData.extra_field_id2, fieldsData.link_video)
