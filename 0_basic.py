# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

image = [
    [
        [255, 10, 20], [25, 255, 50]
    ],
    [
        [255, 0, 255], [0, 255, 150]
    ]
]

x = np.array(image, dtype=np.uint8)
print(x)

plt.imshow(x, cmap="gray")
plt.show()

new_image = []
for i in image:
    avg = []
    for j in i:
        avg.append(sum(j)/len(j))
    new_image.append(avg)

print(new_image)
x = np.array(new_image, dtype=np.uint8)
print(x)

plt.imshow(x, cmap="gray")
plt.show()
