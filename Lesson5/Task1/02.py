# Введення цілого додатного числа n з клавіатури
n = int(input("Введіть ціле додатне число n: "))

# Ініціалізація змінної для збереження суми кубів
suma = 0

# Цикл for для обчислення суми кубів з винятком чисел, кратних 3
for i in range(1, n + 1):
    if i % 3 != 0:  # Виняток для чисел, кратних 3
        suma += i ** 3

# Виведення результату
print(f"Сума кубів чисел від 1 до {n}, ігноруючи числа кратні 3: {suma}")