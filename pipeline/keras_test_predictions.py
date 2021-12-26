import os
import sys
import tensorflow as tf
from tensorflow import keras
from preprocessing import image_size
from keras_classifiers import make_model, categories, data_augmentation, get_train_dataset, filename
import matplotlib.pyplot as plt
import numpy as np

def view_augmented_images(train_dataset):
    plt.figure(figsize=(10,10))
    for images, _ in train_dataset.take(1):
        for i in range(9):
            augmented_images = data_augmentation(images)
            ax = plt.subplot(3, 3, i+1)
            plt.imshow(augmented_images[0].numpy().astype('uint8'))
            plt.axis('off')
    
    plt.show()

# from Deep Learning with Python, chapter 5
def view_intermediate_layers(model, image_as_array):
    activations = model.predict(image_as_array)
    
    layer_names = []
    for layer in model.layers:
        layer_names.append(layer.name)

    images_per_row = 16
    for layer_name, layer_activation in zip(layer_names, activations):
        n_features = layer_activation.shape[-1]
        size = layer_activation.shape[1]
        n_cols = n_features // images_per_row
        display_grid = np.zeroes((size * n_cols, images_per_row * size))

        for col in range(n_cols):
            for row in range(images_per_row):
                channel_image = layer_activation[0, :, :, col * images_per_row + row]
                channel_image -= channel_image.mean()
                channel_image /= channel_image.std()
                channel_image *= 64
                channel_image += 128
                channel_image = np.clip(channel_image, 0, 255).astype('uint8')
                display_grid[col*size : (col+1)*size, row*size : (row+1)*size] = channel_image

        scale = 1.0/size
        plt.figure(figsize=(scale*display_grid.shape[1], scale*display_grid.shape[0]))
        plt.title(layer_name)
        plt.grid(False)
        plt.imshow(display_grid, aspect='auto', cmap='viridis')
    
    plt.show()

def view_predictions(model, unseen_path):
    for filename in os.listdir(unseen_path):
        path = os.path.join(unseen_path, filename)
        img = keras.preprocessing.image.load_img(path, target_size=image_size)
        img_arr = keras.preprocessing.image.img_to_array(img)
        img_arr = tf.expand_dims(img_arr, 0)

        predictions = model.predict(img_arr)
        battle_score = predictions[0][0] * 100
        clear_chapter_score = predictions[0][1] * 100
        clear_stage_score = predictions[0][2] * 100
        defeat_score = predictions[0][3] * 100
        loading_score = predictions[0][4] * 100
        main_menu_score = predictions[0][5] * 100
        map_score = predictions[0][6] * 100
        
        output = f"""Score for {filename}: 
        Battle score {battle_score}%, 
        Clear chapter score {clear_chapter_score}%,
        Clear stage score {clear_stage_score}%,
        Defeat score {defeat_score}%,
        Loading score {loading_score}%,
        Main menu score {main_menu_score}%,
        Map score {map_score}%
        """

        print(output)

        # view_intermediate_layers(model, img_arr)

def main(train_path, unseen_path):
    train_dataset = get_train_dataset(train_path)

    view_augmented_images(train_dataset)

    model = make_model(input_shape=image_size + (3,), num_classes=categories)
    model.load_weights(filename)

    view_predictions(model, unseen_path)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])