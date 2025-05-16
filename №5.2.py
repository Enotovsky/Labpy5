import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, color='red', edgecolor='black')
plt.title('Гистограмма нормального распределения 1000 точек')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(axis='y', linestyle = '--')
plt.show()