import cv2
import numpy as np

# Replace 'source.jpg' with the path to your image file
image_path = 'source.jpg'

# Read the image
image = cv2.imread(image_path)

# Split the image into its color channels (B, G, R)
b, g, r = cv2.split(image)

# Add the constant value to each channel
b = cv2.add(b, 0)
g = cv2.add(g, 0)
r = cv2.add(r, 0)

# Create metric 0 (grayscale) images with the same dimensions as the original image
zeros = np.zeros(image.shape[:2], dtype=np.uint8)

# Merge the metric 0 images for blue, green, and red channels
merge_b = cv2.merge((b, zeros, zeros))
merge_g = cv2.merge((zeros, g, zeros))
merge_r = cv2.merge((zeros, zeros, r))
filtered = cv2.merge((b, g, r))

frame = np.hstack((image, merge_r, merge_g, merge_b, filtered))
# Display the frame
cv2.imshow('Image Frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()