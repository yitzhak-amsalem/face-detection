from deepface import DeepFace


class FaceVerifier:
    def __init__(self, model_images, images_to_filter):
        self.model_images = model_images
        self.images_to_filter = images_to_filter

    def verify_faces(self):
        verified_photos = []
        index = 0
        for image_to_filter in self.images_to_filter:
            index += 1
            try:
                result = DeepFace.verify(img1_path=self.model_images[0],
                                         img2_path=image_to_filter,
                                         detector_backend="mtcnn",
                                         distance_metric="cosine",
                                         model_name="ArcFace"
                                         )
                print(f'{index}: {result["distance"]}')
                if result["distance"] < 0.65:
                    verified_photos.append(image_to_filter)
            except Exception as e:
                print(f"Error processing image: {str(e)}")
        return verified_photos

    def verify_faces1(self):
        verified_photos = []
        index = 0
        for image_to_filter in self.images_to_filter:
            index += 1
            for model_images in self.model_images:
                try:
                    result = DeepFace.verify(img1_path=model_images,
                                             img2_path=image_to_filter,
                                             detector_backend="mtcnn",
                                             distance_metric="cosine",
                                             model_name="ArcFace"
                                             )
                    if result["distance"] < 0.6:
                        verified_photos.append(image_to_filter)
                        break
                except Exception as e:
                    print(f"Error processing image: {str(e)}")
        return verified_photos
