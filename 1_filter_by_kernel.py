import cv2
import numpy as np

# Replace 'source.jpg' with the path to your image file
image_path = 'source.jpg'

# Read the image
image = cv2.imread(image_path)

# Define your custom 3x3 kernel
kernel_1 = np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]], dtype=np.float32)

kernel_2 = np.array([[0.0625, 0.125, 0.0625],
                  [0.125, 0.25, 0.125],
                  [0.0625, 0.125, 0.0625]], dtype=np.float32)

# Apply the 2D convolution with the custom kernel
filtered_1= cv2.filter2D(image, -1, kernel_1)
filtered_2= cv2.filter2D(image, -1, kernel_2)

frame = np.hstack((filtered_1, image, filtered_2))
# Display the frame
cv2.imshow('Image Frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()