import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x_data = np.random.rand(100)  # Массив из 100 случайных чисел для оси X
y_data = np.random.rand(100)  # Массив из 100 случайных чисел для оси Y

# Создание диаграммы рассеяния
plt.scatter(x_data, y_data)

# Оформление графика
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Диаграмма рассеяния')

# Показ графика
plt.show()