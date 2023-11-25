import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
image_path = 'image/6jZ1RNDmJb.JPG'
img = mpimg.imread(image_path)

# Plot the image
plt.imshow(img)

# Show the plot
plt.show()