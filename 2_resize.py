import cv2
import numpy as np

# Create a random 50x50 image
random_image = np.random.randint(0, 256, (2,2,3), dtype=np.uint8)

# Resize the random image to a larger size (e.g., 200x200) using bilinear interpolation
new_size = (500, 500)

resize_list = []
for interpolation in [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC]:
    resize_list.append(cv2.resize(random_image, new_size, interpolation=interpolation))

frame = np.hstack(resize_list)
# Display the frame
cv2.imshow('Image Frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()