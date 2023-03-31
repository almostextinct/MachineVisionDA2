from PIL import Image, ImageOps

# Open the input image
input_image = Image.open("img_01.jpg")

# Invert the image
inverted_image = ImageOps.invert(input_image)

# Show the inverted image
inverted_image.show()
