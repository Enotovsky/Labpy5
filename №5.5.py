import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))


x = np.linspace(0, 10, 100)
y = x ** 2
ax1.plot(x, y, color='blue', linewidth=2)
ax1.set_title('Линейный график: y = x^2')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)

np.random.seed(50)
x_scatter = np.random.rand(30) * 10
y_scatter = np.random.rand(30) * 100
ax2.scatter(x_scatter, y_scatter, color='red')
ax2.set_title('Точечный график случайных данных')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.grid(True)

categories = ['A', 'B', 'C']
values = [4, 5, 1]
ax3.bar(categories, values, color=['pink', 'green', 'purple'])
ax3.set_title('Столбчатая диаграмма')
ax3.set_xlabel('Категории')
ax3.set_ylabel('Значения')
ax3.grid(axis='y')

plt.show()