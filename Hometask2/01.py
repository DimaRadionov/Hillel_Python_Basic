# Запит користувача на введення строки
original_string = input("Введіть довільну строку: ")

# Створення строки лише з парних символів
even_characters = original_string[1::2]

# Створення строки із введеної у зворотній послідовності та у верхньому регістрі
reversed_and_upper = original_string[::-1].upper()

# Виведення результатів
print("Введена строка:", original_string)
print("Строка лише з парних символів:", even_characters)
print("Строка у верхньому регістрі та у зворотній послідовності:", reversed_and_upper)
