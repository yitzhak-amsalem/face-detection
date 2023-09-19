import os
from faceDetection import FaceVerifier
import convertor


class ResponseModel(object):

    def __init__(self, requestModel):
        self.filteredImages = []
        self.jpg_model_images = convertor.convertBase64ArrayToImg(requestModel.photoModel, "model")
        self.jpg_filter_images = convertor.convertBase64ArrayToImg(requestModel.photoFilter, "filter")

    def process(self):
        print("verify faces...")
        face_verifier = FaceVerifier(self.jpg_model_images, self.jpg_filter_images)
        self.filteredImages = face_verifier.verify_faces()
        return convertor.convertJpgArrayToBase64(self.filteredImages)

    def deleteImages(self):
        deleteImagesFromPath(self.jpg_model_images)
        deleteImagesFromPath(self.jpg_filter_images)


def deleteImagesFromPath(imagesPath):
    for img in imagesPath:
        if os.path.exists(img):
            os.remove(img)

