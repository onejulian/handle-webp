import os
from PIL import Image
import requests
from dotenv import load_dotenv

load_dotenv()

s3_url_pattern = os.getenv("S3_URL_PATTERN")
endpoint_upload = os.getenv("ENDPOINT_UPLOAD")

def convert_to_webp(id_article, ext):
    urls = []
    folder_crops = "/pulzo-dev/images-cropped/"
    folder_resized = "/images-resized/"
    path_crops = s3_url_pattern + folder_crops + id_article
    path_resized = s3_url_pattern + folder_resized + id_article

    urls.append(path_crops + "-horizontal." + ext)
    urls.append(path_crops + "-vertical." + ext)
    urls.append(path_crops + "-square." + ext)
    urls.append(path_resized + "-h-s." + ext)
    urls.append(path_resized + "-h-m." + ext)
    urls.append(path_resized + "-h-b." + ext)
    urls.append(path_resized + "-h-o." + ext)
    urls.append(path_resized + "-v-s." + ext)
    urls.append(path_resized + "-v-m." + ext)
    urls.append(path_resized + "-v-b." + ext)
    urls.append(path_resized + "-v-o." + ext)
    urls.append(path_resized + "-s-s." + ext)
    urls.append(path_resized + "-s-m." + ext)
    urls.append(path_resized + "-s-b." + ext)
    urls.append(path_resized + "-s-o." + ext)

    for url in urls:
        name = url.split("/")[-1].split(".")[0]
        image = Image.open(requests.get(url, stream=True).raw)
        image.save(name + ".webp", "WEBP")
        
        if '-horizontal' in name or '-vertical' in name or '-square' in name:
            upload_image(folder_crops, name + ".webp")
        else:
            upload_image(folder_resized, name + ".webp")
        
        os.remove(name + ".webp")

def upload_image(path, nameImage):
    payload = {
        'path': path,
        'contentType': 'image/webp'
    }
    
    files = [
        ('file', (nameImage, open(nameImage, 'rb'), 'image/webp'))
    ]
    
    headers = {}

    requests.request("POST", endpoint_upload, headers=headers, data=payload, files=files)
