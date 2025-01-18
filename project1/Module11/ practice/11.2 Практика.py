from PIL import Image


# im = Image.open('img_dog.jpg')

# print(f'Формат картинки: {im.format}\n'
#       f'Размер картинки: {im.size}\n'
#       f'Мод: {im.mode}')

# Т.к.  def size(self) -> tuple[int, int]:
#         return self._size
# То можно присвоить двум переменным значения ширины и высоты
# w, h = im.size
# print(f'Ширина: {w}, высота: {h}')

# print(dir(Image)) # Классы и функции модуля

# out = im.resize((w//2, h//2)) # Уменьшение размера изображения вдвое

# out.show()  # - показать картинку

# Функция меняет размер изображения
def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_photo('img_dog.jpg')
im_2 = new_photo('smile.png')
# im_2.show()

im.paste(im_2, (75, 500))
im.show('Новая фотография')
