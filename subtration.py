from PIL import Image

# Open the image file
img = Image.open("img_01.jpg")

# Subtract 50 from every pixel in the image
img = img.point(lambda p: p - 50)

# Display the modified image
img.show()
