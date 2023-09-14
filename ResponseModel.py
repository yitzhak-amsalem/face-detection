import base64
import io
import os

from PIL import Image

from faceDetection import FaceVerifier


class ResponseModel(object):

    def __init__(self, requestModel):
        self.filteredImages = []
        self.jpg_model_images = []
        self.jpg_filter_images = []
        self.jpg_model_images = self.convertBase64ArrayToImg(requestModel.photoModel, "model")
        self.jpg_filter_images = self.convertBase64ArrayToImg(requestModel.photoFilter, "filter")
        print("in the verify faces")
        face_verifier = FaceVerifier(self.jpg_model_images, self.jpg_filter_images)
        print("after the verify faces")
        self.filteredImages = face_verifier.verify_faces()
        self.filteredImages64 = self.convertJpgArrayToBase64(self.filteredImages)
        self.deletImages(self.jpg_model_images)
        self.deletImages(self.jpg_filter_images)

    def convertImgToBase64(self, img):
        with open(img, 'rb') as image_file:
            base64_bytes = base64.b64encode(image_file.read())
            base64_string = base64_bytes.decode()
        return base64_string

    def convertJpgArrayToBase64(self, jpg_filtered_images):
        base64_images = []
        for img in jpg_filtered_images:
            base64_images.append(self.convertImgToBase64(img))
        return base64_images

    def convertBase64ArrayToImg(self, base64_images, type):
        count = 0
        images_path = []
        for base64_string in base64_images:
            path = f"{type}{count}.jpeg"
            self.convertBase64ToImg(base64_string["image"], path)
            images_path.append(path)
            count += 1
        return images_path

    def convertBase64ToImg(self, base64_string, path):
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_string, "utf-8"))))
        img.save(path, 'jpeg')

    def deletImages(self, images):
        for img in images:
            if os.path.exists(img):
                os.remove(img)
