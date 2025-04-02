import pandas as pd
import matplotlib.pyplot as plt

# Чтение CSV-файла
df = pd.read_csv('tseny_na_divany.csv', encoding='utf-8')

# Удаление пробелов и замена запятой на точку
df['price'] = df['price'].str.replace(r'\s+', '', regex=True).str.replace(',', '.', regex=True)

# Преобразование строки в числа с плавающей точкой
df['price'] = df['price'].astype(float)

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика
plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')  # Строим гистограмму с 20 интервалами
plt.title('Распределение цен на диваны')  # Заголовок графика
plt.xlabel('Цена')  # Подпись оси X
plt.ylabel('Частота')  # Подпись оси Y
plt.grid(True)  # Показываем сетку
plt.show()  # Отображаем график
