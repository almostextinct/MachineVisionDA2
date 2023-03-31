from PIL import Image, ImageFilter, ImageDraw

# Open the input image
input_image = Image.open("img_04.jpeg")

# Apply a smoothing filter to the image
smoothed_image = input_image.filter(ImageFilter.SMOOTH)

# Apply a sharpening filter to the image
sharpened_image = input_image.filter(ImageFilter.SHARPEN)

# Create a new image with three times the width to hold all three images side by side
output_image = Image.new("RGB", (input_image.width*3 + 60, input_image.height + 20), (255, 255, 255))
draw = ImageDraw.Draw(output_image)

# Add labels to the images
draw.text((10, 5), "Input Image", fill=(0, 0, 0))
draw.text((input_image.width+30, 5), "Smoothed Image", fill=(0, 0, 0))
draw.text((input_image.width*2+50, 5), "Sharpened Image", fill=(0, 0, 0))

# Add borders to the images
draw.rectangle([(5, 15), (input_image.width+15, input_image.height+5)], outline=(0, 0, 0))
draw.rectangle([(input_image.width+25, 15), (input_image.width*2+35, input_image.height+5)], outline=(0, 0, 0))
draw.rectangle([(input_image.width*2+45, 15), (input_image.width*3+55, input_image.height+5)], outline=(0, 0, 0))

# Paste the images into the output image
output_image.paste(input_image, (10, 20))
output_image.paste(smoothed_image, (input_image.width+30, 20))
output_image.paste(sharpened_image, (input_image.width*2+50, 20))

# Show the output image
output_image.show()
