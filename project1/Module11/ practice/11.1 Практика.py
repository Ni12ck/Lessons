from PIL import Image

im = Image.open('img_dog.jpg')

print(f'Формат картинки: {im.format}\n'
      f'Размер картинки: {im.size}\n'
      f'Мод: {im.mode}')



# print(dir(Image)) # Классы и функции модуля

out = im.resize((600, 480))

out.show() # - показать картинку