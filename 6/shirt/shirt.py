import sys
import os
from PIL import Image, ImageOps

list_of_extensions = ['.jpg', '.jpeg', '.png']

if len(sys.argv) != 3:
    sys.exit("2 CLA required")

tuple1 = os.path.splitext(sys.argv[1])[1].lower()
tuple2 = os.path.splitext(sys.argv[2])[1].lower()

if tuple1 not in list_of_extensions or tuple2 not in list_of_extensions:
    sys.exit("Invalid extension")
elif tuple1 != tuple2:
    sys.exit("different file extensions")

input_img = Image.open(sys.argv[1])
shirt = Image.open("shirt.png")

cropped_input_img = ImageOps.fit(input_img, shirt.size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))


cropped_input_img.paste(shirt, shirt)
cropped_input_img.save(sys.argv[2])





