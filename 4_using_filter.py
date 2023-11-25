import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np

# Load the image
image_path = 'image/6jZ1RNDmJb.JPG'
img = mpimg.imread(image_path)

# Plot the original image
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')

# Define the kernel for convolution
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.int8)

# Perform convolution using cv2.filter2D
result = cv2.filter2D(img, -1, kernel)

# Plot the image after convolution
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.title('Image after Convolution')

# Show the side-by-side comparison
plt.show()
