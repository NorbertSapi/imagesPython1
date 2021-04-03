# This is an exercise to manipulate pictures.

from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# filtered BLUR
filtered_img = img.filter(ImageFilter.BLUR)

# Filtered SHARP
sharp_img = img.filter(ImageFilter.SHARPEN)

# converted from GRB to Black & White
convert_img = img.convert('L')

# resize image
resize = convert_img.resize((300, 300))
resize.save("grey2.png", 'png')

# save results
filtered_img.save("blur.png", 'png')
sharp_img.save("sharp.png", 'png')
convert_img.save("grey.png", 'png')

#show the result
sharp_img.show()
