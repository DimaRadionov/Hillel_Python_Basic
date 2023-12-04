def count_occurrences(numbers):
    # Ініціалізуємо порожній словник для зберігання кількості входжень кожного числа
    occurrences = {}

    # Проходимося по кожному числу у списку
    for number in numbers:
        # Використовуємо метод get() для отримання значення (кількості входжень) за ключем (числом)
        # Якщо ключа ще немає в словнику, повертаємо 0
        occurrences[number] = occurrences.get(number, 0) + 1

    return occurrences

# Приклад використання:
number_list = [1, 2, 3, 1, 2, 3, 1, 2, 1, 4, 5, 4, 5, 4, 5]
result = count_occurrences(number_list)

# Виведення результатів
for number, count in result.items():
    print(f"Число {number} зустрічається {count} раз(ів).")
