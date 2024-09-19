import os
import requests
import json
import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class orderFunctions:
    # wysłanie linku do filmu
    def sendLinkVideo(Data):

        # parametry w formacie JSON
        parameters = {
            "order_id": Data.order_id,
            "custom_extra_fields": {
                Data.extra_field_id2: Data.link_video
            }
        }

        # dane do wysłania w żądaniu POST
        data = {
            'token': Data.api_key,
            'method': 'setOrderFields',
            'parameters': json.dumps(parameters)
        }

        # wysyłanie żądania POST
        response = requests.post(Data.url, data=data)

        # sprawdzanie odpowiedzi
        if response.status_code == 200:
            print('Sukces:', response.json())
        else:
            print('Błąd:', response.status_code, response.text)
            try:
                print('Szczegóły błędu:', response.json())
            except json.JSONDecodeError:
                print('Nie można zdekodować odpowiedzi JSON')

    # sprawdzenie rozmiaru pliku
    def checkImage(Data):
        file_size = os.path.getsize(Data.box_image)
        return file_size

        # wysłanie linku do zdjęcia
    
    # wysłanie linku ze zdjęciem
    def sendLinkImage(Data, link):       

        # parametry w formacie JSON
        parameters = {
            "order_id": Data.order_id,
            "custom_extra_fields": {
                Data.extra_field_id3: link
            }
        }

        # dane do wysłania w żądaniu POST
        data = {
            'token': Data.api_key,
            'method': 'setOrderFields',
            'parameters': json.dumps(parameters)
        }

        # wysyłanie żądania POST
        response = requests.post(Data.url, data=data)

        # sprawdzanie odpowiedzi
        if response.status_code == 200:
            print('Sukces:', response.json())
        else:
            print('Błąd:', response.status_code, response.text)
            try:
                print('Szczegóły błędu:', response.json())
            except json.JSONDecodeError:
                print('Nie można zdekodować odpowiedzi JSON')

    # wysłanie zdjęcia google drive
    def sendImageGoogleDrive(Data):

        # funkcja google1
        def authenticate_google_drive():
            SCOPES = ['https://www.googleapis.com/auth/drive.file']
            SERVICE_ACCOUNT_FILE = r'C:\Users\Admin\Documents\principal-fact-436109-r8-51df4c2c472c.json'

            credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            service = build('drive', 'v3', credentials=credentials)
            return service

        # funkcja google2
        def upload_to_google_drive(service, file_path, title, folder_id):
            file_metadata = {
                'name': title,
                'parents': [folder_id]
            }
            media = MediaFileUpload(file_path, mimetype='image/jpeg')
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'Plik {title} został przesłany na Google Drive. ID pliku: {file.get("id")}')
            return file.get('id')

        # funkcja generująca link do udostępnienia
        def get_shareable_link(service, file_id):
            request_body = {
                'role': 'reader',
                'type': 'anyone'
            }
            service.permissions().create(fileId=file_id, body=request_body).execute()
            link = f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"
            return link

        print('Plik jest za duży. Przesyłanie na Google Drive...')
        service = authenticate_google_drive()
        file_id = upload_to_google_drive(service, Data.box_image, Data.title, Data.folder_id)
        link = get_shareable_link(service, file_id)
        orderFunctions.sendLinkImage(Data, link)

    # wysłanie zdjęcia baselinker
    def sendImageBaseLinker(Data):
            
        # wczytanie obrazu
        with open(Data.box_image, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        # dodanie prefiksu "data:"
        encoded_image = "data:" + encoded_image

        # parametry w formacie JSON
        parameters = {
            "order_id": Data.order_id,
            "custom_extra_fields": {
                Data.extra_field_id: 
                {
                        "title": Data.title,
                        "file": encoded_image
                }
            }
        }

        # dane do wysłania w żądaniu POST
        data = {
            'token': Data.api_key,
            'method': 'setOrderFields',
            'parameters': json.dumps(parameters)
        }

        # wysyłanie żądania POST
        response = requests.post(Data.url, data=data)

        # sprawdzanie odpowiedzi
        if response.status_code == 200:
            print('Sukces:', response.json())
        else:
            print('Błąd:', response.status_code, response.text)
            try:
                print('Szczegóły błędu:', response.json())
            except json.JSONDecodeError:
                print('Nie można zdekodować odpowiedzi JSON')