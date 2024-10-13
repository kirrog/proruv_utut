import os
import random
import shutil
from pathlib import Path

test_percent = 0.2
valid_percent = 0.1

processed_path = Path('../data/processed')
images_path = processed_path / "images"
labels_path = processed_path / "labels"

dataset_path = '../data/dataset'
train_images_path = os.path.join(dataset_path, 'train', 'images')
train_labels_path = os.path.join(dataset_path, 'train', 'labels')
valid_images_path = os.path.join(dataset_path, 'valid', 'images')
valid_labels_path = os.path.join(dataset_path, 'valid', 'labels')
test_images_path = os.path.join(dataset_path, 'test', 'images')
test_labels_path = os.path.join(dataset_path, 'test', 'labels')

os.makedirs(train_images_path, exist_ok=True)
os.makedirs(train_labels_path, exist_ok=True)
os.makedirs(valid_images_path, exist_ok=True)
os.makedirs(valid_labels_path, exist_ok=True)
os.makedirs(test_images_path, exist_ok=True)
os.makedirs(test_labels_path, exist_ok=True)

images = [f for f in os.listdir(str(images_path)) if f.endswith(('.jpg', '.jpeg', '.png'))]
labels = [f for f in os.listdir(str(labels_path)) if f.endswith('.txt')]

images.sort()
labels.sort()

if len(images) != len(labels):
    print("Количество изображений и меток не совпадает.")
    exit()

data = list(zip(images, labels))
random.shuffle(data)
images, labels = zip(*data)

num_images = len(images)
num_test = int(num_images * test_percent)
num_valid = int(num_images * valid_percent)
num_train = num_images - num_test - num_valid


def move_files(file_list, source_image_dir, source_label_dir, dest_image_dir, dest_label_dir):
    for file in file_list:
        image_path = os.path.join(source_image_dir, file)
        label_path = os.path.join(source_label_dir, os.path.splitext(file)[0] + '.txt')
        shutil.copy(image_path, os.path.join(dest_image_dir, file))
        shutil.copy(label_path, os.path.join(dest_label_dir, os.path.splitext(file)[0] + '.txt'))


move_files(images[num_test + num_valid:],
           images_path, labels_path,
           train_images_path, train_labels_path)

move_files(images[:num_test],
           images_path, labels_path,
           test_images_path, test_labels_path)

move_files(images[num_test:num_test + num_valid],
           images_path, labels_path,
           valid_images_path, valid_labels_path)

print(f"Перемещено {num_test} изображений в папку test.")
print(f"Перемещено {num_valid} изображений в папку valid.")
print(f"Осталось {num_train} изображений в папке train.")
