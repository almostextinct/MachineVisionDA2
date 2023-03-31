from PIL import Image

# Open the image file
img = Image.open("img_02.jpg")

# Convert the image to grayscale
img = img.convert('L')

# Display the grayscale image
img.show()