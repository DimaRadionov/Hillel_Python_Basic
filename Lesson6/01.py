import random


def generate_random_number():
    return random.randint(1, 10)


def guess_number(secret_number, max_attempts=3):
    print("Спробуйте вгадати число від 1 до 10.")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Спроба {attempt}: Введіть ваше число: "))

        if guess == secret_number:
            print("Вітаємо! Ви вгадали число!")
            return True
        else:
            print("Неправильно. Спробуйте ще раз.")
            if guess < secret_number:
                print("Загадане число більше.")
            else:
                print("Загадане число менше.")

    print(f"Ви використали всі спроби. Загадане число було {secret_number}. Спробуйте ще раз.")
    return False


def play_game():
    play_again = True

    while play_again:
        secret_number = generate_random_number()
        success = guess_number(secret_number)

        if not success:
            print("Гра завершена.")

        play_again_input = input("Бажаєте зіграти знову? (так/ні): ")
        play_again = play_again_input.lower() == 'так'


if __name__ == "__main__":
    play_game()
