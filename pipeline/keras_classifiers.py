import sys
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pipeline.preprocessing import image_size

batch_size = 32
epochs = 15
categories = 7
filename = 'al_classifier_keras_v3.h5'

callbacks = [
    keras.callbacks.ModelCheckpoint(filepath="save_at_{epoch}.h5"),
    keras.callbacks.EarlyStopping(patience=2)
]

data_augmentation = keras.Sequential(
        [
            layers.RandomTranslation(
                (-0.1, 0.1),
                (-0.1, 0.1),
                fill_mode='constant'
            ),
            layers.RandomZoom(
                (-0.1, 0.1),
                width_factor=(-0.1, 0.1),
                fill_mode='constant'
            )
        ]
    )

# from https://keras.io/examples/vision/image_classification_from_scratch/
def make_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)
    x = data_augmentation(inputs)

    x = layers.Rescaling(1.0/255)(x)
    x = layers.Conv2D(32, 3, strides=2, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)
    
    x = layers.Conv2D(64, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    previous_block_activation = x

    for size in [128, 256, 512, 720, 1024]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

        residual = layers.Conv2D(size, 1, strides=2, padding="same")(previous_block_activation)
        x = layers.add([x, residual])
        previous_block_activation = x

    x = layers.SeparableConv2D(2048, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.GlobalAveragePooling2D()(x)
    if num_classes == 2:
        activation = "sigmoid"
        units = 1
    else:
        activation = "softmax"
        units = num_classes
    
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(units, activation=activation)(x)

    return keras.Model(inputs, outputs)

def get_train_dataset(train_path):
    return tf.keras.preprocessing.image_dataset_from_directory(
        train_path,
        validation_split=0.2,
        subset='training',
        seed=1234,
        image_size=image_size,
        batch_size=batch_size
    )

def get_validation_dataset(train_path):
    return tf.keras.preprocessing.image_dataset_from_directory(
        train_path,
        validation_split=0.2,
        subset='validation',
        seed=1234,
        image_size=image_size,
        batch_size=batch_size
    )

def main(train_path):
    train_dataset = get_train_dataset(train_path)
    vaiidation_dataset = get_validation_dataset(train_path)

    model = make_model(input_shape=image_size + (3,), num_classes=categories)
    model.summary()

    model.compile(
        optimizer=keras.optimizers.Adam(1e-3),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(train_dataset, epochs=epochs, callbacks=callbacks, validation_data=vaiidation_dataset)

    model.save_weights(filename)

if __name__ == '__main__':
    main(sys.argv[1])