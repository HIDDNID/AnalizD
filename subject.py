import pandas as pd
import matplotlib.pyplot as plt

# Исходные данные
data = {
    'name': ['Иван Петров', 'Алиса Смирнова', 'Мария Иванова', 'Сергей Кузнецов', 'Ольга Васильева', 'Дмитрий Соколов', 'Екатерина Морозова', 'Наталья Сергеева', 'Михаил Андреев', 'Софья Попова'],
    'subject': ['Физкультура', 'Математика', 'Обществознание', 'Физика', 'Химия']
}

# Создаем DataFrame с учениками и предметами
students_df = pd.DataFrame(data['name'], columns=['name'])
subjects_df = pd.DataFrame(data['subject'], columns=['subject'])

# Создаем полную комбинацию студентов и предметов
full_combination = students_df.assign(key=1).merge(subjects_df.assign(key=1), on='key').drop('key', axis=1)

# Задаем конкретные оценки для каждого ученика и предмета
grades = [
    # Оценки для Ивана Петрова
    [4, 3, 4, 4, 5],
    # Оценки для Алисы Смирновой
    [3, 5, 5, 4, 3],
    # Оценки для Марии Ивановой
    [4, 4, 3, 5, 4],
    # Оценки для Сергея Кузнецова
    [5, 4, 3, 4, 5],
    # Оценки для Ольги Васильевой
    [3, 5, 4, 5, 4],
    # Оценки для Дмитрия Соколова
    [4, 3, 5, 4, 5],
    # Оценки для Екатерины Морозовой
    [5, 4, 3, 5, 4],
    # Оценки для Натальи Сергеевой
    [3, 5, 4, 5, 4],
    # Оценки для Михаила Андреева
    [4, 3, 5, 4, 5],
    # Оценки для Софьи Поповой
    [5, 4, 3, 5, 4]
]

# Добавляем столбец grade с заданными оценками
# Преобразуем массив оценок в плоскую структуру
flat_grades = [item for sublist in grades for item in sublist]

# Присваиваем оценки каждой строке DataFrame
full_combination['grade'] = flat_grades

print(full_combination.head())
print(full_combination.describe())

# Рассчитываем средние оценки по каждому предмету
average_grades_by_subject = full_combination.groupby('subject')['grade'].mean().reset_index()

# Выводим результат средней оценки
print(average_grades_by_subject)

# Рассчитываем медианную оценку по каждому предмету
median_grades_by_subject = full_combination.groupby('subject')['grade'].median().reset_index()

# Выводим результат медианной оценки
print(median_grades_by_subject)