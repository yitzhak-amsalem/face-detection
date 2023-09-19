import base64
import io
import os
from PIL import Image


def convertImgToBase64(img):
    with open(img, 'rb') as image_file:
        base64_bytes = base64.b64encode(image_file.read())
        base64_string = base64_bytes.decode()
    return base64_string


def convertJpgArrayToBase64(jpg_filtered_images):
    base64_images = []
    for img in jpg_filtered_images:
        base64_images.append(convertImgToBase64(img))
    return base64_images


def convertBase64ArrayToImg(base64_images, imageType):
    count = 0
    images_path = []
    for base64_string in base64_images:
        path = f"{imageType}{count}.jpeg"
        convertBase64ToImg(base64_string["image"], path)
        images_path.append(path)
        count += 1
    return images_path


def convertBase64ToImg(base64_string, path):
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_string, "utf-8"))))
    img.save(path, 'jpeg')
