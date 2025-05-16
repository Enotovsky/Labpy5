import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue')
plt.plot(x, z, label='cos(x)', color='red')

plt.title('Графики функций sin(x) и cos(x)')
plt.xlabel('x')
plt.ylabel('y, z')
plt.legend()
plt.grid(True)
plt.show()