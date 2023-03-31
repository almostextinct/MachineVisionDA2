import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# Open the image file
img = Image.open("img_04.jpeg")

# Convert the image to grayscale
gray_img = img.convert("L")

# Apply histogram equalization
eq_img = np.array(gray_img)
eq_img = cv2.equalizeHist(eq_img)

# Display original image and its histogram
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.hist(np.array(gray_img).flatten(), 256, [0, 256])
plt.title("Original Histogram")
plt.xlim([0, 256])

# Display modified image and its histogram
plt.subplot(2, 2, 3)
plt.imshow(eq_img, cmap='gray')
plt.title("Equalized Image")
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.hist(eq_img.flatten(), 256, [0, 256])
plt.title("Equalized Histogram")
plt.xlim([0, 256])

# Show the plots
plt.show()
