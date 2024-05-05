while True:
    print('Программа "Конвертер валют')
    print('Выберите операцию (0 для выхода):',
            '1. Конвертировать рубли в доллары',
            '2. Конвертировать доллары в рубли', sep= '\n')
    
    
    number_of_operation: int = int(input('Введите номер операции: '))
    if number_of_operation == 0: 
        print('До свидания!')
        break
    elif number_of_operation == 1:
        rate: int = input('Введите курс доллара к рублю: ')
        amunth: int = input('Введите количество рублей: ')
        resalt = int(rate) * int(amunth)
        print(f'Вы получите {resalt} USD')
    elif number_of_operation == 2:
        rate: int = input('Введите курс рубля к доллару: ')
        amunth: int = input('Введите количество долларов: ')
        resalt = rate * amunth
        print(f'Вы получите {resalt} RUB')
    else: 
        print('Номер операции не коректин, попробуйте ещё раз')
    print(number_of_operation == 1)
    
  
    
    
