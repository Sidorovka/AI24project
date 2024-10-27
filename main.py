import kagglehub

# Download latest version
path = kagglehub.dataset_download("misrakahmed/vegetable-image-dataset")

print("Path to dataset files:", path)

import os
from PIL import Image
import numpy as np

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
