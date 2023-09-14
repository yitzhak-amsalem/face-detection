import string


class RequestModel(object):

    def __init__(self, images, imagesModel):
        self.photoFilter = images
        self.photoModel = imagesModel
