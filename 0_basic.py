import matplotlib.pyplot as plt
import numpy as np

# Define the image array
x = []
x = np.array(x, dtype=np.uint8)  # Correct dtype

# Display the image using matplotlib
plt.imshow(x, cmap="gray")  # Corrected argument name
plt.show()
