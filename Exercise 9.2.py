import numpy as np
import matplotlib.pyplot as plt

points = np.random.rand(100, 2)
colors = np.where(np.sqrt(points[:, 0]**2 + points[:, 1]**2) < 1, 'g', 'r')
area = (np.abs(points[:, 0]) + np.abs(points[:, 1]))*300

plt.scatter(points[:, 0], points[:, 1], c=colors, s=area, alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')

plt.show()