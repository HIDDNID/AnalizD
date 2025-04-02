import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins=50, density=True, facecolor='b', alpha=0.75)

# Добавление линий плотности нормального распределения
x = np.linspace(min(data), max(data), 100)
pdf = 1/(np.sqrt(2*np.pi)*std_dev) * np.exp(-(x-mean)**2 / (2*std_dev**2))
plt.plot(x, pdf, color='r', linewidth=2)

# Оформление графика
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('Гистограмма нормально распределённых данных')

# Показ графика
plt.show()