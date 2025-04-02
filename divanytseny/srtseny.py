import pandas as pd

# Чтение CSV-файла
df = pd.read_csv('tseny_na_divany.csv', encoding='utf-8')

# Удаление пробелов и замена запятой на точку
df['price'] = df['price'].str.replace(r'\s+', '', regex=True).str.replace(',', '.', regex=True)

# Преобразование строки в числа с плавающей точкой
df['price'] = df['price'].astype(float)

# Вычисление средней цены
mean_price = df['price'].mean()

# Вывод результата
print(f"Средняя цена диванов: {mean_price:.2f}")