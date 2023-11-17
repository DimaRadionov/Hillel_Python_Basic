while True:
    age = input('Your age: ')
    name = input('Your name: ')

    if age.isdigit() and int(age) > 0:
        if int(age) < 10:
            print(f'Привіт, шкет, {name}')
        elif int(age) <= 18:
            print(f'Як справи, {name}', end='?\n')
        elif int(age) < 100:
            print(f'Що бажаєте {name}', end='?\n')
        else:
            print(f'{name}, ви брешете - у наш час стільки не живуть...')
    else:
        print('Помилка, повторіть введення')

    exit_choice = input('Бажаєте вийти? (Д/Y): ')
    if exit_choice.lower() in ['д', 'y']:
        print('До побачення!')
        break
