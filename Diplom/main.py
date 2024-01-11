from person import Person
from database import Database
import datetime


def calculate_age(birth_date, death_date=None):
    today = datetime.date.today()
    birth_date = datetime.datetime.strptime(birth_date, "%d.%m.%Y").date()
    if death_date:
        death_date = datetime.datetime.strptime(death_date, "%d.%m.%Y").date()
        age = (death_date - birth_date).days // 365
    else:
        age = (today - birth_date).days // 365
    return age


def main():
    db = Database()

    while True:
        print("\n1. Додати нову особу")
        print("2. Пошук за ім'ям, прізвищем або по батькові")
        print("3. Зберегти дані у файл")
        print("4. Завантажити дані з файлу")
        print("5. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            middle_name = input("Введіть по батькові: ")
            birth_date = input("Введіть дату народження (у форматі dd.mm.yyyy): ")
            death_date = input("Введіть дату смерті (необов'язково, у форматі dd.mm.yyyy): ")
            gender = input("Введіть стать (m/f): ")
            person = Person(first_name, last_name, middle_name, birth_date, death_date, gender)
            db.add_person(person)

        elif choice == '2':
            query = input("Введіть ім'я, прізвище або по батькові для пошуку: ")
            results = db.search_person(query)
            for person in results:
                age = calculate_age(person.birth_date, person.death_date)
                print(f"{person.first_name} {person.last_name} {person.middle_name} {age} років, {person.gender}")

        elif choice == '3':
            filename = input("Введіть ім'я файлу для збереження: ")
            db.save_to_file(filename)

        elif choice == '4':
            filename = input("Введіть ім'я файлу для завантаження: ")
            db.load_from_file(filename)

        elif choice == '5':
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
