import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15]) # Change percent
mylabels = ["Blue", "Yellow", "Green", "Red"]

plt.pie(y, labels = mylabels)
plt.show()
