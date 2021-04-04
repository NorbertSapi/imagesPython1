# This is an exercise to create a jpg to png converter.
# 1. create a new directory - new\ and the app should convert all the jpg from Pokedex convert to PNG.
#
import sys
import os
from PIL import Image

# 1. grab the second and first arguments.
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# 2. check if the new folder exist and if not create one.

path = r"c:\Users\ncssa\PycharmProjects\imagesPython1\new"

if os.path.exists(output_folder):
    print(output_folder)
else:
    os.mkdir(path)
    print(output_folder)
# print(image_folder, output_folder)

# 3. loop through Pokedex directory
# 4. convert images to png
# 5. save images to the new folder
