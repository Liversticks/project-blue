from tensorflow import keras
from PIL import Image
from pipeline.preprocessing import image_size
from pipeline.keras_classifiers import make_model, categories
import tensorflow as tf

class Classifier():

    def __init__(self):
        model_file_name = 'al_classifier_keras_v2.h5'
        self.model = make_model(input_shape=image_size + (3,), num_classes=categories)
        self.model.load_weights(model_file_name)

    def to_numpy(self, image):
        # PIL example: https://python-mss.readthedocs.io/examples.html
        img = Image.frombytes("RGB", image.size, image.bgra, "raw", "BGRX")
        img = img.resize((image_size[1], image_size[0]))
        return tf.expand_dims(keras.preprocessing.image.img_to_array(img), 0)

    def predict(self, image):
        category_predictions = self.model.predict(image)
        result = category_predictions.argmax()
        print(f"Prediction: {result}")
        return result
