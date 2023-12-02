# https://www.analyticsvidhya.com/blog/2019/09/feature-engineering-images-introduction-hog-feature-descriptor/
# http://ethesisarchive.library.tu.ac.th/thesis/2016/TU_2016_5509035043_6948_4816.pdf
from skimage.io import imread
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import cv2

image_path = 'image/6jZ1RNDmJb.JPG'
img = imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute the HOG features and their visualization
fd, hog_image = hog(image=gray, visualize=True)

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

# Display original and processed images
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.imshow(img, cmap="gray")
ax1.set_title('Input Image')
ax1.axis('off')

ax2.imshow(gray, cmap="gray")
ax2.set_title('Grayscale Image')
ax2.axis('off')

ax3.imshow(hog_image, cmap="gray")
ax3.set_title('HOG Image')
ax3.axis('off')

# Create a new figure for the histogram
plt.figure(figsize=(10, 4))
plt.hist(hog_image_rescaled.ravel(), bins=20)
plt.title('Histogram of HOG Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
