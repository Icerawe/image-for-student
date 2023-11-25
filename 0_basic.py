import matplotlib.pyplot as plt
import numpy as np

x = [
    [[255, 40, 12], [0, 255, 39]],
    [[0, 90, 255], [255, 225, 0]]
]

x_gray = []
for i in x:
    avg = []
    for j in i:
        avg.append(np.mean(j))
    x_gray.append(avg)

x = np.array(x, dtype=np.uint)
plt.imshow(x, cmap="gray")
plt.show()


x_gray = np.array(x_gray, dtype=np.uint)
plt.imshow(x_gray, cmap="gray")
plt.show()
