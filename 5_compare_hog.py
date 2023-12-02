from skimage.io import imread
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import cv2
import os

# List to store HOG images
hogs = []

# List to store image paths
image_paths = [f"data/{file}" for file in os.listdir("data/")]
image_paths = sorted(image_paths)

# Loop through each image
for image_path in image_paths:
    img = imread(image_path)

    # Resize image to a fixed size (e.g., 128x128)
    resized_img = cv2.resize(img, (128, 128))

    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Compute the HOG features and their visualization
    fd, hog_image = hog(gray, orientations=8, pixels_per_cell=(12, 12), cells_per_block=(3, 3), visualize=True)

    # Rescale histogram for better display
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
    
    # Append HOG image to the list
    hogs.append(hog_image_rescaled)

# Display original, grayscale, and HOG images
fig, axes = plt.subplots(2, len(image_paths), figsize=(12, 5))

for i, ax in enumerate(axes[0]):
    ax.imshow(hogs[i], cmap=plt.cm.gray)
    ax.set_title(f"Image {i+1}")
    ax.axis('off')

# Create a new figure for the histogram
for i, ax in enumerate(axes[1]):
    ax.hist(hogs[i].ravel(), bins=20)
    ax.set_title(f'Histogram {i+1}')

plt.tight_layout()
plt.show()
