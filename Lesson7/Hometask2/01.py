check_parity = lambda x: "парне" if x % 2 == 0 and x != 0 else "не парне" if x != 0 else "нуль"

# Приклад використання:
number = int(input('Ваше число: '))
result = check_parity(number)
print(f"Число {number} - {result}")
