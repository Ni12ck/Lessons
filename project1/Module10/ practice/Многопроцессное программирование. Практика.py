# уменьшение изображение
# изменение картинки в чёрно-белый цвет

import multiprocessing

# Скачал библиотеку Pillow (pip install Pillow)
from PIL import Image

# Импорт ошибки Empty
from queue import Empty

# Импорт time
import time


# Сначала меняем размер
def resize_image(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((800, 600))
        queue.put((image_path, image))


# Потом изменённой картинке меняем цвет
def change_color(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=3)  # Поставил таймаут 3 секунд, чтобы не было бесконечного цикла
        except Empty:
            break  # Как очередь станет пустой, и пройдёт 3 секунды, сработает break
        # Делаем картинку чёрно-белой ('L' отвечает за чёрно-белый цвет)
        image = image.convert('L')
        # Сохраняем по пути
        image.save(image_path)


if __name__ == '__main__':
    # Список картинок
    data = []
    queue = multiprocessing.Queue()

    # Создаём список картинок
    for image in range(1, 4):
        data.append(f'./images/img_{image}.jpg')

    # Создание процесса изменения картинки
    resize_process = multiprocessing.Process(target=resize_image, args=(data, queue))
    change_process = multiprocessing.Process(target=change_color, args=(queue,))

    strat_time = time.time()

    # Старт процессов
    resize_process.start()
    change_process.start()

    # Ожидание окончания
    resize_process.join()
    change_process.join()

    end_time = time.time()
    print(f'Время выполнения: {end_time - strat_time}')
