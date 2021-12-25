import skimage.io as io
import skimage.transform as transform
import sys
import pathlib
# import matplotlib.pyplot as plt
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from joblib import dump
import time

category_encoding = {
    "battle": 0,
    "clear_stage": 1,
    "clear_chapter": 2,
    "defeat": 3,
    "loading": 4,
    "map": 5
}

def read_from_subdirectory(base, subdir):
    subdir_path = base / subdir
    return np.array([io.imread(filename.as_posix()).flatten() for filename in subdir_path.glob('*.png')])

def time_operation(description, operation, *args):
    start = time.time()
    result = operation(*args)
    finish = time.time()
    print(f"Elapsed time for {description}: {round(finish - start, 2)} seconds.")
    return result

image_size = (9 * 25, 16 * 25)
def resize_images(img_list):
    return np.array([transform.resize(image, image_size, anti_aliasing=True).flatten() for image in img_list])

def create_labels(label, values):
    return np.full(values, category_encoding[label])

# from https://stackoverflow.com/questions/31467487/memory-efficient-way-to-split-large-numpy-array-into-train-and-test
def custom_train_test_split(X, y, test_proportion):
    ratio = int(X.shape[0] / test_proportion)
    X_train = X[ratio:,:]
    X_test = X[:ratio,:]
    y_train = y[ratio:]
    y_test = y[:ratio]
    return X_train, X_test, y_train, y_test 

def main(input_file_directory):    
    # Load images
    base = pathlib.Path(input_file_directory)
    
    battle_imgs = time_operation("reading battle images", read_from_subdirectory, base, 'battle')
    clear_stage_imgs = time_operation("reading clear_stage images", read_from_subdirectory, base, 'clear_stage')
    clear_chapter_imgs = time_operation("reading clear_chapter images", read_from_subdirectory, base, 'clear_chapter')
    defeat_imgs = time_operation("reading defeat images", read_from_subdirectory, base, 'defeat')
    loading_imgs = time_operation("reading loading images", read_from_subdirectory, base, 'loading')
    map_imgs = time_operation("reading map images", read_from_subdirectory, base, 'map')

    # Shuffle images
    rng = np.random.default_rng()
    rng.shuffle(battle_imgs)
    rng.shuffle(clear_stage_imgs)
    rng.shuffle(clear_chapter_imgs)
    rng.shuffle(defeat_imgs)
    rng.shuffle(loading_imgs)
    rng.shuffle(map_imgs)

    # Generate labels
    battle_labels = create_labels('battle', len(battle_imgs))
    clear_stage_labels = create_labels('clear_stage', len(clear_stage_imgs))
    clear_chapter_labels = create_labels('clear_chapter', len(clear_chapter_imgs))
    defeat_labels = create_labels('defeat', len(defeat_imgs))
    loading_labels = create_labels('loading', len(loading_imgs))
    map_labels = create_labels('map', len(map_imgs))

    battle_X_train, battle_X_valid, battle_y_train, battle_y_valid = custom_train_test_split(battle_imgs, battle_labels, 3)
    clear_stage_X_train, clear_stage_X_valid, clear_stage_y_train, clear_stage_y_valid = custom_train_test_split(clear_stage_imgs, clear_stage_labels, 3)
    clear_chapter_X_train, clear_chapter_X_valid, clear_chapter_y_train, clear_chapter_y_valid = custom_train_test_split(clear_chapter_imgs, clear_chapter_labels, 3)
    defeat_X_train, defeat_X_valid, defeat_y_train, defeat_y_valid = custom_train_test_split(defeat_imgs, defeat_labels, 3)
    loading_X_train, loading_X_valid, loading_y_train, loading_y_valid = custom_train_test_split(loading_imgs, loading_labels, 3)
    map_X_train, map_X_valid, map_y_train, map_y_valid = custom_train_test_split(map_imgs, map_labels, 3)

    X_train = np.concatenate([battle_X_train, clear_stage_X_train, clear_chapter_X_train, defeat_X_train, loading_X_train, map_X_train])
    X_valid = np.concatenate([battle_X_valid, clear_stage_X_valid, clear_chapter_X_valid, defeat_X_valid, loading_X_valid, map_X_valid])
    y_train = np.concatenate([battle_y_train, clear_stage_y_train, clear_chapter_y_train, defeat_y_train, loading_y_train, map_y_train])
    y_valid = np.concatenate([battle_y_valid, clear_stage_y_valid, clear_chapter_y_valid, defeat_y_valid, loading_y_valid, map_y_valid])
    
    model = make_pipeline(
        SVC()
        #RandomForestClassifier(max_depth=20, min_samples_split=3, min_samples_leaf=2)
    )
    model.fit(X_train, y_train)

    print(model.score(X_valid, y_valid))
    predicted = model.predict(X_valid)

    print(f"{classification_report(y_valid, predicted)}")
    print(confusion_matrix(y_valid, predicted))

    dump(model, 'sklearn-intermediate-1.joblib')
    #plt.imshow(defeat_resized[0])
    #plt.show() 

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f"Usage: {sys.argv[0]} <directory containing subfolders with appropriate category names>")
