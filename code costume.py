import sys

from PIL import Image

image = []

for arg in sys.argv:
    image = Image.opean(arg)
    images.append(image)


images[0].save(
    "costumes.gif", save_all=True, append_images=[image[1]], duration=200, loop=0
)