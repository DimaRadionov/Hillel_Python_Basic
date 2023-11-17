while True:
    age = input('Your age: ')
    name = input('Your name: ')

    if age.lower() == 'exit':
        print('До побачення!')
        break

    if age != 0 and age.isdigit():
        if 0 < int(age) < 10:
            print('Привіт, шкет', name)
        elif 10 <= int(age) <= 18:
            print('Як справи,', name, end='?\n')
        elif 18 < int(age) < 100:
            print('Що бажаєте', name, end='?\n')
        else:
            print(name, ', ви брешете - у наш час стільки не живуть...', sep='')
    else:
        print('Помилка, повторіть введення')

    exit_choice = input('Бажаєте вийти? (Д/Y): ')
    if exit_choice.lower() in ['д', 'y']:
        print('До побачення!')
        break
