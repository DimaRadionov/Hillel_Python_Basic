# Введення з клавіатури 4 рядків та збереження їх у змінні
line1 = input("Введіть перший рядок: ")
line2 = input("Введіть другий рядок: ")
line3 = input("Введіть третій рядок: ")
line4 = input("Введіть четвертий рядок: ")

# Створення файлу та запис перших 2 рядків
with open("example.txt", "w") as file:
    file.write(line1 + '\n')
    file.write(line2 + '\n')

# Відкриття файлу на редагування та дозапис останніх 2 рядків
with open("example.txt", "a") as file:
    file.write(line3 + '\n')
    file.write(line4 + '\n')

print("Операція завершена. Зміст файлу 'example.txt':")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
