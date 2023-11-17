# Запитання у користувача числа
user_input = input('Введіть число: ')

# Перевірка чи введено ціле число
if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
    number = int(user_input)

    # Визначення парності/непарності числа за допомогою тернарного виразу
    parity = "парне" if number % 2 == 0 else "непарне" if number != 0 else "нуль"

    # Вивід результату
    print(f"Ви ввели {parity} число.")
else:
    print("Не вірне введення. Введіть ціле число.")
