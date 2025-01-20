from PIL import Image, ImageFont, ImageDraw


class PostMaker:
    def __init__(self, name_photo):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2))

    def paste(self, name_photo):
        paste_image = Image.open(name_photo)
        paste_image = paste_image.resize((paste_image.size[0] // 2, paste_image.size[1] // 2))
        self.image.paste(paste_image, (75, 500))

    def upgrade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('sunday.ttf', 30)
        draw.text((35, 20), text, font=font, fill='red')
        self.image.show()


image = PostMaker('img_dog.jpg')
image.paste('smile.png')
image.upgrade('Улыбнись!')
