from PIL import Image

img = Image.open('favicon.png')
img.save('favicon.ico')