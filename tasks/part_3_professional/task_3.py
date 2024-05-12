user_discount: int = int(input())
cost: list[str] = input().split()

if user_discount >= 100 or user_discount <= 0:
    print('Размер скидки должен быть больше '
          '0 и не должен превышать 100')
else:
    columns: tuple[str, ...] = ('Название', 'Цена', 'Сумма скидки', 'Новая цена')
    template: str = '{:<15} {:<10} {:<15} {:<10}'

    # https://www.youtube.com/watch?v=D6-d5yWOBd0
    print(template.format(*columns))

    for i in range(len(cost)):
        price: float = float(cost[i])
        product: str = f'Товар {i + 1}'
        amounth_discaunt: float = price * (user_discount / 100)
        resalt: float = price - amounth_discaunt

        print(f'{product:<15} '
              f'{price:<10.2f} '
              f'{amounth_discaunt:<15.2f} '
              f'{resalt:<10.2f}')

    # Встроенная функция enumerate
    # https://pythonchik.ru/osnovy/cikl-for-v-python
