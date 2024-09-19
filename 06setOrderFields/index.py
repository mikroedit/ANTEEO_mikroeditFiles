<<<<<<< HEAD
from orderData import Data
from orderDef import orderFunctions

orderFunctions.sendLinkVideo(Data)

file_size = orderFunctions.checkImage(Data)
if file_size < 2 * 1024 * 1024:
    orderFunctions.sendImageBaseLinker(Data)
else:
    orderFunctions.sendImageGoogleDrive(Data)
=======
from orderData import fieldsData
from sendImage import sendImage
from sendLink import sendLink

# funkcja wysyłająca zdjęcie
sendImage(fieldsData.api_key, fieldsData.url, fieldsData.order_id, fieldsData.box_image, fieldsData.title, fieldsData.extra_field_id)

# funkcja zmieniająca opis (dodaje link)
sendLink(fieldsData.api_key, fieldsData.url, fieldsData.order_id, fieldsData.extra_field_id2, fieldsData.link_video)
>>>>>>> 9d70171316c38ee170900cd7a0e6e6db404aa6bb
