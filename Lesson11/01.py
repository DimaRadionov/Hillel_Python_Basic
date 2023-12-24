import json

# Створення словника
dictionary = {
    123456: ('Іван', 25),
    789012: ('Марія', 30),
    345678: ('Петро', 22),
    901234: ('Ольга', 28),
    567890: ('Анна', 35),
    234567: ('Василь', 40)
}

# Запис словника у JSON-файл
with open('dictionary.json', 'w') as json_file:
    json.dump(dictionary, json_file)

print("Словник було успішно записано у 'dictionary.json' файл.")
