import pandas as pd

# Читання CSV-файлу
csv_file = "output.csv"
df = pd.read_csv(csv_file)

# Видалення стовпця з віком
df = df.drop(columns=['Вік'])

# Збереження у Excel-файл
excel_file = "output.xlsx"
df.to_excel(excel_file, index=False)

print(f"Дані було успішно записано у '{excel_file}' файл.")
