import json
import csv
import random

# Читання збереженого JSON-файлу
with open('dictionary.json', 'r') as json_file:
    data = json.load(json_file)

# Формування нового словника з даними для CSV-файлу
csv_data = []
for key, value in data.items():
    user_id = key
    name = value[0]
    age = value[1]

    # Генерація випадкового номера телефону (10 цифр)
    phone = ''.join([str(random.randint(0, 9)) for _ in range(10)])

    csv_data.append([user_id, name, age, phone])

# Запис у CSV-файл
csv_columns = ["ID", "Ім'я", "Вік", "Телефон"]
csv_file = "output.csv"

with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(csv_columns)
    csv_writer.writerows(csv_data)

print(f"Дані було успішно записано у '{csv_file}' файл.")
