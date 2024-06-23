while True:
    
    # def tiping_1(valu_1, valu_2, valu_3):
    #     float(input(f'Введите курс {valu_1} к {valu_2}: '))
    #     float(input(f'Введите количество {valu_3}: '))
    
    dry_0: str = 'Введите курс'
    dry_1: str = 'Введите количество'
    dry_2: str = 'Вы получите'
    value_1: str = 'RUB'
    value_2: str = 'USD'

    print('Программа "Конвертер валют')
    print('Выберите операцию (0 для выхода):',
          '1. Конвертировать рубли в доллары',
          '2. Конвертировать доллары в рубли', sep='\n')

    number_of_operation: int = int(input('Введите номер операции: '))
    if number_of_operation == 0:
        print('До свидания!')
        break
    elif number_of_operation == 1:
        rate: float = float(input(f'{dry_0} доллара к рублю: '))
        amunth: float = float(input(f'{dry_1} рублей: '))
        resalt = rate * amunth
        print(f'{dry_2} {resalt} {value_1}')
    elif number_of_operation == 2:
        rate: float = float(input(f'{dry_0} рубля к доллару: '))
        amunth: float = float(input(f'{dry_1} долларов: '))
        resalt = rate * amunth
        print(f'{dry_2} {resalt} {value_2}')
    else:
        print('Номер операции не коректин, попробуйте ещё раз')
    print()

# TODO: От дублирования кода можно избавиться, смотреть тему №6 задание №10
#  https://github.com/sem123qwe/topic_6/blob/main/tasks/task_10.py
