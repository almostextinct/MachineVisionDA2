import cv2
import numpy
from PIL import Image

# Open the image file
img = Image.open("img_03.jpeg")

# Convert the image to grayscale
gray_img = img.convert("L")

# Convert the grayscale image to a NumPy array
img_arr = cv2.cvtColor(numpy.array(gray_img), cv2.COLOR_GRAY2RGB)

# Apply edge detection using the Canny algorithm
edges = cv2.Canny(img_arr, 100, 200)

# Display the modified image
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

