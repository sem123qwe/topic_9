while True:
    print('Программа "Конвертер валют')
    print('Выберите операцию (0 для выхода):',
          '1. Конвертировать рубли в доллары',
          '2. Конвертировать доллары в рубли', sep='\n')

    number_of_operation: int = int(input('Введите номер операции: '))
    if number_of_operation == 0:
        print('До свидания!')
        break
    if number_of_operation not in (1, 2):
        print('Номер операции не коректин, попробуйте ещё раз')
        continue

    rate_hint: str = 'Введите курс доллара к рублю: '
    amunth_hint: str = 'Введите количество рублей: '
    currency_sign: str = 'USD'

    if number_of_operation == 2:
        rate_hint = 'Введите курс рубля к доллару: '
        amunth_hint = 'Введите количество долларов: '
        currency_sign = 'RUB'

    rate: float = float(input(rate_hint))
    amunth: float = float(input(amunth_hint))
    resalt: float = rate * amunth

    print(f'Вы получите {resalt} {currency_sign}')
