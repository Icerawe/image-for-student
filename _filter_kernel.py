import cv2
import numpy as np

image = np.array([
    [122, 134, 90, 136],
    [85, 50, 123, 135],
    [95, 157, 160, 195],
    [200, 202, 201, 200]
], dtype=np.uint8)

kernel = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
], dtype=np.float32)

# Perform convolution using cv2.filter2D
result = cv2.filter2D(image, -1, kernel)

print("Original Image:")
print(image)
print("\nKernel:")
print(kernel)
print("\nConvolved Image:")
print(result)
