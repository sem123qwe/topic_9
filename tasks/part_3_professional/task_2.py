while True:
    print('Программа "Конвертер валют')
    print('Выберите операцию (0 для выхода):',
          '1. Конвертировать рубли в доллары',
          '2. Конвертировать доллары в рубли', sep='\n')

    number_of_operation: int = int(input('Введите номер операции: '))
    if number_of_operation == 0:
        print('До свидания!')
        break
    elif number_of_operation == 1:
        rate: float = float(input('Введите курс доллара к рублю: '))
        amunth: float = float(input('Введите количество рублей: '))
        resalt = rate * amunth
        print(f'Вы получите {resalt} USD')
    elif number_of_operation == 2:
        rate: float = float(input('Введите курс рубля к доллару: '))
        amunth: float = float(input('Введите количество долларов: '))
        resalt = rate * amunth
        print(f'Вы получите {resalt} RUB')
    else:
        print('Номер операции не коректин, попробуйте ещё раз')
    print()

# TODO: От дублирования кода можно избавиться, смотреть тему №6 задание №10
#  https://github.com/sem123qwe/topic_6/blob/main/tasks/task_10.py
