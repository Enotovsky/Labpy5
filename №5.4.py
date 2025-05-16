import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.randint(1, 11, size=(5, 5))
plt.figure(figsize=(8, 6))
heatmap = plt.imshow(matrix, cmap='plasma')
plt.colorbar(heatmap, label='Значение')

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        plt.text(j, i, matrix[i, j], ha='center', va='center', color='black' if matrix[i, j] > 5 else 'white')

plt.title('Тепловая карта матрицы')
plt.xticks(range(5))
plt.yticks(range(5))
plt.xlabel('Столбцы')
plt.ylabel('Строки')
plt.show()