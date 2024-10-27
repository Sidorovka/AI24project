import kagglehub
import os
from PIL import Image
import numpy as np

# Download latest version
path = kagglehub.dataset_download("misrakahmed/vegetable-image-dataset")

print("Path to dataset files:", path)

processed_files = []

def convert_to_matrix(image_path):
    # Проверяем расширение файла
    file_extension = os.path.splitext(image_path)[-1]
    if file_extension == ".jpg" or file_extension == ".jpeg":
        # Если файл является изображением, проверяем, есть ли он в списке processed_files
        if image_path not in processed_files:
            # Открываем изображение
            img = Image.open(image_path)

            # Преобразуем изображение в массив NumPy
            array = np.asarray(img)

            # Сохраняем матрицу в файл
            np.save(file_path + ".npy", array)
            print("Матрица для файла", file_path, ":\n", array)

            # Добавляем путь к файлу в список processed_files, чтобы предотвратить повторную обработку
            processed_files.append(image_path)
        else:
            print(f"{image_path} уже обработан")
    else:
        print("Файл не является изображением")

# Проходимся по всем файлам в наборе данных
for root, dirs, files in os.walk(path):
    for file in files:
        # Получаем полный путь к файлу
        file_path = os.path.join(root, file)

        # Вызываем функцию convert_to_matrix для обработки файла
        convert_to_matrix(file_path)

import matplotlib.pyplot as plt

# Функция для загрузки и показа изображений
def show_images_in_grid(path, num_cols=10):
    files = [file for file in os.listdir(path) if file.endswith('.npy')]  # Фильтрация по расширению '.npy'
    files = files[:num_cols * 10]  # Берем первые 100 файлов (.npy)

    fig, axes = plt.subplots(nrows=10, ncols=num_cols, figsize=(16, 18))

    for ax, file in zip(axes.flat, files):
        matrix = np.load(os.path.join(path, file))
        image = Image.fromarray(matrix)
        ax.imshow(image)
        ax.axis('off')  # Отключаем оси

    plt.tight_layout()  # Улучшаем компоновку
    plt.show()

 Указываем папку с нужными изображениями
temp_dir = 'Bean'

# Указываем путь к папке с файлами .npy
additional_dirs = ['Vegetable Images', 'test', temp_dir]

# Объединение базового пути с дополнительными каталогами
path = os.path.join(path, *additional_dirs)

show_images_in_grid(path)

# Функция для построения гистограмм
def plot_histograms_in_grid(path, num_cols=10):
    files = [file for file in os.listdir(path) if file.endswith('.npy')]
    files = files[:num_cols * 10]  # Берем первые 100 файлов (.npy)

    fig, axes = plt.subplots(nrows=10, ncols=num_cols, figsize=(16, 18))

    for ax, file in zip(axes.flat, files):
        matrix = np.load(os.path.join(path, file))
        flattened_matrix = matrix.flatten()
        ax.hist(flattened_matrix, bins=256, density=True, color='b', alpha=0.5)
        ax.set_title(file[:-4])  # Название файла без расширения
        ax.tick_params(axis='both', which='major', labelsize=6)

    plt.tight_layout()  # Улучшаем компоновку
    plt.show()

plot_histograms_in_grid(path)

# Функция для построения гистограмм
def plot_channel_histograms_in_grid(path, num_cols=10):
    files = [file for file in os.listdir(path) if file.endswith('.npy')]
    files = files[:num_cols * 10]  # Берем первые 100 файлов (.npy)

    fig, axes = plt.subplots(nrows=10, ncols=num_cols, figsize=(16, 18))

    for ax, file in zip(axes.flat, files):
        matrix = np.load(os.path.join(path, file))
        red_channel = matrix[:, :, 0].flatten()
        green_channel = matrix[:, :, 1].flatten()
        blue_channel = matrix[:, :, 2].flatten()

        ax.hist(red_channel, bins=256, density=True, color='r', alpha=0.5, label='Red')
        ax.hist(green_channel, bins=256, density=True, color='g', alpha=0.5, label='Green')
        ax.hist(blue_channel, bins=256, density=True, color='b', alpha=0.5, label='Blue')
        ax.legend(prop={'size': 6})
        ax.set_title(file[:-4])  # Название файла без расширения
        ax.tick_params(axis='both', which='major', labelsize=6)

    plt.tight_layout()  # Улучшаем компоновку
    plt.show()

plot_channel_histograms_in_grid(path)