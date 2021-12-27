from joblib import load
import numpy as np
import cv2
from skimage import transform
from pipeline.preprocessing import image_size

class Classifier():

    def __init__(self):
        model_file_name = 'sklearn-full-12-20-21.joblib'
        self.model = load(model_file_name)

    def resize_and_channels(self, image):
        raw_img = np.array(image)
        print(raw_img.shape)
        img_alpha = cv2.cvtColor(raw_img, cv2.COLOR_RGB2RGBA)
        print(img_alpha.shape)
        resized_img = transform.resize(img_alpha, image_size, anti_aliasing=True).flatten().reshape(1, -1)
        print(resized_img.shape)
        return resized_img

    def predict(self, image):
        result = self.model.predict(image)
        print(result)
