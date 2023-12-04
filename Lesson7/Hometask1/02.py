import random

# Створення початкового списку
initial_list = [random.randint(1, 10) for _ in range(200)]

# Створення підсумкового словника за допомогою генератора словників
summary_dict = {num: initial_list.count(num) for num in set(initial_list)}

# Сортування підсумкового словника за ключами
sorted_summary = sorted(summary_dict.items())

# Виведення результату
for num, count in sorted_summary:
    print(f"Число {num} зустрічається у первісному списку {count} разів.")
