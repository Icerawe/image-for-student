import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


# Load the image
img_1 = mpimg.imread("image/6jZ1RNDmJb.JPG")
img_2 = mpimg.imread("image/CcekapIPWx.JPG")
img_3 = mpimg.imread("image/fiZMhXf5cM.JPG")

fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].imshow(img_1, cmap="gray")
axs[1].imshow(img_2, cmap="gray")
axs[2].imshow(img_3, cmap="gray")

# add name of figure
fig.suptitle("Math Teacher")

plt.show()