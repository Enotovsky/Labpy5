import numpy as np

matrix = np.random.randint(1, 11, size=(5, 5))
print("Исходная матрица:")
print(matrix)
mean = np.mean(matrix)
print(f"\nСреднее значение: {mean:.2f}")
max = np.max(matrix)
min = np.min(matrix)
print(f"Максимум: {max}")
print(f"Минимум: {min}")
column_sums = np.sum(matrix, axis=0)
print(f"\nСуммы по столбцам:{column_sums}")


