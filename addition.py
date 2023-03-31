from PIL import Image

# Load the image file
image = Image.open("img_01.jpg")

# Create a new blank image with the same size as the original
new_image = Image.new(mode="RGB", size=image.size)

# Loop through each pixel of the original image and add 70 to its RGB values
for x in range(image.width):
    for y in range(image.height):
        r, g, b = image.getpixel((x, y))
        new_image.putpixel((x, y), (r+70, g+70, b+70))

# Display the modified image
new_image.show()

