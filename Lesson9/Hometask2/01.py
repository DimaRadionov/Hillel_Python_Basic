def analyze_input(input_str):
    # Перевірка, чи введений рядок є числом
    if input_str.replace(".", "", 1).replace(",", "", 1).isdigit() or (input_str[1:].replace(".", "", 1).replace(",", "", 1).isdigit() and input_str[0] == '-'):

        # Перевірка, чи введене число є нулем
        if float(input_str) == 0:
            return "Ви ввели нуль"

        # Перевірка, чи введене число є дробовим
        if '.' in input_str or ',' in input_str:
            return f"Ви ввели {'відємне' if input_str[0] == '-' else 'позитивне'} дробове число: {float(input_str)}"

        # Якщо число ціле
        return f"Ви ввели {'відємне' if input_str[0] == '-' else 'позитивне'} ціле число: {int(input_str)}"

    else:
        return f"Ви ввели неправильне число: {input_str}"


while True:
    user_input = input("Введіть число або 'вихід', 'exit', 'quit', 'e' або 'q': ").lower()

    if user_input in ['вихід', 'exit', 'quit', 'e', 'q']:
        print("Вихід з програми.")
        break

    result = analyze_input(user_input)
    print(result)
